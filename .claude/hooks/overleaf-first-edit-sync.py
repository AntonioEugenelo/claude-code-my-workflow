#!/usr/bin/env python3
"""PreToolUse hook for Edit/Write: syncs from Overleaf before first edit to Tariffs_ECB.

On first edit to any file under master_supporting_docs/Tariffs_ECB/, pulls
from Overleaf to ensure the local copy is current. Runs once per session
(tracked by a marker file that resets when the session ends).

Never blocks edits — if sync fails, it warns and continues.
"""
import json, sys, os, subprocess

PROJECT_DIR = os.environ.get('CLAUDE_PROJECT_DIR', '.')
STATE_DIR = os.path.join(PROJECT_DIR, '.claude', 'state')
SYNC_MARKER = os.path.join(STATE_DIR, 'overleaf_synced_this_session')
SYNC_SCRIPT = os.path.join(PROJECT_DIR, 'scripts', 'sync-overleaf.sh')

try:
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    file_path = tool_input.get('file_path', '')

    # Only care about Tariffs_ECB files
    if 'Tariffs_ECB' not in file_path.replace('\\', '/'):
        sys.exit(0)

    # Only sync once per session
    if os.path.exists(SYNC_MARKER):
        sys.exit(0)

    # Create marker FIRST to avoid re-triggering on concurrent edits
    os.makedirs(STATE_DIR, exist_ok=True)
    with open(SYNC_MARKER, 'w') as f:
        f.write('synced')

    # Run pull from Overleaf
    result = subprocess.run(
        ['bash', SYNC_SCRIPT, 'pull'],
        capture_output=True, text=True, timeout=60,
        cwd=PROJECT_DIR
    )

    if result.returncode != 0:
        stderr_short = result.stderr.strip()[:200] if result.stderr else 'unknown error'
        print(json.dumps({
            "decision": "approve",
            "reason": f"Overleaf sync warning (edit proceeding anyway): {stderr_short}"
        }))
    else:
        print(json.dumps({
            "decision": "approve",
            "reason": "Pulled latest from Overleaf before editing Tariffs_ECB."
        }))

except Exception as e:
    # Never block edits due to sync issues
    try:
        print(json.dumps({
            "decision": "approve",
            "reason": f"Overleaf sync skipped ({e}). Edit proceeding."
        }))
    except Exception:
        pass
