#!/usr/bin/env python3
"""
Agent Learning Reminder — PostToolUse hook for the Agent tool.

After a review agent finishes, injects a one-line reminder into Claude's
context to watch for user corrections that should become learned checks.

Token cost: ~30 tokens per review agent invocation (one sentence).
Only fires for review-type subagents, not general-purpose agents.
"""

import json
import sys

REVIEW_AGENTS = {
    "proofreader",
    "domain-reviewer",
    "narrative-reviewer",
    "theory-critic",
    "derivation-auditor",
    "cover-letter-reviewer",
    "slide-auditor",
    "pedagogy-reviewer",
    "tikz-reviewer",
    "r-reviewer",
    "quarto-critic",
}


def main():
    try:
        hook_input = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    tool_input = hook_input.get("tool_input", {})
    subagent_type = tool_input.get("subagent_type", "")

    if subagent_type in REVIEW_AGENTS:
        output = {
            "decision": "allow",
            "reason": (
                f"AGENT LEARNING: {subagent_type} review complete. "
                f"If the user identifies issues this agent missed, "
                f"update .claude/agents/{subagent_type}.md with a learned check "
                f"(per agent-learning.md) or suggest the user run /learn."
            ),
        }
        json.dump(output, sys.stdout)

    sys.exit(0)


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Fail open — never block Claude due to a hook bug
        sys.exit(0)
