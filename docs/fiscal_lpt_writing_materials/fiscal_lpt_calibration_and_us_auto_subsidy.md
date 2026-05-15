# Fiscal LPT Calibration and US Automotive Subsidy Scenario

Date: 2026-05-08

Branch: `govt-julia`

This note explains the fiscal LPT implementation and calibration currently in the Julia runtime, records the simplifications made, and reports the results from a 10 percentage point US automotive production-subsidy shock.

## 1. What Was Implemented

The Julia runtime now includes a fiscal LPT extension with three fiscal wedges:

- `tau_C_k`: a consumption-tax/VAT wedge.
- `tau_N_k`: a labour-income tax wedge.
- `tau_Y_k_i`: a production-tax/subsidy wedge by country and sector.

These wedges enter the model in three places:

1. The household Euler equation includes the consumption-tax wedge.
2. The wage Phillips curve includes consumption and labour tax wedges.
3. The price Phillips curves include the production wedge as `mc_k_i + tau_Y_k_i`.

The fiscal block also adds government revenue and debt accounting:

- `rev_C_k`: consumption-tax revenue.
- `rev_N_k`: labour-tax revenue.
- `rev_Y_k`: production-tax/subsidy revenue.
- `rev_tariff_k`: tariff revenue.
- `bgov_k`: public debt.
- `i_g_k`: government borrowing rate.

The government budget equation links debt, tax revenues, tariff revenues, inflation erosion, and interest costs. The debt-spread channel has been set to zero in the baseline calibration, so `i_g_k = i_k`.

## 2. Country and Sector Ordering

The source spreadsheet uses the country order:

1. Euro area
2. United States
3. China
4. Rest of world

The runtime reorders countries to:

1. Euro area
2. China
3. Rest of world
4. United States

All fiscal vectors in `src/calibration.jl` therefore use:

```text
[EA, China, ROW, USA]
```

The sector order is also transformed. The source spreadsheet has 44 sectors in its original order. The runtime moves the three energy sectors to the front:

```text
[3, 10, 23, 1, 2, 4, 5, 6, 7, 8, 9, 11, ..., 44]
```

The automotive sector is NACE `29`, which is source sector `20`. After the energy-first reordering, it is model sector `21`.

## 3. Calibration Values Currently Used

The current fiscal calibration block is in `src/calibration.jl`.

```julia
Tbar_C = [0.18, 0.12, 0.14, 0.05]
Tbar_N = [0.38, 0.25, 0.25, 0.28]
S_C = [0.514097247020946, 0.399268156139089, 0.552321743529566, 0.683922996897461]
Bgov_ss = [0.878, 0.8833, 0.94, 1.2079]
Psi_bgov_spread = zeros(Knum)
```

The production-subsidy steady state is:

```julia
Tbar_Y = 1.0 ./ M .- 1.0
```

This means each country-sector receives a steady-state production subsidy that offsets its model-implied markup. If `M_k_i` is the gross markup, the subsidy is:

```text
1 + Tbar_Y_k_i = 1 / M_k_i
Tbar_Y_k_i = 1 / M_k_i - 1
```

This is a normative markup-offsetting benchmark, not an observed tax-data calibration.

## 4. Data Sources and Transformations

### Consumption Tax Rates: `Tbar_C`

Values used:

```text
EA    0.18
China 0.12
ROW   0.14
USA   0.05
```

These are effective-wedge benchmark values, not direct statutory rates. They are intended to approximate average consumption-tax wedges. The source logic is:

- European Commission VAT rates provide statutory EU VAT references.
- OECD Consumption Tax Trends provides VAT/GST cross-checks.
- IMF WoRLD and revenue-statistics data are the preferred source for a future effective-tax-rate construction.
- For the United States, a VAT rate is inappropriate, so the benchmark is closer to a low effective sales/excise consumption-tax wedge.

Transformation applied:

- No mechanical data transformation has been implemented yet for `Tbar_C`.
- The values are entered as decimal wedges.
- A future data build should construct `Tbar_C` from tax revenue divided by a consumption base, following the effective average tax-rate method of Mendoza, Razin, and Tesar.

Simplification:

