---
title: "Referee Data Memo: Fiscal-LPT Sectoral C2-SUT Calibration Database"
author: "Codex review memo"
date: "May 14, 2026"
format:
  pdf:
    toc: true
    number-sections: true
    geometry: margin=0.85in
    colorlinks: true
---

# Purpose and Scope

This memo explains the database currently used to construct the Fiscal-LPT
production-wedge calibration in the MCMS Julia runtime. It is written for a
referee who needs to understand what the database contains, where each entry
comes from, how the entries are transformed into model objects, and which
measurement faults remain.

The active production-wedge runtime is now the sectoral C2-SUT layer. It lives
in:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_sectoral_c2_sut
```

The active sectoral builder is:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\scripts\build_fiscal_rule_dataset_sectoral_c2_sut.py
```

The Julia runtime imports the generated file:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_sectoral_c2_sut\sectoral_c2_sut_runtime.jl
```

from:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\src\calibration.jl
```

This memo deliberately focuses on data construction and calibration provenance.
Model-solution diagnostics such as BK conditions are out of scope here, per the
current instruction. The memo records the data limitations that would remain
even if the model-solution issue were ignored.

# Executive Summary

The current runtime production-wedge database is a sectoral calibration built
from BEA Supply-Use tables. It replaces the earlier neutral sectoral allocation
of aggregate Quarterly C2 coefficients with 44 sector-specific production-wedge
rules.

The core design is:

1. Estimate U.S. model-sector production-wedge rules from annual BEA Supply-Use
   rows.
2. Remove the BEA SUT row `Taxes on products and imports`, which includes
   import duties, so the measured wedge is closer to a non-product production
   tax/subsidy margin.
3. Map BEA summary industries into the 44 MCMS model sectors.
4. Transfer the U.S. sectoral rules to EA, China, and ROW using the existing C2
   country scaling inputs. EA uses a direct Eurostat D29 scaling layer; China
   and ROW remain broad-fiscal fallback transfer blocks.
5. Keep unrestricted empirical debt-feedback columns in the CSV audit files,
   but use a runtime sign closure that clips negative production-wedge debt
   feedbacks to zero.
6. Keep the steady-state production wedge as the model-implied markup-offsetting
   object `Tbar_Y = 1/M - 1`, not as observed fiscal data.

The database is transparent and reproducible, but it is not a structural
Leeper-Plante-Traum estimation. It is an annual sectoral reduced-form
calibration layer that feeds the MCMS fiscal block. The earlier aggregate
Quarterly C2 files remain useful as supporting evidence and provenance, but
they are no longer the source of the active production-wedge matrices in
`calibration.jl`.

# Active Runtime Objects

The model rule for the production wedge is:

```text
tau_Y[k,i,t] =
    rho_Y[k,i] * tau_Y[k,i,t-1]
  + (1 - rho_Y[k,i]) * (
        Phi_Y_y[k,i] * output_gap[k,t]
      + Phi_Y_b[k,i] * bgov_dev[k,t-1]
    )
  + Sigma_Y[k,i] * eps_Y[k,i,t]
```

The active runtime matrices are generated in `sectoral_c2_sut_runtime.jl` and
imported by `calibration.jl`. Country order is:

```text
EA, China, ROW, USA
```

The model now assigns the sectoral matrices directly:

```text
sectoral_c2_sut = sectoral_c2_sut_runtime_matrices()
Rho_tau_Y       = sectoral_c2_sut.Rho_tau_Y
Phi_tau_Y_y     = sectoral_c2_sut.Phi_tau_Y_y
Phi_tau_Y_b     = sectoral_c2_sut.Phi_tau_Y_b
Sigma_tau_Y     = sectoral_c2_sut.Sigma_tau_Y
```

The active matrices have shape 4-by-44. The following table summarizes the
runtime range by country:

| Country | Sectors | `Rho` min | `Rho` max | `Phi_y` min | `Phi_y` max | `Phi_b` min | `Phi_b` max | `Sigma` min | `Sigma` max |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| EA | 44 | 0.335170 | 0.673505 | -0.033992 | 0.000813 | 0.000000 | 0.094691 | 0.000234 | 0.013500 |
| China | 44 | 0.228933 | 0.567268 | -0.272646 | 0.006463 | 0.000000 | 0.138534 | 0.000945 | 0.054585 |
| ROW | 44 | 0.292710 | 0.631045 | -0.020092 | 0.000479 | 0.000000 | 0.169720 | 0.000541 | 0.031249 |
| USA | 44 | 0.161373 | 0.838042 | -0.145942 | 0.007139 | 0.000000 | 0.025032 | 0.000688 | 0.039754 |

