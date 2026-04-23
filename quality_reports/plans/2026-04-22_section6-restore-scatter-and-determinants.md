## Objective

Restore the cross-country own-sector scatter in Section 6.3, add a brief self-contained determinants subsection under Section 6.2 using the recovered sectoral-channel material, remove consumption-share columns from the structural scatter grids, and rewrite the section so it stands on its own without Appendix B references or numerical-dump prose.

## Scope

- Update the structural-scatter figure generator in `master_supporting_docs/MCMS/new_process.py`.
- Regenerate the affected structural-scatter figure files and sync them into the paper figures directory.
- Rewrite `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex` to:
  - add a `6.2.1` determinants subsection,
  - restore the US/China/euro-area own-sector scatter in `6.3`,
  - remove Appendix B references,
  - shorten and de-numericalize the prose where possible.
- Recompile the manuscript and confirm the section builds cleanly.

## Assumptions

- “the scatterplot with the US CN and EA point with value added and inflation” refers to the existing cross-country own-sector scatter figure currently stored as `Fig_CN_Structural_Scatter.png`, now using exact sectoral CPI contributions on the vertical axis.
- “remove from the scatterplots the consumption share columns” refers to the structural determinant grid figures for the US, China, and the euro area.
- Keeping explanations brief means prioritizing directional and comparative claims over sector-by-sector number dumps.

## Planned Steps

1. Modify the structural determinant figure generator to drop the consumption-share column and regenerate the three grid figures.
2. Rewrite Section 6 around the current figure set, adding `6.2.1` for determinants and restoring the cross-country own-sector scatter in `6.3`.
3. Remove Appendix B cross-references and replace them with direct, self-contained claims supported by the figures in the section.
4. Compile `0_main.tex`, check the updated section, and note any residual warnings or issues.

## Verification

- The regenerated structural determinant figures render successfully and no longer include the consumption-share column.
- `56_sectoral_channels.tex` contains the requested subsection structure and no Appendix B references.
- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex` succeeds from `master_supporting_docs/Tariffs_ECB/0_clean/`.

## Likely Files To Change

- `quality_reports/plans/2026-04-22_section6-restore-scatter-and-determinants.md`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- regenerated structural figure outputs under `master_supporting_docs/MCMS/output_python/extra_charts/`
- synced figure copies under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
