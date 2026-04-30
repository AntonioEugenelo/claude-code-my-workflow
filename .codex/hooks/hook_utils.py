"""Shared helpers for Codex hook scripts mirrored from Claude behavior."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


def get_project_dir() -> str:
    """Return the best available project directory from Claude, Codex, or cwd."""
    return (
        os.environ.get("CLAUDE_PROJECT_DIR")
        or os.environ.get("CODEX_PROJECT_DIR")
        or os.environ.get("PWD")
        or os.getcwd()
    )


def get_session_dir() -> Path:
    """Return the per-project hook state directory.

    Codex hook state lives in the ignored repo-local quality_reports/hook_state/
    directory so hooks work under workspace-write sandboxing. If the same script
    is run by Claude Code, keep using the inherited ~/.claude/sessions location.
    """
    project_dir = get_project_dir()
    if os.environ.get("CLAUDE_PROJECT_DIR"):
        base_dir = Path.home() / ".claude" / "sessions"
    elif project_dir:
        base_dir = Path(project_dir) / "quality_reports" / "hook_state"
    else:
        base_dir = Path.cwd() / "quality_reports" / "hook_state"
    if not project_dir:
        session_dir = base_dir / "default"
    else:
        project_hash = hashlib.md5(project_dir.encode()).hexdigest()[:8]
        session_dir = base_dir / project_hash
    session_dir.mkdir(parents=True, exist_ok=True)
    return session_dir
