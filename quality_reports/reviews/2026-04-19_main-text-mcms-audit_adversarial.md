# Main-Text MCMS Audit

Scope: main text only. Appendix material is excluded by user instruction.

Admissible evidence:
- MCMS source code
- readable MCMS exported CSV/PNG artifact layer
- direct execution of MCMS scripts
- no claims taken from manuscript prose as evidence

Primary evidence snapshot:
- [maintext_mcms_evidence.json](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/maintext_mcms_evidence.json)
  Includes generation timestamp plus SHA256 and mtime fingerprints for the key CSV and MAT artifacts used in this audit.

Verification commands run:
- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python master_supporting_docs/MCMS/extract_paper_numbers.py`
- `python master_supporting_docs/MCMS/new_process.py`
- `python explorations/full_paper_mcms_audit/scripts/build_maintext_evidence.py`

## Findings

1. High: the Figure 4 elasticity discussion no longer describes the current MCMS export, and it understates the size of the effect.
Location:
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:142)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:153)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:518)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:37)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:196)

What the paper says:
- the counterfactual is `delta = 1, mu = 2`
- only the household trade elasticity changes
- the China three-year average contraction is about `0.03 pp` smaller under low elasticity

What MCMS says:
- Figure 4 is built from `irf_Het_DCP_Baseline_UnitElast.mat` versus `irf_Het_DCP_Baseline.mat`
- the readable `UnitElast` config is `armington = 2`
- `a1_calibration.m` maps `armington = 2` to `Delta_C = 1` and `Delta_X = 1`
- the current export layer gives China three-year averages of `-0.1054` and `-0.1469`, a gap of `0.0415 pp`

Impact:
- the low-elasticity arm in the current figure uses `Delta_C = 1` and `Delta_X = 1`, not a household-only change
- the paragraph and caption materially misstate the experiment behind the plotted numbers
- the prose should say about `0.04 pp` smaller, not `0.03 pp`

2. High: seven robustness captions describe a bilateral tariff shock, but the MCMS pipeline uses the unilateral US-on-China leg only.
Location:
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:91)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:105)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:136)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:153)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:162)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:182)
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:189)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:465)

What MCMS says:
- Figures `2`, `3a`, `4`, `5a`, `17`, and `18` all use `shock_pair = (4, 2)`
- that is the unilateral US tariff on China leg
- only Figure `1` is assembled from both `Figure_1` (`4 -> 2`) and `Figure_1b` (`2 -> 4`)

Impact:
- the captions overstate the experiment and misdescribe what the plotted robustness numbers represent
- the main text already describes some of these figures as unilateral, so the caption layer is internally inconsistent even before checking code

3. Medium: the introduction and conclusion overclaim what the current robustness evidence shows.
Location:
- [11_introduction.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex:11)
- [60_Conclusions.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex:9)

What the paper says:
- IO is the `primary amplification mechanism`

What MCMS currently shows:
- shutting down all IO reduces the Chinese three-year contraction by about `40%`
- shutting down international IO alone accounts for about one-third of the baseline contraction

Impact:
- the code and export layer support IO as a major amplification mechanism
- they do not, by themselves, establish primacy relative to all other robustness margins

4. Medium-low: the exact EA bilateral-margin sentences are not directly table-backed in a single clean readable export.
Location:
- [55a_benchmark_and_robustness.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:33)
- [56_sectoral_channels.tex](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:102)

What is verified:
- the aggregate EA trade-balance and GDP objects are reproduced from `Figure_1_Benchmark_IRFs_TimeSeries.csv`
- the paper's `+0.0171%` trade-balance and `+0.0011%` GDP statements are rounding-consistent with the current export layer
- the readable export layer does contain bilateral fields and related components in `Figure_1_Benchmark_IRFs_SectoralTransmission_Long.csv` and `Figure_1_Benchmark_Transmission_Decomposition.csv`

What is not yet cleanly traced:
- `EA-US`, `EA-China`, and `ROW` bilateral net-margin numbers such as `+0.0785%`, `-0.0604%`, `-0.0268%`, `+0.0368%`

Reason:
- the benchmark MAT is unreadable
- the surviving readable main-text CSV layer does not expose those exact partner-margin sentences in a single dedicated table

Impact:
- those bilateral-margin lines should be treated as not directly table-backed from the surviving readable main-text artifact layer
- they need either a repaired benchmark MAT or a dedicated bilateral export

5. Operational verification risk: the main-text figure pipeline is not currently reproducible from MCMS on this machine.
Location:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:648)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5039)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5357)

Observed execution result:
- `python new_process.py` exits with `KeyError: Unable to synchronously open object (address of object past end of allocation)` when opening `irf_Het_DCP_Baseline.mat`
- the fallback MATLAB preprocessing path then fails with `System Error: File system inconsistency`

Impact:
- active main-text figures cannot currently be regenerated end-to-end from MCMS on this machine
- this is an operational verification blocker rather than a separate paper-number mismatch

## Verified Main-Text Numbers

### Introduction and Conclusions

Supported by current MCMS exports and rounding-consistent:
- 4 economies and 44 sectors
- IO shutdown reduces the Chinese three-year average contraction by about `40%`
  Evidence: baseline `-0.147`, zero-all-IO `-0.088`, attenuation `40.1%`
- international IO alone accounts for about one-third of the baseline contraction
  Evidence: `(-0.147 - -0.097) / 0.147 = 34.0%`
- heterogeneous DCP makes the Chinese three-year average contraction over `30%` larger than PCP
  Evidence: `-0.147` versus `-0.112`, increase `31.3%`
- conclusion values `-0.147`, `-0.119`, and `-0.236` match the current monetary-policy and peg exports

### Calibration

Supported directly by [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:1):
- `K = 4`, `I = 44`, `3` energy sectors, `20` tariffed tradeable manufacturing sectors
- `beta = 0.99`, `sigma = 1`, `varphi = 1`, `gamma_star = 0.001`
- household elasticities `gamma = 0.4`, `eta = 0.9`, `iota = 0.9`
- production non-trade elasticities `gamma_x = 0.4`, `eta_x = 0.2`, `iota_x = 0.2`
- Taylor parameters `rho_r = 0.7`, `phi_pi = 1.5`, `phi_y = 0`, `phi_delta_pi = 0`, `phi_delta_y = 0.125`
- tariff process `rho_tau = 0.96`, `sigma_tau = 1`, monetary shock `sigma_r = 1`
- invoicing counts `PCP = 7`, `LCP = 20`, `DCP = 17`

### Benchmark and Robustness Numbers

All of the following match the readable MCMS export layer to paper rounding:
- benchmark forward leg: `US GDP -0.04%` on impact, `+0.035%` by quarter 8; `China GDP -0.24%` on impact and `-0.08%` by quarter 12; `EA GDP +0.001%` on impact and `+0.012%` by quarter 5
- CPI: `US +0.13 pp` impact and `+0.15 pp` at quarter 4 rolling; `China +0.015 pp`; `EA +0.007 pp`, negative from quarter 5
- trade balance: `US +1.55%` impact and `+0.66%` by quarter 12; `China -1.02%` impact and `-0.17%` by quarter 12; `EA +0.017%` impact
- REER: `US -0.37%`, `China +0.31%`, `EA +0.08%` on impact; reverse leg `US +0.11%`, `China -0.20%`
- consumption: `US -0.257%`, `China -0.055%` on impact; reverse-leg Chinese consumption `-0.052%` at Q1 and `-0.042%` at Q2
- DCP/PCP/full-DCP three-year China GDP: `-0.147`, `-0.112`, `-0.135`
- IO robustness China GDP: `-0.147`, `-0.097`, `-0.088`
- peg robustness China GDP: `-0.147` baseline versus `-0.236` peg, amplification `60.9%`
- monetary-policy robustness: China `-0.147` benchmark versus `-0.119` near-fixed; US `0.019` versus `0.028`; EA `0.009` versus `0.003`

### Sectoral Channels

Supported by `Figure_6_Baseline_Bars_CrossSection.csv` and `Figure_SectoralSpillover_Matrix.csv`:
- US GDP bars: textiles `-0.0285%`, electronics `-0.0095%`, other manufacturing `-0.0069%`
- China GDP bars: textiles `-0.0562%`, electronics `-0.0495%`, other manufacturing `-0.0395%`
- US CPI bars: textiles `0.0460 pp`, electronics `0.0331 pp`, other manufacturing `0.0263 pp`
- China own-sector VA: other manufacturing `-1.80%`, electronics `-1.17%`, textiles `-0.74%`
- EA own-sector VA: electronics `0.139%`, textiles `0.109%`, other manufacturing `0.096%`
- cross-sector gross shares: US `61.19%`, China `59.98%`
- cross-sector dominance counts: US `9/20`, China `18/20`
- US composition shares: services `77.47%`, other tradeables `15.99%`, energy `6.55%`
- China composition shares: services `50.87%`, other tradeables `41.20%`, energy `7.94%`
- US service-share distribution: min `43.8%`, median `74.8%`, max `83.6%`, with `19/20` above `50%`
- China service-share distribution: median `50.0%`, with `10/20` above `50%`
- EA own-positive/aggregate-negative count: `12/20`

## Figure-to-Pipeline Check

Paper-consistent:
- Figure 1: reciprocal benchmark assembled from `Figure_1` and `Figure_1b`
- Section 56 figures: all map cleanly to the unilateral `4 -> 2` benchmark cross-section and spillover exports, which matches the paper captions

Paper-inconsistent:
- robustness captions that say `Shock: 10 pp bilateral tariff across all 20 tradeable sectors`
  MCMS source of truth is unilateral `4 -> 2`

## Overall Audit Status

Main-text numbers in prose are mostly consistent with current readable MCMS exports, often exactly to the displayed rounding. The major paper-facing problems are not broad numeric drift; they are experiment-description mismatches in the robustness block and a reproducibility failure in the active figure generator.
