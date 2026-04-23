# 2026-04-20 Unilateral US-on-China Benchmark Cleanup

## Objective

Remove reciprocal-tariff language from the Tariffs_ECB manuscript tree and recompile the paper so the live PDF presents the benchmark consistently as a unilateral US tariff on Chinese imports.

## Files Updated

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/13_roadmap.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/43_calibration.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55_model_dynamics_and_scenarios.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_dynamics.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/0_main (1).aux`
- `master_supporting_docs/Tariffs_ECB/0_clean/0_section_5_only.tex`
- `master_supporting_docs/MCMS/new_process.py`

## Verification

- Confirmed the active Section 4 source now reads `Aggregate Dynamics After a US Tariff on Chinese Imports`.
- Recompiled the root paper with:
  - `latexmk -pdf -interaction=nonstopmode -file-line-error 0_main.tex`
- Recompiled the redline build with:
  - `latexmk -pdf -interaction=nonstopmode -file-line-error -outdir=build_redline_20260420 0_main.tex`
- Rescanned `master_supporting_docs/Tariffs_ECB/0_clean` for:
  - `Aggregate Dynamics After a Reciprocal Tariff War`
  - `reciprocal US--China tariff shock`
  - `Chinese tariff on US imports`
  - `symmetric Chinese tariff on US imports`
  - `reciprocal tariff`
- Final scan returned no hits under `0_clean`.

## Outputs

- Root PDF: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`
- Redline PDF: `master_supporting_docs/Tariffs_ECB/0_clean/build_redline_20260420/0_main.pdf`

## Remaining LaTeX Warnings

- Pre-existing undefined references:
  - `sec:analytical_insights`
  - `eq:general_model_budget_constraint`
  - `eq:bilateral_nominal_exchange_rate_MU`
- Pre-existing multiply defined labels:
  - `eq:general_model_price_setting_foreign`
  - `eq:budget_constraint`
  - `eq:calvo_inflation_dynamics_2`
