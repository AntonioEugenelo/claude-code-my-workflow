# Plan: Benchmark Rerun And MAT Debug

**Date:** 2026-04-19
**Status:** IN PROGRESS

## Scope

Restore the benchmark launcher to the last known working `a0_launch.m` sequence, rerun the benchmark through that exact call path, force `new_process.py` to regenerate from MAT inputs, and then re-audit the paper numbers against the refreshed MAT-driven outputs.

## Constraints

- Follow the user-ordered sequence strictly:
  1. restore `a0_launch.m` to the last working sequence
  2. rerun the benchmark
  3. run `new_process.py` from MAT inputs rather than trusting prior CSVs
  4. reverify paper numbers
- Use MCMS source/model code as the source of truth.
- Do not rely on stale CSVs as authoritative evidence.
- Avoid appendix-specific work unless strictly required by the main-text benchmark path.
- Treat the existing dirty worktree as pre-existing; do not revert unrelated changes.

## Likely Files

- `master_supporting_docs/MCMS/a0_launch.m`
- `master_supporting_docs/MCMS/a1_calibration.m`
- `master_supporting_docs/MCMS/set_paths.m`
- `master_supporting_docs/MCMS/dynare_files/*.mod`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat`
- `master_supporting_docs/MCMS/output_python/**/*`
- `quality_reports/session_logs/2026-04-19_benchmark-rerun-and-mat-debug.md`

## Work Plan

1. Restore `a0_launch.m` exactly to the committed last-working inline sequence and verify the restored file matches `HEAD`.
2. Rerun the benchmark through that old launcher sequence, recording logs, output fingerprints, and MAT readability.
3. Run `new_process.py` with MAT-driven regeneration, verify that the CSV/figure layer was rebuilt from refreshed MAT inputs, and capture output deltas.
4. Re-audit the paper numbers and figure descriptions against the refreshed MCMS outputs, excluding the appendix.
5. Document the result, any remaining blockers, and the evidence chain.

## Verification

- `git diff -- a0_launch.m` should be empty after the restore
- MATLAB benchmark rerun launched from the restored inline `a0_launch` sequence
- direct HDF5 readability checks for the refreshed benchmark MAT
- `python new_process.py`
- refreshed-output fingerprint comparison against the pre-rerun evidence snapshot
- regenerated main-text numeric audit

## Assumptions

- The last working launcher sequence is the committed `HEAD:a0_launch.m` content that predates the local helper refactor.
- “Using the data from the .mat files rather than csv” means `new_process.py` must regenerate its derived CSV layer from MAT/calibration inputs during this run.
