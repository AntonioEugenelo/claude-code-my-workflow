# Plan: Codebase Cleanup Implementation Wave 1

Date: 2026-04-15

## Goal

Start implementing the codebase-quality audit with high-confidence, low-regret cleanup work that materially reduces duplication and legacy drift without touching `.tex` or `.mod` files.

## Scope

Wave 1 is intentionally limited to three areas:

1. Tariffs_ECB regression-path consolidation
   - `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py`
   - `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py`
   - optional small helper module in the same directory

2. MCMS MATLAB runner deduplication
   - `master_supporting_docs/MCMS/a0_launch.m`
   - `master_supporting_docs/MCMS/a0_launch_missing.m`
   - `master_supporting_docs/MCMS/a0_rerun_DCP.m`
   - `master_supporting_docs/MCMS/a0_rerun_nomonpol.m`
   - `master_supporting_docs/MCMS/a0_rerun_remaining.m`
   - `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
   - one new shared helper file in `master_supporting_docs/MCMS/`

3. Root sync-script cleanup
   - `scripts/sync_to_overleaf.sh`
   - possibly light doc/comment cleanup in `scripts/sync-overleaf.sh`

## Non-Goals

- No `.tex` or `.mod` edits.
- No broad retirement of `.claude/hooks` in this wave; too risky while `.claude/settings.json` still wires them.
- No attempt to fully solve every audit finding in one pass.
- No deletion of potentially manual-use scripts unless replaced or clearly wrapped.

## Assumptions

- Preserve user-facing entrypoints where possible; prefer wrappers over hard deletion in wave 1.
- Reduce duplication first, then tighten schemas/error handling in later waves.
- Keep write scopes disjoint when delegating.

## Steps

1. Consolidate Tariffs_ECB stacked-regression logic so `run_stacked_regressions.py` is no longer an independent duplicated implementation.
2. Extract a shared MCMS MATLAB scenario runner and update the benchmark/rerun scripts to use it.
3. Convert `scripts/sync_to_overleaf.sh` into a thin compatibility wrapper around the canonical `scripts/sync-overleaf.sh`.
4. Verify each changed code path:
   - Python: run the affected scripts in a non-destructive/helpful mode when feasible, or run syntax/import checks.
   - MATLAB: static validation plus targeted path/config checks if runtime execution would be too expensive.
   - Shell: run `bash -n` and command-level smoke checks where possible.
5. Run code review agents on the changed code and address findings.

## Verification

- `python -m py_compile` on changed Python files
- `bash -n` on changed shell scripts
- targeted static validation for MATLAB helper integration
- code review via `code-critic` and `code-structurer`
