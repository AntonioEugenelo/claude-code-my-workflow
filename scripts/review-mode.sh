#!/bin/bash
# review-mode.sh — Track explicit review progress for Codex review rounds.
#
# Usage:
#   ./scripts/review-mode.sh start "master_supporting_docs/**/*.tex" [round] [standard|adversarial]
#   ./scripts/review-mode.sh mark proofreader
#   ./scripts/review-mode.sh conflict "summary of reviewer disagreement"
#   ./scripts/review-mode.sh resolve
#   ./scripts/review-mode.sh stop
#   ./scripts/review-mode.sh reset
#   ./scripts/review-mode.sh status

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_DIR="$PROJECT_DIR/quality_reports/tmp/review_state"

MODE_FILE="$STATE_DIR/review_active.json"
TRACKING_FILE="$STATE_DIR/review_agents.txt"
CONTEXT_FILE="$STATE_DIR/review_context.txt"
CONFLICT_FILE="$STATE_DIR/review_conflict.txt"

mkdir -p "$STATE_DIR"

is_active() {
  [ -f "$MODE_FILE" ] && grep -q '"active": true' "$MODE_FILE"
}

case "${1:-status}" in
  start)
    doc_pattern="${2:-unknown}"
    round="${3:-1}"
    review_kind="${4:-standard}"
    case "$review_kind" in
      adversarial)
        adversarial=true
        ;;
      standard|"")
        adversarial=false
        review_kind="standard"
        ;;
      *)
        echo "Usage: review-mode.sh start <pattern> [round] [standard|adversarial]"
        exit 1
        ;;
    esac
    : > "$TRACKING_FILE"
    : > "$CONTEXT_FILE"
    : > "$CONFLICT_FILE"
    cat > "$MODE_FILE" <<EOF
{"active": true, "pattern": "$doc_pattern", "round": $round, "adversarial": $adversarial, "started": "$(date -Iseconds 2>/dev/null || date)"}
EOF
    echo "Review tracking ACTIVE for: $doc_pattern (round $round, $review_kind)"
    if [ "$round" -gt 1 ]; then
      echo "Re-review round recorded. Re-run only the review agents still justified by the current changes."
    fi
    if [ "$adversarial" = true ]; then
      echo "Adversarial mode recorded. The Stop hook can enforce the challenge pass as part of completeness."
    fi
    echo "Use 'mark <agent>' after each completed review-agent pass."
    ;;
  mark)
    agent="${2:-}"
    if [ -z "$agent" ]; then
      echo "Usage: review-mode.sh mark <agent>"
      exit 1
    fi
    if ! is_active; then
      echo "Review mode is not active. Run: review-mode.sh start <pattern> [round]"
      exit 1
    fi
    printf '%s\n' "$agent" >> "$TRACKING_FILE"
    sort -u "$TRACKING_FILE" -o "$TRACKING_FILE"
    echo "Recorded review agent: $agent"
    ;;
  conflict)
    summary="${2:-}"
    if [ -z "$summary" ]; then
      echo "Usage: review-mode.sh conflict <summary>"
      exit 1
    fi
    if ! is_active; then
      echo "Review mode is not active. Run: review-mode.sh start <pattern> [round] [standard|adversarial]"
      exit 1
    fi
    printf '%s\n' "$summary" > "$CONFLICT_FILE"
    echo "Recorded unresolved reviewer conflict."
    ;;
  resolve|clear-conflict)
    : > "$CONFLICT_FILE"
    echo "Reviewer conflict cleared."
    ;;
  stop|reset)
    cat > "$MODE_FILE" <<EOF
{"active": false, "pattern": "", "round": 0, "adversarial": false, "stopped": "$(date -Iseconds 2>/dev/null || date)"}
EOF
    : > "$TRACKING_FILE"
    : > "$CONTEXT_FILE"
    : > "$CONFLICT_FILE"
    echo "Review mode OFF. Tracking state reset."
    ;;
  status)
    if is_active; then
      echo "Review mode: ACTIVE"
      cat "$MODE_FILE"
      echo ""
      if [ -s "$TRACKING_FILE" ]; then
        echo "Review agents recorded so far:"
        sort -u "$TRACKING_FILE"
      else
        echo "Review agents: (none yet)"
      fi
      echo ""
      if [ -s "$CONFLICT_FILE" ]; then
        echo "Reviewer conflict: ACTIVE"
        cat "$CONFLICT_FILE"
      else
        echo "Reviewer conflict: none"
      fi
    else
      echo "Review mode: INACTIVE"
      echo "No review round is currently being tracked."
    fi
    ;;
  *)
    echo "Usage: review-mode.sh {start|mark|conflict|resolve|clear-conflict|stop|reset|status} [doc_pattern|agent|summary]"
    echo ""
    echo "  start <pattern> [round] [standard|adversarial]  Start tracking a review round"
    echo "  mark <agent>                                  Record a completed review agent"
    echo "  conflict <summary>                            Record an unresolved reviewer conflict"
    echo "  resolve                                       Clear the recorded reviewer conflict"
    echo "  clear-conflict                                Same as resolve (alias)"
    echo "  stop                                          Deactivate and clear tracking state"
    echo "  reset                                         Same as stop (alias)"
    echo "  status                                        Show current review mode state"
    exit 1
    ;;
esac