The generated coefficient file keeps both unrestricted empirical debt-feedback
columns and runtime debt-feedback columns. The runtime uses a closure rule
named:

```text
clip_negative_phi_b_to_zero
```

This distinction matters. Negative unrestricted sectoral debt responses are not
deleted from the audit file, but they are not passed into the Julia runtime.
The rationale is economic and computational rather than empirical: with the
model sign convention, a negative production-wedge debt feedback means that
higher inherited debt lowers production taxes or raises subsidies. The runtime
therefore prevents the production-wedge instrument from becoming a
debt-destabilizing margin and leaves debt stabilization to other instruments or
non-negative production-wedge debt responses.

# Source Inventory

## U.S. Quarterly Sources

All U.S. active production-wedge source series are pulled from FRED, which
mirrors BEA National Income and Product Account or industry-account series.
FRED is used because it gives stable CSV endpoints and public source metadata.

| Internal column | FRED series | Description | Frequency | Unit | Origin website |
| --- | --- | --- | --- | --- | --- |
| `us_topi_less_subsidies_billions_saar` | `W254RC1Q027SBEA` | Taxes on production and imports less subsidies | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/W254RC1Q027SBEA> |
| `us_federal_excise_taxes_billions_saar` | `B234RC1Q027SBEA` | Federal excise taxes | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/B234RC1Q027SBEA> |
| `us_customs_duties_billions_saar` | `B235RC1Q027SBEA` | Federal customs duties | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/B235RC1Q027SBEA> |
| `us_state_local_sales_taxes_billions_saar` | `B248RC1Q027SBEA` | State and local sales taxes | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/B248RC1Q027SBEA> |
| `us_gross_output_billions_saar` | `GOAI` | Gross output by industry, all industries | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/GOAI> |
| `us_gdp_billions_saar` | `GDP` | Nominal GDP | Quarterly | Billions of dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/GDP> |
| `us_real_gdp_billions_2017_saar` | `GDPC1` | Real GDP | Quarterly | Billions of chained 2017 dollars, seasonally adjusted annual rate | <https://fred.stlouisfed.org/series/GDPC1> |
| `us_federal_debt_pct_gdp` | `GFDEGDQ188S` | Federal debt as percent of GDP | Quarterly | Percent of GDP | <https://fred.stlouisfed.org/series/GFDEGDQ188S> |

FRED's public metadata for `W254RC1Q027SBEA` identifies BEA as the source,
reports quarterly frequency, and reports the unit as billions of dollars at a
seasonally adjusted annual rate. The same FRED metadata structure is used for
the other U.S. series.

## Euro Area Quarterly Sources

The euro-area source block is pulled from Eurostat API endpoints.

| Internal object | Eurostat dataset / item | Description | Frequency | Unit | Origin website |
| --- | --- | --- | --- | --- | --- |
| `D29REC` | `gov_10q_ggnfa` | Other taxes on production, revenue | Quarterly | Percent of GDP | <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10q_ggnfa?format=JSON&lang=en&freq=Q&unit=PC_GDP&sector=S13&geo=EA20> |
| `D39PAY` | `gov_10q_ggnfa` | Other subsidies on production, expenditure | Quarterly | Percent of GDP | Same endpoint |
| `GD` | `gov_10q_ggdebt` | General-government gross debt | Quarterly | Percent of GDP | <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10q_ggdebt?format=JSON&lang=en&freq=Q&unit=PC_GDP&sector=S13&geo=EA20&na_item=GD> |
| `B1GQ` | `namq_10_gdp` | GDP at market prices, chain-linked volumes | Quarterly | Chain-linked volume, million euro | <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/namq_10_gdp?format=JSON&lang=en&freq=Q&unit=CLV15_MEUR&s_adj=SCA&na_item=B1GQ&geo=EA20> |

The generated metadata records:

