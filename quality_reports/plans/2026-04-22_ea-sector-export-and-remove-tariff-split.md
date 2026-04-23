## Plan: EA Sector Export And Remove Tariff Split

**Date:** 2026-04-22
**Status:** IN PROGRESS

## Scope

Add the missing EA sector-by-partner trade-flow IRFs needed for the sectoral EA decomposition export, and remove the local benchmark-tariff split machinery that separates consumption and intermediate tariffs so the launcher/model path returns to the last working baseline.

## Constraints

- Treat the committed MCMS baseline as the reference for "last working version" unless a narrower local evidence trail shows otherwise.
- Do not revert unrelated local edits in the dirty MCMS worktree.
- Keep the fix as narrow as possible: restore baseline logic for tariff treatment, but preserve any unrelated runner improvements that are not part of the split.
- Verify with actual regenerated outputs rather than reasoning from code alone.

## Likely Files

- `master_supporting_docs/MCMS/run_irf_scenario.m`
- `master_supporting_docs/MCMS/mcms_runner_support.m`
- `master_supporting_docs/MCMS/a1_calibration.m`
- `master_supporting_docs/MCMS/dynare_files/b3_declare_par.mod`
- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
- `master_supporting_docs/MCMS/dynare_files/b0_main.mod`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat`
- `quality_reports/session_logs/2026-04-22_ea-sector-export-and-remove-tariff-split.md`

## Work Plan

1. Identify the exact local files and code paths introduced for the consumption-vs-intermediate tariff split, and restore the affected launcher/model logic to the last working baseline.
2. Patch the IRF export path so the saved benchmark `.mat` includes the needed EA sector-by-partner trade-flow series for tariff shocks.
3. Remove the split-only helper scripts if they are purely local scaffolding and no longer needed.
4. Regenerate the benchmark export and confirm that the saved `irfs_saved` object now includes the required `exp_1_l_i_*` and `imp_1_l_i_*` tariff-shock keys.
5. Record the result and any residual caveats in a session log.

## Verification

- Code diff check on the restored model/calibration files against the committed baseline for the split-specific logic.
- Regenerated `output_matlab/irf_Het_DCP_Baseline.mat`.
- Direct key-presence check for examples such as:
  - `exp_1_2_5_varepsilon_tau_4_2_1`
  - `imp_1_2_5_varepsilon_tau_4_2_1`
  - `exp_1_4_5_varepsilon_tau_4_2_1`
  - `exp_1_3_5_varepsilon_tau_4_2_1`
- Sanity check that the baseline aggregate partner-level EA trade-flow keys remain present.

## Assumptions

- The user wants the local tariff-split experiment removed from the active MCMS workflow, including helper launchers and model switches added only for that experiment.
- The minimal acceptable solution for the new EA decomposition is to get the needed sector-by-partner IRFs into the saved benchmark `.mat`; downstream figure construction can follow after that.
