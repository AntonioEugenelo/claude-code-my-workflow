# Horse-Race Appendix Replication Audit

Date: 2026-04-20

## Target

- Deleted appendix previously included in the paper:
  `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- Recovered copy audited here:
  `quality_reports/recovered/2026-04-20_horse_race_appendix_recovered.tex`

## Replication Method

- Ran `master_supporting_docs/MCMS/run_horse_race_appendix.py` in isolation.
- Redirected output away from the live manuscript tree to:
  `quality_reports/tmp/horse_race_replication_2026-04-20/current_run/`
- Checked narrative claims against:
  - regenerated CSV / JSON outputs in that scratch directory
  - direct `.mat` extraction from `irf_Het_DCP_Baseline.mat` and `irf_PCP_Baseline.mat`

## Verdict

The appendix is **mostly correct**, but **not fully correct as a self-consistent generated object**.

- The China direct-exposure section, the 160-observation role-interacted section, the alpha-versus-mu-by-role section, the amplification section, the regime comparison, and the weighted-robustness paragraph all replicate.
- The failure is concentrated in the **Aggregate Consumption and CPI** subsection.
- The current runner mixes two benchmark sources:
  - benchmark heterogeneous-DCP aggregate blocks use the cached CSV `output_python/extra_charts/Figure_1_Benchmark_IRFs_CrossSection.csv`
  - the role-interacted benchmark blocks use direct `.mat` extraction
- GDP, consumption, and sectoral value added are consistent across those two sources.
- Benchmark **CPI** is not.

## Confirmed Claims

- China direct exposure:
  - GDP trade-share fit `R^2 = 0.931`
  - GDP `alpha` fit `0.041`
  - GDP `mu` fit `0.872`
  - own-sector value added trade fit `0.495`
  - own-sector value added `alpha` fit `0.003`
  - own-sector value added `mu` fit `0.494`
  - adding IO to trade raises GDP fit by about `0.002`
  - `alpha + mu` gives GDP `R^2 = 0.900`
- Full 160-observation role analysis:
  - role fixed effects `R^2 = 0.254`
  - adding trade-by-role lifts fit to `0.897`
  - adding IO-by-role adds effectively `0.000`
  - trade slopes:
    - Imposing `-5.90`
    - Receiving `-14.93`
    - ThirdParty `+0.53`
- Country-shock grid:
  - Shock A:
    - CHN `0.931`
    - USA `0.907`
    - RoW `0.901`
    - EA `0.068`
  - Shock B:
    - USA receiving `0.684`
    - CHN imposing `0.435`
    - RoW `0.000` after rounding
- Trade-share range claim is correct:
  - Shock A max share `0.4207%`
  - Shock B max share `0.0676%`
- Amplification paragraph:
  - `n = 57`
  - IO `R^2 = 0.016`
  - `p = 0.342`
  - `CV = 3.65`
  - range `[0.020, 2096.23]`
- Regime comparison:
  - EA GDP under heterogeneous DCP `R^2 = 0.068`, `p = 0.266`
  - EA GDP under PCP `R^2 = 0.930`, `p < 0.001`
- Weighted robustness:
  - China GDP `0.939`
  - United States GDP `0.877`
  - Euro area GDP `0.034`

## Failed Or Inconsistent Claims

### 1. Aggregate Consumption and CPI paragraph is not consistent with the current generated benchmark tables

Appendix text:

- EA CPI under heterogeneous DCP: `R^2 = 0.924`
- EA GDP under heterogeneous DCP: `R^2 = 0.068`
- EA GDP under PCP: `R^2 = 0.930`
- EA CPI under PCP: `R^2 = 0.128`

Current generated aggregate-outcomes table:

- EA GDP under heterogeneous DCP: `0.068`
- EA CPI under heterogeneous DCP: `0.275`
- EA GDP under PCP: `0.930`
- EA CPI under PCP: `0.128`

Interpretation:

- The heterogeneous-DCP EA GDP and the PCP values are fine.
- The heterogeneous-DCP EA CPI claim `0.924` is **not** reproduced by the current generated aggregate-outcomes table.

### 2. Aggregate alpha-versus-mu paragraph is not consistent with the current generated aggregate alpha/mu table

Appendix text:

- For China and the United States, `mu` explains most of GDP, consumption, and CPI variation, with `R^2` between `0.789` and `0.897`
- For the euro area, `mu` explains CPI strongly with `R^2 = 0.874`

Current generated aggregate alpha/mu table:

- China CPI `mu`: `0.770`
- United States `mu` range: `0.789` to `0.897`
- Euro area CPI `mu`: `0.403`

Interpretation:

- The text is **not** consistent with the current generated aggregate alpha/mu table for benchmark CPI.

## Why This Happens

`run_horse_race_appendix.py` mixes benchmark sources.

- Around the benchmark aggregate build, it uses `load_benchmark_cross_section()` for the heterogeneous-DCP benchmark.
- That loader reads `master_supporting_docs/MCMS/output_python/extra_charts/Figure_1_Benchmark_IRFs_CrossSection.csv`.
- The role analysis instead reads the benchmark `.mat` directly through `extract_cross_section_all_countries(...)`.

The cached CSV matches the benchmark `.mat` almost exactly for:

- `GDP_CHN`
- `Cons_CHN`
- `GDP_USA`
- `Cons_USA`
- `GDP_EA`
- `Cons_EA`
- `SecVA_CHN`

But it does **not** match for benchmark CPI:

- `CPI_CHN` max absolute difference: `0.002229`
- `CPI_USA` max absolute difference: `0.006406`
- `CPI_EA` max absolute difference: `0.001477`

So the appendix text is mixing:

- direct `.mat` benchmark CPI numbers in some narrative claims
- cached-CSV benchmark CPI numbers in the generated aggregate tables

## Bottom Line

The deleted appendix was **substantively right in most places**, but it was **not cleanly reproducible as written from the current runner**.

Safe statement:

- most of the appendix numerics replicate
- the benchmark CPI-related claims in the aggregate-outcome subsection are internally inconsistent because the pipeline mixes a stale or non-equivalent cached benchmark CSV with direct benchmark `.mat` extraction
