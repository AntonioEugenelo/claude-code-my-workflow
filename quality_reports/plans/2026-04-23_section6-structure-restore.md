## Objective

Restore the active manuscript Section 6/Section 5 source in `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex` to the intended recent subsection structure, while keeping the updated cumulative figure set and the refreshed numerical interpretation.

## Scope

- Replace the current drifted `56_sectoral_channels.tex` scaffold with the intended recent section structure.
- Preserve the cumulative figure references now in use:
  - sectoral GDP bars
  - sectoral CPI bars
  - own-sector cumulative scatter
  - US and China cumulative transmission matrices
  - GDP/CPI structural-determinants `3x3` grids
- Update only the numbers and narrative needed to match the refreshed cumulative results.
- Recompile the manuscript and check the active section labels/cross-references.

## Likely Files To Change

- `quality_reports/plans/2026-04-23_section6-structure-restore.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/session_logs/2026-04-23_section6-structure-restore.md`

## Assumptions

- The user wants the structure that existed immediately before the structural-determinants variable refresh, not the older recovered Section 6 scaffold.
- `55b_sectoral_transmission_decomposition.tex` is the best local reference for that intended structure.
- The regenerated cumulative figures already on disk are correct and do not need another export pass.

## Verification

- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -g -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Check that the compiled auxiliary output contains `sec:sectoral_decomposition` and the expected subsection labels.
- Run a local consistency pass on captions and prose to confirm they describe 12-quarter cumulative objects rather than on-impact or four-quarter objects.
