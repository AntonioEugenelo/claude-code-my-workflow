# Unit-Elasticity US Automotive Subsidy Scenario

Date: 2026-05-08

Branch: `govt-julia`

This note reports the US automotive 10 percentage point production-subsidy experiment after permanently switching the runtime Armington elasticities to one.

## Permanent Elasticity Change

The Julia runtime has two Armington substitution parameters:

- `Delta_C`: substitution across source countries in final consumption.
- `Delta_X`: substitution across source countries in intermediate input demand.

The previous benchmark default used `armington=3`, which implied:

```text
Delta_C = 2
Delta_X = 2
```

I changed the default to `armington=2`, which implies:

```text
Delta_C = 1
Delta_X = 1
```

This is now the default in:

- `src/calibration.jl`
- `src/solve_onkio.jl`
- `src/a2_preprocessing.jl`
- `src/dynare_params.jl`
- `scripts/run_benchmark_irf_only.jl`

The scenario list in `src/solve_onkio.jl` now uses the unit-elasticity calibration as the benchmark. I also left an explicit high-elasticity variant, `ArmHigh`, corresponding to the old `armington=3` setting.

## Scenario Definition

The policy experiment is unchanged:

```text
Country: United States = model country 4
Sector: automotive, NACE 29 = source sector 20 = model sector 21
Shock: varepsilon_tau_Y_4_21
Shock size: -0.10 in tau_Y on impact
```

The negative sign means a subsidy. In the Phillips curve, the production wedge enters as:

```text
mc_4_21 + tau_Y_4_21
```

so a negative `tau_Y` lowers the effective marginal-cost wedge.

The run verified:

```text
Delta_C = 1.0
Delta_X = 1.0
Equations = 6762
Variables = 6762
Shocks = 448
```

The run completed without a Blanchard-Kahn error.

Output files:

- `output_us_auto_subsidy_10pct_elasticity1_summary.csv`
- `output_us_auto_subsidy_10pct_elasticity1_cross_country.csv`

## Calibration Objects in the Shocked Sector

For the US automotive sector:

```text
M_US_auto = 1.1277510976849443
Tbar_Y_US_auto = -0.11327951526466495
S_MCY_US_auto = 0.024111818302871266
```

The steady state already has a markup-offsetting production subsidy:

```text
Tbar_Y = 1/M - 1
```

The experiment adds a temporary 10 percentage point additional subsidy wedge through `tau_Y_4_21`.

## Domestic US Results

All numbers below are `100 * IRF`. For log-linear real variables, this is approximately percent deviation from steady state. For fiscal variables, the units are the model's linearized fiscal-accounting units.

| Variable | Impact | Period 4 | Period 8 | Period 20 | Peak | Peak period |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `tau_Y_4_21` | -10.0000 | -5.1179 | -2.0917 | -0.1361 | -10.0000 | 1 |
| `y_4_21` automotive output | 1.1946 | 2.4973 | 2.0941 | 0.3694 | 2.5125 | 5 |
| `mc_4_21` automotive marginal cost | -0.2115 | -0.4491 | -0.3881 | -0.0827 | -0.4548 | 5 |
| `p_X_4_21` automotive producer price | -0.2481 | -0.5262 | -0.4536 | -0.0944 | -0.5327 | 5 |
| `pi_C_4` CPI inflation | -0.0180 | -0.0038 | 0.0018 | 0.0017 | -0.0180 | 1 |
| `pi_C_core_4` core CPI inflation | -0.0194 | -0.0039 | 0.0021 | 0.0017 | -0.0194 | 1 |
| `y_4` aggregate output | 0.0133 | 0.0086 | -0.0245 | -0.0398 | -0.0434 | 15 |
| `c_4` consumption | 0.0097 | 0.0012 | -0.0308 | -0.0403 | -0.0456 | 14 |
| `n_4` labour | 0.0130 | 0.0084 | -0.0236 | -0.0374 | -0.0411 | 15 |
| `w_4` wage | 0.0154 | 0.0298 | 0.0184 | -0.0102 | 0.0298 | 4 |
| `bgov_4` public debt | 0.2323 | 0.6618 | 0.8848 | 0.7774 | 0.9219 | 11 |
| `rev_Y_4` production-tax revenue | -0.2221 | -0.1189 | -0.0391 | 0.0173 | -0.2221 | 1 |
| `i_4` policy rate | -0.0076 | -0.0093 | -0.0020 | 0.0028 | -0.0105 | 3 |
| `exp_4` exports | 0.0522 | 0.0967 | 0.0637 | -0.0095 | 0.0967 | 4 |
| `imp_4` imports | 0.0262 | 0.0431 | 0.0182 | -0.0130 | 0.0452 | 3 |
| `nfa_4` net foreign assets | -0.0035 | -0.0242 | -0.0510 | -0.0689 | -0.0705 | 17 |

## Domestic Story

The policy works directly in the targeted sector:

```text
10 percentage point production subsidy
-> lower effective marginal-cost wedge
-> lower automotive producer price
-> higher automotive output
```

Automotive output rises on impact and peaks around period 5:

```text
impact: +1.195
peak:   +2.512
```

