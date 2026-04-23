# Plan: Sectoral Bar Figures to Three-Year Cumulative Metrics

**Status:** IN PROGRESS  
**Date:** 2026-04-23

## Objective

Change the active sectoral bar figures for aggregate GDP and aggregate inflation so they report three-year cumulative responses rather than the current short-horizon objects, then update the manuscript captions and nearby descriptive text to match.

## Scope

- Figure generator:
  - `master_supporting_docs/MCMS/new_process.py`
- Manuscript sources likely affected:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
  - any other active section that reuses `Fig_Sectoral_Bars_GDP.png` or `Fig_Sectoral_Bars_CPI.png`
- Verification targets:
  - regenerated PNGs in `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Assumptions

1. “Three year cumulative GDP” means the sum of the quarterly GDP IRF over 12 quarters in the same single-sector decomposition.
2. “Cumulative Inflation” means the sum of quarterly CPI inflation over 12 quarters in the same single-sector decomposition.
3. The change applies to the bar figures only; other section-5 figures keep their current objects unless they directly reuse these same PNGs.

## Planned Steps

1. Add cumulative 12-quarter GDP and CPI fields to the benchmark sectoral cross-section export used by the active bar charts.
2. Repoint the two bar-chart functions to those cumulative fields and update figure titles/axis labels.
3. Revise the manuscript captions and local prose that describe those figures so they explicitly say three-year cumulative GDP and cumulative inflation.
4. Regenerate the figure pipeline from source.
5. Recompile `0_main.tex` and check that the figures and text are aligned.

## Verification

- Inspect the refreshed cross-section CSV to confirm the bar functions are using cumulative 12-quarter objects.
- Regenerate `Fig_Sectoral_Bars_GDP.png` and `Fig_Sectoral_Bars_CPI.png` from `new_process.py`.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.
- Manually check the updated captions and nearby descriptive paragraphs against the regenerated figures.
