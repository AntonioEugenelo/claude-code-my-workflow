# Plan: Section 4/5 Review Routing, Figure Polish, and Overleaf Markup

**Status:** ACTIVE
**Branch:** `codex-ecb-tariffs`
**Scope:** `docs/codex-workflows/`, `.codex/review_agents/`, `scripts/review_plan.py`, `master_supporting_docs/MCMS/new_process.py`, `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`, `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`

## Objective

Tighten the matrix figures and captions, add a dedicated read-only pedagogical reviewer to the Codex routing stack, then run the full Section 4/5 review loop to a 95 floor before marking Section 4 changes against the Overleaf baseline with the requested color treatment.

## Files Expected

- `.codex/review_agents/pedagogical-reviewer.md`
- `.codex/review_agents/README.md`
- `docs/codex-workflows/review-agents.md`
- `docs/codex-workflows/review-routing.md`
- `scripts/review_plan.py`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/reviews/2026-04-13_section4-5-round*.md`
- `quality_reports/session_logs/2026-04-13_section4-section5-review-routing-overleaf-markup.md`

## Execution Order

1. Add `pedagogical-reviewer` to the active review-agent cards, documentation, and review planner, keeping the route read-only and `explorer`-only.
2. Increase spillover-matrix typography again, remove matrix subtitles, and simplify the active matrix captions.
3. Regenerate figures and rebuild the manuscript in `build_verify/`.
4. Run the full routed review loop, including the new pedagogical reviewer, until each active category reaches at least `95/100`.
5. Compare Section 4 against `overleaf/master`, preserve any existing red markup, color all changed text red, and color the monetary-policy and full-DCP discussions blue.
6. Rebuild and log the final verification state.

## Non-Negotiables

- Review agents remain read-only and are always spawned as Codex `explorer` agents.
- Overleaf is comparison-only; do not push or modify the remote branch.
- Keep the current local manuscript as the editing source of truth.
- Do not revert unrelated local changes in the dirty worktree.
