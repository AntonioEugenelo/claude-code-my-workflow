Date: 2026-04-15

Task: MCMS runner-support wave-2 cleanup

Summary:
- Added `master_supporting_docs/MCMS/mcms_runner_support.m` as the shared bootstrap/helper for MCMS runners.
- Refactored the six runner entrypoints to use shared config merging, shared output-dir setup, and shared preflight/path bootstrap.
- Removed the hardcoded Dynare installation path from `a0_launch.m` and replaced it with the `MCMS_DYNARE_MATLAB_PATH` contract.
- Trimmed dead `armington_string` / `invoicing_name` helpers from `run_irf_scenario.m`.

Verification:
- Static scans confirmed all six entrypoints now call `mcms_runner_support()` and use the shared config/output helpers.
- Static scans confirmed the hardcoded `/Applications/Dynare/...` path is gone from `a0_launch.m`.
- `git -C master_supporting_docs/MCMS status --short -- <touched files>` confirmed the expected changed file set in the MCMS workspace.
- `matlab -batch` `checkcode` smoke test was attempted, but MATLAB failed to start locally with `System Error: File system inconsistency`.
