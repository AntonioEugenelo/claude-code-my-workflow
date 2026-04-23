# Plan: Section 5 EA Chart and Layout Cleanup

**Status:** COMPLETED
**Date:** 2026-04-15

## Objective

Replace the current euro-area own-sector Figure 15 with a dual-axis column chart that reports both aggregate GDP contribution and own-sector value added by sector, tighten the Section 5 float layout so the compiled manuscript uses space more cleanly, and update the abstract to state the benchmark and four-block model structure.

## Scope

- Figure source: `master_supporting_docs/MCMS/new_process.py`
- Manuscript source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Abstract source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
- Verification target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Generated artifacts:
  - `master_supporting_docs/MCMS/output_python/extra_charts/Fig_EA_Sectoral_Heatmap_USCN.png`
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_EA_Sectoral_Heatmap_USCN.png`

## Assumptions

1. Figure 15 should continue to use the benchmark single-sector decomposition already exported in `Figure_1_Benchmark_IRFs_CrossSection.csv`.
2. The two series to show are `GDP_EA_Benchmark` and `Sec_VA_EA_Benchmark`.
3. Layout cleanup should preserve the user’s revised Section 5 prose and focus on float placement, sizing, and caption alignment rather than structural rewrites.
4. The abstract change is limited to clarifying the benchmark shock and the four-block structure.

## Planned Steps

1. Confirm the live CSV columns and current figure-generation path.
2. Replace the current EA horizontal bar chart with a dual-axis vertical bar chart in `new_process.py`.
3. Update the Section 5 text/caption around Figure 15 so it describes both metrics correctly.
4. Adjust Section 5 float placement and sizing to reduce large white-space gaps in the compiled paper.
5. Update the abstract opening sentence to state the benchmark and four-block model structure.
6. Regenerate the active manuscript figures from source.
7. Rebuild `0_main.tex` and inspect the output/log for layout and compilation issues.

## Verification

- `python new_process.py`
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build_verify 0_main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build_verify 0_main.tex`
- Inspect the refreshed PDF pages covering Section 5 for remaining float/layout problems.

## Likely Files To Change

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/plans/2026-04-15_section5-ea-chart-layout.md`
- `quality_reports/session_logs/2026-04-15_section5-ea-chart-layout.md`
