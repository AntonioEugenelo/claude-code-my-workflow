# Fiscal-LPT quarterly C2 calibration audit

Date: May 13, 2026

This note documents the current Fiscal-LPT production-wedge calibration used by
the MCMS Julia runtime. It intentionally documents only the active
specification. Earlier candidate calibrations, source screens, and alternative
benchmark options have been removed from this file so that the audit trail does
not read as a menu of live choices.

The active runtime calibration is:

```text
Quarterly C2
```

The active model-country order is:

```text
EA, China, ROW, USA
```

The live runtime file is:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\src\calibration.jl
```

The active dataset builder is:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\scripts\build_fiscal_rule_dataset_quarterly_c2.py
```

The generated data artifacts live in:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_quarterly_c2
```

The companion derivation audit is:

```text
C:\CustomTools\MCMS_gvt\claude-code-my-workflow\docs\model specifics\fiscal_lpt_derivations.md
```

## Executive summary

The active production-wedge fiscal rule is a quarterly reduced-form calibration,
not an LPT-style structural posterior. The update improves the frequency and
source fit of the production-wedge rule:

1. The United States is estimated directly from quarterly BEA/FRED public data.
2. The euro area is estimated directly from quarterly Eurostat public data.
3. China and ROW are not directly estimated from sectoral quarterly
   production-subsidy data; they are scaled aggregate transfer calibrations.
4. The sectoral file distributes country aggregate rules by neutral output-share
   allocation, so sector wedge rates equal the country aggregate wedge rate.
5. Tariffs are excluded from the U.S. production-wedge rule by subtracting
   customs duties.
6. The calibration remains reduced-form and does not estimate the fiscal block
   jointly inside the DSGE model.
7. The unrestricted quarterly debt-feedback estimates are negative in all four
   country blocks. The active runtime therefore clips production-wedge debt
   feedbacks to zero. With that sign restriction, the full model solves and
   exports IRFs.

The active runtime vectors, in country order `EA, China, ROW, USA`, are:

```text
Rho_tau_Y   = [0.063774648629, 0.492689602429, 0.556466637195, 0.688885276387]
Phi_tau_Y_y = [0.058864842374, 0.012643484605, 0.000961129245, 0.010127182982]
Phi_tau_Y_b = [0, 0, 0, 0]
Sigma_tau_Y = [0.005259124882, 0.004784228152, 0.002738881214, 0.003484321722]
```

These values are repeated across sectors within each country in the runtime
calibration.

## Model object being calibrated

The relevant fiscal rule in the Julia model is the production-wedge rule for
`tau_Y`. The implemented model normalization is:

```text
tau_Y[k,i,t] =
    rho_Y[k,i] * tau_Y[k,i,t-1]
  + (1 - rho_Y[k,i]) * (
        Phi_Y_y[k,i] * output_gap[k,t]
      + Phi_Y_b[k,i] * bgov_dev[k,t-1]
    )
  + Sigma_Y[k,i] * eps_Y[k,i,t]
```

where:

```text
k = country block
i = sector
tau_Y = production wedge
output_gap = country output gap
bgov_dev = public-debt deviation from benchmark debt/GDP
eps_Y = production-wedge fiscal shock
```

The empirical regression estimates reduced-form quarterly coefficients:

```text
tau_t = rho * tau_(t-1)
      + beta_y * output_gap_t
      + beta_b * bgov_dev_(t-1)
      + residual_t
```

The conversion to the model rule is:

```text
Phi_y = beta_y / (1 - rho)
Phi_b = beta_b / (1 - rho)
```

This conversion is applied inside the dataset builder before writing the
runtime vectors.

## U.S. quarterly source construction

The U.S. production-wedge series is built from quarterly BEA series mirrored by
FRED. The source series are:

| Series | Meaning | Use |
| --- | --- | --- |
| `W254RC1Q027SBEA` | Taxes on production and imports less subsidies | starting numerator |
| `B234RC1Q027SBEA` | Federal excise taxes | product-tax subtraction |
| `B235RC1Q027SBEA` | Customs duties | tariff/customs subtraction |
| `B248RC1Q027SBEA` | State and local general sales taxes | product-tax subtraction |
| `GOAI` | Gross output, all industries | denominator |
| `GDP` | Current-dollar GDP | auxiliary scale |
| `GDPC1` | Real GDP | output-gap construction |
| `GFDEGDQ188S` | Federal debt as percent of GDP | debt feedback variable |

The U.S. quarterly C2 numerator is:

```text
US_C2_numerator =
    TOPI_less_subsidies
  - federal_excise_taxes
  - customs_duties
  - state_local_general_sales_taxes
