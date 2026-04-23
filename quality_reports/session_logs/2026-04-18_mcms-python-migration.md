Date: 2026-04-18

Task: MCMS Python migration for horse-race appendix workflow

Summary:
- Moved the real horse-race Python source files into `master_supporting_docs/MCMS/`:
  - `horse_race_data.py`
  - `horse_race_regression_utils.py`
  - `run_horse_race_appendix.py`
  - `run_stacked_regressions.py`
- Replaced the paper-side files in `master_supporting_docs/Tariffs_ECB/0_clean/` with compatibility wrappers that delegate to MCMS.
- Updated MCMS path resolution so the appendix runner writes paper-facing outputs back into `Tariffs_ECB/0_clean/generated/`.
- Updated `master_supporting_docs/MCMS/README.md` and `master_supporting_docs/MCMS/PIPELINE_MAP.md` to document MCMS ownership of the appendix-table workflow.
- Hardened `run_horse_race_appendix.py` against the current broken `irf_Het_DCP_Baseline.mat` by:
  - using `Figure_1_Benchmark_IRFs_CrossSection.csv` for the benchmark shock-A cross section
  - falling back to cached role-analysis artifacts in `Tariffs_ECB/0_clean/generated/` when the two-shock benchmark HDF5 read fails

Verification:
- Non-writing syntax checks passed for the moved MCMS modules and the paper-side wrappers.
- Import checks passed for the MCMS-native appendix runner and the paper-side wrapper.
- `python run_stacked_regressions.py` succeeded from `master_supporting_docs/MCMS/`.
- `python run_horse_race_appendix.py` succeeded from `master_supporting_docs/MCMS/`, with an explicit warning that cached role-analysis artifacts were reused because `irf_Het_DCP_Baseline.mat` is unreadable.
- `python run_stacked_regressions.py` succeeded from `master_supporting_docs/Tariffs_ECB/0_clean/`.
- `python run_horse_race_appendix.py` succeeded from `master_supporting_docs/Tariffs_ECB/0_clean/`, again using the cached role-analysis fallback.
- Attempted `matlab -batch "run_benchmark_irf_export"` to repair `irf_Het_DCP_Baseline.mat`; Dynare completed preprocessing but exited with `Dynare ran but no IRFs were found in oo_`.

Open issue:
- `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat` remains unreadable at `irfs_saved` (`address of object past end of allocation`), so full fresh recomputation of the role-interacted benchmark appendix still depends on repairing or regenerating that benchmark IRF export.
