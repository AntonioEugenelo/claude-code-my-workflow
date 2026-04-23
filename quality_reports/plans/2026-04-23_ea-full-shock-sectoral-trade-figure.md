## Plan: EA Full-Shock Sectoral Trade Figure

**Date:** 2026-04-23
**Status:** IN PROGRESS

## Objective

Produce a new figure for the active manuscript that shows, for the full benchmark US tariff shock on Chinese imports, euro-area sectoral exports and imports by partner with model-consistent weighting, and highlight the resulting sectoral net trade balance so the Section 5 EA argument can be read directly from the chart.

## Scope

- Confirm the exact bilateral sectoral export and import objects implemented in the model and how they are normalized in the paper and Dynare code.
- Reuse the active benchmark-shock construction for the full 20-sector tariff experiment rather than the existing single-sector decomposition chart.
- Add a new figure generator to the active MCMS Python pipeline and save the output into the active paper figure set.
- Update the active EA subsection in `0_clean/sections/56_sectoral_channels.tex` to include the new figure and align the surrounding discussion/caption with the new object.
- Verify by compiling the main manuscript in place from `0_main.tex`.

## Constraints

- Do not revert unrelated local changes in either nested repo.
- Treat `new_process.py`, the Dynare model files, and the manuscript `.tex` sources as authoritative.
- Use the model’s own bilateral sectoral trade objects (`exp_1_l_i`, `imp_1_l_i`) and benchmark-shock aggregation, not an ad hoc reconstruction from downstream CSVs.
- Verify on the main manuscript only; do not create any verification wrapper or build directory.

## Likely Files

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_EA_Sectoral_Trade_Margins.png`
- `quality_reports/session_logs/2026-04-23_ea-full-shock-sectoral-trade-figure.md`

## Work Plan

1. Confirm the model-consistent bilateral sectoral export/import formulas and the available benchmark IRF keys for the EA.
2. Implement a new full-shock EA sectoral trade figure that shows partner-specific exports and imports by sector and overlays net trade by sector.
3. Regenerate the figure in the active pipeline and sync it into the manuscript figure directory.
4. Update the active EA subsection caption and text to reference the new figure and the correct accounting.
5. Compile `0_main.tex` in place and record any remaining warnings or blockers.

## Verification

- Direct code check of the export/import formulas in the Dynare model against the manuscript notation.
- Successful regeneration of the new EA figure from `new_process.py`.
- Successful in-place compile of `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.

## Assumptions

- The user wants the chart to represent the linearized full benchmark shock created by summing the 20 tariff-sector shocks, consistent with the paper’s first-order aggregation argument.
- “Highlighting the final trade balance by sector” means showing the sectoral net trade response (exports minus imports across partners) prominently on top of the partner-level gross margins.