This is materially smaller than under the old high-elasticity calibration, where the automotive-output peak was roughly 4 percent. With `Delta_C = Delta_X = 1`, households and firms substitute less aggressively toward the now-cheaper US automotive supply. The direct sectoral expansion is still strong, but it is no longer amplified as much by trade and input substitution.

The aggregate US effect is small and changes sign:

```text
y_4 impact: +0.0133
y_4 peak absolute response: -0.0434 in period 15
```

The reason is fiscal. The subsidy has a direct budget cost:

```text
rev_Y_4 impact: -0.2221
```

Debt therefore rises:

```text
bgov_4 peak: +0.9219 in period 11
```

The fiscal rules then gradually tighten future tax wedges in response to debt. That later fiscal tightening, together with reallocation away from the initially targeted sector, pushes aggregate output, consumption, and labour mildly below steady state.

Inflation falls on impact because the subsidy lowers production costs:

```text
pi_C_4 impact:      -0.0180
pi_C_core_4 impact: -0.0194
```

The monetary rule responds with a small policy-rate cut:

```text
i_4 peak cut: -0.0105 in period 3
```

That rate response cushions the shock but is not large enough to offset the fiscal cost.

## International Results

Peak aggregate output responses:

| Country | Impact | Peak absolute response | Peak period |
| --- | ---: | ---: | ---: |
| EA | -0.0006 | -0.0027 | 7 |
| China | -0.0001 | -0.0009 | 7 |
| ROW | 0.0022 | -0.0041 | 10 |
| USA | 0.0133 | -0.0434 | 15 |

Trade responses:

| Country | Export impact | Export peak | Import impact | Import peak |
| --- | ---: | ---: | ---: | ---: |
| EA | 0.0023 | -0.0079 | 0.0021 | -0.0058 |
| China | 0.0056 | 0.0074 | 0.0041 | 0.0052 |
| ROW | 0.0075 | 0.0112 | 0.0203 | 0.0340 |
| USA | 0.0522 | 0.0967 | 0.0262 | 0.0452 |

Inflation responses:

| Country | CPI impact | Core CPI impact |
| --- | ---: | ---: |
| EA | -0.0005 | -0.0005 |
| China | -0.0003 | -0.0004 |
| ROW | -0.0026 | -0.0033 |
| USA | -0.0180 | -0.0194 |

Fiscal spillovers:

| Country | Public debt impact | Public debt peak |
| --- | ---: | ---: |
| EA | 0.0002 | 0.0034 |
| China | 0.0002 | 0.0005 |
| ROW | 0.0016 | -0.0032 |
| USA | 0.2323 | 0.9219 |

## International Story

The international spillovers are smaller under unit elasticity than under the previous high-elasticity run. The reason is mechanical and economically intuitive: with `Delta_C = Delta_X = 1`, foreign buyers and firms respond less to relative-price movements. The US subsidy still lowers the relative cost of US automotive supply, but demand does not reallocate across origins as strongly.

The main international channel is still trade, not foreign fiscal stress:

```text
US automotive subsidy
-> lower US sectoral producer price
-> higher US exports
-> foreign trade reallocation
-> small foreign output and inflation responses
```

US exports rise, but less than in the previous high-elasticity run:

```text
unit elasticity export peak: +0.0967
old high-elasticity export peak: about +0.1709
```

US imports now also rise on impact:

```text
US imports impact: +0.0262
US imports peak:   +0.0452
```

This is a useful change relative to the earlier run. Under lower substitution, the US sectoral supply expansion generates a domestic income and production response, but does not produce as large a foreign-demand switch toward US output. Some of the general-equilibrium adjustment therefore shows up as higher US imports rather than a large net export improvement.

Net foreign assets for the US fall:

```text
nfa_4 peak: -0.0705
```

This is the international counterpart of the fiscal-cost and import-demand story. The US subsidizes production, expands the targeted sector, but the trade-balance response is not strong enough to improve the external position under unit elasticity.

For foreign regions:

- EA aggregate output falls slightly, with a peak absolute response of about `-0.0027`.
- China aggregate output barely moves, with a peak absolute response below `0.001`.
- ROW output rises slightly on impact but later falls by about `-0.0041`.
- Foreign CPI effects are tiny compared with the US.
- Foreign debt responses are essentially negligible.

So the full international conclusion is:

```text
The US automotive subsidy has clear domestic sectoral effects and visible trade spillovers,
but under unit Armington elasticities the foreign aggregate effects are very small.
The main cross-border action is trade composition, not foreign output, inflation, or debt.
```

## Comparison With Previous High-Elasticity Run

The permanent switch to unit elasticity changes the story in three important ways:

1. The automotive output gain is smaller:
   - Old high-elasticity peak: about `+3.997`.
   - Unit-elasticity peak: `+2.512`.

2. The export response is smaller:
   - Old high-elasticity US export peak: about `+0.171`.
   - Unit-elasticity US export peak: `+0.097`.

3. The external position worsens:
   - Old run had a positive US `nfa_4` response.
   - Unit-elasticity run has `nfa_4` falling to about `-0.0705`.

The fiscal dynamics remain similar:

- Production-tax revenue falls immediately.
- Debt rises persistently.
- Fiscal-rule feedback eventually tightens tax wedges.
- Aggregate US activity turns mildly negative after the initial sectoral boost.

