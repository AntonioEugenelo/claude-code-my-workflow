# Tariffs ECB Shock-Narrative Audit

Date: 2026-04-11

Scope: included manuscript files in `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`, with emphasis on narrative claims about tariff-shock direction, mechanism, and sectoral ranking.

Files checked:
- `0_clean/sections/02_title_page.tex`
- `0_clean/sections/11_introduction.tex`
- `0_clean/sections/55a_benchmark_and_robustness.tex`
- `0_clean/sections/56_sectoral_channels.tex`
- `0_clean/sections/60_Conclusions.tex`
- `0_clean/sections/a_appendix_horse_race.tex`

Primary quantitative sources:
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_1_Benchmark_IRFs_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_1b_Benchmark_Reverse_IRFs_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_8_Baseline_Sectoral_CrossSection.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_17_DCP_PCP_FullDCP_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_18_Benchmark_vs_NoMonPol_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_5b_Cumul_Benchmark_vs_Peg_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_2_Cumul_IO_Decomposition_TimeSeries.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_results.json`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_alpha_mu_by_role.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_alpha_mu_aggregate.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_stacked_160.csv`

## Verified claims

- Benchmark directional narrative in Section 4 is broadly consistent with the IRFs.
  - Shock A (`USA -> CHN`): US CPI rises on impact, US GDP falls modestly then recovers, China contracts more sharply, EA GDP is near zero on impact.
  - Shock B (`CHN -> USA`): US GDP contracts more strongly on impact, China GDP rises modestly, Chinese CPI rises on impact.

- The benchmark EA “near zero” aggregate response is supported by the accounting used in the text.
  - On impact, EA GDP is about `+0.001%`.
  - The decomposition `consumption ~= -0.003%` and `scaled net exports ~= +0.004%` is consistent with the narrative that trade diversion and cost pressure offset in aggregate.

- The invoicing-regime claims in the introduction and benchmark section are supported.
  - China three-year average GDP is more negative under heterogeneous DCP than under PCP (`-0.147%` vs `-0.110%`).
  - EA sectoral GDP ranking is weakly related to the trade proxy under heterogeneous DCP (`R^2 = 0.068`) but strongly related under PCP (`R^2 = 0.930`).

- The revised appendix claims on the alpha/mu split are supported.
  - China GDP under Shock A: trade `R^2 = 0.931`, `alpha = 0.041`, `mu = 0.872`.
  - US GDP under Shock A: trade `R^2 = 0.907`, `alpha = 0.014`, `mu = 0.789`.
  - China trade-plus-IO adds almost nothing to the fit (`0.931 -> 0.933`).
  - EA benchmark CPI is strongly organized by the proxy under DCP (`R^2 = 0.924`), while EA GDP is not (`R^2 = 0.068`); under PCP this flips for GDP/CPI (`0.930` / `0.128`).

## Claims revised

- Abstract sentence on the euro area.
  - Old version implied a stable ranking comparison between “cost-push” and “expenditure-switching” channels.
  - Revised because the regenerated appendix shows a regime reversal: benchmark DCP organizes EA CPI but not GDP, while PCP organizes EA GDP but not CPI.

- Section 5 opening sectoral-ranking paragraph.
  - Removed stale exact bilateral-share percentages for Textiles and Electronics.
  - Kept the verified ordering claim: Textiles has the largest benchmark bilateral trade share and Electronics the second-largest.

- Conclusion paragraph on sectoral ranking.
  - Replaced stale legacy diagnostics (`R^2 = 0.89 / 0.85`, Domar-weight result, `beta_vartheta = 5.3`, EA `77%` vs `19%`) with the current appendix outputs.
  - New paragraph now matches the regenerated horse-race tables and alpha/mu decomposition.

## Residual limits

- Some mechanism language remains interpretive rather than directly identified.
  - In particular, statements about “trade diversion” versus “upstream cost propagation” in the EA are supported by sign patterns and accounting identities, but the two channels are not separately identified in general equilibrium.

- The audit covered the compiled manuscript only.
  - Legacy draft files not included in `0_main.tex` were not cleaned up in this pass.

## Build check

- Recompiled successfully with:
  - `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`
- Output:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`
- Remaining messages were non-fatal LaTeX warnings already present in the project.
