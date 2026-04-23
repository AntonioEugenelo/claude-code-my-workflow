# Plan: Section 5 Three-Layer Rewrite

**Status:** ACTIVE
**Date:** 2026-04-15
**Branch:** `codex-ecb-tariffs`

## Objective

Rewrite the active Section 5 around a three-layer decomposition of tariff transmission, verify the manuscript build, and run the full adversarial review loop on the rewritten section.

## Scope

- Primary source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Build target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Spec: `quality_reports/specs/2026-04-15_section5-three-layer-rewrite.md`
- Session log: `quality_reports/session_logs/2026-04-15_section5-three-layer-rewrite.md`
- Review artifacts: `quality_reports/reviews/2026-04-15_section5-three-layer-*.md`

## Assumptions

1. The live Section 5 remains `56_sectoral_channels.tex`, not archived `55_*.tex` drafts.
2. The rewrite can preserve the current figure set and subsection count if the prose structure becomes materially clearer.
3. Reviewer findings will be integrated locally in the main thread; review agents remain read-only.

## Planned Steps

1. Rewrite the section outline and main argument so it follows the user-specified three-layer decomposition, with a distinct euro-area payoff subsection.
2. Revise subsection transitions and mechanism claims so each block does one analytical job and uses model numbers rather than figure narration.
3. Build `0_main.tex` with `latexmk` and inspect the output for blocking issues.
4. Run `python scripts/review_plan.py ... --round 1 --adversarial` and start tracked review mode for the rewritten Section 5.
5. Run the full routed review sequence, including the adversarial challenge pass, save all findings on disk, and apply fixes locally.
6. Rebuild and rerun the required review agents until the section clears at least the `95/100` external-review gate or a blocker stops progress.

## Verification

- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex --round 1 --adversarial`
- Review reports exist on disk for every routed reviewer in the completed round
- Final build succeeds after the last material review-driven fix

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/specs/2026-04-15_section5-three-layer-rewrite.md`
- `quality_reports/plans/2026-04-15_section5-three-layer-rewrite.md`
- `quality_reports/session_logs/2026-04-15_section5-three-layer-rewrite.md`
- `quality_reports/reviews/2026-04-15_section5-three-layer-*.md`
