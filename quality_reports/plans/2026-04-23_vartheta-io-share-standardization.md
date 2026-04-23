## Objective

Standardize the terminology for `\vartheta` across the manuscript and structural-determinants figures so it is referred to as the `IO share`, not `IO centrality`.

## Scope

- Update the active manuscript text in `0_clean`.
- Update appendix text and generated appendix table notes that are compiled into `0_main.tex`.
- Update the active structural-determinants figure generator labels in `master_supporting_docs/MCMS/new_process.py`.
- Regenerate the affected structural-determinants figures and recompile the manuscript in `0_clean`.

## Files Likely To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/*.tex` where the note text names `\vartheta`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_Structural_Determinants_GDP_3x3.png`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_Structural_Determinants_CPI_3x3.png`

## Assumptions

- The user wants the compiled manuscript to be internally consistent first; inactive draft files outside the active compile path are lower priority unless they directly affect the generated figure/text assets.
- `IO share` is the preferred display label for `\vartheta_{ki}` in prose, captions, and chart axes/titles.
- Recompiling `0_main.tex` in `0_clean` remains the correct verification target.

## Verification

- Search the active compile path and the structural-determinants chart generator for `IO centrality` after the edits and confirm it is gone.
- Regenerate the structural-determinants charts used in the paper.
- Run `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` in `master_supporting_docs/Tariffs_ECB/0_clean`.