```text
gov_10q_ggnfa updated: 2026-04-22T11:00:00+0200
gov_10q_ggdebt updated: 2026-04-22T11:00:00+0200
namq_10_gdp updated: 2026-05-13T11:00:00+0200
government-finance seasonal adjustment used: NSA
real GDP seasonal adjustment used: SCA
```

Eurostat's public metadata describes `gov_10q_ggdebt` as quarterly
general-government debt measured at the end of each quarter, compiled under ESA
2010, and available in percent of GDP. Eurostat metadata for
`gov_10q_ggnfa` describes quarterly non-financial accounts for general
government. Eurostat metadata for `namq_10_gdp` describes quarterly national
accounts, including chain-linked volume measures.

## Active Sectoral SUT Sources

The active U.S. sectoral source layer lives in:

```text
MCMS-private\input_data\fiscal_rules_sectoral_c2_sut
```

The source is BEA Supply-Use data:

```text
https://apps.bea.gov/industry/release/zip/SUPPLY-USE.zip
```

The generated metadata records:

```text
content_type: application/x-zip-compressed
content_length: 4791455
last_modified: Thu, 25 Sep 2025 12:30:06 GMT
```

The sectoral builder reads `Use_Summary.xlsx` inside that zip file. For each
BEA summary industry and year, it constructs:

```text
C2_SUT_wedge =
    Other taxes on production
  - Other subsidies on production
  - Subsidies on products
```

and divides by total industry output at basic prices. It excludes the BEA SUT
row:

```text
Taxes on products and imports
```

This SUT layer is now the active dynamic production-wedge runtime. It is not,
however, a full international sectoral fiscal database. It is annual, the
underlying sector-specific estimates are U.S.-only, and it depends on a mapping
from BEA summary industries into the model's 44 sectors. EA, China, and ROW are
constructed by scaling these U.S. sectoral rules with C2 country-level scaling
inputs.

# Supporting Aggregate U.S. Quarterly C2 Wedge

The earlier aggregate U.S. Quarterly C2 layer remains useful as supporting
country-level evidence. Its numerator is:

```text
US_C2_numerator =
    taxes_on_production_and_imports_less_subsidies
  - federal_excise_taxes
  - customs_duties
  - state_local_general_sales_taxes
```

In source names:

```text
US_C2_numerator =
    W254RC1Q027SBEA
  - B234RC1Q027SBEA
  - B235RC1Q027SBEA
  - B248RC1Q027SBEA
```

The U.S. production-wedge level is:

```text
US_C2_wedge = US_C2_numerator / GOAI
```

This construction removes customs duties, so tariff revenue is not loaded into
the production-wedge rule. It also removes federal excise and state/local sales
taxes, which are product-tax or consumption-tax-like components.

The main remaining U.S. source limitation is that the quarterly public series
does not expose every product-tax subcomponent available in the richer annual
NIPA decomposition. The quarterly construction is therefore a major observable
product-tax exclusion, not a perfect annual-style product-tax exclusion.

# Supporting Aggregate Euro-Area Quarterly C2 Wedge

The supporting aggregate euro-area quarterly object is:

```text
EA_C2_wedge = D29REC - D39PAY
```

where:

```text
D29REC = other taxes on production, revenue
D39PAY = other subsidies on production, expenditure
```

Eurostat reports both as percent of GDP in the API call used by the builder.
The interpretation is a non-product firm-side production-tax/subsidy wedge at
quarterly frequency.

The strongest feature of this construction is concept fit: D29 and D39 are much
closer to non-product production taxes and subsidies than a broad taxes-on-
production-and-imports measure. The main limitation is denominator mismatch:
the EA object is a GDP share, while the U.S. object is a gross-output share.
This matters because the model production wedge is naturally closer to a
firm-side cost wedge than to a GDP revenue ratio. The current builder accepts
this mismatch in order to use direct quarterly public data.

# International Transfer Construction

EA, China, and ROW do not have integrated direct sectoral production-tax and
production-subsidy rules comparable to the U.S. BEA SUT panel. They are
constructed by scaling the U.S. sectoral C2-SUT rules with existing C2
country-level scaling inputs.

For each non-U.S. country block:

1. Start from the 44 U.S. sectoral C2-SUT production-wedge rules.
2. Use the existing C2 country fiscal-responsiveness scaling inputs from:

```text
MCMS-private\input_data\fiscal_rules_calibration_c2\calibration_c2_country_scaling_inputs.csv
```

