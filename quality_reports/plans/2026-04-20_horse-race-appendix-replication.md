Status: in progress

Task
- Replicate the full results for the horse-race appendix that was previously included in the paper, verify the generated tables and narrative claims against source outputs, and report any mismatches.

Target appendix
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`

Scope
- `master_supporting_docs/MCMS/run_horse_race_appendix.py`
- `master_supporting_docs/MCMS/horse_race_data.py`
- `master_supporting_docs/MCMS/output_matlab/calib.mat`
- `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat`
- `master_supporting_docs/MCMS/output_matlab/irf_PCP_Baseline.mat`
- scratch verification outputs under `quality_reports/`

Plan
1. Recover the exact appendix source that was previously in the paper and enumerate every generated table and quantitative textual claim it depends on.
2. Run the current horse-race pipeline in isolation from the dirty manuscript tree and export fresh appendix artifacts to a scratch location.
3. Compare regenerated table values and summary statistics against the deleted appendix text and identify any discrepancies.
4. Summarize whether the appendix is numerically correct as written, and if not, list the exact claims that fail.

Constraints
- Do not modify the live manuscript or the unresolved merge file in `56_sectoral_channels.tex`.
- Treat current repos as dirty and avoid reverting or overwriting user changes.
- Prefer isolated scratch outputs over writing back into `0_clean/generated/`.
