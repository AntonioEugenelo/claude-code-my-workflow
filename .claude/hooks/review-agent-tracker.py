#!/usr/bin/env python3
"""PostToolUse hook for Agent: tracks which review agents have been called.

Appends the subagent_type to a tracking file and extracts file paths from
the prompt to determine routing context.
"""
import json, sys, os, re, tempfile

TRACKING_FILE = os.path.join(tempfile.gettempdir(), 'claude_review_agents.txt')
CONTEXT_FILE = os.path.join(tempfile.gettempdir(), 'claude_review_context.txt')

REVIEW_AGENTS = {'proofreader', 'narrative-reviewer', 'theory-critic', 'domain-reviewer',
                 'derivation-auditor', 'cover-letter-reviewer', 'pedagogy-reviewer',
                 'slide-auditor', 'tikz-reviewer', 'r-reviewer',
                 'code-critic', 'code-structurer'}

try:
    data = json.load(sys.stdin)
    tool_input = data.get('tool_input', {})
    agent_type = tool_input.get('subagent_type', '')

    if agent_type in REVIEW_AGENTS:
        # Log agent type
        with open(TRACKING_FILE, 'a') as f:
            f.write(f'{agent_type}\n')

        # Extract file paths from prompt for routing context
        prompt = tool_input.get('prompt', '')
        # Match common path patterns
        paths = re.findall(r'[A-Za-z]:[^\s\n"\']+\.(?:tex|qmd|md|R|py|xml)', prompt)
        paths += re.findall(r'/[^\s\n"\']+\.(?:tex|qmd|md|R|py|xml)', prompt)
        if paths:
            with open(CONTEXT_FILE, 'a') as f:
                for p in paths:
                    f.write(f'{p}\n')
except Exception:
    pass
