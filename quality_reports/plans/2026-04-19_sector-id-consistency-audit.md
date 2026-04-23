# Plan: Sector ID Consistency Audit

**Date:** 2026-04-19
**Status:** IN PROGRESS

## Scope

Audit sector numbering end to end in the MCMS model and active manuscript pipeline, starting from the assumption that sector IDs are inconsistent somewhere until the full chain is checked.

The audit covers:
- MATLAB calibration and sector classification in `a1_calibration.m`
- Dynare variable naming and shock indexing in the benchmark results/export layer
- Python constants and mappings in `new_process.py`
- active manuscript CSV outputs derived from MCMS
- any remap points between global `1..44` sector IDs and tariff-sector-local `1..20` indices

## Constraints

- Treat model code and saved outputs as the source of truth.
- Assume inconsistency exists until each boundary is checked.
- Do not rely on manuscript prose as evidence.
- Keep the audit read-only for product code unless a later user instruction asks for fixes.
- Treat the current dirty worktree as pre-existing.

## Likely Files

- `master_supporting_docs/MCMS/a1_calibration.m`
- `master_supporting_docs/MCMS/dynare_files/*.mod`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/extract_paper_numbers.py`
- `master_supporting_docs/MCMS/output_matlab/*.mat`
- `master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat`
- `master_supporting_docs/MCMS/output_python/extra_charts/*.csv`
- `quality_reports/session_logs/2026-04-19_sector-id-consistency-audit.md`

## Work Plan

1. Establish the canonical sector ordering and tariffed-sector subset from `a1_calibration.m` and Dynare names.
2. Inventory every Python mapping or label table that encodes sector order, sector codes, or `1..20` local indices.
3. Trace each extraction path from MAT/Dynare outputs into CSVs, checking whether IDs stay global or are remapped.
4. Compare representative saved outputs against direct MAT/Dynare pulls to detect off-by-3, local/global, or reordered-sector bugs.
5. Write a finding memo stating exactly where numbering is consistent and exactly where it is not.

## Verification

- Direct inspection of `M_.endo_names`, `oo_.irfs`, and saved benchmark MAT keys
- Cross-check of Python constant tables against the canonical 44-sector ordering
- Representative recomputation of sector-tagged outputs from MAT/results files
- Explicit confirmation for each boundary: consistent, intentionally remapped, or inconsistent

## Assumptions

- “Entire process” means the model-to-manuscript path currently used for the active benchmark and sectoral figures, not archived appendix-only code paths.
- A local `1..20` tariff-sector index is acceptable only if it is clearly labeled and never confused with the global `1..44` sector ID.
