#!/usr/bin/env python3
"""Codex hook: enforce review completeness and unresolved conflict state at Stop."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = REPO_ROOT / "quality_reports" / "tmp" / "review_state"
REVIEW_MODE_FILE = STATE_DIR / "review_active.json"
TRACKING_FILE = STATE_DIR / "review_agents.txt"
CONFLICT_FILE = STATE_DIR / "review_conflict.txt"
REVIEW_PLAN = REPO_ROOT / "scripts" / "review_plan.py"


def load_payload() -> dict[str, Any]:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def load_review_mode() -> dict[str, Any] | None:
    if not REVIEW_MODE_FILE.exists():
        return None
    try:
        return json.loads(REVIEW_MODE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return None


def load_called_agents() -> set[str]:
    if not TRACKING_FILE.exists():
        return set()
    return {
        line.strip()
        for line in TRACKING_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def load_conflict_summary() -> str | None:
    if not CONFLICT_FILE.exists():
        return None
    summary = CONFLICT_FILE.read_text(encoding="utf-8").strip()
    return summary or None


def compute_required_agents(pattern: str, round_number: int, adversarial: bool) -> set[str]:
    cmd = [
        sys.executable,
        str(REVIEW_PLAN),
        pattern,
        "--round",
        str(round_number),
        "--json",
    ]
    if adversarial:
        cmd.append("--adversarial")

    output = subprocess.check_output(
        cmd,
        cwd=str(REPO_ROOT),
        text=True,
        stderr=subprocess.DEVNULL,
    )
    plan = json.loads(output)
    return set(plan.get("all_agents", []))


def emit_block(reason: str) -> None:
    print(json.dumps({"decision": "block", "reason": reason}))


def main() -> int:
    payload = load_payload()
    if str(payload.get("hook_event_name", "")) != "Stop":
        return 0

    review_mode = load_review_mode()
    if not review_mode:
        return 0
    if not bool(review_mode.get("active", False)):
        return 0

    conflict_summary = load_conflict_summary()
    if conflict_summary:
        emit_block(
            "Reviewer disagreement is unresolved. Ask the user to settle the difference "
            "before editing further. Conflict summary: "
            f"{conflict_summary}"
        )
        return 0

    pattern = str(review_mode.get("pattern", "")).strip()
    if not pattern:
        return 0

    round_number = int(review_mode.get("round", 1))
    adversarial = bool(review_mode.get("adversarial", False))
    required = compute_required_agents(pattern, round_number, adversarial)
    if not required:
        return 0

    called = load_called_agents()
    missing = sorted(required - called)
    if missing:
        emit_block(
            "Review round incomplete. Run and record the missing review agents before "
            "claiming completion. Missing agents: "
            f"{', '.join(missing)}."
        )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Fail open: hook bugs should not break Codex.
        sys.exit(0)
