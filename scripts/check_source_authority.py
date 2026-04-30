#!/usr/bin/env python3
"""Print source-authority context before sync, push, pull, or merge actions."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE = ROOT / "quality_reports" / "decisions" / "ACTIVE.md"
SOURCE_AUTHORITY = ROOT / "quality_reports" / "decisions" / "source_authority.md"


def run_git(args: list[str], cwd: Path) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=cwd, text=True, stderr=subprocess.STDOUT).strip()
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        output = getattr(exc, "output", "")
        return output.strip() or str(exc)


def print_repo_status(label: str, path: Path) -> None:
    print(f"## {label}: {path}")
    print("branch/status:")
    print(run_git(["status", "--short", "--branch"], path) or "(clean or unavailable)")
    print("remotes:")
    print(run_git(["remote", "-v"], path) or "(no remotes or unavailable)")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", action="append", default=[], help="Additional nested repo path to inspect")
    args = parser.parse_args()

    print("# Source Authority Check")
    print()
    print(f"Active decisions: {ACTIVE}")
    print(f"Source authority: {SOURCE_AUTHORITY}")
    print()
    print_repo_status("parent", ROOT)

    for raw_path in args.path:
        path = Path(raw_path)
        if not path.is_absolute():
            path = ROOT / path
        print_repo_status("nested", path)

    print("Read the decision files above before push, pull, sync, merge, or cross-repo copy.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