3. Apply the country-specific tax-margin, output-feedback, debt-feedback,
   shock-scale, and persistence proxies in that file.
4. For EA, use the direct Eurostat D29 scaling layer recorded in the C2 scaling
   file.
5. For China and ROW, keep the broad-fiscal absolute fallback treatment and
   inherit the U.S. sectoral sign pattern where direct production-tax data are
   unavailable.

EA, China, and ROW should therefore be described as calibrated transfer blocks
for sectoral fiscal dynamics, not as direct country-sector production-tax
estimates.

# Harmonisation Steps

## Country Order

All runtime matrices are written in the MCMS runtime country order:

```text
EA, China, ROW, USA
```

This order is repeated in the generated sectoral CSVs, the generated
`sectoral_c2_sut_runtime.jl` file, and `src/calibration.jl`.

## Frequency

The active sectoral C2-SUT calibration is annual because the BEA SUT source is
annual. This means the latest update reintroduces a frequency limitation: the
active sectoral rules have better sectoral tax-base measurement but weaker
model-frequency alignment than the aggregate Quarterly C2 layer.

The aggregate Quarterly C2 layer remains available as supporting country-level
evidence, but `calibration.jl` now uses the sectoral C2-SUT matrices for
`Rho_tau_Y`, `Phi_tau_Y_y`, `Phi_tau_Y_b`, and `Sigma_tau_Y`.

## Model Deviations

For the aggregate quarterly EA and USA evidence, observed wedge series are
converted to model deviations around latest-20-quarter means:

```text
tau_Y_model_dev =
    log(1 + observed_wedge_t)
  - log(1 + latest20_average_wedge)
```

Public debt is converted into an additive deviation:

```text
bgov_dev_t =
    debt_gdp_t
  - latest20_average_debt_gdp
```

For the active sectoral C2-SUT layer, each U.S. sectoral annual wedge is
converted relative to a latest-five-year sectoral benchmark:

```text
tau_Y_us_sector_c2_sut_model_dev =
    log(1 + c2_sut_non_product_share_output_t)
  - log(1 + sector_tbar_c2_sut_latest5)
```

In both layers, `tau_Y` is a log gross-wedge deviation, while public debt is an
additive deviation.

## Output Gap

The output gap is a reduced-form statistical gap. For each directly observed
country block, the builder:

1. takes real GDP,
2. logs it,
3. fits a linear trend in quarterly time,
4. uses the residual as `output_gap_log_linear`.

This is transparent and reproducible, but it is not a model-consistent output
gap from the DSGE solution.

## Regression Form

The quarterly rule is estimated without intercept:

```text
tau_t =
    rho * tau_(t-1)
  + beta_y * output_gap_t
  + beta_b * bgov_dev_(t-1)
  + residual_t
```

The no-intercept specification is chosen because the dependent variable and
debt variable are already centered around recent steady-state benchmarks. It
also aligns the estimated object with a model rule that has no constant term in
deviation form.

## Model-Rule Conversion

The implemented model rule uses:

```text
(1-rho) * Phi
```

inside the fiscal feedback term. Therefore the reduced-form beta coefficients
are converted into model-rule coefficients as:

```text
Phi_y = beta_y / (1-rho)
Phi_b = beta_b / (1-rho)
```

The generated files keep both unrestricted empirical beta/Phi columns and the
runtime beta/Phi columns after the debt-feedback closure rule.

## Runtime Debt-Feedback Closure

The unrestricted empirical sectoral estimates can imply negative
production-wedge debt feedbacks. The generated runtime columns impose:

```text
Phi_tau_Y_b = 0 when empirical Phi_tau_Y_b < 0
Beta_tau_Y_b = 0 when empirical Beta_tau_Y_b < 0
```

The closure is not an empirical estimate. It is a policy/modeling restriction
used to prevent the production-wedge instrument from lowering taxes or raising
subsidies in response to high debt.

# Generated Files and Entries

The active sectoral C2-SUT folder contains these files:

