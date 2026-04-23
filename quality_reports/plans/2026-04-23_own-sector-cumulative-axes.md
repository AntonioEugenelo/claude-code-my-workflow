# Plan: Own-Sector Scatter to 12-Quarter Cumulative Axes

**Status:** IN PROGRESS
**Date:** 2026-04-23

## Objective

Change the active own-sector value-added versus inflation figure so both axes use 12-quarter cumulative responses, then update the associated captions, labels, and nearby manuscript text to match.

## Scope

- Figure/data pipeline:
  - `master_supporting_docs/MCMS/new_process.py`
- Active manuscript sources:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Verification targets:
  - regenerated `Fig_CN_Structural_Scatter.png`
  - any paired own-sector heatmap that shares the same axis objects
  - section-only verification PDF under `build_verify/`

## Assumptions

1. “12 period cumulative” means the 12-quarter sum of the relevant IRF in the same single-sector experiment.
2. The x-axis should use cumulative own-sector value added, not on-impact value added.
3. The y-axis should use cumulative own-sector inflation over the same 12-quarter horizon.
4. Any figure panels reusing the same own-sector objects should be updated for consistency unless doing so would contradict the user request.

## Planned Steps

1. Add cumulative 12-quarter own-sector value-added and inflation fields to the benchmark cross-section export.
2. Repoint the active scatter and any paired own-sector heatmap labels to those cumulative fields.
3. Update captions and nearby text in Sections 5 and 6 so they explicitly describe 12-quarter cumulative own-sector value added and inflation.
4. Regenerate the affected figures from source.
5. Compile a scoped verification document and confirm the updated labels and captions build cleanly.

## Verification

- Inspect the regenerated cross-section CSV to confirm cumulative own-sector columns are populated.
- Regenerate `Fig_CN_Structural_Scatter.png` and verify the axis labels.
- Compile a section-only verification target and confirm the updated captions resolve cleanly.
