#!/usr/bin/env python3
"""Plan read-only review-agent waves for a target path."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROUND_1_ONLY = {"derivation-auditor", "figure-reviewer"}

ROUTES = [
    {
        "name": "cover-letter",
        "waves": [
            ["proofreader", "domain-reviewer", "narrative-reviewer"],
            ["cover-letter-reviewer"],
        ],
        "tier": "Standard",
        "adversarial": [["devils-advocate"]],
    },
    {
        "name": "slides",
        "waves": [
            ["proofreader", "narrative-reviewer"],
            ["domain-reviewer"],
        ],
        "tier": "Standard",
        "adversarial": [["devils-advocate"]],
    },
    {
        "name": "research-paper",
        "waves": [
            ["proofreader", "derivation-auditor", "figure-reviewer"],
            ["theory-critic", "pedagogical-reviewer", "narrative-reviewer"],
        ],
        "tier": "Deep",
        "adversarial": [["devils-advocate"]],
    },
    {
        "name": "journal-review",
        "waves": [["proofreader"], ["narrative-reviewer"]],
        "tier": "Light",
        "adversarial": [["devils-advocate"]],
    },
    {
        "name": "exam-or-problem-set",
        "waves": [["proofreader"], ["domain-reviewer"]],
        "tier": "Light",
        "adversarial": [],
    },
    {
        "name": "documentation",
        "waves": [["proofreader"]],
        "tier": "Quick",
        "adversarial": [["devils-advocate"]],
    },
    {
        "name": "code-and-analysis",
        "waves": [["code-critic", "code-structurer"]],
        "tier": "Standard",
        "adversarial": [],
    },
]


def match_route(target: str) -> dict:
    normalized = target.replace("\\", "/").lower()
    suffix = Path(normalized).suffix.lower()

    if normalized.startswith("letters/") and suffix == ".tex":
        return ROUTES[0]
    if (normalized.startswith("slides/") and suffix == ".tex") or (normalized.startswith("quarto/") and suffix == ".qmd"):
        return ROUTES[1]
    if normalized.startswith("master_supporting_docs/") and suffix == ".tex":
        return ROUTES[2]
    if "review" in normalized and suffix in {".md", ".xml"}:
        return ROUTES[3]
    if any(token in normalized for token in ["exam", "pset", "tutorial"]):
        return ROUTES[4]
    if suffix in {".py", ".m", ".r"}:
        return ROUTES[6]
    if suffix == ".md":
        return ROUTES[5]
    raise SystemExit(f"No review route found for target: {target}")


def filtered_waves(route: dict, round_number: int) -> list[list[str]]:
    waves: list[list[str]] = []
    for wave in route["waves"]:
        filtered = [
            agent for agent in wave
            if round_number == 1 or agent not in ROUND_1_ONLY
        ]
        if filtered:
            waves.append(filtered)
    return waves


def build_plan(target: str, round_number: int, adversarial: bool) -> dict:
    route = match_route(target)
    waves = filtered_waves(route, round_number)
    challenge = route["adversarial"] if adversarial else []
    return {
        "target": target,
        "document_type": route["name"],
        "tier": route["tier"],
        "round": round_number,
        "read_only_agent_type": "explorer",
        "round_1_only_agents": sorted(ROUND_1_ONLY),
        "baseline_waves": waves,
        "adversarial_waves": challenge,
        "all_agents": [agent for wave in waves + challenge for agent in wave],
        "escalation_rule": (
            "If reviewer sets give materially incompatible directions, stop and ask "
            "the user to choose before implementing more fixes."
        ),
    }


def print_text(plan: dict) -> None:
    print(f"Target: {plan['target']}")
    print(f"Document type: {plan['document_type']}")
    print(f"Tier: {plan['tier']}")
    print(f"Round: {plan['round']}")
    print(f"Spawn review agents as: {plan['read_only_agent_type']} (read-only)")
    print("")
    print("Baseline review waves:")
    for idx, wave in enumerate(plan["baseline_waves"], start=1):
        print(f"  Wave {idx}: {', '.join(wave)}")
    if plan["adversarial_waves"]:
        print("")
        print("Adversarial challenge waves:")
        for idx, wave in enumerate(plan["adversarial_waves"], start=1):
            print(f"  Challenge {idx}: {', '.join(wave)}")
    print("")
    print(f"Escalation rule: {plan['escalation_rule']}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan review-agent waves for a target.")
    parser.add_argument("target", help="Target file path or pattern")
    parser.add_argument("--round", type=int, default=1, dest="round_number", help="Review round number")
    parser.add_argument("--adversarial", action="store_true", help="Include adversarial challenge waves")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    plan = build_plan(args.target, args.round_number, args.adversarial)
    if args.json:
        print(json.dumps(plan, indent=2))
    else:
        print_text(plan)


if __name__ == "__main__":
    main()
