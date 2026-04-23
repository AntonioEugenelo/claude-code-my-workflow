## Summary

Corrected the active Section 6 after an earlier pass had updated the preserved Section 7 copy instead of the live sectoral-decomposition section. Section 6 now contains the requested `6.2.1` subsection, the restored cross-country own-sector scatter in `6.3`, and self-contained prose that no longer relies on Appendix B for the main claims.

## Files Changed

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/13_roadmap.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`

## What Changed

- Rewrote the active Section 6 to:
  - add `6.2.1 Determinants of Sectoral Transmission`,
  - restore the US/China/euro-area own-sector scatter to `6.3`,
  - update all price-side references from legacy “inflation” wording to the corrected CPI-contribution object,
  - remove direct references to Appendix B / `sec:horse_race`,
  - cut most numerical-dump prose in favor of brief directional claims supported by the figures in the section.
- Updated the roadmap so Section 6 is described as self-contained instead of appendix-backed.
- Removed the appendix’s redundant structural-scatter-panel subsection, which had become inconsistent with the new main-text placement and the updated `3x3` figure layout.
- Corrected the remaining appendix heatmap caption to say “CPI contribution” instead of “inflation”.

## Verification

- Recompiled with:
  - `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- Confirmed from `build_verify/0_main.aux`:
  - `6.2.1 Determinants of Sectoral Transmission`
  - `6.3 Direct Incidence Inside the Tariffed Sector`
  - restored `Fig_CN_Structural_Scatter` now appears in Section 6 as `fig:new_cn_scatter`
- Confirmed Appendix B no longer contains the duplicated structural-scatter-panel subsection.

## Residual Issues

- The full manuscript still has pre-existing warnings outside this task:
  - duplicate equation labels (`eq:general_model_price_setting_foreign`, `eq:budget_constraint`, `eq:calvo_inflation_dynamics_2`)
  - undefined references including `sec:benchmark`, `sec:analytical_insights`, and `eq:general_model_budget_constraint`
- These were not introduced by the Section 6 fix.

## Follow-up Revision

- Refined `6.2.1` to make bilateral trade share the first mechanism and to define all three structural objects directly in the main text.
- Added `6.2.2 Evidence from the Structural Scatterplots`, with the evidence claim tightened to the regenerated charts: bilateral trade exposure visibly organizes the US and China cross sections, while IO centrality and price flexibility are harder to isolate in raw scatter space because model feedbacks mix them with broader equilibrium adjustments.
- Expanded `6.4 Cross-Sector Propagation in the United States and China` so the matrix discussion now emphasizes mechanism: US sign reversals through service-heavy offsets, Chinese amplification through broader domestic propagation, and the more localized role of CPI contributions.
- Expanded `6.5 The Euro Area as an Offsetting-Margins Object` to reconnect the euro-area subsection to the restored scatter and structural-scatter evidence.
- Recompiled successfully with `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex` and confirmed from `build_verify/0_main.aux` that `6.2.2` is present and `6.4`/`6.5` are correctly numbered.