| File | Role |
| --- | --- |
| `metadata.json` | Source URLs, generation principle, package versions, generated-file manifest |
| `raw_bea_sut_summary_tax_rows.csv` | BEA SUT summary-industry tax rows and wedge components |
| `sector_mapping_model_to_bea_summary.csv` | Explicit mapping from 44 model sectors to BEA summary industries |
| `us_model_sector_c2_sut_wedges.csv` | Annual U.S. sectoral wedge levels by model sector |
| `us_model_sector_c2_sut_panel.csv` | U.S. sectoral panel with output gap, debt deviation, latest-five-year benchmark, and model deviations |
| `us_model_sector_c2_sut_rule_estimates.csv` | Direct U.S. sector-by-sector reduced-form rule estimates |
| `sectoral_c2_sut_scaled_tau_y_coefficients.csv` | 176 country-sector empirical and runtime coefficients after country scaling |
| `Rho_tau_Y_sectoral_c2_sut_matrix.csv` | Active 4-by-44 persistence matrix |
| `Phi_tau_Y_y_sectoral_c2_sut_matrix.csv` | Active 4-by-44 output-feedback matrix |
| `Phi_tau_Y_b_sectoral_c2_sut_matrix.csv` | Active 4-by-44 runtime debt-feedback matrix |
| `Sigma_tau_Y_sectoral_c2_sut_annual_matrix.csv` | Active 4-by-44 annual shock-scale matrix |
| `sectoral_c2_sut_runtime.jl` | Generated Julia runtime matrices imported by `src/calibration.jl` |
| `sectoral_c2_sut_audit.md` | Machine-generated audit note |

The scaled country-sector coefficient file has the most important entries:

| Column | Meaning |
| --- | --- |
| `model_country` | MCMS country block in runtime order |
| `model_sector_index` | MCMS sector index, 1 to 44 |
| `model_sector` | MCMS sector code |
| `bea_summary_codes` | BEA summary industry code or codes mapped into the model sector |
| `mapping_note` | Manual mapping caveat where BEA and model classifications do not align cleanly |
| `Rho_tau_Y_sectoral_c2_sut` | Runtime persistence in the sectoral production-wedge rule |
| `Beta_tau_Y_y_empirical_sectoral_c2_sut` | Unrestricted reduced-form output-gap beta |
| `Beta_tau_Y_b_empirical_sectoral_c2_sut` | Unrestricted reduced-form debt beta |
| `Phi_tau_Y_y_empirical_sectoral_c2_sut` | Unrestricted output-feedback model-rule coefficient |
| `Phi_tau_Y_b_empirical_sectoral_c2_sut` | Unrestricted debt-feedback model-rule coefficient |
| `Beta_tau_Y_y_sectoral_c2_sut` | Runtime output-gap beta |
| `Beta_tau_Y_b_sectoral_c2_sut` | Runtime debt beta after closure |
| `Phi_tau_Y_y_sectoral_c2_sut` | Runtime output-feedback coefficient |
| `Phi_tau_Y_b_sectoral_c2_sut` | Runtime debt-feedback coefficient after closure |
| `Sigma_tau_Y_sectoral_c2_sut_annual` | Annual residual shock scale |
| `debt_feedback_closure` | Name of the rule mapping unrestricted debt feedback to runtime debt feedback |
| `tax_margin_scale` | Country scaling factor for the non-product tax margin |
| `fiscal_y_scale` | Country scaling factor for output-gap responsiveness |
| `fiscal_b_scale` | Country scaling factor for debt responsiveness |
| `fiscal_sigma_scale` | Country scaling factor for shock scale |
| `fiscal_rho_proxy` | Country persistence proxy used when transferring U.S. sectoral rules |
| `fiscal_proxy_type` | Whether scaling is direct or fallback |
| `source_status` | Direct or transfer-calibrated provenance statement |

# Supporting Aggregate Quarterly Estimates

The aggregate Quarterly C2 files still report direct country-level estimates.
They are useful as a frequency-aligned diagnostic and as provenance for the C2
update, but they are not the active source of `Rho_tau_Y`, `Phi_tau_Y_y`,
`Phi_tau_Y_b`, and `Sigma_tau_Y` after the sectoral update.

The direct U.S. aggregate estimate uses 83 quarterly observations from 2005Q2
to 2025Q4:

| Object | Value |
| --- | ---: |
| rho | 0.688885 |
| beta_y | 0.003151 |
| beta_b | -0.002875 |
| Phi_y | 0.010127 |
| Phi_b | -0.009242 |
| sigma | 0.003484 |
| R2, no intercept | 0.622560 |

