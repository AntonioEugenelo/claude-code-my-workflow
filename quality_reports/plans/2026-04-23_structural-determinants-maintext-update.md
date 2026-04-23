# Plan: Structural Determinants Main-Text Update

**Status:** COMPLETED
**Date:** 2026-04-23

## Objective

Rewire the active Section 5 “Mechanisms behind the sectoral ranking” subsection to the new structural-determinants charts and rewrite the mechanism discussion so bilateral trade share is the first-stage exposure margin while consumption share, IO centrality, and price flexibility are the three displayed structural parameters.

## Scope

- Main manuscript source:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- Verification target:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Assumptions

1. The user’s remark that the charts “still have the old figures” refers to the active Section 5 source, which still includes `Fig_CHN_Structural_Scatter_3x4.png`, `Fig_US_Structural_Scatter_3x4.png`, and `Fig_EA_Structural_Scatter_3x4.png`.
2. Bilateral trade share should remain in the explanatory text even though the new main-text figures no longer display it as a column.
3. The new figures to use in main text are `Fig_Structural_Determinants_GDP_3x3.png` and `Fig_Structural_Determinants_CPI_3x3.png`.

## Planned Steps

1. Rewrite the subsection text around the updated mechanism ordering and the new cumulative GDP/CPI charts.
2. Replace the old figure blocks with the new structural-determinants figure pair and updated captions/labels.
3. Compile `0_main.tex` and confirm the rebuilt PDF references the new figures.
4. Record the work in a session log.

## Verification

- `55b_sectoral_transmission_decomposition.tex` references the new GDP/CPI structural-determinants figures.
- `latexmk -g -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex` succeeds.
- The build auxiliary files show the new figure labels are present in the compiled manuscript.
