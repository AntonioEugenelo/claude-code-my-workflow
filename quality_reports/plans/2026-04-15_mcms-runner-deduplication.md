Date: 2026-04-15

Status: Completed

## Goal

Deduplicate the shared MCMS MATLAB scenario-run skeleton used by the benchmark and rerun entrypoints, while preserving each script's current entrypoint behavior and skip/continue semantics.

## Scope

Allowed edits:

- `master_supporting_docs/MCMS/a0_launch.m`
- `master_supporting_docs/MCMS/a0_launch_missing.m`
- `master_supporting_docs/MCMS/a0_rerun_DCP.m`
- `master_supporting_docs/MCMS/a0_rerun_nomonpol.m`
- `master_supporting_docs/MCMS/a0_rerun_remaining.m`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- one new shared helper under `master_supporting_docs/MCMS/`

## Non-Goals

- No `.mod` edits.
- No `.tex` edits.
- No expensive Dynare runs during verification.
- No behavior changes outside the shared runner skeleton.

## Assumptions

- The duplicated logic to centralize is: config unpacking, filename derivation helpers, optional bytecode cleanup, Dynare launch, and MAT save behavior.
- Each entrypoint may still need to keep its own scenario lists, loop structure, and failure policy.
- MATLAB smoke checks should stay non-destructive and avoid solving the model.

## Planned Changes

1. Inspect the six allowed scripts and identify the exact common execution pattern.
2. Add one shared helper that performs the common calibration/Dynare/save workflow from a config struct plus options.
3. Refactor each allowed script to use the helper while preserving script-specific orchestration and error handling.
4. Run lightweight verification:
   - static reference/path checks
   - MATLAB parse/path smoke checks if available without running Dynare

## Verification

- Search-based validation that all six entrypoints call the new helper.
- Check that helper inputs cover the existing variants.
- Run safe MATLAB `which` / existence smoke checks if the local environment permits.

## Outcome

- The entrypoints now share `mcms_runner_support.m` for default config construction, override merging, output-dir setup, and preflight/path bootstrap.
- The Dynare path is now resolved via `MCMS_DYNARE_MATLAB_PATH` or an existing MATLAB path entry.
- MATLAB `checkcode` was attempted, but local startup failed with a system file-system inconsistency error.
