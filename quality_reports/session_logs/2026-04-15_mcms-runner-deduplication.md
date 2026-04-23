Date: 2026-04-15

Task: Deduplicate the shared MCMS MATLAB runner skeleton across the allowed entrypoints.

Files changed:

- `master_supporting_docs/MCMS/a0_launch.m`
- `master_supporting_docs/MCMS/a0_launch_missing.m`
- `master_supporting_docs/MCMS/a0_rerun_DCP.m`
- `master_supporting_docs/MCMS/a0_rerun_nomonpol.m`
- `master_supporting_docs/MCMS/a0_rerun_remaining.m`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- `master_supporting_docs/MCMS/run_irf_scenario.m`
- `quality_reports/plans/2026-04-15_mcms-runner-deduplication.md`

Summary:

- Added `run_irf_scenario.m` to centralize the shared calibration/Dynare/save workflow.
- Updated each allowed entrypoint to keep its own scenario list, skip policy, backup behavior, and progress logging while delegating the common run skeleton to the helper.
- Kept bytecode cleanup opt-in so the baseline batch launcher remains aligned with its prior behavior while the rerun and benchmark scripts still clear bytecode before Dynare.
- Preserved pragmatic failure handling:
  - batch scripts continue to the next scenario on failure,
  - the single-run benchmark export still rethrows via helper options,
  - the NoMonPol rerun still reports a single failure without crashing the session.

Verification:

1. Static helper wiring:
   - `Select-String` confirmed every intended entrypoint now calls `run_irf_scenario(...)`.
   - `Select-String` confirmed `dynare b0_main.mod noclearall` now appears only in `run_irf_scenario.m`.

2. Git/path checks:
   - `git -C master_supporting_docs/MCMS status --short` shows only the intended modified files plus existing unrelated repo dirt.
   - temporary refactor files used during replacement were removed.

3. MATLAB smoke attempt:
   - attempted `matlab -batch` with `checkcode(...)` over the changed files
   - blocked before script execution by MATLAB startup failure:
     `Fatal Startup Error: System Error: File system inconsistency`

Notes:

- `rg` is not installed in this shell, so static search used `Select-String`.
- Copying temp files over the nested-repo MATLAB scripts worked; direct move/delete operations initially hit Windows access errors in this workspace.
