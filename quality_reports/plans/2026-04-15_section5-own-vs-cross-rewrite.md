# Plan: Section 5 Own-vs-Cross Rewrite

**Status:** ACTIVE
**Date:** 2026-04-15

## Objective

Rewrite active Section 5 around an own-sector versus cross-sector decomposition, add a data-based service-demand discussion, verify the manuscript build, and then start the full adversarial review workflow.

## Scope

- Primary source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Verification target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Supporting evidence: benchmark transmission CSVs in `master_supporting_docs/MCMS/output_python/extra_charts/`
- Tracking files:
  - `quality_reports/specs/2026-04-15_section5-own-vs-cross-rewrite.md`
  - `quality_reports/session_logs/2026-04-15_section5-own-vs-cross-rewrite.md`

## Assumptions

1. The current figure set remains usable after the prose rewrite.
2. The benchmark transmission decomposition is sufficient to support a careful "household-demand-dominant vs intermediate/cost-dominant" discussion for the largest US losses.
3. The full adversarial review can be started immediately after the rewrite even if its later rounds extend beyond the rewrite itself.

## Planned Steps

1. Save the new spec, plan, and session log for this rewrite pass.
2. Extract the sector examples and quantitative comparisons needed for the service-loss discussion.
3. Rewrite Section 5 in `56_sectoral_channels.tex` with:
   - neutral non-Eugenelo prose
   - own-sector versus cross-sector framing
   - simultaneous-effect language
   - data-based service-demand discussion
4. Rebuild `0_main.tex` with `latexmk` and confirm the section compiles cleanly.
5. Start the adversarial review workflow:
   - run `python scripts/review_plan.py ... --round 1 --adversarial`
   - start `scripts/review-mode.sh`
   - record the routed review waves in the session log

## Verification

- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex --round 1 --adversarial`
- `scripts/review-mode.sh start "master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex" 1`

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/specs/2026-04-15_section5-own-vs-cross-rewrite.md`
- `quality_reports/plans/2026-04-15_section5-own-vs-cross-rewrite.md`
- `quality_reports/session_logs/2026-04-15_section5-own-vs-cross-rewrite.md`
