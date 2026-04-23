# Main-Text MCMS Audit After Fresh Benchmark Rerun

Scope: active main text only. Appendix material is excluded by user instruction.

This report supersedes the pre-rerun main-text audit for any claim that depends on the benchmark run, the saved benchmark MAT, or the transmission-decomposition layer.

## Source Of Truth

- Restored [a0_launch.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a0_launch.m:1) exactly to the last committed inline sequence.
- Reran the benchmark through the old inline path via [a0_launch_benchmark_rerun.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a0_launch_benchmark_rerun.m:1), with the run log in [benchmark_rerun_oldpath.log](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/benchmark_rerun_oldpath.log:1).
- Fresh benchmark export:
  - [irf_Het_DCP_Baseline.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat)
  - SHA256: `6c40c0b54ced3a5f8231365ca80b27a0057bc9e3074bd2aea2bfb438bea72414`
  - mtime UTC: `2026-04-19T12:30:14.194636+00:00`
- Fresh full Dynare solution from the rerun:
  - [b0_main_results.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat)
  - mtime local: `2026-04-19 14:30:04`
- Rebuilt the manuscript-facing CSV layer from MAT inputs with `python new_process.py`.
- Refreshed evidence snapshot:
  - [maintext_mcms_evidence.json](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/maintext_mcms_evidence.json)
  - [active_claim_inventory.md](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/active_claim_inventory.md)
  - [2026-04-19_direct_mat_checks.json](C:/CustomTools/claude-code-my-workflow/quality_reports/tmp/2026-04-19_direct_mat_checks.json)
  - [2026-04-19_extract_paper_numbers_after_rerun.txt](C:/CustomTools/claude-code-my-workflow/quality_reports/tmp/2026-04-19_extract_paper_numbers_after_rerun.txt)

## Findings

1. High: the Figure 4 text and caption still describe the wrong elasticity experiment.
Location:
- [43_calibration.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/43_calibration.tex:60)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:142)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:153)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:37)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:196)

What MCMS says:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:595) builds Figure 4 from `irf_Het_DCP_Baseline_UnitElast.mat` versus `irf_Het_DCP_Baseline.mat`.
- The saved `config_used.armington` for `irf_Het_DCP_Baseline_UnitElast.mat` is `2`, recorded in [2026-04-19_direct_mat_checks.json](C:/CustomTools/claude-code-my-workflow/quality_reports/tmp/2026-04-19_direct_mat_checks.json:1).
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:196) maps `armington = 2` to `Delta_C = 1` and `Delta_X = 1`.
- The China three-year averages are `-0.1054` and `-0.1469`, a gap of `0.0415 pp`, not `0.03 pp`.

Impact:
- The current figure is a `delta = mu = 1` counterfactual, not a household-only `delta = 1, mu = 2` exercise.
- Section 43 is internally consistent with the code, but Section 55a is not.
- The prose and caption should be rewritten to match the actual `delta = mu = 1` export, with the China attenuation rounded to about `0.04 pp`.

2. High: the robustness captions in Section 55a still describe bilateral shocks, while the code and MAT pipeline use the unilateral `4 -> 2` US-on-China leg.
Location:
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:91)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:105)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:136)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:153)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:162)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:182)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:189)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:557)

What MCMS says:
- Figures `2`, `3a`, `4`, `5a`, `17`, and `18` all use `shock_pair = (4, 2)`.
- Only Figure `1` combines both legs: `Figure_1` (`4 -> 2`) and `Figure_1b` (`2 -> 4`).

Impact:
- The caption layer is still overstating the experiment.
- The main-text prose already describes several of these exercises as unilateral, so the captions are code-inconsistent and manuscript-inconsistent at the same time.

3. Medium: the introduction still overstates what the current MCMS evidence establishes.
Location:
- [11_introduction.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex:11)

What MCMS shows:
- Zeroing international IO attenuates the Chinese three-year average contraction from `-0.1469` to `-0.0975`.
- Zeroing all IO attenuates it further to `-0.0883`.
- Those magnitudes support IO as a major amplification channel.