- Country-specific benchmark rates replace the previous uniform `0.20`.
- ROW is a proxy, not a residual aggregation from all non-EA/non-China/non-US countries.

### Labour Tax Rates: `Tbar_N`

Values used:

```text
EA    0.38
China 0.25
ROW   0.25
USA   0.28
```

These are effective labour-tax wedge benchmarks. The source logic is:

- OECD Taxing Wages is useful for OECD cross-checks, especially EA countries and the US.
- IMF WoRLD/revenue statistics plus national accounts are the preferred source for an effective labour-tax construction.
- China and ROW need more careful official revenue/national-account construction.

Transformation applied:

- No mechanical data transformation has been implemented yet for `Tbar_N`.
- The values are entered as decimal wedges.

Simplification:

- Employee taxes, employer social contributions, and personal income taxes are collapsed into one labour wedge.
- Mixed income is not yet allocated between labour and capital.

### Consumption Base: `S_C`

Values used:

```text
EA    0.514097247020946
China 0.399268156139089
ROW   0.552321743529566
USA   0.683922996897461
```

Source:

- World Bank WDI API, household final consumption expenditure as percent of GDP.
- Indicator checked: `NE.CON.PRVT.ZS`.
- API checks returned:
  - Euro area: 2023, 51.4097247020946
  - China: 2024, 39.9268156139089
  - World: 2022, 55.2321743529566
  - United States: 2022, 68.3922996897461

Transformation applied:

```text
S_C = WDI percent of GDP / 100
```

Simplification:

- ROW uses the world aggregate as a proxy. A stricter treatment would construct ROW as a residual aggregate excluding EA, China, and the US, using model-consistent GDP weights.
- The current `S_C` uses private/household consumption rather than total final consumption. That is more appropriate for a household consumption-tax base but may miss parts of the VAT base.

### Labour Base: `S_L`

Current runtime formula:

```julia
S_L[k] = 1.0 - sum((1.0 - Psi_rs[k, i] / M[k, i]) * Lambda[k, i] for i in 1:Inum)
```

Source:

- This is model-implied from the MCMS IO calibration, markups, and sectoral weights.

Transformation applied:

- The labour base is inferred internally from model shares rather than loaded from external compensation-of-employees data.

Simplification:

- This avoids mixing source-account concepts before the fiscal block is fully validated.
- A future empirical build should compare this object against compensation of employees over GDP from OECD/Eurostat/national accounts and decide whether to add a mixed-income adjustment.

### Public Debt: `Bgov_ss`

Values used:

```text
EA    0.878
China 0.8833
ROW   0.94
USA   1.2079
```

Source logic:

- Eurostat government-debt releases are the preferred source for EA government debt.
- IMF WEO general-government gross debt is the preferred cross-country source for China, the US, and world/ROW-like aggregates.
- World Bank WDI central-government debt was checked, but it is narrower than the model budget object and is therefore only a fallback.

Transformation applied:

```text
Bgov_ss = debt percent of GDP / 100
```

Simplification:

- ROW is a proxy and should eventually be replaced by a residual model-weighted debt aggregate.
- The debt concept is general-government gross debt in the intended calibration, not central-government debt.

### Debt Spread: `Psi_bgov_spread`

Current value:

```text
0 for every country
```

Reason:

- The fiscal extension is an accounting and tax-wedge block.
- Adding a positive debt-spread elasticity would introduce a sovereign-risk mechanism without the rest of a sovereign-risk model.

Simplification:

- The government borrowing rate equals the policy rate.
- Sovereign-risk experiments can be added later as robustness exercises.

### Production Subsidies: `Tbar_Y`

Current formula:

```julia
Tbar_Y = 1.0 ./ M .- 1.0
```

Source:

- `M` is the model-implied gross markup matrix from the existing MCMS calibration.
- `M` is computed from the calibrated value-added and IO structure.

Transformation applied:

- The gross markup is converted into the subsidy that makes the gross production wedge equal to the inverse markup.

For the US automotive sector:

```text
M_US_auto = 1.1277510976849443
Tbar_Y_US_auto = -0.11327951526466495
```

Simplification:

