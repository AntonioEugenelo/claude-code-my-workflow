## Summary

Updated Section 6 of the Tariffs_ECB manuscript to restore the cross-country own-sector scatter in 6.3, add a brief determinants subsection under 6.2, remove Appendix B dependence from the section text, and trim the structural scatter grids by dropping the consumption-share column.

## Files Changed

- `quality_reports/plans/2026-04-22_section6-restore-scatter-and-determinants.md`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- regenerated structural figure outputs under `master_supporting_docs/MCMS/output_python/extra_charts/`
- synced figure copies under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`

## What Changed

- Patched the active structural-scatter generator to remove the consumption-share column and render a `3x3` layout while keeping the existing output filenames.
- Regenerated:
  - `Fig_CN_Structural_Scatter.png`
  - `Fig_US_Structural_Scatter_3x4.png`
  - `Fig_CHN_Structural_Scatter_3x4.png`
  - `Fig_EA_Structural_Scatter_3x4.png`
- Rewrote `56_sectoral_channels.tex` to:
  - keep Section 6 self-contained,
  - add `6.2.1 Determinants of Sectoral Transmission`,
  - move the cross-country own-sector scatter into `6.3`,
  - update matrix language to refer to sectoral CPI contributions,
  - remove placeholder text, red text, Appendix B references, and most sector-by-sector numerical dumps.
- Renamed the new main-text structural-scatter labels to avoid collisions with appendix-era labels that are still present elsewhere in the manuscript.

## Verification

- Confirmed the updated section file contains no Appendix/appendix references or stale `Consumption Share` wording.
- Rebuilt the manuscript from `master_supporting_docs/Tariffs_ECB/0_clean/` with:
  - `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- Compile succeeded after the label rename.

## Residual Issues

- The full manuscript still has pre-existing warnings outside this task:
  - duplicate equation labels (`eq:general_model_price_setting_foreign`, `eq:budget_constraint`, `eq:calvo_inflation_dynamics_2`)
  - undefined references including `sec:benchmark`, `sec:analytical_insights`, and `eq:general_model_budget_constraint`
- These warnings were already in the manuscript build and were not introduced by the Section 6 rewrite.