```

The U.S. quarterly C2 wedge is:

```text
US_C2_wedge = US_C2_numerator / all_industries_gross_output
```

Customs duties are subtracted explicitly. This prevents tariff revenue from
being loaded into the production-wedge fiscal rule.

Audit caveat: this is the best available quarterly public construction. It is
not identical to the richer annual decomposition because the quarterly public
series used here expose the major product-tax lines, not every product-tax
subcomponent available in annual NIPA detail.

## EA quarterly source construction

The euro-area production-wedge series is built from Eurostat quarterly
government finance and national-account data:

| Dataset / item | Meaning | Use |
| --- | --- | --- |
| `gov_10q_ggnfa D29REC` | Other taxes on production, revenue | production-tax numerator |
| `gov_10q_ggnfa D39PAY` | Other subsidies on production, expenditure | production-subsidy subtraction |
| `gov_10q_ggdebt GD` | General-government gross debt | debt feedback variable |
| `namq_10_gdp B1GQ` | Real GDP, chain-linked volumes | output-gap construction |

The EA quarterly C2 wedge is:

```text
EA_C2_wedge = D29REC - D39PAY
```

Eurostat reports this object as a ratio to GDP in the API call used by the
builder. This is closer to the model's non-product firm-side wedge than a broad
taxes-on-production-and-imports measure because it nets other subsidies on
production from other taxes on production.

## China and ROW construction

China and ROW are not estimated from direct quarterly sectoral production-tax or
production-subsidy data. The active treatment is a transfer calibration:

1. Start from the U.S. quarterly aggregate production-wedge rule.
2. Apply the existing C2 country fiscal-responsiveness scales for China and ROW.
3. Blend persistence with the country fiscal-persistence proxy used in the C2
   scaling inputs.
4. Use neutral tax-margin scaling where no clean non-product production-tax
   margin is available.
5. Distribute the resulting country aggregate rule across sectors with neutral
   output-share allocation.

The neutral output-share allocation is:

```text
sector_amount_s = aggregate_amount * (sector_output_s / aggregate_output)
sector_wedge_s  = sector_amount_s / sector_output_s
                = aggregate_amount / aggregate_output