- This is not an observed subsidy rate.
- It is a normative efficient-steady-state benchmark.
- The dynamic shock still operates through `tau_Y`; the steady-state subsidy affects revenue accounting through `Tbar_Y`.

### Production-Tax Base: `S_MCY`

Current formula:

```julia
S_MCY = Lambda ./ M
```

Source:

- Existing model steady-state sectoral shares and markups.

Transformation applied:

- Sectoral production bases are mapped into the marginal-cost production base used in the revenue equation.

For the US automotive sector:

```text
S_MCY_US_auto = 0.024111818302871266
```

Simplification:

- Marginal-cost output is not directly observed in national accounts.
- This should remain model-implied, with OECD/Eurostat IO data used only for validation.

## 5. Fiscal Rules

The current calibration uses different fiscal rules across countries, but common production-tax/subsidy rules across all sectors within a country.

### Consumption-Tax Rule

```text
tau_C_k = rho_C_k tau_C_k(-1)
        + (1-rho_C_k) (phi_C_y_k y_k + phi_C_b_k bgov_k(-1))
        + sigma_C_k shock
```

Values:

```text
rho_C     [0.85, 0.75, 0.80, 0.85]
phi_C_y   [0.04, 0.03, 0.03, 0.02]
phi_C_b   [0.02, 0.03, 0.02, 0.015]
sigma_C   [0.008, 0.012, 0.010, 0.008]
```

### Labour-Tax Rule

```text
rho_N     [0.90, 0.80, 0.85, 0.90]
phi_N_y   [0.01, 0.02, 0.015, 0.005]
phi_N_b   [0.08, 0.10, 0.08, 0.06]
sigma_N   [0.006, 0.010, 0.008, 0.006]
```

### Production-Tax/Subsidy Rule

Country-level vectors:

```text
rho_Y     [0.80, 0.70, 0.75, 0.80]
phi_Y_y   [0.02, 0.03, 0.02, 0.01]
phi_Y_b   [0.015, 0.020, 0.015, 0.010]
sigma_Y   [0.006, 0.010, 0.008, 0.006]
```

These are repeated across all 44 sectors within each country:

```julia
Rho_tau_Y = repeat(rho_tau_Y_by_country, 1, Inum)
Phi_tau_Y_y = repeat(phi_tau_Y_y_by_country, 1, Inum)
Phi_tau_Y_b = repeat(phi_tau_Y_b_by_country, 1, Inum)
Sigma_tau_Y = repeat(sigma_tau_Y_by_country, 1, Inum)
```

Simplification:

- We do not estimate 176 separate sectoral fiscal rules.
- This keeps the fiscal reaction function identified at the country level while preserving sector-specific shocks and markup-offsetting steady-state subsidies.

## 6. Scenario: 10 Percent US Automotive Production Subsidy

The requested experiment is a 10 percentage point subsidy to US automotive production.

Model mapping:

```text
Country: USA = model country 4
Sector: automotive, NACE 29 = source sector 20 = model sector 21
Shock: varepsilon_tau_Y_4_21
```

Implementation:

```julia
c = calibrate(data_path="input_data")
c.Sigma_tau_Y[4, 21] = -0.10
res = solve_scenario(data_path="input_data", irf_periods=20, calib_override=c)
```

The negative sign matters. In the Phillips curve, `tau_Y` enters as a marginal-cost tax wedge:

```text
mc + tau_Y
```

So a production subsidy is a negative `tau_Y` shock. Setting `Sigma_tau_Y[4,21] = -0.10` makes a unit positive innovation produce a 10 percentage point subsidy on impact.

## 7. Solver Check

The model solved successfully:

```text
Equations: 6762
Variables: 6762
Shocks: 448
Stable eigenvalues: 1885
Required stable eigenvalues: 1885
Static elimination residual: 2.842e-14
Decision-rule consistency error: 4.357e-13
```

The compact scenario output was saved to:

```text
output_us_auto_subsidy_10pct_summary.csv
```

## 8. Main Results

All entries below are reported as 100 times the model variable. For log-linear quantity and price variables, this is approximately percent deviation from steady state. For debt and revenue variables, interpret the numbers as scaled linearized deviations in the model's fiscal accounting units, not literal percentage changes in the debt stock.

