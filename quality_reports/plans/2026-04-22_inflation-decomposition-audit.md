# Plan: Inflation Decomposition Audit

**Date:** 2026-04-22
**Status:** ACTIVE

## Objective

Verify why the sectoral inflation outputs used in the Section 5 spillover figures do not sum to aggregate CPI, check the earlier figure interpretation against the model and export code, and identify what would need to change for sectoral inflation responses to add up exactly to the aggregate CPI response.

## Scope

- Model source:
  - `master_supporting_docs/MCMS/dynare_files/`
  - `master_supporting_docs/MCMS/a1_calibration.m`
  - `master_supporting_docs/MCMS/new_process.py`
- Active manuscript source:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Exported benchmark evidence:
  - `master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv`
  - `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
- Tracking:
  - `quality_reports/plans/2026-04-22_inflation-decomposition-audit.md`

## Planned Steps

1. Read the model equations defining aggregate CPI, sectoral prices, imported-variety prices, and expenditure aggregation.
2. Trace the Python export path for the Section 5 sectoral inflation figures and identify the exact plotted object.
3. Check whether the plotted inflation cells can, by construction, sum to aggregate CPI, and quantify any mismatch against the benchmark aggregate CPI outputs.
4. Re-check the earlier explanation against the code and correct any inaccurate claim.
5. Describe the minimal accounting object and code changes needed to make sectoral inflation responses sum exactly to aggregate CPI.

## Verification

- Direct inspection of the Dynare model equations and calibration objects used in CPI aggregation.
- Read-only extraction and comparison of benchmark CSV outputs.
- A small reproducible script or command that compares candidate inflation decompositions with the saved aggregate CPI response.

## Assumptions

1. The user is asking for an audit and design path, not an immediate implementation patch.
2. The relevant inflation object is the lower-panel sectoral inflation response in Figures 12 and 13, plus the own-sector inflation object in Figure 11 where needed for comparison.
3. Aggregate CPI in the manuscript is the benchmark CPI object exported in `Figure_6_Baseline_Bars_CrossSection.csv`.
