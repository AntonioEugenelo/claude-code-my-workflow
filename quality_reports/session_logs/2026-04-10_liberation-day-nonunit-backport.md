Status: complete

Task:
- Backport only non-unit-elasticity changes from the unit-elasticity workspace into the elasticity-two paper line, using the benchmark figure layout change as the main example.

What changed:
- Updated `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
  to replace the single combined benchmark IRF panel with the split two-page subfigure layout using:
  - `Fig_Benchmark_CPI.png`
  - `Fig_Benchmark_GDP.png`
  - `Fig_Benchmark_Consumption.png`
  - `Fig_Benchmark_TB.png`
  - `Fig_Benchmark_REER_DW.png`
- Updated `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
  to disable the broken legacy `\title`/`\author` macro block and use the compile-safe standalone title-page structure, while preserving the elasticity-two abstract text.

What was intentionally excluded:
- Any `_UnitElast` file references
- Armington-1 / unit-elasticity narrative, captions, or benchmark swaps
- Section 5 horse-race / 3x3 structural-scatter rewrites
- Figure 4 unit-vs-high-elasticity comparisons

Verification:
- `latexmk -pdf -interaction=nonstopmode -jobname=0_main_layoutcheck 0_main.tex`
  passed in `master_supporting_docs/Tariffs_ECB/0_clean`
  and produced `0_main_layoutcheck.pdf`.