```

Therefore the sectoral wedge rates are equal within a country. This is
deliberate. It avoids inventing sector-specific China/ROW fiscal reactions that
are not observed in the data.

## Estimation sample and coefficients

Both directly observed country series are transformed to model deviations around
latest-20-quarter averages:

```text
tau_Y_model_dev = log(1 + observed_wedge) - log(1 + latest20_wedge)
bgov_dev        = debt_gdp - latest20_debt_gdp
```

The output gap is the residual from a country-specific linear trend in log real
GDP at quarterly frequency.

The direct quarterly estimates are:

| Country | Observations | Period | rho | beta_y | beta_b | Phi_y | Phi_b | sigma |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| EA | 95 | 2002-Q2-2025-Q4 | 0.063774648629 | 0.055110757735 | -0.014042419300 | 0.058864842374 | -0.014998973569 | 0.005259124882 |
| USA | 83 | 2005Q2-2025Q4 | 0.688885276387 | 0.003150715735 | -0.002875342134 | 0.010127182982 | -0.009242063830 | 0.003484321722 |

The country-level runtime coefficients are:

| Country | rho | Phi_y | Phi_b | sigma | Source status |
| --- | ---: | ---: | ---: | ---: | --- |
| EA | 0.063774648629 | 0.058864842374 | 0 | 0.005259124882 | direct quarterly Eurostat estimate, debt feedback sign-restricted |
| China | 0.492689602429 | 0.012643484605 | 0 | 0.004784228152 | scaled aggregate transfer, debt feedback sign-restricted |
| ROW | 0.556466637195 | 0.000961129245 | 0 | 0.002738881214 | scaled aggregate transfer, debt feedback sign-restricted |
| USA | 0.688885276387 | 0.010127182982 | 0 | 0.003484321722 | direct quarterly BEA/FRED estimate, debt feedback sign-restricted |

The unrestricted empirical debt-feedback estimates remain in
`quarterly_c2_country_coefficients.csv` as:

```text
Phi_tau_Y_b_empirical = [-0.014998973569, -0.028840117005, -0.037070159208, -0.009242063830]
```

They are not used in the runtime because, under the model's sign convention,
higher debt would lower production taxes or raise production subsidies. The
active runtime closure is:

```text
debt_feedback_closure = clip_negative_phi_b_to_zero
```

## Runtime integration

The quarterly C2 vectors are loaded from the generated runtime artifact:

```text
C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_quarterly_c2\quarterly_c2_runtime.jl
```

`src/calibration.jl` includes this generated file and repeats the country
vectors across sectors. The generated runtime file currently contains:

```julia
rho_tau_Y_by_country = [0.06377464862897264, 0.49268960242939547, 0.5564666371949851, 0.6888852763870515]
phi_tau_Y_y_by_country = [0.05886484237361775, 0.012643484605117439, 0.0009611292452423523, 0.010127182982481558]
phi_tau_Y_b_by_country = [0, 0, 0, 0]
sigma_tau_Y_by_country = [0.00525912488192555, 0.004784228152489203, 0.002738881214194855, 0.0034843217217488142]
```

The steady-state production wedge remains:

```text
Tbar_Y = 1 ./ M - 1
```

That object is model-implied from markups. The quarterly C2 data update affects
the dynamic production-wedge rule, not the steady-state markup-offsetting
benchmark.

## Generated files

The active quarterly C2 output folder contains:

```text
metadata.json
raw_us_quarterly_c2_panel.csv
raw_ea_quarterly_c2_panel.csv
quarterly_c2_us_estimate.csv
quarterly_c2_ea_estimate.csv
quarterly_c2_country_coefficients.csv
quarterly_c2_sectoral_coefficients.csv
quarterly_c2_runtime.jl
Rho_tau_Y_quarterly_c2_matrix.csv
Phi_tau_Y_y_quarterly_c2_matrix.csv
Phi_tau_Y_b_quarterly_c2_matrix.csv
Sigma_tau_Y_quarterly_c2_matrix.csv
quarterly_c2_audit.md
```

The key files are:

| File | Role |
| --- | --- |
| `raw_us_quarterly_c2_panel.csv` | U.S. source panel, transformed wedge, output gap, and debt deviation |
| `raw_ea_quarterly_c2_panel.csv` | EA source panel, transformed wedge, output gap, and debt deviation |
| `quarterly_c2_us_estimate.csv` | Direct U.S. quarterly regression output |
| `quarterly_c2_ea_estimate.csv` | Direct EA quarterly regression output |
| `quarterly_c2_country_coefficients.csv` | Country-order coefficients used for runtime patching |
| `quarterly_c2_sectoral_coefficients.csv` | 176 country-sector rows after neutral sectoral allocation |
| `quarterly_c2_runtime.jl` | Generated Julia runtime artifact loaded by `src/calibration.jl` |
| `*_matrix.csv` | 4 x 44 matrices in model country-sector form |
| `quarterly_c2_audit.md` | Machine-generated audit note from the builder |
| `metadata.json` | Source URLs, package versions, and generated-file manifest |

## Reproducibility

From:

```text
C:\CustomTools\MCMS_gvt\MCMS-private
```

run:

```powershell
python -B scripts\build_fiscal_rule_dataset_quarterly_c2.py
```

This refreshes the active quarterly C2 data folder.

To verify that the Julia runtime is loading the patched vectors, run:

```powershell
julia --project=. scripts\check_quarterly_c2_calibration.jl
```

Expected printed vectors:

```text
Rho_tau_Y[:,1] = [0.06377464862897264, 0.49268960242939547, 0.5564666371949851, 0.6888852763870515]
Phi_tau_Y_y[:,1] = [0.05886484237361775, 0.012643484605117439, 0.0009611292452423523, 0.010127182982481558]
Phi_tau_Y_b[:,1] = [0.0, 0.0, 0.0, 0.0]
Sigma_tau_Y[:,1] = [0.00525912488192555, 0.004784228152489203, 0.002738881214194855, 0.0034843217217488142]
```

To check whether the model solves under this specification, run:

```powershell
julia --project=. scripts\run_c2_full_model_check.jl
```

## Verification status

The active builder was run successfully on May 13, 2026.

The builder produced:

```text
USA direct estimate: 83 quarterly observations, 2005Q2-2025Q4
EA direct estimate: 95 quarterly observations, 2002-Q2-2025-Q4
Country coefficient rows: 4
Country-sector coefficient rows: 176
```

The Julia calibration check completed and printed the expected vectors.

The full model check completed calibration, equation generation, parsing,
static elimination, QZ, and IRF export:

```text
static elimination residual = 2.842154310930614e-14
stable eigenvalues = 1,885
required stable eigenvalues = 1,885
unstable eigenvalues = 723
required unstable eigenvalues = 723
output = output_julia\irfs\irf_C2_FullModelCheck_2026-05-14_13-48-45.mat
```

Therefore the active quarterly C2 dataset with the sign-restricted
production-wedge debt closure is integrated into the runtime and solves.

## Audit limitations

The limitations of the active specification are:

1. The calibration is reduced-form OLS, not a structural Bayesian posterior.
2. The fiscal rule is not estimated jointly with the private-sector model or the
   fiscal budget block.
3. China and ROW are scaled transfer calibrations, not direct country-sector
   estimates.
4. The U.S. quarterly product-tax subtraction is limited to major observable
   quarterly product-tax lines.
5. The sectoral matrix uses neutral output-share allocation, so it does not
   identify sector-specific policy response heterogeneity.
6. The production-wedge debt feedback uses a sign restriction: the unrestricted
   empirical coefficients are negative and are kept only as audit columns.
7. The current runtime steady-state `Tbar_Y` is model-implied from markups, not
   observed from fiscal data.

The safe statement is:

```text
The active Fiscal-LPT production-wedge calibration is Quarterly C2. It uses
direct quarterly public data for EA and USA, excludes U.S. customs duties from
the production-wedge rule, nets EA other production subsidies from other
production taxes, and treats China and ROW as scaled aggregate transfer
calibrations distributed sectorally by neutral output shares. The calibration is
loaded into `src/calibration.jl` through a generated runtime artifact. It
remains reduced-form and not an LPT posterior, but the sign-restricted runtime
specification passes BK and exports IRFs.
```