| Variable | Impact | Period 4 | Period 8 | Period 20 | Peak | Peak period |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `tau_Y_4_21` | -10.0000 | -5.1177 | -2.0915 | -0.1359 | -10.0000 | 1 |
| `y_4_21` US automotive output | 1.8990 | 3.9717 | 3.3343 | 0.5902 | 3.9972 | 5 |
| `mc_4_21` US automotive marginal cost | -0.2116 | -0.4494 | -0.3885 | -0.0835 | -0.4551 | 5 |
| `p_X_4_21` US automotive producer price | -0.2483 | -0.5270 | -0.4546 | -0.0956 | -0.5336 | 5 |
| `pi_C_4` US CPI inflation | -0.0178 | -0.0035 | 0.0021 | 0.0017 | -0.0178 | 1 |
| `pi_C_core_4` US core CPI inflation | -0.0192 | -0.0037 | 0.0023 | 0.0017 | -0.0192 | 1 |
| `y_4` aggregate US output | 0.0237 | 0.0290 | -0.0102 | -0.0422 | -0.0433 | 17 |
| `c_4` US consumption | 0.0107 | 0.0030 | -0.0282 | -0.0381 | -0.0432 | 14 |
| `n_4` US labour | 0.0235 | 0.0289 | -0.0094 | -0.0403 | -0.0413 | 17 |
| `w_4` US real wage | 0.0164 | 0.0326 | 0.0221 | -0.0084 | 0.0326 | 4 |
| `bgov_4` US public debt | 0.2345 | 0.6753 | 0.9103 | 0.8008 | 0.9510 | 11 |
| `rev_Y_4` US production-tax revenue | -0.2258 | -0.1262 | -0.0444 | 0.0179 | -0.2258 | 1 |
| `i_4` US policy rate | -0.0071 | -0.0087 | -0.0017 | 0.0028 | -0.0098 | 3 |
| `i_g_4` US government borrowing rate | -0.0071 | -0.0087 | -0.0017 | 0.0028 | -0.0098 | 3 |
| `exp_4` US exports | 0.0893 | 0.1709 | 0.1090 | -0.0297 | 0.1709 | 4 |
| `imp_4` US imports | -0.0042 | -0.0161 | -0.0205 | -0.0003 | -0.0210 | 7 |
| `nfa_4` US net foreign assets | 0.0065 | 0.0431 | 0.0874 | 0.1155 | 0.1173 | 17 |

## 9. Interpretation

The shock behaves as expected for a targeted production subsidy:

1. The subsidy reduces the effective marginal-cost wedge in US automotive production.
2. US automotive output rises materially, peaking near 4 percent above steady state around period 5.
3. US automotive producer prices and marginal costs fall.
4. Aggregate US output rises only slightly on impact because the automotive sector is one sector within a 44-sector model.
5. The aggregate output effect later turns mildly negative as fiscal financing and general-equilibrium reallocation dominate the initial sectoral boost.
6. Production-tax revenue falls on impact because the subsidy is a fiscal cost.
7. Public debt rises persistently because the subsidy is not immediately offset one-for-one by other fiscal instruments.
8. Inflation falls slightly on impact, and the policy rate falls slightly in response.
9. US exports rise on impact and peak around period 4, consistent with a lower automotive production-cost wedge improving supply conditions and external competitiveness.

## 10. Remaining Caveats

The scenario is operational and internally consistent, but it should be read with the following caveats:

1. The fiscal tax rates are benchmark effective wedges, not a fully constructed dataset yet.
2. ROW is still a world-proxy value, not a residual aggregate.
3. `Tbar_Y = 1/M - 1` is a normative markup-offsetting subsidy, not observed production-subsidy data.
4. Sectoral fiscal rules are deliberately country-level rules repeated across sectors; this is more defensible than 176 separately estimated rules, but it does not capture sector-specific fiscal reaction functions.
5. The 10 percent subsidy is represented as a 10 percentage point negative production-tax wedge, not as a budget-neutral program.
6. The model computes IRFs for all shocks each run, so the scenario is computationally expensive even though only one shock is reported.

