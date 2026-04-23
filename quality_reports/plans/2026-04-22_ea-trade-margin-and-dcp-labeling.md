# Plan: EA Trade-Margin Figure and DCP Label Cleanup

**Status:** IN PROGRESS
**Date:** 2026-04-22

## Objective

Add a manuscript-facing figure that shows the euro area's on-impact trade-response decomposition into bilateral/multilateral net margins under heterogeneous invoicing and PCP, and clean up the active DCP robustness figure labels so they display `DCP` and `heterogeneous invoicing` consistently.

## Scope

- Figure source: `master_supporting_docs/MCMS/new_process.py`
- Manuscript source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- Verification target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Generated artifacts:
  - `master_supporting_docs/MCMS/output_python/extra_charts/Fig_EA_Trade_Margin_Decomposition.png`
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_EA_Trade_Margin_Decomposition.png`
  - refreshed DCP robustness figures in `master_supporting_docs/MCMS/output_python/extra_charts/`

## Assumptions

1. The new figure should use the same benchmark shock as the existing invoicing comparison in Section 4: a 10 pp US tariff on Chinese imports across the 20 tradeable manufacturing sectors.
2. The euro-area partner margins should be computed directly from the MAT bilateral trade objects as:
   - EA--US: `exp_1_4 - imp_1_4`
   - EA--China: `exp_1_2 - imp_1_2`
   - EA--ROW: `exp_1_3 - imp_1_3`
   - optional total: `exp_1 - imp_1`
3. The figure should show heterogeneous invoicing and PCP separately; DCP remains discussed in the text and in the existing three-year-average figure.
4. The DCP robustness-label cleanup applies to the active generator outputs, not just the manuscript captions.

## Planned Steps

1. Add a MAT-to-CSV export for the EA on-impact partner-margin decomposition under heterogeneous invoicing and PCP.
2. Add a new manuscript-facing plot for that decomposition and sync it into `Tariffs_ECB/0_clean/figures`.
3. Rename active DCP robustness figure labels from `Het. DCP` / `Full DCP` to `heterogeneous invoicing` / `DCP`.
4. Replace the manuscript placeholder text with a reference to the new figure and tighten the surrounding explanation.
5. Regenerate the relevant figures from source.
6. Recompile `0_main.tex`.
7. Run a targeted review pass on the modified figure/text alignment and note any residual compile blockers.

## Verification

- Regenerate the relevant figures from `master_supporting_docs/MCMS/new_process.py` or equivalent targeted calls.
- Visually inspect the refreshed EA decomposition figure and DCP robustness figure labels.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.
- Confirm that the new figure is referenced in the manuscript and that the EA paragraph no longer refers to an unseen object.

## Likely Files To Change

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `quality_reports/plans/2026-04-22_ea-trade-margin-and-dcp-labeling.md`
