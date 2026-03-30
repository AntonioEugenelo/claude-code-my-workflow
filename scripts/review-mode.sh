#!/bin/bash
# review-mode.sh — Start, stop, reset, or check review tracking mode.
#
# The review-completeness hook only enforces agent completeness when a
# review round is explicitly active. This script manages that state.
#
# Usage:
#   ./scripts/review-mode.sh start "master_supporting_docs/**/*.tex"
#   ./scripts/review-mode.sh stop
#   ./scripts/review-mode.sh reset
#   ./scripts/review-mode.sh status

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_DIR="$PROJECT_DIR/.claude/state"

MODE_FILE="$STATE_DIR/review_active.json"
TRACKING_FILE="$STATE_DIR/review_agents.txt"
CONTEXT_FILE="$STATE_DIR/review_context.txt"

mkdir -p "$STATE_DIR"

case "${1:-status}" in
  start)
    doc_pattern="${2:-unknown}"
    round="${3:-1}"
    # Clear any stale tracking from previous rounds
    rm -f "$TRACKING_FILE" "$CONTEXT_FILE"
    # Create mode marker with round number
    cat > "$MODE_FILE" <<EOF
{"active": true, "pattern": "$doc_pattern", "round": $round, "started": "$(date -Iseconds 2>/dev/null || date)"}
EOF
    echo "Review mode ACTIVE for: $doc_pattern (round $round)"
    if [ "$round" -gt 1 ]; then
      echo "RE-SCORE round: derivation-auditor and figure-reviewer will be skipped."
    fi
    echo "Hook will now enforce agent completeness per agent-routing.md."
    ;;
  stop|reset)
    rm -f "$MODE_FILE" "$TRACKING_FILE" "$CONTEXT_FILE"
    echo "Review mode OFF. All tracking state cleared."
    ;;
  status)
    if [ -f "$MODE_FILE" ]; then
      echo "Review mode: ACTIVE"
      cat "$MODE_FILE"
      echo ""
      if [ -f "$TRACKING_FILE" ]; then
        echo "Agents called so far:"
        sort -u "$TRACKING_FILE"
      else
        echo "Agents called: (none yet)"
      fi
    else
      echo "Review mode: INACTIVE"
      echo "Ad-hoc agent calls will not trigger completeness enforcement."
    fi
    ;;
  *)
    echo "Usage: review-mode.sh {start|stop|reset|status} [doc_pattern]"
    echo ""
    echo "  start <pattern>  Activate review mode for a document type"
    echo "  stop             Deactivate and clear tracking state"
    echo "  reset            Same as stop (alias)"
    echo "  status           Show current review mode state"
    exit 1
    ;;
esac
