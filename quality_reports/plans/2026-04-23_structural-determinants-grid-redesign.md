# Plan: Structural Determinants Grid Redesign

**Status:** COMPLETED
**Date:** 2026-04-23

## Objective

Redesign the structural-determinants figures so the manuscript uses two 3x3 scatter grids instead of the current country-by-country 3x4 appendix layout: one figure for three-year cumulative GDP responses and one for three-year cumulative inflation responses.

## Scope

- Figure generator:
  - `master_supporting_docs/MCMS/new_process.py`
- Manuscript sources likely affected:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
  - any active section that still references the old `Fig_*_Structural_Scatter_3x4.png` files
- Verification targets:
  - regenerated PNGs under `master_supporting_docs/MCMS/output_python/extra_charts/`
  - synced figure copies under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Assumptions

1. The new 3x3 figures use countries (`USA`, `CHN`, `EA`) as rows and the three requested determinants as columns.
2. “Three year cumulative GDP” means the 12-quarter sum of the aggregate GDP IRF for each single-sector tariff decomposition.
3. “Three year cumulative inflation” means the 12-quarter sum of the aggregate CPI inflation IRF for each single-sector tariff decomposition.
4. The active manuscript should reference the new two-figure layout rather than keep the old three country-specific appendix figures in parallel.

## Planned Steps

1. Patch the structural-cross-section chart generator to use `GDP_Cum12_*` and `CPI_Cum12_*` with `C_Share_*`, `IO_Share_*`, and `Flex_*`.
2. Replace the current three-country 3x4 structural-determinants outputs with two cross-country 3x3 figures in the active figure manifest and sync pipeline.
3. Update manuscript figure blocks and captions to reference the new GDP and inflation grids and include the cumulative-response formulas.
4. Regenerate the figure pipeline from source and compile `0_main.tex`.
5. Run the required read-only reviews for the changed Python and TeX files, then fix any findings.

## Verification

- Confirm the regenerated structural-determinants PNGs use cumulative 12-quarter GDP and CPI columns from the benchmark cross-section export.
- Confirm the paper figures directory contains the refreshed two-chart outputs referenced by the manuscript.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.
- Review the changed Python and TeX files with the routed read-only reviewers.
