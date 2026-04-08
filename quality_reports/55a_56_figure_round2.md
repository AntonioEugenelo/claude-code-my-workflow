# Figure-Data Consistency Report: Tariffs_ECB Sections 4 and 5

- **Scope:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`, `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`, directly relevant appendix/supporting text under `master_supporting_docs/Tariffs_ECB/0_clean/sections/`, and the full figure inventory under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
- **Round:** 2
- **Reviewer focus:** figure-data consistency only; no source edits made.

## Evidence Note

I reviewed the active sections, the appendix derivation text, the older `55_model_dynamics_and_scenarios.tex` variant, and the relevant figure inventory in `figures/`. I did not find CSV, MAT, or similar raw data artifacts anywhere under `master_supporting_docs/Tariffs_ECB/`, so exact machine-checking is still limited to the visible figures and the numeric annotations printed in the paper text.

## Summary

The active section-4/5 claims remain consistent with the rendered figures. The broader scope did not expose any new contradiction in the current paper text. It did, however, add two useful layers of corroboration:

- The older dynamics/scenario variant confirms that the repository also contains superseded cumulative-GDP versions of the same figure family, which are internally consistent with their own captions but are not the active normalization used in `55a_benchmark_and_robustness.tex`.
- The appendix-sectoral-targeting file and its figures provide independent confirmation for a separate EA-targeting experiment, including exact sector rankings and retaliation trade-offs.

The only items still not fully checkable are the exact decomposition claims that require underlying time-series or cross-section data, especially the EA GDP decomposition in section 5 and the policy-rate / channel-decomposition subclaims in section 4.

## Claim Checks: Active Sections

### Claim F-1: Benchmark CPI responses
- **Location:** `55a_benchmark_and_robustness.tex:15`
- **Claimed value:** US CPI rises `0.13` pp on impact and peaks at `0.15` pp in Q4; China rises `+0.015` pp on impact; under the Chinese tariff, US CPI reaches `-0.007` pp by Q11 and China rises `+0.030` pp on impact.
- **Evidence:** `Fig_Benchmark_CPI.png`
- **Actual value:** The figure shows the same ordering and approximate magnitudes: a large US impact response, a much smaller Chinese response under the US tariff, and the reversed sign pattern under retaliation.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-2: Benchmark real GDP responses
- **Location:** `55a_benchmark_and_robustness.tex:19`
- **Claimed value:** US GDP falls by about `0.04%` on impact and reaches roughly `+0.035%` by Q8; China falls by `0.24%` on impact and about `-0.08%` by Q12; under retaliation, China rises by `0.04%`.
- **Evidence:** `Fig_Benchmark_GDP.png`
- **Actual value:** The US line starts near `-0.04`, crosses back above zero, and reaches the quoted positive range by mid-horizon; China starts near `-0.24` and recovers only partially by Q12. The retaliation panel also matches the stated sign reversal.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-3: Benchmark consumption responses
- **Location:** `55a_benchmark_and_robustness.tex:86` and `55a_benchmark_and_robustness.tex:90`
- **Claimed value:** US consumption contracts by about `0.26%` on impact and stays negative; China contracts by about `0.06%` on impact; under retaliation China is `-0.052%` on impact and `-0.042%` by Q2.
- **Evidence:** `Fig_Benchmark_Consumption.png`
- **Actual value:** The plotted paths are consistent with the quoted magnitudes and signs in both directions.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-4: Trade balance responses
- **Location:** `55a_benchmark_and_robustness.tex:78`
- **Claimed value:** Under the US tariff, US trade balance improves by `+1.55%` on impact and declines to `+0.66%` by Q12; China worsens by `-1.02%` on impact and recovers to `-0.17%`; the EA peaks around `+0.017%` in Q3. Under retaliation, the US worsens by `-0.93%`, China improves by `+0.51%`, and the EA is about `+0.01%`.
- **Evidence:** `Fig_Benchmark_TB.png`
- **Actual value:** The figure shows the same sign pattern and the same rough magnitudes, including the EA's small positive hump around Q3 and the reversed retaliation panel.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-5: REER responses in the benchmark shock
- **Location:** `55a_benchmark_and_robustness.tex:82`
- **Claimed value:** Under the US tariff, the US REER appreciates by `-0.37%` on impact, China depreciates by `+0.31%` on impact and `+0.25%` by Q12, and the EA depreciates by `+0.08%` on impact. Under retaliation, the US depreciates by `+0.11%` and China appreciates by `-0.20%`.
- **Evidence:** `Fig_Benchmark_REER_DW.png`
- **Actual value:** The plotted REER paths align with the quoted signs and the approximate impact / end-horizon values.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-6: Sectoral GDP decomposition of the benchmark response
- **Location:** `55a_benchmark_and_robustness.tex:102`
- **Claimed value:** US top GDP drags are Textiles `-0.029%`, Electronics `-0.009%`, and Other Manufacturing `-0.007%`; China top GDP drags are Textiles `-0.056%`, Electronics `-0.049%`, and Other Manufacturing `-0.039%`; EA spillovers are negligible, with Electronics `-0.001%` and Textiles `-0.000%`.
- **Evidence:** `Fig_Sectoral_Bars_GDP.png`
- **Actual value:** The bar ranks and approximate magnitudes match the text, including the concentration of the US and China effects in the same top sectors and the near-zero EA bars.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-7: Sectoral CPI decomposition of the benchmark response
- **Location:** `55a_benchmark_and_robustness.tex:111`
- **Claimed value:** US CPI contributions are led by Textiles `+0.046` pp, Electronics `+0.033` pp, and Other Manufacturing `+0.026` pp; China contributions are much smaller, with Electronics `+0.002` pp and Textiles `+0.001` pp; EA is muted, with Electronics `+0.001` pp leading.
- **Evidence:** `Fig_Sectoral_Bars_CPI.png`
- **Actual value:** The figure shows the same ranking and the same order-of-magnitude gap between the US and China panels.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-8: Chinese own-sector heatmap and the China-vs-US ranking
- **Location:** `56_sectoral_channels.tex:15`, `56_sectoral_channels.tex:17`, `56_sectoral_channels.tex:19`, `56_sectoral_channels.tex:40`
- **Claimed value:** All 20 US sectors have positive own-sector value-added responses; China's largest contractions are Other Manufacturing `-1.80%`, Electronics `-1.17%`, Textiles `-0.74%`, Electrical Equipment `-0.62%`, and Fabricated Metals `-0.56%`; only 3 of 20 Chinese sectors have negative own-sector inflation, with Electronics `+0.0001` pp and Textiles `+0.00004` pp the largest positive responses.
- **Evidence:** `Fig_CN_Sectoral_Heatmap.png` and `Fig_CN_Structural_Scatter.png`
- **Actual value:** The heatmap and scatter show the quoted ordering and magnitudes. The US top panels are uniformly positive, the Chinese bottom panels show the cited large negative sectors, and the inflation panel has only a few negative sectors with the quoted tiny positive leaders.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-9: EA structural scatter correlations
- **Location:** `56_sectoral_channels.tex:49` and `56_sectoral_channels.tex:58`
- **Claimed value:** For the EA, all nine correlations are negligible and lie in `[0.000, 0.013]`; the largest is price flexibility vs. CPI at `R^2 = 0.013` (`p = 0.64`), while the US has weak correlations (`R^2 in [0.013, 0.053]`) and China has a meaningful IO-linkage correlation (`R^2 approx 0.165`, `p = 0.075`).
- **Evidence:** `Fig_CN_Structural_Scatter_3x3.png`, `Fig_CHN_Structural_Scatter_3x3.png`, `Fig_US_Structural_Scatter_3x3.png`
- **Actual value:** The annotations in the scatter grids match the quoted R-squared values and p-values.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-10: EA own-sector heatmap and composition
- **Location:** `56_sectoral_channels.tex:82`, `56_sectoral_channels.tex:86`, `56_sectoral_channels.tex:97`
- **Claimed value:** EA own-sector value added is positive or near-zero in all 20 sectors, led by Electronics `+0.14%`, Textiles `+0.11%`, and Other Manufacturing `+0.10%`; the sectoral gains and losses nearly cancel, leaving aggregate EA GDP near zero on impact.
- **Evidence:** `Fig_EA_Sectoral_Heatmap_USCN.png`
- **Actual value:** The bar chart confirms the positive-or-near-zero pattern and the top-sector ranking.
- **Verdict:** MATCH for the heatmap claim
- **Severity:** none
- **Note:** The exact GDP decomposition numbers in the surrounding prose (`+0.005%`, `+0.004%`, `+0.009%`, and the on-impact `+0.001% = -0.003% + 0.004%`) are not directly visible in any figure and could not be independently checked because no underlying data file was available.

### Claim F-11: DCP regime averages and REER comparison
- **Location:** `55a_benchmark_and_robustness.tex:154`, `55a_benchmark_and_robustness.tex:156`, `55a_benchmark_and_robustness.tex:162`, `55a_benchmark_and_robustness.tex:167`, `55a_benchmark_and_robustness.tex:174`
- **Claimed value:** Heterogeneous DCP gives China `-0.147%` vs. `-0.11%` under PCP, and EA `+0.009%` under both; Full DCP gives China `-0.135%`; the DCP REER figure shows larger Chinese depreciation under Heterogeneous DCP than under PCP.
- **Evidence:** `DCP_Average_Combined_Compare.png` and `Fig_DCP_REER_DW.png`
- **Actual value:** The bar chart and REER paths show the stated ordering and the quoted average values to plotting precision.
- **Verdict:** MATCH
- **Severity:** none
- **Note:** The channel-decomposition numbers in the prose (`-0.88%` vs. `-1.02%` trade balance, `-0.08%` vs. `-0.06%` consumption, `-1.86%` vs. `-1.68%` exports, and the associated narrative interpretation) are not directly visible in the plotted figure and could not be separately audited without raw data artifacts.

### Claim F-12: IO and elasticity robustness
- **Location:** `55a_benchmark_and_robustness.tex:186`, `55a_benchmark_and_robustness.tex:195`, `55a_benchmark_and_robustness.tex:200`
- **Claimed value:** Removing international IO attenuates China's average contraction to `-0.10%`, and removing all IO attenuates it further to `-0.09%`; lowering the household Armington elasticity to `delta = 1` makes China's three-year GDP contraction about `0.03` pp smaller.
- **Evidence:** `IO_Average_Combined_Compare.png` and `Elasticity_Average_Combined_Compare.png`
- **Actual value:** The figure bars and markers align with the quoted magnitudes and the expected attenuation pattern.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-13: Exchange-rate peg robustness
- **Location:** `55a_benchmark_and_robustness.tex:204`, `55a_benchmark_and_robustness.tex:209`
- **Claimed value:** A Chinese peg deepens the average China contraction from `-0.147%` to `-0.236%` (about `61%`), while US and EA GDP rise to `+0.035%` and `+0.023%`.
- **Evidence:** `Peg_Average_Combined_Compare.png`
- **Actual value:** The benchmark-vs-peg bars show the same sign pattern and the same approximate values.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-14: Monetary-policy robustness
- **Location:** `55a_benchmark_and_robustness.tex:215`, `55a_benchmark_and_robustness.tex:226`, `55a_benchmark_and_robustness.tex:233`
- **Claimed value:** Near-fixed policy reduces China's three-year GDP contraction from `-0.147%` to `-0.119%`, raises US GDP from `+0.019%` to `+0.028%`, and lowers EA GDP from `+0.009%` to `+0.003%`; the REER figure shows benchmark overshooting for the US and much less overshooting under near-fixed rates.
- **Evidence:** `MonPol_Average_Combined_Compare.png` and `Fig_MonPol_REER_DW.png`
- **Actual value:** The bars and REER paths match the quoted average responses and the overshooting / no-overshooting contrast.
- **Verdict:** MATCH
- **Severity:** none
- **Note:** The exact policy-rate magnitudes in the prose (`+0.056` pp on impact for the benchmark and `<0.001` pp under near-fixed rates) are not directly visible in any available figure and could not be independently checked without raw time-series data.

## Broader-Scope Appendix Checks

### Claim F-15: Appendix sectoral ranking for the EA-targeting experiment
- **Location:** `a_appendix_sectoral_targeting.tex:18`
- **Claimed value:** Pharmaceuticals generates the largest contraction (`-0.085` pp), accounting for roughly 30% of the total aggregate GDP effect (`-0.285` pp across all 20 tradeable sectors), followed by Chemical Products (`-0.034` pp), Motor Vehicles (`-0.031` pp), Food & Beverages (`-0.026` pp), and Other Manufacturing (`-0.024` pp).
- **Evidence:** `Fig_Sectoral_Ranking_EA.png`
- **Actual value:** The bar chart confirms the exact ranking and the approximate magnitudes.
- **Verdict:** MATCH
- **Severity:** none

### Claim F-16: Appendix retaliation trade-off
- **Location:** `a_appendix_sectoral_targeting.tex:43`, `a_appendix_sectoral_targeting.tex:45`, `a_appendix_sectoral_targeting.tex:79`
- **Claimed value:** The largest US GDP impacts are Chemicals (`-0.016` pp), Electronics (`-0.015` pp), and Pharmaceuticals (`-0.013` pp); the largest EA CPI increases are Electronics and Pharmaceuticals (`0.008` pp each); and retaliating across all 20 sectors yields US GDP `-0.107` pp, EA GDP `+0.031` pp, and EA CPI `+0.054` pp.
- **Evidence:** `Fig_Retaliation_Tradeoff.png`
- **Actual value:** The scatter plot shows the same ordering and the same approximate values.
- **Verdict:** MATCH
- **Severity:** none

## Broader-Scope Notes

- The older `55_model_dynamics_and_scenarios.tex` file and its companion figure family (`Fig_Robust_DCP_GDP.png`, `Fig_Robust_IO_GDP.png`, `Fig_Robust_Elast_GDP.png`, `Fig_Robust_Peg_GDP.png`, `Fig_Liberation_GDP.png`, `Fig_EA_Comparison.png`, `Fig_EA_TradeBalance.png`, `Fig_EA_Sectoral_Triptych.png`) are useful context, but they use different normalizations and scenario sets than the active section-4/5 text. They are internally consistent with their own captions and are not evidence of a current-paper error.
- The appendix derivation text in `a_appendix.tex` confirms the sign conventions and identities behind the trade-balance, GDP, DCP, and REER interpretations used in the current sections, but it does not replace missing raw data for exact machine-level checks.

## Figure-Level Verdicts

- `Fig_Benchmark_CPI.png`: CONSISTENT
- `Fig_Benchmark_GDP.png`: CONSISTENT
- `Fig_Benchmark_Consumption.png`: CONSISTENT
- `Fig_Benchmark_TB.png`: CONSISTENT
- `Fig_Benchmark_REER_DW.png`: CONSISTENT
- `Fig_Sectoral_Bars_GDP.png`: CONSISTENT
- `Fig_Sectoral_Bars_CPI.png`: CONSISTENT
- `Fig_CN_Sectoral_Heatmap.png`: CONSISTENT
- `Fig_CN_Structural_Scatter.png`: CONSISTENT
- `Fig_CN_Structural_Scatter_3x3.png`: CONSISTENT
- `Fig_CHN_Structural_Scatter_3x3.png`: CONSISTENT
- `Fig_US_Structural_Scatter_3x3.png`: CONSISTENT
- `Fig_EA_Sectoral_Heatmap_USCN.png`: CONSISTENT
- `DCP_Average_Combined_Compare.png`: CONSISTENT
- `Fig_DCP_REER_DW.png`: CONSISTENT
- `IO_Average_Combined_Compare.png`: CONSISTENT
- `Elasticity_Average_Combined_Compare.png`: CONSISTENT
- `Peg_Average_Combined_Compare.png`: CONSISTENT
- `MonPol_Average_Combined_Compare.png`: CONSISTENT
- `Fig_MonPol_REER_DW.png`: CONSISTENT
- `Fig_Structural_Scatter_EA.png`: CONSISTENT
- `Fig_Sectoral_Ranking_EA.png`: CONSISTENT
- `Fig_Sectoral_Phillips.png`: CONSISTENT
- `Fig_Retaliation_Tradeoff.png`: CONSISTENT

## Score Suggestion

- **Suggested deduction:** `0`
- **Suggested score:** `100/100`
- **Rationale:** No directly checkable claim contradicted its figure. The remaining limitations are auditability gaps caused by absent raw CSV/MAT artifacts, not evidence of a paper error.
