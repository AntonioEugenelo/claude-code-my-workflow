## Summary

Added a second IO robustness figure to the live Section 5 manuscript using the counterfactual MAT files that preserve US--China bilateral links.

## Changes Made

- In `master_supporting_docs/MCMS/new_process.py`:
  - added `Figure_2b` to the direct MAT export job specs using:
    - `irf_Het_DCP_Direct2_USChi_Iso.mat`
    - `irf_Het_DCP_Direct3_Strict_USChi.mat`
  - added `IO_Average_Combined_Compare_USChi_Links.png` to the active paper figure sync list
  - added a second call to `create_average_combined_compare(...)` for the new `Figure_2b` CSV
  - extended `regenerate_csvs_from_mat(...)` allow-lists so the new time-series CSV is generated in the active manuscript pipeline
- In `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`:
  - inserted a new figure immediately after the existing IO robustness figure
  - left the surrounding prose unchanged
  - added a caption specific to the US--China-links-preserved counterfactual

## Generated Artifacts

- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_2b_Cumul_IO_Decomposition_USChiLinks_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/IO_Average_Combined_Compare_USChi_Links.png`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/IO_Average_Combined_Compare_USChi_Links.png`

## Verification

- Ran the targeted export/generation path for `Figure_2b` from source code
- Visually checked `IO_Average_Combined_Compare_USChi_Links.png`
- Compiled `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in place with:
  - `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`

## Result

- Build succeeded
- The new figure is present in `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`

## Residual Warnings

- Pre-existing undefined references remain in the manuscript
- Pre-existing multiply-defined labels remain in the manuscript
- Non-blocking `0_main.synctex.gz` file-lock warning remains during `latexmk`
