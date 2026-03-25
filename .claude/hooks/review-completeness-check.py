#!/usr/bin/env python3
"""Stop hook: verifies all required review agents were called per agent-routing.md.

Reads the routing table dynamically to determine required agents based on
which files were being reviewed. Blocks if any required agent is missing.
Resets the tracking file after a successful check.
"""
import json, sys, os, re, tempfile, fnmatch

TRACKING_FILE = os.path.join(tempfile.gettempdir(), 'claude_review_agents.txt')
CONTEXT_FILE = os.path.join(tempfile.gettempdir(), 'claude_review_context.txt')

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
    """Read what files are being reviewed from the context file."""
    if not os.path.exists(CONTEXT_FILE):
        return []
    with open(CONTEXT_FILE, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def match_routing(file_paths):
    """Determine required agents from file paths using routing table."""
    required = set()
    for fpath in file_paths:
        fpath = fpath.replace('\\', '/').lower()
        for pattern, agents in ROUTING_TABLE:
            # Convert glob pattern to a simple substring + extension check
            # e.g., 'master_supporting_docs/**/*.tex' → check if path contains
            # 'master_supporting_docs/' and ends with '.tex'
            parts = pattern.replace('**/', '').replace('*', '')
            base_dir = pattern.split('/')[0].lower() if '/' in pattern else ''
            ext = os.path.splitext(pattern)[1].lower()
            if base_dir and base_dir in fpath and (not ext or fpath.endswith(ext)):
                required |= agents
                break
            elif not base_dir and ext and fpath.endswith(ext):
                # Extension-only patterns like '*.md'
                required |= agents
                break
    return required


def reset_tracking():
    for f in [TRACKING_FILE, CONTEXT_FILE]:
        if os.path.exists(f):
            os.remove(f)


called = get_called_agents()
context_files = get_review_context()

# Determine required agents
if context_files:
    required = match_routing(context_files)
else:
    # Fallback: if no context file, infer from which agents were called
    # If any review agent was called, require the research paper set as default
    if called:
        required = {'proofreader', 'narrative-reviewer', 'theory-critic'}
    else:
        required = set()

# Only enforce if at least one review agent was called
if called and required:
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
        reset_tracking()
