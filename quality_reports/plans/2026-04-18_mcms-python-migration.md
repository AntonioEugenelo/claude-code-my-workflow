Date: 2026-04-18

Status: In Progress

## Goal

Move the Tariffs ECB paper's Python regression/table-generation workflow into MCMS so the code is owned and runnable from `master_supporting_docs/MCMS/` while the paper continues to receive the same generated outputs.

## Scope

Primary targets:

- `master_supporting_docs/Tariffs_ECB/0_clean/horse_race_data.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/horse_race_regression_utils.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py`
- new or updated Python files under `master_supporting_docs/MCMS/`
- any minimal paper-side wrappers or call-site adjustments needed for compatibility
- MCMS documentation for the new execution path

## Non-Goals

- No MATLAB/Dynare model logic changes.
- No manuscript prose edits beyond compatibility with generated-output paths.
- No cleanup of unrelated dirty files in the top repo, MCMS, or Tariffs_ECB.

## Assumptions

- The intended migration scope is the paper-side Python workflow, not every Python file in the monorepo.
- MCMS should own both shared helpers and the runnable entrypoints.
- Keeping a thin paper-side wrapper is acceptable if it preserves seamless use and reduces workflow breakage.

## Planned Changes

1. Trace all references to the four paper-side Python files and identify output-path contracts.
2. Choose an MCMS layout for the migrated code and adjust imports/path discovery accordingly.
3. Move or recreate the Python source under MCMS, keeping generated-output behavior compatible with the paper workflow.
4. Replace paper-side logic with wrappers or compatibility entrypoints only if they are still useful.
5. Update MCMS docs or pipeline notes so the new ownership is explicit.
6. Verify by executing the MCMS-native scripts and checking the expected artifacts.

## Verification

- Static search confirms the moved entrypoints import only MCMS-owned helpers.
- Running the migrated entrypoints from `master_supporting_docs/MCMS/` succeeds.
- Expected output files for the paper workflow are created or refreshed in the correct destination.
- Any retained wrapper in `Tariffs_ECB/0_clean/` successfully delegates to MCMS.

## Risks

- Existing paper automation may hardcode the old file locations.
- Relative-path logic may currently rely on the Tariffs_ECB file layout.
- The MCMS repo is already dirty, so edits must stay scoped and non-destructive.
