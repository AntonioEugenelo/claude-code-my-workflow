#!/usr/bin/env python3
"""Codex hook: block clearly dangerous Bash commands for this repository."""

from __future__ import annotations

import json
import re
import sys
from typing import Any


BLOCK_RULES: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r"\bgit\s+reset\s+--hard\b", re.IGNORECASE),
        "Blocked by repository policy: do not use 'git reset --hard'.",
    ),
    (
        re.compile(r"\bgit\s+checkout\s+--\b", re.IGNORECASE),
        "Blocked by repository policy: do not discard changes with 'git checkout --'.",
    ),
    (
        re.compile(r"\bgit\s+clean\b.*\b-f\b", re.IGNORECASE),
        "Blocked by repository policy: do not use forceful 'git clean' from Codex.",
    ),
    (
        re.compile(r"\bgit\s+push\b.*(?:--force|-f)(?:\s|$)", re.IGNORECASE),
        "Blocked by repository policy: force-push commands are not allowed from Codex.",
    ),
    (
        re.compile(r"\brm\s+-rf\s+(/|\$HOME\b|~\b)", re.IGNORECASE),
        "Blocked by repository policy: recursive deletion of root or home paths is not allowed.",
    ),
]


def load_payload() -> dict[str, Any]:
    try:
        return json.load(sys.stdin)
    except Exception:
        return {}


def get_command(payload: dict[str, Any]) -> str:
    tool_input = payload.get("tool_input", {})
    if isinstance(tool_input, dict):
        command = tool_input.get("command", "")
        if isinstance(command, str):
            return command
    return ""


def find_block_reason(command: str) -> str | None:
    for pattern, reason in BLOCK_RULES:
        if pattern.search(command):
            return reason
    return None


def emit_pretool_deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }
        )
    )


def emit_permission_deny(reason: str) -> None:
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "PermissionRequest",
                    "decision": {
                        "behavior": "deny",
                        "message": reason,
                    },
                }
            }
        )
    )


def main() -> int:
    payload = load_payload()
    event_name = str(payload.get("hook_event_name", ""))
    command = get_command(payload)
    if not command:
        return 0

    reason = find_block_reason(command)
    if not reason:
        return 0

    if event_name == "PreToolUse":
        emit_pretool_deny(reason)
    elif event_name == "PermissionRequest":
        emit_permission_deny(reason)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Fail open: a hook bug should not break Codex itself.
        sys.exit(0)
