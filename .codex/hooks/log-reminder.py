#!/usr/bin/env python3
"""
Session Log Reminder Hook for Claude Code

A Stop hook that tracks how many responses have passed since the session
log was last updated, and nudges Claude to update the log via stderr
advisories. **Never blocks** — always exits 0 without writing a decision
to stdout. Two advisory triggers (fired at most once per session each):
  1. No session log exists under quality_reports/session_logs/ at all.
  2. THRESHOLD responses have passed without the most-recent log being
     touched.

Design rationale: a previous version of this hook emitted
{"decision": "block"} to stop Claude mid-turn. That was effective but
disrupted autonomous flows. Reminders are now advisory only — the user
remains responsible for deciding when to write the log.

Adapted from: https://gist.github.com/michaelewens/9a1bc5a97f3f9bbb79453e5b682df462

Usage (in .claude/settings.json):
    "Stop": [{ "hooks": [{ "type": "command", "command": "python3 \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/log-reminder.py" }] }]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import datetime

from hook_utils import get_session_dir

THRESHOLD = 50
DRIFT_THRESHOLD = 20


def get_project_dir():
    """Get project directory from stdin JSON or environment."""
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        hook_input = {}

    # If stop_hook_active, Claude is already continuing from a previous
    # Stop hook block — let it stop this time to avoid infinite loops.
    if hook_input.get("stop_hook_active", False):
        sys.exit(0)

    return hook_input.get("cwd", ""), hook_input


def get_state_path() -> Path:
    """Return the state file path for the current project."""
    return get_session_dir() / "log-reminder-state.json"


def load_state(state_path: Path) -> dict:
    """Load persisted state, or return defaults."""
    try:
        return json.loads(state_path.read_text())
    except (FileNotFoundError, json.JSONDecodeError):
        return {"counter": 0, "last_mtime": 0.0, "reminded": False, "no_log_reminded": False}


def save_state(state_path: Path, state: dict):
    """Persist state to disk."""
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state))


def find_latest_log(project_dir: str) -> tuple[Path | None, float]:
    """Find the most recently modified .md file in session_logs/."""
    log_dir = Path(project_dir) / "quality_reports" / "session_logs"
    if not log_dir.is_dir():
        return None, 0.0

    md_files = list(log_dir.glob("*.md"))
    if not md_files:
        return None, 0.0

    latest = max(md_files, key=lambda f: f.stat().st_mtime)
    return latest, latest.stat().st_mtime


def find_latest_file(directory: Path, pattern: str = "*.md") -> Path | None:
    """Return newest matching file in a directory, if any."""
    if not directory.is_dir():
        return None
    files = list(directory.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda f: f.stat().st_mtime)


def run_card_exists_for_current_run(project_dir: str) -> bool:
    """Check whether current long-run state points to an existing run card."""
    state_file = Path(project_dir) / "quality_reports" / "run_state" / "current.json"
    if not state_file.exists():
        return True
    try:
        state = json.loads(state_file.read_text())
    except (json.JSONDecodeError, IOError):
        return False
    if state.get("status") not in {"planned", "running"}:
        return True
    run_card = state.get("run_card", "")
    if not run_card:
        return False
    path = Path(run_card)
    if not path.is_absolute():
        path = Path(project_dir) / path
    return path.exists()


def drift_warnings(project_dir: str, state: dict) -> list[str]:
    """Return advisory warnings for workflow drift."""
    root = Path(project_dir)
    reports = root / "quality_reports"
    warnings: list[str] = []

    active_decisions = reports / "decisions" / "ACTIVE.md"
    source_authority = reports / "decisions" / "source_authority.md"
    latest_plan = find_latest_file(reports / "plans")
    latest_checkpoint = find_latest_file(reports / "checkpoints")

    if latest_plan and not active_decisions.exists():
        warnings.append("active plan exists but quality_reports/decisions/ACTIVE.md is missing")

    if not source_authority.exists():
        warnings.append("source authority guard is missing")

    if not run_card_exists_for_current_run(project_dir):
        warnings.append("current long-run state is running without an existing run card")

    drift_counter = state.get("drift_counter", 0) + 1
    state["drift_counter"] = drift_counter

    if drift_counter >= DRIFT_THRESHOLD:
        if latest_plan and latest_checkpoint is None:
            warnings.append("many responses with an active plan but no checkpoint")
        state["drift_counter"] = 0

    return warnings


def main():
    project_dir, _ = get_project_dir()
    if not project_dir:
        sys.exit(0)

    state_path = get_state_path()
    state = load_state(state_path)
    warnings = drift_warnings(project_dir, state)
    if warnings:
        for warning in warnings:
            sys.stderr.write(f"\n[workflow-drift] {warning}.\n")

    latest_log, current_mtime = find_latest_log(project_dir)
    today = datetime.now().strftime("%Y-%m-%d")

    # Case 1: No session log exists — advisory reminder to stderr, never blocks.
    if latest_log is None:
        if not state.get("no_log_reminded", False):
            state["no_log_reminded"] = True
            save_state(state_path, state)
            sys.stderr.write(
                f"\n[session-log] No session log yet. Consider creating "
                f"quality_reports/session_logs/{today}_description.md "
                f"to capture goal + key context.\n"
            )
        sys.exit(0)

    # Case 2: Log was updated since last check — reset everything
    if current_mtime != state["last_mtime"]:
        state = {"counter": 0, "last_mtime": current_mtime, "reminded": False, "no_log_reminded": False}
        save_state(state_path, state)
        sys.exit(0)

    # Case 3: Log not updated — increment counter
    state["counter"] += 1

    if state["counter"] >= THRESHOLD and not state["reminded"]:
        state["reminded"] = True
        save_state(state_path, state)
        sys.stderr.write(
            f"\n[session-log] {state['counter']} responses without updating "
            f"{latest_log.name}. Consider appending recent progress.\n"
        )
        sys.exit(0)

    save_state(state_path, state)
    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Fail open — never block Claude due to a hook bug
        sys.exit(0)