Why the wording is still too strong:
- The code establishes importance, not a full ranking against every other mechanism in the model.
- `"Primary amplification mechanism"` is stronger than the current robustness evidence strictly delivers.

## Resolved Relative To The Pre-Rerun Audit

- The exact EA bilateral-margin numbers are now directly verified from the fresh MAT/results layer. The earlier `"not cleanly table-backed"` concern no longer stands.
- `new_process.py` completed successfully after the fresh benchmark rerun, so the earlier hard reproducibility blocker is gone.
- Remaining technical nuance: the saved benchmark MAT is now readable and sufficient for aggregate and bilateral trade checks, but the transmission-decomposition export in [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5031) still falls back to [b0_main_results.mat](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat) for the `c/x` blocks needed by `extract_benchmark_transmission_decomposition()`.

## Verified Main-Text Numbers

### Calibration

Directly supported by [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:1):
- `K = 4`, `I = 44`, `3` energy sectors, `21` services, `20` tradeable manufacturing sectors
- `beta = 0.99`, `sigma = 1`, `varphi = 1`, `gamma_star = 0.001`
- household elasticities `gamma = 0.4`, `eta = 0.9`, `iota = 0.9`
- production elasticities `gamma_x = 0.4`, `eta_x = 0.2`, `iota_x = 0.2`
- Taylor-rule parameters `rho_r = 0.7`, `phi_pi = 1.5`, `phi_y = 0`, `phi_delta_pi = 0`, `phi_delta_y = 0.125`
- tariff process `rho_tau = 0.96`, `sigma_tau = 1`, monetary shock `sigma_r = 1`
- invoicing counts `PCP = 7`, `LCP = 20`, `DCP = 17`

### Benchmark Aggregate Dynamics

Supported by the fresh benchmark MAT/export layer:
- US tariff on China leg: `US GDP -0.041` on impact and `+0.035` by quarter 8; `China GDP -0.242` on impact and `-0.081` by quarter 12; `EA GDP +0.0011` on impact and `+0.0116` by quarter 5
- CPI: `US +0.127 pp` on impact and `+0.151 pp` at quarter 4 rolling; `China +0.0146 pp`; `EA +0.0069 pp`, turning negative from quarter 5
- trade balance: `US +1.555` on impact and `+0.656` by quarter 12; `China -1.024` on impact and `-0.171` by quarter 12; `EA +0.0171` on impact
- REER: `US -0.371`, `China +0.307`, `EA +0.080` on impact; reverse leg `US +0.111`, `China -0.200`
- consumption: `US -0.257`, `China -0.055` on impact; reverse-leg Chinese consumption `-0.0516` at Q1 and `-0.0422` at Q2

### EA Bilateral Margins

Directly verified from the fresh benchmark MAT/results layer:
- US tariff on China:
  - EA exports to US `+0.0598`
  - EA imports from US `-0.0187`
  - EA-US net margin `+0.0785`
  - EA exports to China `-0.0613`
  - EA imports from China `-0.0009`
  - EA-China net margin `-0.0604`
  - EA-ROW net margin `-0.0010`
  - total EA trade-balance response `+0.0171`
- China tariff on US:
  - EA-US net margin `-0.0268`
  - EA-China net margin `+0.0368`
  - EA-ROW net margin `+0.0029`
  - total EA trade-balance response `+0.0128`

### Invoicing And Other Robustness Numbers

Supported by the refreshed MAT-driven output layer:
- heterogeneous DCP versus PCP:
  - China three-year GDP `-0.1469` versus `-0.1123`, a `31.3%` larger contraction under heterogeneous DCP
  - on-impact EA GDP `+0.0011` under heterogeneous, `+0.0171` under PCP, and `-0.0170` under full DCP
  - on-impact EA-US net margin `+0.0785` heterogeneous, `+0.1485` PCP, `+0.1094` full DCP
  - on-impact EA-China net margin `-0.0604` heterogeneous, `-0.1108` PCP, `-0.0877` full DCP
  - on-impact EA-ROW net margin `-0.0010` heterogeneous, `+0.0124` PCP, `-0.0163` full DCP
