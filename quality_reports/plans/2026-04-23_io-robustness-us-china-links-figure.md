## Objective

Add a new manuscript figure immediately after the existing IO robustness check in Section 5. The new figure should replicate the existing chart layout, but use the alternative IO counterfactual MAT files that preserve US--China bilateral links.

## Scope

- Reuse the active IO robustness chart design in `master_supporting_docs/MCMS/new_process.py`.
- Build a second figure from:
  - `irf_Het_DCP_Direct2_USChi_Iso.mat`
  - `irf_Het_DCP_Direct3_Strict_USChi.mat`
- Sync the new figure into `master_supporting_docs/Tariffs_ECB/0_clean/figures/`.
- Insert the new figure environment immediately after the existing IO robustness figure in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`.
- Do not change surrounding prose. Only add the new figure and its caption/label.

## Likely Files To Change

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- generated figure asset under `master_supporting_docs/MCMS/output_python/extra_charts/`
- synced figure asset under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`

## Assumptions

- “No international IO and no all IO MAT files which keep the US China bilateral links” refers to:
  - `Direct2_USChi_Iso`: remove all international IO except US--China bilateral links, keep domestic IO
  - `Direct3_Strict_USChi`: keep only US--China bilateral links, remove domestic IO and all other international IO
- The new figure should use the same benchmark comparator and the same three-year-average transformation as the existing IO robustness figure.

## Verification

- Regenerate the new figure from source code rather than by hand.
- Confirm the new asset is copied into `0_clean/figures/`.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in place.
- Check that the new figure appears in the manuscript and that the build succeeds or only shows pre-existing warnings.