The direct EA aggregate estimate uses 95 quarterly observations from 2002-Q2 to
2025-Q4:

| Object | Value |
| --- | ---: |
| rho | 0.063775 |
| beta_y | 0.055111 |
| beta_b | -0.014042 |
| Phi_y | 0.058865 |
| Phi_b | -0.014999 |
| sigma | 0.005259 |
| R2, no intercept | 0.209047 |

The low EA no-intercept R2 is not fatal for a calibration object, but it should
be disclosed. It means the EA quarterly production-wedge movement is only
weakly explained by lagged wedge, trend-output gap, and lagged debt deviation
in this simple reduced-form rule.

# Sectoral Calibration

The active runtime no longer repeats country aggregate rates across sectors.
The U.S. row of each 4-by-44 runtime matrix is estimated sector by sector from
the BEA SUT panel. The non-U.S. rows preserve this U.S. sectoral pattern but
scale it with country-level C2 factors.

The U.S. sectoral estimation equation is:

```text
tau_Y_sector[s,t] =
    rho_s * tau_Y_sector[s,t-1]
  + beta_y_s * output_gap[t]
  + beta_b_s * bgov_dev[t-1]
  + residual[s,t]
```

The model-rule conversion remains:

```text
Phi_y_s = beta_y_s / (1-rho_s)
Phi_b_s = beta_b_s / (1-rho_s)
```

The panel covers 44 U.S. model sectors and 1997-2024 annual SUT observations.
The rule estimates use 27 regression observations per U.S. sector after the
lag. All 44 U.S. sectoral rules are estimated; none are missing.

Important mapping caveats remain:

1. Model sector `01T02` uses BEA `111CA`, so forestry is not separately
   identified.
2. Model sector `03` uses BEA `113FF`, which also contains forestry and
   related activities.
3. Chemicals and pharmaceuticals, model sectors `20` and `21`, both use BEA
   `325`.
4. Several services sectors combine multiple BEA summary industries because the
   model and BEA classifications are not one-to-one.

# Relation to LPT

The current database is LPT-style only in the narrow sense that fiscal
instruments respond to output and inherited debt in a partial-adjustment rule.
It is not an LPT estimation.

The differences are:

1. LPT estimates fiscal rules inside a DSGE model.
2. The current database estimates reduced-form OLS rules outside the DSGE.
3. LPT is a structural posterior exercise; this is a data bridge plus
   calibration restriction.
4. The current database estimates only the production-wedge dynamic rule.
   Consumption-tax, labour-tax, and several steady-state fiscal objects remain
   benchmarked or model-implied.

The safe language is:

```text
The fiscal block uses an LPT-style partial-adjustment debt-feedback structure.
The active production-wedge coefficients are annual sectoral reduced-form
calibration objects, not structural LPT posterior estimates.
```

# Remaining Faults and Open Issues

## EA, China, and ROW sectoral rules are not directly estimated

EA, China, and ROW are transfer calibrations at the sectoral level. The
database does not contain direct sector-by-sector production-tax or
production-subsidy rules for those blocks. Their coefficients are scaled from
the U.S. sectoral C2-SUT rule using existing C2 responsiveness proxies.

## ROW is not residual ROW

ROW should ideally be the world aggregate net of EA, China, and USA. The
current supporting scaling infrastructure treats ROW as a world proxy in older
data layers. This is not the same object as the residual MCMS rest of world.

## Sectoral detail comes at annual frequency

The latest update improves sectoral measurement but gives up the quarterly
frequency of the aggregate C2 layer. The active matrices are derived from
annual BEA SUT observations. A referee could reasonably ask whether annual
sectoral variation should be transformed or rescaled before entering a
quarterly model.

## U.S. and EA denominators differ in the supporting aggregate layer

The U.S. wedge is measured over gross output. The EA wedge is measured as a
percent of GDP. This is a substantive harmonisation issue. Gross output is
closer to a production cost base; GDP is closer to an aggregate revenue base.
The difference is accepted because direct quarterly public EA gross-output
denominators were not integrated.

## U.S. sector mapping is explicit but imperfect

The sectoral SUT layer maps BEA summary industries into 44 model sectors. This
is transparent in `sector_mapping_model_to_bea_summary.csv`, but it is not
always one-to-one. The largest visible compromises are forestry/fishing,
chemicals/pharmaceuticals, water and waste, transport support, real estate,
rental/leasing, and several service composites.

