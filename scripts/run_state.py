#!/usr/bin/env python3
"""Track the current long-running job in quality_reports/run_state/current.json."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
STATE_DIR = ROOT / "quality_reports" / "run_state"
STATE_FILE = STATE_DIR / "current.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def git_value(args: list[str]) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=ROOT, text=True, stderr=subprocess.DEVNULL).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def read_state() -> dict[str, Any]:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"status": "corrupt", "path": str(STATE_FILE)}


def write_state(state: dict[str, Any]) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, sort_keys=True), encoding="utf-8")


def start(args: argparse.Namespace) -> int:
    if STATE_FILE.exists() and not args.force:
        state = read_state()
        status = state.get("status")
        if status in {"planned", "running"}:
            print(f"Active run already exists: {STATE_FILE}")
            print(json.dumps(state, indent=2, sort_keys=True))
            return 2

    state = {
        "name": args.name,
        "status": "running",
        "stage": args.stage or "started",
        "message": args.message or "",
        "command": args.command,
        "run_card": args.run_card,
        "expected_outputs": args.expected_output,
        "started_at": now_iso(),
        "updated_at": now_iso(),
        "pid": args.pid or os.getpid(),
        "cwd": str(ROOT),
        "git_branch": git_value(["branch", "--show-current"]),
        "git_sha": git_value(["rev-parse", "--short", "HEAD"]),
    }
    write_state(state)
    print(f"Started run state: {STATE_FILE}")
    return 0


def update(args: argparse.Namespace) -> int:
    state = read_state()
    if not state:
        print(f"No run state found at {STATE_FILE}")
        return 2
    if args.stage:
        state["stage"] = args.stage
    if args.message:
        state["message"] = args.message
    if args.expected_output:
        existing = list(state.get("expected_outputs", []))
        existing.extend(args.expected_output)
        state["expected_outputs"] = existing
    state["updated_at"] = now_iso()
    write_state(state)
    print(f"Updated run state: {STATE_FILE}")
    return 0


def finish(args: argparse.Namespace) -> int:
    state = read_state()
    if not state:
        print(f"No run state found at {STATE_FILE}")
        return 2
    state["status"] = args.status
    state["message"] = args.message or state.get("message", "")
    state["finished_at"] = now_iso()
    state["updated_at"] = now_iso()
    write_state(state)
    print(f"Finished run state: {STATE_FILE}")
    return 0


def status(_: argparse.Namespace) -> int:
    state = read_state()
    if not state:
        print(f"No run state found at {STATE_FILE}")
        return 1
    print(json.dumps(state, indent=2, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command_name", required=True)

    p_start = sub.add_parser("start", help="Create or replace current run state")
    p_start.add_argument("--name", required=True)
    p_start.add_argument("--command", required=True)
    p_start.add_argument("--run-card", default="")
    p_start.add_argument("--stage", default="")
    p_start.add_argument("--message", default="")
    p_start.add_argument("--expected-output", action="append", default=[])
    p_start.add_argument("--pid", type=int, default=0)
    p_start.add_argument("--force", action="store_true")
    p_start.set_defaults(func=start)

    p_update = sub.add_parser("update", help="Update current run progress")
    p_update.add_argument("--stage", default="")
    p_update.add_argument("--message", default="")
    p_update.add_argument("--expected-output", action="append", default=[])
    p_update.set_defaults(func=update)

    p_finish = sub.add_parser("finish", help="Mark current run finished")
    p_finish.add_argument("--status", choices=["succeeded", "failed", "cancelled"], required=True)
    p_finish.add_argument("--message", default="")
    p_finish.set_defaults(func=finish)

    p_status = sub.add_parser("status", help="Print current run state")
    p_status.set_defaults(func=status)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
