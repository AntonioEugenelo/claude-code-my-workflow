# Session Log: Sector ID Consistency Audit

Date: 2026-04-19

Goal:
- audit sector numbering end to end in the MCMS model and active manuscript pipeline
- start from the assumption that a numbering inconsistency exists until each boundary is checked

## Files Inspected

- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:1)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:1)
- [horse_race_data.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/horse_race_data.py:1)
- [b0_main_results.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat)
- [calib.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_matlab/calib.mat)
- active CSV outputs in `master_supporting_docs/MCMS/output_python/extra_charts/`

## Key Checks

- Verified canonical sector reorder in `a1_calibration.m`
- Verified tariffed-sector global IDs are `4..23`
- Verified Python global sector tables match that ordering
- Verified which outputs use global IDs and which use local tariff-sector IDs
- Compared live single-shock output files against the code path that selects shocks from `Figure_6_Baseline_Bars_CrossSection.csv`

## Main Finding

Confirmed active numbering bug in the single-shock transmission path:
- `Figure_6_Baseline_Bars_CrossSection.csv` uses local `SectorID = 1..20`
- `_compute_single_shock_transmission_payload_from_mat()` and `_compute_single_shock_transmission_payload()` rename that field directly to `shock_sector_id`
- downstream code then treats it as a global ID

Evidence from live outputs:
- [Figure_SingleShock_Transmission_Shocks.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_Shocks.csv) says:
  - `6 Textiles`
  - `15 Electronics`
  - `20 Other manuf`
- [Figure_SingleShock_Transmission_Panels.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_Panels.csv) and [Figure_SingleShock_Transmission_IO.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_IO.csv) say:
  - `6 Metal ores`
  - `15 Non-met min`
  - `20 Machinery`

So the same integer is interpreted under two different numbering systems in the same artifact family.

## Secondary Findings

- The benchmark transmission decomposition and spillover-matrix paths are consistent and use global IDs correctly.
- The appendix horse-race helper layer explicitly normalizes benchmark cross-section `SectorID` by adding `3`, so it avoids the active bug.
- `apply_sector_names()` and row-order-based structural concatenation are fragile contracts, but I did not confirm a live numerical mismatch there.

## Output

- Audit memo: [2026-04-19_sector-id-consistency-audit.md](C:/CustomTools/claude-code-my-workflow/quality_reports/reviews/2026-04-19_sector-id-consistency-audit.md)
