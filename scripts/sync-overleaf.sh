#!/bin/bash
# sync-overleaf.sh — Bidirectional sync between Overleaf, GitHub, and local.
#
# Overleaf (master) ←→ Local (main) ←→ GitHub (main)
#
# Usage:
#   ./scripts/sync-overleaf.sh pull    # Overleaf → local → GitHub
#   ./scripts/sync-overleaf.sh push    # Local → Overleaf (+ GitHub)
#   ./scripts/sync-overleaf.sh sync    # Both directions
#   ./scripts/sync-overleaf.sh status  # Compare HEADs across all three
#
# Credentials: .codex/state/overleaf.env (gitignored)
# Overleaf uses 'master', local/GitHub use 'main'.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_DIR="$PROJECT_ROOT/.codex/state"
ENV_FILE="$STATE_DIR/overleaf.env"
SUBMODULE_PATH="$PROJECT_ROOT/master_supporting_docs/Tariffs_ECB"
LOG_FILE="$STATE_DIR/overleaf-sync.log"

# ── Load credentials ────────────────────────────────────────────────
if [ ! -f "$ENV_FILE" ]; then
    echo "ERROR: Overleaf credentials not found at $ENV_FILE"
    echo "Create it with OVERLEAF_TOKEN and OVERLEAF_PROJECT_ID"
    exit 1
fi
source "$ENV_FILE"

if [ -z "${OVERLEAF_TOKEN:-}" ] || [ -z "${OVERLEAF_PROJECT_ID:-}" ]; then
    echo "ERROR: OVERLEAF_TOKEN or OVERLEAF_PROJECT_ID not set in $ENV_FILE"
    exit 1
fi

OVERLEAF_AUTH_URL="https://git:${OVERLEAF_TOKEN}@git.overleaf.com/${OVERLEAF_PROJECT_ID}"

# ── Helpers ─────────────────────────────────────────────────────────
log() {
    local msg="[$(date '+%Y-%m-%d %H:%M:%S')] $1"
    echo "$msg"
    echo "$msg" >> "$LOG_FILE"
}

ensure_submodule() {
    if [ ! -d "$SUBMODULE_PATH/.git" ] && [ ! -f "$SUBMODULE_PATH/.git" ]; then
        echo "ERROR: Tariffs_ECB submodule not initialised at $SUBMODULE_PATH"
        echo "Run: git submodule update --init master_supporting_docs/Tariffs_ECB"
        exit 1
    fi
}

update_parent_submodule() {
    # Update the submodule pointer in the parent repo if it changed
    cd "$PROJECT_ROOT"
    local sub_sha
    sub_sha=$(cd "$SUBMODULE_PATH" && git rev-parse HEAD)
    local parent_sha
    parent_sha=$(git ls-tree HEAD -- master_supporting_docs/Tariffs_ECB | awk '{print $3}')
    if [ "$sub_sha" != "$parent_sha" ]; then
        log "Updating submodule pointer in parent repo ($parent_sha → $sub_sha)"
        git add master_supporting_docs/Tariffs_ECB
        git commit -m "Update Tariffs_ECB submodule: sync from Overleaf

Co-Authored-By: sync-overleaf.sh <noreply@local>"
        git push origin HEAD
    fi
}

# ── Commands ────────────────────────────────────────────────────────
do_pull() {
    log "PULL: Overleaf → local → GitHub"
    ensure_submodule
    cd "$SUBMODULE_PATH"

    # Stash any local changes
    local stashed=false
    if [ -n "$(git status --porcelain)" ]; then
        log "Stashing local changes..."
        git stash push -m "sync-overleaf auto-stash"
        stashed=true
    fi

    # Fetch from Overleaf (master) and merge into local (main)
    log "Fetching from Overleaf..."
    git fetch "$OVERLEAF_AUTH_URL" master
    local local_head overleaf_head
    local_head=$(git rev-parse HEAD)
    overleaf_head=$(git rev-parse FETCH_HEAD)

    if [ "$local_head" = "$overleaf_head" ]; then
        log "Already up to date."
    else
        log "Merging Overleaf changes ($overleaf_head)..."
        # --allow-unrelated-histories handles the first-ever merge when
        # Overleaf and GitHub repos were created independently. After the
        # initial link, this flag is harmless on subsequent merges.
        if ! git merge FETCH_HEAD --allow-unrelated-histories --no-edit \
                -m "Merge Overleaf edits"; then
            log "ERROR: Merge conflict! Resolve manually in $SUBMODULE_PATH"
            git merge --abort
            if [ "$stashed" = true ]; then git stash pop; fi
            exit 1
        fi
        # Push merged result to GitHub
        log "Pushing to GitHub..."
        git push origin main
    fi

    # Restore stashed changes
    if [ "$stashed" = true ]; then
        log "Restoring stashed changes..."
        git stash pop
    fi

    update_parent_submodule
    log "PULL complete."
}

do_push() {
    log "PUSH: local → Overleaf (+ GitHub)"
    ensure_submodule
    cd "$SUBMODULE_PATH"

    # Push to GitHub first
    log "Pushing to GitHub..."
    git push origin main

    # Push to Overleaf (local main → overleaf master)
    log "Pushing to Overleaf..."
    git push "$OVERLEAF_AUTH_URL" main:master

    update_parent_submodule
    log "PUSH complete. Overleaf will reflect changes immediately."
}

do_sync() {
    log "SYNC: bidirectional"
    do_pull
    do_push
}

do_status() {
    ensure_submodule
    cd "$SUBMODULE_PATH"
    local local_head github_head overleaf_head
    local_head=$(git rev-parse HEAD)
    github_head=$(git ls-remote origin HEAD 2>/dev/null | cut -f1)
    overleaf_head=$(git ls-remote "$OVERLEAF_AUTH_URL" HEAD 2>/dev/null | cut -f1)

    echo "=== Overleaf Sync Status ==="
    echo "  Local:    $local_head"
    echo "  GitHub:   $github_head"
    echo "  Overleaf: $overleaf_head"
    if [ "$local_head" = "$github_head" ] && [ "$local_head" = "$overleaf_head" ]; then
        echo "  Status: ALL IN SYNC"
    else
        [ "$local_head" != "$overleaf_head" ] && echo "  ! Overleaf has diverged from local" || true
        [ "$local_head" != "$github_head" ] && echo "  ! GitHub has diverged from local" || true
    fi
}

# ── Main ────────────────────────────────────────────────────────────
mkdir -p "$STATE_DIR"
DIRECTION="${1:-status}"

case "$DIRECTION" in
    pull)   do_pull ;;
    push)   do_push ;;
    sync)   do_sync ;;
    status) do_status ;;
    *)
        echo "Usage: sync-overleaf.sh {pull|push|sync|status}"
        echo ""
        echo "  pull    Overleaf → local → GitHub"
        echo "  push    Local → Overleaf (+ GitHub)"
        echo "  sync    Both directions"
        echo "  status  Compare HEADs"
        exit 1
        ;;
esac
