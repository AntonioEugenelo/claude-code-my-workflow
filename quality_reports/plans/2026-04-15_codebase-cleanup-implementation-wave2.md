# Plan: Codebase Cleanup Implementation Wave 2

Date: 2026-04-15

## Goal

Reduce the next layer of duplication left after wave 1, focusing on medium-risk internal cleanup that simplifies maintenance without changing `.tex` or `.mod` files.

## Scope

Wave 2 is limited to two areas:

1. Tariffs_ECB horse-race shared layer
   - `master_supporting_docs/Tariffs_ECB/0_clean/horse_race_data.py`
   - `master_supporting_docs/Tariffs_ECB/0_clean/horse_race_regression_utils.py`
   - thin callers only if required for interface compatibility

2. MCMS runner/config support
   - `master_supporting_docs/MCMS/run_irf_scenario.m`
   - `master_supporting_docs/MCMS/a0_launch.m`
   - `master_supporting_docs/MCMS/a0_launch_missing.m`
   - `master_supporting_docs/MCMS/a0_rerun_DCP.m`
   - `master_supporting_docs/MCMS/a0_rerun_nomonpol.m`
   - `master_supporting_docs/MCMS/a0_rerun_remaining.m`
   - `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
   - one small new shared helper file in `master_supporting_docs/MCMS/`

## Non-Goals

- No `.tex` or `.mod` edits.
- No broad retirement of `.claude/` in this wave.
- No large-scale `new_process.py` architecture split yet.
- No removal of legacy scripts unless they remain covered by stable wrappers or explicit retirement markers.

## Targeted Problems

1. `horse_race_data.py` still duplicates cross-section extraction and structural predictor assembly.
2. `horse_race_regression_utils.py` still duplicates weighted and unweighted regression preparation.
3. The MCMS runner entrypoints still repeat default-config setup, override application, output-dir setup, and environment/preflight logic.
4. `a0_launch.m` still carries a hardcoded Dynare path that should be replaced by a shared environment contract.

## Steps

1. Refactor the Tariffs_ECB shared layer around reusable helpers for:
   - sector-row assembly from IRF MAT files,
   - structural predictor assembly from calibration arrays,
   - common regression masking/design-matrix construction.
2. Introduce one MCMS runner-support helper for:
   - default IRF config construction,
   - config override application,
   - output-dir creation,
   - shared preflight/path setup, including Dynare path resolution.
3. Update the MATLAB entrypoints to use that helper and remove duplicated config/path scaffolding.
4. Verify changed code paths with static checks and targeted smoke tests.
5. Run focused code review on the updated files and address any concrete findings.

## Verification

- Python AST parse for changed `.py` files
- synthetic equivalence tests for refactored regression helpers
- static MATLAB integration checks via text searches / call-site validation
- `bash` checks only if shell wrappers change again
