#!/usr/bin/env python3
"""PostToolUse hook for Agent: tracks which review agents have been called.

Only tracks when an explicit review round is active (marker file exists).
Ad-hoc agent calls are ignored — no tracking, no enforcement.

Marker file is created by: scripts/review-mode.sh start "<pattern>"
"""
import json, sys, os, re

# State lives in project dir (gitignored), not system temp
STATE_DIR = os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude', 'state')
REVIEW_MODE_FILE = os.path.join(STATE_DIR, 'review_active.json')
TRACKING_FILE = os.path.join(STATE_DIR, 'review_agents.txt')
CONTEXT_FILE = os.path.join(STATE_DIR, 'review_context.txt')

REVIEW_AGENTS = {'proofreader', 'narrative-reviewer', 'theory-critic', 'domain-reviewer',
                 'derivation-auditor', 'cover-letter-reviewer', 'pedagogy-reviewer',
                 'slide-auditor', 'tikz-reviewer', 'r-reviewer',
                 'code-critic', 'code-structurer', 'figure-reviewer'}

try:
    # Only track if a review round is explicitly active
    if not os.path.exists(REVIEW_MODE_FILE):
        sys.exit(0)

    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    agent_type = tool_input.get('subagent_type', '')

    if agent_type in REVIEW_AGENTS:
        os.makedirs(STATE_DIR, exist_ok=True)

        # Log agent type
        with open(TRACKING_FILE, 'a') as f:
            f.write(f'{agent_type}\n')

        # Extract file paths from prompt for routing context
        prompt = tool_input.get('prompt', '')
        paths = re.findall(r'[A-Za-z]:[^\s\n"\']+\.(?:tex|qmd|md|R|py|xml)', prompt)
        paths += re.findall(r'/[^\s\n"\']+\.(?:tex|qmd|md|R|py|xml)', prompt)
        if paths:
            with open(CONTEXT_FILE, 'a') as f:
                for p in paths:
                    f.write(f'{p}\n')
except Exception:
    pass
