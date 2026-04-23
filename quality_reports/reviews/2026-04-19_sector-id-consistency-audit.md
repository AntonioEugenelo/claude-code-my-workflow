# Sector ID Consistency Audit

Date: 2026-04-19
Scope: MCMS model-to-manuscript pipeline, with emphasis on where sector IDs are assigned, remapped, exported, and consumed.

## Verdict

Yes. There is a confirmed sector-numbering inconsistency in the active pipeline.

The core issue is not that the code uses two numbering schemes. That part is acceptable:
- global sector IDs `1..44`, with tariffed sectors `4..23`
- local tariff-sector IDs `1..20` in some cross-section CSVs

The confirmed bug is that one active downstream path reads a local `1..20` `SectorID` and then reuses it as if it were a global `1..44` `shock_sector_id`.

## Canonical Sector Numbering

The model’s canonical global ordering is established in [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:9):
- original data sectors `3`, `10`, and `23` are reordered to the front as energy sectors
- after reordering, the global 44-sector order is:
  - `1` `05-06`
  - `2` `19`
  - `3` `35`
  - `4..23` are the 20 tariffed tradeable sectors
  - `24..44` are the remaining non-tariffed sectors

Python mirrors that global ordering in [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:47), [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:82), and [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:89):
- `TARIFF_SECTORS = list(range(4, 24))`
- `FULL_SECTOR_CODES` length `44`
- `FULL_SECTOR_NAMES` length `44`

`Ind_E` from [calib.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_matlab/calib.mat) also confirms energy sectors are global IDs `1, 2, 3`.

## Where Numbering Is Consistent

These parts are internally consistent with the global scheme:

1. Benchmark MAT and Dynare IRF keys
- Shock keys are global, e.g. `varepsilon_tau_4_2_4` through `varepsilon_tau_4_2_23`.
- Dynare results in [b0_main_results.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat) expose global `1..44` sector suffixes in `M_.endo_names` and `oo_.irfs`.

2. Transmission-decomposition exports
- [Figure_1_Benchmark_IRFs_SectoralTransmission_Long.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_1_Benchmark_IRFs_SectoralTransmission_Long.csv) uses `sector_id = 1..44`
- [Figure_1_Benchmark_Transmission_Decomposition.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_1_Benchmark_Transmission_Decomposition.csv) uses `seller_sector_id = 1..44`
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:523) and [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:560) build these from global `1..44` loops

3. Spillover matrix exports
- [Figure_SectoralSpillover_Matrix.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv) uses:
  - `shocked_sector_id = 4..23`
  - `responding_sector_id = 1..44`
- That matches [extract_sectoral_spillover_matrices()](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:1038) and [create_sectoral_spillover_matrix()](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:4062)

4. Appendix horse-race helper layer
- [horse_race_data.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/horse_race_data.py:28) stores tariff-sector `SECTORS` as global IDs `4..23`
- when it loads the benchmark cross-section CSV, it explicitly repairs the local numbering via [horse_race_data.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/horse_race_data.py:149) and [horse_race_data.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/horse_race_data.py:151):
  - `csv_df["SectorID"] = csv_df["SectorID"] + 3`

## The Confirmed Numbering Bug

The active bug is in the single-shock transmission path in [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3330) and [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3613).

### What happens

1. The code reads [Figure_6_Baseline_Bars_CrossSection.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv), whose `SectorID` is local `1..20`, not global `4..23`.
Evidence:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:747) writes cross-section CSVs with:
  - `SectorID = 1..20`
  - `Label = TARGET_SECTOR_CODES`
- the live CSV confirms:
  - `1 -> 01-02`
  - `6 -> 13-15`
  - `15 -> 26`
  - `20 -> 31-33`

2. The single-shock code renames that local `SectorID` directly to `shock_sector_id`, without adding `3`.
Evidence:
- MAT path:
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3369)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3372)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3376)
- full-solution fallback path:
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3641)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3644)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3648)

3. That `shock_sector_id` is then treated as global when the code:
- builds the IRF shock tag
- indexes `FULL_SECTOR_NAMES`
- indexes sector-level response arrays
Evidence:
- [build_single_sector_shock_path()](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3303)
- [_impact_from_irfs()](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3322)
- MAT path uses it as global at:
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3417)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3531)
- full-solution path uses it as global at:
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3696)
  - [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3811)

### What the live outputs show

This is not just a theoretical bug. The generated files are internally inconsistent.

In [Figure_SingleShock_Transmission_Shocks.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_Shocks.csv):
- `6 -> Textiles`
- `15 -> Electronics`
- `20 -> Other manuf`

But in both:
- [Figure_SingleShock_Transmission_Panels.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_Panels.csv)
- [Figure_SingleShock_Transmission_IO.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SingleShock_Transmission_IO.csv)

the same `shock_sector_id` values are labeled as:
- `6 -> Metal ores`
- `15 -> Non-met min`
- `20 -> Machinery`

So the pipeline is mixing:
- local `1..20` names from `Figure_6`
- global `1..44` names from `FULL_SECTOR_NAMES`

for the same integer.

### Why this is a real numerical corruption, not just a label bug

The shock summary totals and the panel totals do not match.

Examples from the live outputs:
- Panel 1:
  - shock summary says `shock_sector_id = 6`, `Textiles`, total `-0.028532`
  - panel rows say `shock_sector_id = 6`, `Metal ores`
  - panel contribution sum is about `+0.000047`
- Panel 2:
  - shock summary says `15`, `Electronics`, total `-0.009476`
  - panel rows say `15`, `Non-met min`
  - panel contribution sum is about `+0.001188`
- Panel 3:
  - shock summary says `20`, `Other manuf`, total `-0.006863`
  - panel rows say `20`, `Machinery`
  - panel contribution sum is about `+0.000569`

That means the downstream decomposition is using the wrong underlying shock, not merely the wrong displayed name.

## Additional Fragility Points

These are not yet confirmed as live numerical bugs, but they are weak contracts:

1. [apply_sector_names()](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:1119)
- If a DataFrame has `SectorID` and length `20`, it overwrites `Description` using a hard-coded ordered list.
- It does not inspect actual `SectorID` values.
- This is safe only if row order stays canonical.

2. `export_standard_jobs_from_mat()` alignment by row position
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:747) writes `SectorID = 1..20`
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:767) then concatenates structural columns by row order, not by sector key
- This is fine only because current row order matches `TARIFF_SECTORS = 4..23` exactly

These are design risks. The confirmed active bug remains the single-shock transmission path.

## Bottom Line

I am not convinced the entire pipeline is inconsistent. Most of the active benchmark and sectoral-manuscript path is numerically consistent once you distinguish:
- global `1..44`
- local tariff-sector `1..20`

But I am convinced there is at least one material inconsistency:
- the single-shock transmission pipeline in [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3330) and [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3613)
- plus its generated outputs

That path currently leaks local tariff-sector IDs into global-sector logic and therefore produces wrong shock identities and wrong decomposition numbers.
