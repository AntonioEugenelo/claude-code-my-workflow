Status: IN PROGRESS

Goal
- Bring the Codex branch's review stack as close as possible to the old Claude adversarial review workflow while keeping review agents read-only.

Scope
- Active review workflow docs, helper scripts, public guide docs, and repo-native review-agent definitions/prompts.
- No changes to nested project repos beyond preserving their current state.

Assumptions
- Review agents should map to Codex `explorer` agents to preserve read-only behavior.
- The old reviewer names should be retained where practical to reduce migration friction.
- Hook-based enforcement cannot be reproduced exactly, so the closest Codex equivalent is explicit routing, prompt cards, and tracked review rounds.

Likely Files
- `docs/codex-workflows/review-routing.md`
- `docs/codex-workflows/orchestrator.md`
- `docs/codex-workflows/capabilities.md`
- `docs/codex-workflows/adversarial-review.md`
- `docs/codex-workflows/review-agents.md`
- `.codex/review_agents/*.md`
- `scripts/review-mode.sh`
- `scripts/review_plan.py`
- `AGENTS.md`
- `README.md`
- `guide/workflow-guide.qmd`
- `guide/workflow-guide.html`
- `docs/workflow-guide.html`
- `docs/index.html`
- `quality_reports/specs/2026-04-13_adversarial-review-loop-port.md`
- `quality_reports/session_logs/2026-04-13_adversarial-review-loop-port.md`

Execution Steps
1. Write the spec and working log.
2. Port old reviewer roles into active Codex-native review-agent definitions with explicit read-only/explorer instructions.
3. Update routing/orchestration docs to use review agents and define the adversarial loop.
4. Add a helper script for routing/round planning and align `review-mode.sh` terminology with review agents.
5. Update top-level/public docs so the active workflow advertises the new review-agent layer.
6. Verify the helper script, tracking helper, and guide render.

Verification
- Run the new review planning helper on representative file paths.
- Run `scripts/review-mode.sh` status/start/mark/stop` as needed to verify the updated terminology still works.
- Re-render `guide/workflow-guide.qmd` if changed and sync the generated HTML.
- Read back the modified docs and search for stale review-language inconsistencies.

Known Risks
- Exact Claude hook parity is impossible; the best achievable Codex version is explicit and procedural rather than runtime-enforced.
- The repo currently has many untracked quality-report artifacts; preserve them untouched.
