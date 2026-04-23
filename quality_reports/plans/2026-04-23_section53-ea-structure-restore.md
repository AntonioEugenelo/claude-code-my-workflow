## Plan: Section 5.3 EA Structure Restore

**Date:** 2026-04-23
**Status:** IN PROGRESS

## Objective

Restore the two-part structure of the active EA subsection in `56_sectoral_channels.tex`, align the first part with the new aggregate-contribution figure, and rewrite the second part around the sectoral trade-balance mechanism using the local Cochrane-style reference guidance.

## Scope

- Restore two `\subsubsection{}` blocks inside the EA subsection of the active manuscript.
- Reinsert the EA sectoral trade-margins figure into the active text if needed for the restored second block.
- Reframe the first block so the EA result is explained as a mostly own-sector/trade-balance object rather than a US/China-style cross-sector propagation object.
- Reframe the second block so it lists the Section 4 EA margins and draws conclusions from the current sectoral trade data.
- Verify on the main manuscript in `0_clean`.

## Likely Files

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/session_logs/2026-04-23_section53-ea-structure-restore.md`

## Evidence Base

- `Figure_6_Baseline_Bars_CrossSection.csv`
- `Figure_6d_EA_FullShock_Sectoral_Trade.csv`
- `reference_material/john_cochrane/README.md`
- Section 4 EA discussion in `55a_benchmark_and_robustness.tex`

## Work Plan

1. Restore the two-part subsection scaffold in the EA part of `56_sectoral_channels.tex`.
2. Rewrite 5.3.1 around Figure 15, emphasizing that the sectors driving EA GDP are mainly own-term objects and that the cross term is usually secondary in the quantitatively important rows.
3. Rewrite 5.3.2 around the trade-balance figure, list the Section 4 EA margins, and state which margins the current sectoral data support.
4. Compile `0_main.tex` in place and record any remaining blockers.

## Verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`

## Assumptions

- “Restore the old structure” means two `\subsubsection{}` blocks inside the existing EA subsection, not a new top-level subsection split.
- The active EA trade-margins figure should return to the main text because the requested 5.3.2 discussion depends on it.
