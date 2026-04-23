# Plan: Remove Buggy Single-Shock Material

- Date: 2026-04-19
- Status: in progress
- Goal: eliminate manuscript references, generated artifacts, and active pipeline outputs that depend on the confirmed buggy single-shock sector-ID path in `master_supporting_docs/MCMS/new_process.py`

## Scope

- Source audit across:
  - `master_supporting_docs/Tariffs_ECB/0_clean/**/*.tex`
  - `master_supporting_docs/MCMS/new_process.py`
  - any figure sync lists or paper-facing figure references
- Remove or disable all active references/material tied to:
  - `Figure_SingleShock_Transmission_*`
  - `Figure_SingleShock_Transmission_Top3*`
  - `Fig_Benchmark_Transmission_USA_Top3.png`
  - `Fig_Textiles_CrossSector_Story_USA.png`
  - any other manuscript-facing object derived from that same buggy branch

## Likely Files To Change

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/*.tex` if any manuscript references remain
- `quality_reports/session_logs/2026-04-19_remove-buggy-single-shock-material.md`

## Verification

1. Search source files to confirm no remaining manuscript references to buggy outputs.
2. Run the relevant `new_process.py` path or a narrower validation to ensure the buggy branch is no longer generated in the active pipeline.
3. Rebuild the manuscript and check for missing-figure or dangling-reference failures.

## Assumptions

- The confirmed bug is the local `1..20` vs global `1..44` sector-ID leak in the single-shock transmission branch.
- Clean benchmark bars, spillover matrix, structural scatter, and EA heatmap remain in scope unless they depend on that buggy branch.
- Existing unrelated worktree changes must be preserved.
