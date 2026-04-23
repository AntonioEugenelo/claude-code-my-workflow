#!/bin/bash
# Deprecated compatibility wrapper for the canonical Overleaf sync workflow.
#
# This keeps the old entrypoint name alive while forwarding to the
# Codex-first sync script.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CANONICAL_SCRIPT="$SCRIPT_DIR/sync-overleaf.sh"

if [ ! -x "$CANONICAL_SCRIPT" ]; then
    echo "ERROR: canonical sync script not found at $CANONICAL_SCRIPT" >&2
    exit 1
fi

if [ "$#" -eq 0 ]; then
    COMMAND="push"
else
    COMMAND="$1"
fi

case "$COMMAND" in
    pull|push|sync|status)
        ;;
    *)
        echo "ERROR: unsupported arguments for deprecated wrapper: $*" >&2
        echo "Use ./scripts/sync-overleaf.sh {pull|push|sync|status}." >&2
        echo "Legacy commit-message mode is no longer supported by sync_to_overleaf.sh." >&2
        exit 2
    ;;
esac

echo "NOTE: sync_to_overleaf.sh is deprecated. Use ./scripts/sync-overleaf.sh $COMMAND instead." >&2
exec "$CANONICAL_SCRIPT" "$COMMAND"
