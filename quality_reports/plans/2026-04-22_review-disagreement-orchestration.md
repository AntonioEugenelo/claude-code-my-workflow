# Plan: Review Disagreement Orchestration

**Date:** 2026-04-22
**Status:** COMPLETED

## Objective

Update the Codex review workflow so that:

1. the `narrative-reviewer` agent explicitly checks for the structural rewrite principles now being used in manuscript section rewrites
2. the review orchestration stops and asks the user to resolve conflicts when review-agent sets materially disagree

## Scope

- `.codex/review_agents/narrative-reviewer.md`
- `docs/codex-workflows/adversarial-review.md`
- `docs/codex-workflows/orchestrator.md`
- `docs/codex-workflows/review-agents.md`
- `scripts/review_plan.py` if the new disagreement-stop rule should be surfaced in planner output

## Assumptions

- "Relevant instructions" for the narrative reviewer means codifying the rewrite principles that affect narrative quality directly: claim-first openings, logic-first structure, explicit asymmetries, decomposition of near-zero net effects, and bridge endings.
- "Sets of agents are going to disagree" means conflicts across reviewer families that would change implementation direction, not minor differences in emphasis or severity.
- The new stop rule should be procedural and user-facing rather than automatically resolved by the main agent.

## Planned Steps

1. Add rewrite-aware narrative-review criteria to the active prompt card.
2. Add a disagreement-escalation stop rule to the adversarial review workflow.
3. Add the same rule to the main orchestrator so it applies beyond one document-specific page.
4. Update review-agent documentation and, if useful, `scripts/review_plan.py` text output so the rule is visible during execution.
5. Verify by reading back the edited docs and running the planner on a representative paper path.

## Verification

- Read back all modified files.
- Run `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex --round 1 --adversarial`
- Confirm the docs consistently state the new disagreement-stop behavior.

## Risks

- If the disagreement rule is too broad, it may halt routine review unnecessarily.
- If the narrative prompt is too specific to one section, it may become brittle; the added criteria therefore need to be general enough to apply to analogous manuscript rewrites.
