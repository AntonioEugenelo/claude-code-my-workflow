# Monetary Policy Figure Audit

- **Date:** 2026-04-08
- **Question:** Is the monetary-policy paragraph in Sections 4 and 5 consistent with the saved code/data pipeline, especially the claim that US inflation is higher under the benchmark than under near-fixed rates?

## Scope

- Paper text:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_conclusions.tex`
- Model/code repo:
  - `master_supporting_docs/MCMS/a0_rerun_nomonpol.m`
  - `master_supporting_docs/MCMS/a1_calibration.m`
  - `master_supporting_docs/MCMS/a2_preprocessing.m`
  - `master_supporting_docs/MCMS/new_process.py`
  - `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_NoMonPol.mat`
  - `master_supporting_docs/MCMS/output_python/extra_charts/Figure_18_Benchmark_vs_NoMonPol_TimeSeries.csv`

## Pipeline Check

1. The near-fixed-rate scenario is the corrected `monetary_policy = 4` run, not the stale `monetary_policy = 2` run.
   - `a0_rerun_nomonpol.m` sets `monetary_policy = 4` and saves `config_used`.
   - The saved `.mat` file records `monetary_policy = 4`, while the backup `irf_Het_DCP_NoMonPol_WRONG_MP2.mat` records `monetary_policy = 2`.

2. Figure 18 preprocessing uses the corrected `.mat`.
   - `a2_preprocessing.m` builds Figure 18 from `irf_Het_DCP_Baseline.mat` and `irf_Het_DCP_NoMonPol.mat`.

3. The robustness bar chart averages GDP directly and computes inflation as a 4-quarter rolling sum before averaging.
   - `new_process.py` uses `.rolling(4, min_periods=1).sum()` for `piC` and `.mean()` over the 12-quarter horizon.

## Recovered Numbers from Figure 18 CSV

Using `Figure_18_Benchmark_vs_NoMonPol_TimeSeries.csv`:

- **US GDP, 3-year average**
  - Benchmark: `+0.0191%`
  - NoMonPol: `+0.0280%`

- **China GDP, 3-year average**
  - Benchmark: `-0.1469%`
  - NoMonPol: `-0.1187%`

- **US CPI, 3-year average of 4-quarter rolling sum**
  - Benchmark: `+0.0637 pp`
  - NoMonPol: `+0.0351 pp`

- **China CPI, 3-year average of 4-quarter rolling sum**
  - Benchmark: `-0.0020 pp`
  - NoMonPol: `+0.0094 pp`

- **US interest rate, Q1**
  - Benchmark: `+0.0558 pp`
  - NoMonPol: `+0.00018 pp`

- **US REER, Q1**
  - Benchmark: `-0.3705%`
  - NoMonPol: `-0.2374%`

## Interpretation

The phrase "stronger appreciation makes the US inflation path more inflationary" is too loose and should not be used.

The verified interpretation is:

- The tariff wedge raises US CPI on impact in both regimes.
- Under the benchmark Taylor rule, the dollar appreciates more sharply and then reverses more strongly than under near-fixed rates.
- That overshooting-and-reversal path keeps the US CPI measure more elevated on average over the 12-quarter window.
- For China, the benchmark path turns mildly deflationary after Q1, while the near-fixed path remains mildly positive on average.

So the correct claim is about the **exchange-rate path as a whole**, not about appreciation by itself.

## Reproducibility Caveat

There is a figure-provenance issue:

- `MCMS/output_python/extra_charts/MonPol_Average_Combined_Compare.png`
- `Tariffs_ECB/0_clean/figures/MonPol_Average_Combined_Compare.png`

These files are not byte-identical and have different dimensions/timestamps. That does **not** overturn the numbers above, which come from the saved Figure 18 CSV, but it does mean the paper-side PNG is not a direct byte-for-byte copy of the current MCMS output.

`Fig_MonPol_REER_DW.png` is present in the paper repo but was not found in the current `MCMS/output_python/extra_charts/` folder during this audit, so that figure should ideally be regenerated and re-synced for full provenance.

## Action Taken

- Revised the paper text in Sections 4 and 60 to describe the mechanism as an overshooting-and-reversal path rather than impact appreciation in isolation.
- Clarified that the benchmark is a heterogeneous-DCP environment rather than a pure-DCP environment.

## Verification

- Overleaf sync status on 2026-04-08:
  - Local and Overleaf both point to `8c91fb9b1ec9bd3acf39fc5556e0a59e7d0bebd4`.
  - The nested paper repo's GitHub remote has diverged from local, but Overleaf does not have unseen remote changes.

- Build check:
  - `latexmk -pdf -interaction=nonstopmode -bibtex 0_sections_4_5_only.tex` reports the sections-only target as up to date and succeeds.
  - `latexmk -pdf -interaction=nonstopmode -bibtex 0_main.tex` still returns a non-zero status because of pre-existing full-paper issues outside this wording change, including a title-page brace error and many undefined citations.
  - `0_main.pdf` is still produced, and the current monetary-policy wording change does not introduce a new compile blocker in the log.