- heterogeneous versus full DCP:
  - China trade balance on impact `-1.0240` versus `-0.8771`
  - China consumption on impact `-0.0552` versus `-0.0778`
  - China exports on impact `-1.6809` versus `-1.8604`
- IO counterfactuals:
  - China three-year GDP `-0.1469`, `-0.0975`, `-0.0883`
  - attenuation from zeroing all IO is `40.1%`
  - attenuation attributable to international IO alone is `34.0%` of the baseline contraction
- peg:
  - China `-0.1469` baseline versus `-0.2364` peg
  - amplification `60.9%`
- monetary policy:
  - China `-0.1469` benchmark versus `-0.1187` near-fixed
  - US `+0.0191` versus `+0.0280`
  - EA `+0.0085` versus `+0.0032`
  - US CPI three-year average rolling-four-quarter measure `0.0637` benchmark versus `0.0351` near-fixed
  - US quarter-by-quarter CPI is `+0.0082` in Q2 and `+0.0079` in Q3 under the benchmark, versus `+0.0003` and `-0.0004` under near-fixed
  - US REER on impact `-0.3705` benchmark versus `-0.2374` near-fixed
  - US rate on impact `+0.0558 pp` benchmark versus `+0.00018 pp` near-fixed

### Sectoral Channels

Supported by [Figure_6_Baseline_Bars_CrossSection.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv) and [Figure_SectoralSpillover_Matrix.csv](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv):
- US GDP bars: textiles `-0.0285`, electronics `-0.0095`, other manufacturing `-0.0069`
- China GDP bars: textiles `-0.0562`, electronics `-0.0495`, other manufacturing `-0.0395`
- US CPI bars: textiles `+0.0460 pp`, electronics `+0.0326 pp`, other manufacturing `+0.0262 pp`
- China own-sector VA: other manufacturing `-1.80`, electronics `-1.17`, textiles `-0.74`, electrical equipment `-0.62`
- EA own-sector VA: electronics `+0.139`, textiles `+0.109`, other manufacturing `+0.096`
- cross-sector gross shares: US `61.19%`, China `59.98%`
- cross-sector dominance counts: US `9/20`, China `18/20`
- US composition shares: services `77.47%`, other tradeables `15.99%`, energy `6.55%`
- China composition shares: services `50.87%`, other tradeables `41.20%`, energy `7.94%`
- US service-share distribution: min `43.8%`, median `74.8%`, max `83.6%`, with `19/20` above `50%`
- China service-share distribution: median `50.0%`, with `10/20` above `50%`
- EA positive-own / negative-aggregate count: `12/20`

Dense narrative spot-checks in Section 56 also match the refreshed matrix:
- US textiles own share `0.19%`, own VA `+3.192%`, own GDP contribution `+0.00619`, aggregate `-0.02853`
- US textiles service-offset paragraph: real estate `-0.0369` VA and `-0.00617` GDP contribution; health `-0.00385`; finance `-0.00354`; wholesale `-0.00243`; four-sector subtotal `-0.0160`, equal to `46.1%` of the textiles cross-sector term
- electronics paragraph: the same four services account for `49.3%` of the electronics cross-sector term

## Overall Status

After restoring the old launcher path, rerunning the benchmark, and rebuilding the manuscript CSV layer from MAT inputs, the main-text numbers remain largely stable. The benchmark-side numerical claims, the EA bilateral-margin claims, and the sectoral-accounting claims are now directly backed by the fresh MCMS MAT/results layer. The remaining manuscript problems are not broad numeric drift; they are description mismatches:
- Figure 4 still describes the wrong experiment and understates the gap.
- Section 55a robustness captions still label unilateral exercises as bilateral.
- The introduction still overclaims primacy for IO amplification.
