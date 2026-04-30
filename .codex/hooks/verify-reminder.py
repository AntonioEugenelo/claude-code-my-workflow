#!/usr/bin/env python3
"""
Verification Reminder Hook

Non-blocking reminder that fires on Write/Edit to academic files (.tex, .qmd, .R)
to remind about compiling/rendering before marking a task as done.

Hook Event: PostToolUse
Returns: Exit code 0 (non-blocking, reminder visible but doesn't stop work)

Skips:
- Configuration files (.json, .yaml, .toml, etc.)
- Documentation files (.md, .txt, README)
- Test files and generated files
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

from hook_utils import get_session_dir

CYAN = "\033[0;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
NC = "\033[0m"

VERIFY_EXTENSIONS = {
    ".tex": "compile with /compile-latex",
    ".qmd": "render with quarto render",
    ".R": "run to verify output"
}

SKIP_EXTENSIONS = [
    ".md", ".txt", ".rst",
    ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg",
    ".lock", ".env", ".gitignore",
    ".svg", ".png", ".jpg", ".pdf",
    ".bib", ".cls", ".sty"
]

SKIP_DIRS = [
    "/docs/",
    "/templates/",
    "/quality_reports/",
    "/.claude/",
    "/.codex/",
    "/node_modules/",
    "/build/",
    "/dist/"
]


def should_skip(file_path: str) -> bool:
    """Check if this file should skip verification reminder."""
    path = Path(file_path)
    normalized = file_path.replace("\\", "/")
    if not normalized.startswith("/"):
        normalized = f"/{normalized}"

    if path.suffix.lower() in SKIP_EXTENSIONS:
        return True

    for skip_dir in SKIP_DIRS:
        if skip_dir in normalized:
            return True

    name = path.name.lower()
    if name.startswith("test_") or name.endswith("_test.py"):
        return True

    return False


def extract_candidate_paths(hook_input: dict) -> list[str]:
    """Extract edited file paths from Claude- or Codex-shaped tool input."""
    tool_input = hook_input.get("tool_input", {})
    if not isinstance(tool_input, dict):
        return []

    paths: list[str] = []
    for key in ("file_path", "path", "filename"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            paths.append(value)

    for key in ("patch", "input", "content"):
        value = tool_input.get(key)
        if not isinstance(value, str):
            continue
        for match in re.finditer(r"^\*\*\* (?:Add|Update|Delete) File: (.+)$", value, re.MULTILINE):
            paths.append(match.group(1).strip())

    seen: set[str] = set()
    unique_paths: list[str] = []
    for path in paths:
        if path not in seen:
            unique_paths.append(path)
            seen.add(path)
    return unique_paths


def needs_verification(file_path: str) -> tuple[bool, str]:
    """Check if this file needs verification and return the action."""
    path = Path(file_path)
    suffix = path.suffix.lower()

    if suffix in VERIFY_EXTENSIONS:
        return True, VERIFY_EXTENSIONS[suffix]

    return False, ""


def was_recently_reminded(file_path: str) -> bool:
    """Check if we already reminded about this file recently (within 5 minutes)."""
    cache_file = get_session_dir() / "verify-reminder-cache.json"

    try:
        if cache_file.exists():
            cache = json.loads(cache_file.read_text())
        else:
            cache = {}
    except (json.JSONDecodeError, IOError):
        cache = {}

    last_reminder = cache.get(file_path, 0)
    now = time.time()

    cache[file_path] = now

    cache = {k: v for k, v in cache.items() if now - v < 300}

    try:
        cache_file.write_text(json.dumps(cache))
    except IOError:
        pass

    return (now - last_reminder) < 300


def format_reminder(file_path: str, action: str) -> str:
    """Format the verification reminder."""
    filename = Path(file_path).name
    return f"""
{CYAN}[verification]{NC} {filename}
   -> {GREEN}{action}{NC} before marking task complete
"""


def main() -> int:
    """Main hook entry point."""
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, IOError):
        return 0

    file_paths = extract_candidate_paths(hook_input)
    if not file_paths:
        return 0

    for file_path in file_paths:
        if should_skip(file_path):
            continue

        needs_verify, action = needs_verification(file_path)
        if not needs_verify:
            continue

        if was_recently_reminded(file_path):
            continue

        print(format_reminder(file_path, action))

    return 0  # Non-blocking


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # Fail open — never block Claude due to a hook bug
        sys.exit(0)
