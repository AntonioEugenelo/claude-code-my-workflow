# Plan: Section 5 Split, Determinants Restore, and Adversarial Review

**Status:** ACTIVE
**Date:** 2026-04-22
**Branch:** `codex-ecb-tariffs`
**Targets:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`, Section 5 review artifacts, and verification outputs

## Objective

1. Split the current Section 5.1 into separate aggregate-effects and sectoral-effects subsections.
2. Reintroduce the sectoral-determinants material as its own subsection, using the existing structural scatterplot grids and preserving José-Elías's live Section 5 changes outside the requested restructuring.
3. Clean obvious placeholders and editorial markup inside Section 5 so the section is reviewable.
4. Compile the manuscript and run the full Section 5 adversarial review workflow on the modified draft.

## Scope

- Primary manuscript source:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Historical source for recovered determinants material:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels_recovered_ae2e56d.tex`
- Supporting appendix source for current horse-race diagnostics:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- Build target:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Review artifacts:
  - `quality_reports/reviews/2026-04-22_section5-*.md`
- Session log:
  - `quality_reports/session_logs/2026-04-22_section5-split-determinants-adversarial-review.md`

## Constraints

- Keep edits outside Section 5 untouched.
- Preserve José-Elías's current Section 5 substance unless a change is needed to implement the requested split, restore the determinants subsection, or resolve review-blocking issues.
- Verify with a clean LaTeX build before reporting completion.
- Use the adversarial review routing defined by `scripts/review_plan.py` and `docs/codex-workflows/adversarial-review.md`.

## Planned Steps

1. Restructure `56_sectoral_channels.tex` so the current mixed 5.1 becomes:
   - aggregate effects
   - sectoral effects
   - structural determinants of sectoral rankings
2. Rewrite placeholder notes in the aggregate subsection using the current cross-section data.
3. Restore and adapt the determinants discussion from the recovered section and current appendix so the scatter grids are commented consistently with the live figures.
4. Compile `0_main.tex` into `build_verify/` and inspect errors/warnings.
5. Run the round-1 adversarial review plan and start review tracking.
6. Save round-1 reviewer-style findings on disk, apply fixes locally, rebuild, and rerun the reduced round-2 adversarial route.
7. Stop when the modified Section 5 is coherent, builds cleanly, and the final review pass has no blocking findings.

## Verification

- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex --round 1 --adversarial`
- `python scripts/review_plan.py master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex --round 2 --adversarial`
- Review artifacts written to `quality_reports/reviews/`

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/reviews/2026-04-22_section5-*.md`
- `quality_reports/session_logs/2026-04-22_section5-split-determinants-adversarial-review.md`
