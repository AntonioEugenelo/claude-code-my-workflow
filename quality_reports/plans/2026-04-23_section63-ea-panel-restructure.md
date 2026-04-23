## Plan: Section 6.3 EA Panel Restructure

**Date:** 2026-04-23
**Status:** IN PROGRESS

## Objective

Restructure the active EA discussion in Section 6.3 and redesign the EA trade-margins figure so the chart and prose jointly emphasize two points: sectoral detail does not map cleanly into the aggregate EA response, and large bilateral sectoral trade effects offset each other enough to leave muted aggregate EA responses.

## Scope

- Redesign the active EA sectoral trade figure in `new_process.py`.
- Keep only the 20 shocked tradeable sectors.
- Reorder the large outer panels so imports are on the left and exports are on the right.
- Replace the current full-width middle trade-balance decomposition with a thinner middle panel that shows total sectoral imports on the left, total sectoral exports on the right, and a marker for the sectoral net trade balance.
- Rewrite the active EA subsection in `0_clean/sections/56_sectoral_channels.tex` into two subsubsections with a mechanism-first structure guided by the local Cochrane reference note.
- Verify by regenerating the figure and compiling the main manuscript in place from `0_main.tex`.

## Constraints

- Do not create a verification wrapper or build directory.
- Do not revert unrelated changes in the dirty nested repos.
- Use the model-consistent bilateral sectoral export/import objects already implemented in the MCMS pipeline.
- Keep the figure/manuscript discussion aligned with the exact objects plotted.

## Likely Files

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_EA_Sectoral_Trade_Margins.png`
- `quality_reports/session_logs/2026-04-23_ea-full-shock-sectoral-trade-figure.md`

## Work Plan

1. Inspect the active plotting function and Section 6.3 source to map the exact edits needed.
2. Patch the EA trade-margins figure layout and panel logic in `new_process.py`.
3. Regenerate the figure from source and confirm the stack identities still hold.
4. Rewrite the EA subsection into two subsubsections and update the figure caption to match the new layout and argument.
5. Compile `0_main.tex` in place and record any remaining warnings or blockers.

## Verification

- Python execution of the active figure-generation path succeeds.
- Partner-level components still sum to the plotted sectoral totals up to machine precision.
- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` succeeds in `master_supporting_docs/Tariffs_ECB/0_clean/`.

## Assumptions

- “Split Section 6.3 into two subsections” means keeping the existing EA subsection as the containing subsection and introducing two `\subsubsection{}` blocks inside it.
- “Marker to indicate the total” in the middle panel means showing the sectoral net trade balance as a point over the gross import/export bars.
