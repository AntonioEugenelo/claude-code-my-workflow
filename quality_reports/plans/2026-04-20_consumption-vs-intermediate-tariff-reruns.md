# Plan: Consumption Vs Intermediate Tariff Reruns

**Date:** 2026-04-20
**Status:** IN PROGRESS

## Scope

Create two new MCMS baseline reruns for the benchmark US tariff on Chinese imports:

1. a rerun where the tariff wedge applies only to intermediate-input imports
2. a rerun where the tariff wedge applies only to household consumption imports

Then verify whether the two reruns add up to the benchmark baseline response.

## Constraints

- Work inside the existing MCMS runner/Dynare pipeline rather than creating an ad hoc fork.
- Keep the current benchmark definition and shock process unchanged except for the tariff-use split.
- Use clear scenario names that can live alongside the existing `irf_Het_DCP_Baseline.mat`.
- Treat the model code and saved `.mat` outputs as the source of truth.
- Do not disturb unrelated local changes in the dirty worktree.

## Likely Files

- `master_supporting_docs/MCMS/mcms_runner_support.m`
- `master_supporting_docs/MCMS/run_irf_scenario.m`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- `master_supporting_docs/MCMS/a1_calibration.m`
- `master_supporting_docs/MCMS/dynare_files/b3_declare_par.mod`
- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
- `master_supporting_docs/MCMS/` new rerun/check scripts
- `quality_reports/session_logs/2026-04-20_consumption-vs-intermediate-tariff-reruns.md`

## Model Notes

- The consumption-side tariff wedge enters the Dynare model in the international varieties consumption-demand block.
- The remaining explicit tariff-wedge terms in the Dynare model sit in intermediate-input demand and accounting blocks.
- This makes a clean split feasible with two scalar switches:
  - one for consumption-use tariffs
  - one for intermediate-use tariffs

## Work Plan

1. Add tariff-use switches to the MCMS configuration and calibration output so Dynare can see them as parameters.
2. Route the consumption-demand tariff term through the consumption switch and the intermediate-demand/accounting tariff terms through the intermediate switch.
3. Add two explicit rerun entry points with clear names for the two new baseline variants.
4. Add a verification script that compares the benchmark IRFs with the sum of the two split reruns.
5. Execute the reruns and the additivity check, then log the outcome and any residual discrepancy.

## Verification

- MATLAB/Dynare rerun for the intermediate-only baseline completes successfully and writes a new `.mat`.
- MATLAB/Dynare rerun for the consumption-only baseline completes successfully and writes a new `.mat`.
- The verification script compares the split reruns with the benchmark on a consistent set of IRFs and reports the max absolute discrepancy.
- If the model is behaving linearly under the split, the discrepancy should be numerically negligible; otherwise document which variables fail and by how much.

## Assumptions

- “Check that the two add up to the benchmark” means comparing the split-rerun IRFs against `irf_Het_DCP_Baseline.mat`, not reinterpreting the benchmark through a new post-processing layer.
- The requested reruns are for the heterogeneous-DCP benchmark baseline unless later expanded by the user to other invoicing regimes.
