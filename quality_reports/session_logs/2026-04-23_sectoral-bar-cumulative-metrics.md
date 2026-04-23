# 2026-04-23 Sectoral Bar Cumulative Metrics

## Summary

Updated the sectoral aggregate bar figures to use 12-quarter cumulative GDP and CPI inflation contributions instead of the previous on-impact GDP and 4-quarter CPI metrics.

## Files Changed

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/0_verify_sectoral_cumulative_figures.tex`

## Verification

- Regenerated the bar figures via `python new_process.py`.
- Confirmed the refreshed PNGs show three-year cumulative GDP and CPI inflation labels.
- Full `0_main.tex` build is currently blocked by a pre-existing missing appendix asset:
  - `figures/Fig_Structural_Determinants_GDP_3x3.png`
- Verified the edited sectoral sections by compiling:
  - `master_supporting_docs/Tariffs_ECB/0_clean/build_verify/0_verify_sectoral_cumulative_figures.pdf`

## Notes

- Updated both active references to the bar figures:
  - Section 5 (`55b_sectoral_transmission_decomposition.tex`)
  - Preserved Overleaf Section 6 (`56_sectoral_channels.tex`)
- Adjusted the Section 6 matrix discussion so it no longer incorrectly states that the on-impact spillover rows reproduce the now-cumulative bar figures.
