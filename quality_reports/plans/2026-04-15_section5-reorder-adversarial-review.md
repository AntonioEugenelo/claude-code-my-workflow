# Plan: Section 5 Reorder and Adversarial Review

**Status:** ACTIVE
**Date:** 2026-04-15
**Branch:** `codex-ecb-tariffs`
**Targets:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`, Section 5 review artifacts, and supporting verification outputs

## Objective

1. Swap the current Section 5.2 and 5.3 blocks in the active manuscript source.
2. Preserve internal coherence after the reorder by updating bridge text as needed.
3. Verify the manuscript with a clean LaTeX build.
4. Run the full adversarial review loop on Section 5 using the repo's read-only review agents.
5. Record the current MATLAB benchmark entrypoint and Dynare bytecode location for handoff clarity.

## Scope

- Primary manuscript source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Build target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Review routing target: the active Section 5 source file above
- Review artifacts: `quality_reports/reviews/2026-04-15_section5-*.md`
- Session log: `quality_reports/session_logs/2026-04-15_section5-reorder-adversarial-review.md`

## Assumptions

- "Swap Section 5.2 and 5.3" refers to the second and third `\subsection` blocks inside `56_sectoral_channels.tex`.
- The requested adversarial review should be run on the current active Section 5 source after the reorder, not on archived or superseded drafts.
- The clean benchmark MATLAB entrypoint should be reported from the current tracked MCMS pipeline rather than from missing untracked helper scripts mentioned in older logs.

## Planned Steps

1. Reorder the 5.2 and 5.3 subsection blocks in `56_sectoral_channels.tex`.
2. Update local transition text and roadmap wording so the new order reads cleanly.
3. Build `0_main.tex` into `build_verify/` and inspect the result for blocking errors.
4. Run `python scripts/review_plan.py ... --round 1 --adversarial` and start tracked review mode.
5. Launch the routed read-only review agents wave by wave, save findings on disk, and aggregate blocking issues.
6. Apply fixes locally, rebuild, and rerun the reduced adversarial route until the active reviewers clear the `90/100` gate or a blocker stops progress.

## Verification

- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex --round 1 --adversarial`
- Review artifacts exist on disk for each required review wave and rerun
- Final active reviewer scores are rechecked on the current file, not estimated from memory

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/session_logs/2026-04-15_section5-reorder-adversarial-review.md`
- `quality_reports/reviews/2026-04-15_section5-adversarial-round1.md`
- `quality_reports/reviews/2026-04-15_section5-adversarial-round2.md` if rerun is needed
