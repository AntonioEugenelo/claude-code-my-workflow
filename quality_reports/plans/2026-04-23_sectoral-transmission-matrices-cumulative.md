# Plan: Sectoral Transmission Matrices to Three-Year Cumulative Metrics

**Status:** COMPLETED
**Date:** 2026-04-23

## Objective

Switch the active USA and China sectoral transmission matrices from impact GDP and 4-quarter inflation objects to 12-quarter cumulative GDP and inflation objects, then regenerate the figures and update the manuscript discussion accordingly.

## Scope

- Generator:
  - `master_supporting_docs/MCMS/new_process.py`
- Active manuscript sources:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Verification targets:
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_CN_Structural_Scatter.png`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_SectoralSpillover_USA.png`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_SectoralSpillover_CHN.png`
- `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Assumptions

1. Three-year cumulative means summing quarters `0` through `11`.
2. The top matrix panel should remain a GDP-contribution decomposition, but with cumulative sectoral value-added responses replacing impact responses.
3. Existing figure labels can remain unchanged; only the underlying data and surrounding text need to change.

## Planned Steps

1. Update the spillover extraction path in `new_process.py` to sum the 12-quarter sectoral VA and CPI responses and repoint the internal validation checks to cumulative reference columns.
2. Update matrix color-bar labels and CSV field semantics so the exported artifacts describe the cumulative objects correctly.
3. Revise the Section 5 and Section 6 figure captions and any nearby explanatory text that still describe on-impact GDP or four-quarter inflation.
4. Regenerate the active matrix figures from source and refresh the own-sector scatter after the user's follow-up changes.
5. Recompile `0_main.tex` and verify the new matrix captions and figure outputs are active.
6. Record the work in a session log and close out the plan.

## Verification

- `Figure_SectoralSpillover_Matrix.csv` contains cumulative GDP and CPI contributions consistent with the 12-quarter benchmark cross-section columns.
- `Fig_CN_Structural_Scatter.png`, `Fig_SectoralSpillover_USA.png`, and `Fig_SectoralSpillover_CHN.png` are regenerated after the code change.
- `latexmk -g -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex` succeeds.
- The active manuscript source no longer describes these matrices as on-impact GDP or four-quarter inflation.
