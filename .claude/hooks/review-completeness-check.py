#!/usr/bin/env python3
"""Stop hook: verifies all required review agents were called per agent-routing.md.

Only enforces when a review round is explicitly active (marker file exists).
Ad-hoc agent calls never trigger this check.

Marker file is created by: scripts/review-mode.sh start "<pattern>"
"""
import json, sys, os, re

# State lives in project dir (gitignored), not system temp
STATE_DIR = os.path.join(os.environ.get('CLAUDE_PROJECT_DIR', '.'), '.claude', 'state')
REVIEW_MODE_FILE = os.path.join(STATE_DIR, 'review_active.json')
TRACKING_FILE = os.path.join(STATE_DIR, 'review_agents.txt')
CONTEXT_FILE = os.path.join(STATE_DIR, 'review_context.txt')

# Agents that only run in Round 1 (skipped in RE-SCORE rounds 2+)
ROUND_1_ONLY = {'derivation-auditor', 'figure-reviewer'}

# Routing table from agent-routing.md (path pattern → required agents)
ROUTING_TABLE = [
    ('Letters/**/*.tex',
     {'proofreader', 'domain-reviewer', 'narrative-reviewer', 'cover-letter-reviewer'}),
    ('Slides/**/*.tex',
     {'proofreader', 'narrative-reviewer', 'domain-reviewer'}),
    ('master_supporting_docs/**/*.tex',
     {'proofreader', 'derivation-auditor', 'theory-critic', 'narrative-reviewer', 'figure-reviewer'}),
    ('.py',
     {'code-critic', 'code-structurer'}),
    ('.m',
     {'code-critic', 'code-structurer'}),
    ('.R',
     {'code-critic', 'code-structurer'}),
    ('**/*review*.xml',
     {'proofreader', 'narrative-reviewer'}),
    ('**/*review*.md',
     {'proofreader', 'narrative-reviewer'}),
    ('**/*exam*.*',
     {'proofreader', 'domain-reviewer'}),
    ('**/*PSet*.*',
     {'proofreader', 'domain-reviewer'}),
    ('quality_reports/**/*.md',
     {'proofreader'}),
]


def get_called_agents():
    if not os.path.exists(TRACKING_FILE):
        return set()
    with open(TRACKING_FILE, 'r') as f:
        return set(line.strip() for line in f if line.strip())


def get_review_context():
    """Read file paths from the context file, or from the mode file's pattern."""
    paths = []
    if os.path.exists(CONTEXT_FILE):
        with open(CONTEXT_FILE, 'r') as f:
            paths = [line.strip() for line in f if line.strip()]
    # Also read the pattern from the mode file if context file is empty
    if not paths and os.path.exists(REVIEW_MODE_FILE):
        try:
            with open(REVIEW_MODE_FILE, 'r') as f:
                mode = json.load(f)
            pattern = mode.get('pattern', '')
            if pattern:
                paths = [pattern]
        except (json.JSONDecodeError, KeyError):
            pass
    return paths


def match_routing(file_paths):
    """Determine required agents from file paths using routing table."""
    required = set()
    for fpath in file_paths:
        fpath = fpath.replace('\\', '/').lower()
        for pattern, agents in ROUTING_TABLE:
            base_dir = pattern.split('/')[0].lower() if '/' in pattern else ''
            ext = os.path.splitext(pattern)[1].lower()
            if base_dir and base_dir in fpath and (not ext or fpath.endswith(ext)):
                required |= agents
                break
            elif not base_dir and ext and fpath.endswith(ext):
                required |= agents
                break
    return required


def reset_tracking():
    """Clean up all review state files (mode + tracking)."""
    for f in [REVIEW_MODE_FILE, TRACKING_FILE, CONTEXT_FILE]:
        if os.path.exists(f):
            os.remove(f)


# --- Main ---

# Only enforce when a review round is explicitly active
if not os.path.exists(REVIEW_MODE_FILE):
    sys.exit(0)

# Read hook input
try:
    hook_input = json.load(sys.stdin)
except (json.JSONDecodeError, EOFError):
    hook_input = {}

# If stop_hook_active, Claude is already continuing from a previous
# Stop hook block — let it stop this time to avoid infinite loops.
if hook_input.get("stop_hook_active", False):
    reset_tracking()
    sys.exit(0)

called = get_called_agents()
context_files = get_review_context()
required = match_routing(context_files) if context_files else set()

# Check round number from mode file — round 2+ skips ROUND_1_ONLY agents
try:
    with open(REVIEW_MODE_FILE, 'r') as f:
        mode = json.load(f)
    review_round = mode.get('round', 1)
except (json.JSONDecodeError, KeyError, FileNotFoundError):
    review_round = 1

if review_round > 1:
    required -= ROUND_1_ONLY

# Enforce completeness
if required:
    missing = required - called
    if missing:
        result = {
            "decision": "block",
            "reason": (
                f"Review round incomplete. Missing required agents: {', '.join(sorted(missing))}. "
                f"Called so far: {', '.join(sorted(called))}. "
                f"Per agent-routing.md, the following agents are required: "
                f"{', '.join(sorted(required))}."
            )
        }
        print(json.dumps(result))
    else:
        # All agents called — review round complete, clean up
        reset_tracking()
