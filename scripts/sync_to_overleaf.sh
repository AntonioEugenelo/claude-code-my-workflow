#!/bin/bash
# sync_to_overleaf.sh — Sync Slides/, Figures/, Preambles/, and Bibliography
# from this project into the Tariffs_ECB Overleaf repo.
#
# Usage: ./scripts/sync_to_overleaf.sh [commit message]
# Default commit message: "Sync from claude-code-my-workflow"

set -euo pipefail

# Paths
PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OVERLEAF_REPO="$PROJECT_ROOT/master_supporting_docs/Tariffs_ECB"
TARGET_DIR="$OVERLEAF_REPO/0_clean"

if [ ! -d "$OVERLEAF_REPO/.git" ]; then
    echo "ERROR: Tariffs_ECB repo not found at $OVERLEAF_REPO"
    echo "Clone it first: git clone <url> master_supporting_docs/Tariffs_ECB"
    exit 1
fi

COMMIT_MSG="${1:-Sync from claude-code-my-workflow}"

echo "=== Syncing to Overleaf repo ==="

# Ensure target directories exist
mkdir -p "$TARGET_DIR/sections"
mkdir -p "$TARGET_DIR/figures"

# Sync .tex files from Slides/ → 0_clean/sections/
if [ -d "$PROJECT_ROOT/Slides" ]; then
    echo "Syncing .tex files from Slides/..."
    find "$PROJECT_ROOT/Slides" -name "*.tex" -exec cp -v {} "$TARGET_DIR/sections/" \;
fi

# Sync figures from Figures/ → 0_clean/figures/
if [ -d "$PROJECT_ROOT/Figures" ]; then
    echo "Syncing figures from Figures/..."
    find "$PROJECT_ROOT/Figures" \( -name "*.png" -o -name "*.pdf" -o -name "*.jpg" -o -name "*.jpeg" -o -name "*.svg" -o -name "*.eps" \) -exec cp -v {} "$TARGET_DIR/figures/" \;
fi

# Sync preamble/header files from Preambles/ → 0_clean/
if [ -d "$PROJECT_ROOT/Preambles" ]; then
    echo "Syncing preamble files from Preambles/..."
    find "$PROJECT_ROOT/Preambles" -name "*.tex" -o -name "*.sty" | while read f; do
        cp -v "$f" "$TARGET_DIR/"
    done
fi

# Sync bibliography
if [ -f "$PROJECT_ROOT/Bibliography_base.bib" ]; then
    echo "Syncing bibliography..."
    cp -v "$PROJECT_ROOT/Bibliography_base.bib" "$TARGET_DIR/bibliography.bib"
fi

# Commit and push from Overleaf repo
cd "$OVERLEAF_REPO"
if [ -n "$(git status --porcelain)" ]; then
    echo ""
    echo "=== Changes detected, committing ==="
    git add -A
    git status --short
    echo ""
    read -p "Commit and push? [y/N] " confirm
    if [[ "$confirm" =~ ^[Yy]$ ]]; then
        git commit -m "$COMMIT_MSG"
        git push
        echo "=== Pushed to Overleaf remote ==="
    else
        echo "Staged but not committed. Review with: cd $OVERLEAF_REPO && git diff --cached"
    fi
else
    echo "No changes to sync."
fi
