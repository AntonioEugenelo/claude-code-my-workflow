## Objective

Fix the sectoral transmission matrix ordering so upstreamness is computed from the full calibration rather than the filtered calibration, then regenerate the affected figures and verify that the x-axis ordering is no longer degenerate.

## Scope

- Edit `master_supporting_docs/MCMS/new_process.py`
- Regenerate:
  - `master_supporting_docs/MCMS/output_python/extra_charts/Fig_SectoralSpillover_USA.png`
  - `master_supporting_docs/MCMS/output_python/extra_charts/Fig_SectoralSpillover_CHN.png`
  - `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
- Sync regenerated figures into:
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
- Recompile:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Assumptions

1. Upstreamness should be based on the unfiltered domestic IO structure.
2. `output_matlab/calib_full.mat` is the intended calibration source for that ordering object.
3. No manuscript prose changes are needed if only the ordering changes.

## Planned Steps

1. Patch the upstreamness helper to read `calib_full.mat` instead of `calib.mat`.
2. Add a guard that catches degenerate domestic IO matrices early.
3. Regenerate the spillover matrix CSV and the USA/CHN matrix PNGs.
4. Verify that the own-sector x-positions are no longer contiguous in the regenerated output.
5. Recompile `0_main.tex` in place and report the result.

## Verification

- `compute_country_upstreamness` produces dispersed sector ranks rather than a flat vector of ones.
- The regenerated matrix CSV shows scattered own-sector column ranks for the 20 tariffed sectors.
- The paper figures match the regenerated MCMS exports.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` succeeds in `0_clean/`.