## Supporting U.S. quarterly product-tax exclusion is incomplete

The U.S. quarterly construction removes customs duties, federal excise taxes,
and state/local sales taxes. It does not remove every product-tax subcomponent
available in the annual decomposition. The annual data are richer; the
quarterly data are better aligned with model frequency.

## Supporting EA fiscal variables are not seasonally adjusted

The Eurostat government-finance extraction uses NSA data for `gov_10q_ggnfa`.
The EA real GDP series used for the output gap is seasonally and calendar
adjusted. This mismatch can introduce seasonal components into the fiscal
regression. A future version should test seasonal adjustment, seasonal dummies,
or four-quarter changes.

## Output gaps are statistical, not structural

The output gap is the residual from a linear trend in log real GDP. It is not a
model-implied output gap and not an official potential-output gap. This keeps
the build transparent, but it is a simple proxy.

## Debt concepts differ across countries and layers

The active sectoral U.S. panel inherits the U.S. debt concept from the
Benchmark B panel, while the supporting aggregate quarterly layer uses federal
debt as a percent of GDP for the United States and general-government gross
debt for the euro area. These are not identical government-sector concepts. A
fully harmonised build would use a common general-government debt concept for
all regions.

## Debt-feedback clipping is a model restriction

Zero entries in the runtime debt-feedback matrix are not necessarily estimated
zeros. They are sign/closure restrictions imposed after unrestricted empirical
sectoral rules generate negative debt feedbacks. This should be described as a
model discipline, not as a data finding.

## `Tbar_Y` remains model-implied

The steady-state production wedge remains:

```text
Tbar_Y = 1/M - 1
```

This is a markup-offsetting object. It is not observed production-tax or
subsidy data. The active database calibrates only dynamic production-wedge
rules.

## Labour and consumption fiscal blocks are not rebuilt here

The sectoral C2-SUT database is a production-wedge database. It does not solve
the labour-tax wedge or consumption-tax wedge calibration. In the runtime,
`Tbar_C`, `Tbar_N`, `Phi_tau_C_*`, and `Phi_tau_N_*` remain benchmarked or
hand-set relative to the production-wedge data effort.

## Generated artifacts are improved but still need governance

`calibration.jl` now imports the generated sectoral runtime file rather than
only manually copying constants. This is an improvement. The next step is
stronger artifact governance: checksums, generation timestamp in the runtime,
and an automatic test that rejects mismatches between CSV coefficients and
Julia matrices.

# Recommended Referee-Facing Statement

A concise referee-facing description would be:

> The active production-wedge database is a sectoral C2-SUT calibration layer.
> For the United States, sectoral wedges are built from BEA Supply-Use tables
> by taking other taxes on production minus other subsidies on production minus
> subsidies on products, dividing by sector output at basic prices, and
> excluding the SUT row for taxes on products and imports, which includes
> import duties. Forty-four U.S. model-sector rules are estimated in
> no-intercept partial-adjustment form with output-gap and lagged-debt terms.
> EA, China, and ROW are not direct country-sector estimates; they scale the
> U.S. sectoral rules using the C2 country scaling layer. The unrestricted
> empirical debt-feedback coefficients are retained in the audit files, but the
> runtime clips negative production-wedge debt feedbacks to zero. The resulting
> runtime matrices are sectoral, but their non-U.S. rows are transferred
> calibrations rather than independently observed sectoral fiscal rules.

# Reproducibility

From:

```text
C:\CustomTools\MCMS_gvt\MCMS-private
```

rebuild the active sectoral dataset with:

```powershell
python -B scripts\build_fiscal_rule_dataset_sectoral_c2_sut.py
```

The supporting aggregate Quarterly C2 dataset can be rebuilt with:

```powershell
python -B scripts\build_fiscal_rule_dataset_quarterly_c2.py
```

verify the active Julia runtime integration by checking that `calibration.jl`
imports and assigns the generated sectoral matrices:

```powershell
Select-String -Path src\calibration.jl -Pattern "sectoral_c2_sut_runtime_matrices"
```

The active generated runtime file is:

```text
input_data\fiscal_rules_sectoral_c2_sut\sectoral_c2_sut_runtime.jl
```

and the active Julia runtime imports it from:

```text
src\calibration.jl
```
