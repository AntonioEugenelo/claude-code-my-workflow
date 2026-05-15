# Hierarchical mixed-frequency fiscal-rule calibration bridge

Date: 2026-05-14

Status: design note plus first operational prototype. The repository now has a
Bayesian mixed-frequency fiscal-rule-block candidate generated in
`MCMS-private/input_data/fiscal_rules_hmf`. This is still not a full LPT
structural posterior, because the MCMS equilibrium conditions are not inside
the likelihood. The passing runtime handoff uses aggregate HMF posterior
vectors for `tau_C` and `tau_N` and a solve-filtered sectoral `tau_Y` blend:
75 percent HMF annual-weight allocation and 25 percent C2-SUT solution anchor.
The pure unanchored sectoral HMF `tau_Y` allocation is generated and audited;
in the current five-draw diagnostic filter, four of five draws pass at the
pure-HMF anchor while one draw needs the 25 percent C2-SUT solution anchor.

## Notation and acronyms

This note uses the following terms.

```text
LPT: Leeper, Plante, and Traum (2010).
MCMS: the multi-country, multi-sector Julia model in this repository.
Fiscal-LPT: this project's LPT-motivated fiscal-rule extension.
DSGE: dynamic stochastic general equilibrium.
EA: euro area.
ROW: rest of world.
SUT: supply-use table.
NACE: European activity classification used by Eurostat.
C2-SUT: the current sectoral production-wedge calibration that removes product
        taxes and import duties using supply-use tax allocations, while product
        subsidies remain in the wedge.
MCMC/SMC: posterior simulation methods, Markov chain Monte Carlo and
          sequential Monte Carlo.
```

The canonical estimated objects in this note are the **aggregate country
fiscal instruments**:

```text
tau_C: aggregate consumption-tax wedge
tau_N: aggregate income/labour-tax wedge
tau_Y: aggregate production-tax/subsidy wedge
```

`tau_C` and `tau_N` remain aggregate country instruments in the baseline
process. They are not sectoralized in the HMF handoff. The only instrument that
receives annual sectoral weights is `tau_Y`, because production taxes and
subsidies have a natural sectoral denominator and because the model already
uses sectoral production wedges.

The strict accounting target for `tau_Y` is:

```text
strict_production_wedge =
    Other taxes on production
  - Other subsidies on production
```

divided by gross output at basic prices. In ESA/SNA notation this is `D29 -
D39`, excluding taxes on products, subsidies on products, VAT, sales taxes,
excises, customs duties, and import VAT. Product and import tax objects belong
to product/consumption/import wedges, not to the production wedge unless the
paper explicitly switches to a purchaser-price or import-price wedge.

The exact accounting object differs by source and must be carried as metadata.
In the current U.S. C2-SUT layer the measured sectoral object is wider than the
strict target:

```text
C2_SUT_wedge =
    Other taxes on production
  - Other subsidies on production
  - Subsidies on products
```

divided by industry output at basic prices, with the BEA SUT row `Taxes on
products and imports` excluded. This removes product taxes and import duties
where the source permits it, but it does **not** remove product subsidies. The
quarterly aggregate U.S. C2 layer is weaker: it removes major observed product
tax components from TOPI less subsidies, not every product-tax subcomponent in
the annual accounts.

`y` is the output-gap or output-deviation control. `b` is the government-debt
state used in the fiscal rule. `T` is the source fiscal wedge in level or ratio
units. `Tbar` is the model steady-state wedge. `omega` is an aggregation
weight; when log wedges are aggregated, it must be the full log-linear
aggregation weight, not merely a denominator share.

## Executive summary

A defensible feasible design is a hierarchical mixed-frequency fiscal-rule
estimator with a strict division of labour across instruments. Quarterly
aggregate fiscal and macro data discipline country-level fiscal-rule dynamics
for `tau_C`, `tau_N`, and `tau_Y`. Consumption and income/labour taxes remain
aggregate country instruments. Annual sectoral information enters only for the
production-tax/subsidy wedge `tau_Y`, where it constructs annual sectoral
weights for production taxes and production subsidies. The resulting sectoral
production-wedge matrices are candidate model-frequency objects, not directly
observed quarterly sectoral tax/subsidy estimates.

This is best described as:

```text
Bayesian mixed-frequency fiscal-rule calibration bridge, motivated by LPT.
```

It should not be described as a direct replication of Leeper, Plante, and Traum
(2010), because LPT estimate fiscal rules jointly inside a DSGE model using
quarterly U.S. observables and a Bayesian posterior. The proposed procedure
uses a structural fiscal-rule state-space layer that can later be embedded in
the DSGE likelihood, but its first implementable version would remain a
calibration/estimation bridge unless the full private-sector model is included
in the likelihood.

The updated data architecture is:

1. Quarterly aggregate country layer:
   - `tau_C`: aggregate receipt-based consumption-tax wedge.
   - `tau_N`: aggregate receipt-based income/labour-tax wedge.
   - `tau_Y`: aggregate receipt-based production-tax/subsidy wedge.
   - United States and euro area: direct quarterly public-data layers where
     available.
   - China and ROW: aggregate proxies, mixed-frequency data, or transferred
     country-level priors, with wider measurement error.
2. Annual sectoral production-weight layer:
   - United States: BEA industry/SUT annual production-tax and production-
     subsidy rows, mapped to the 44 MCMS sectors.
   - Euro area: Eurostat annual sectoral production-tax/subsidy information,
     ESA SUT/IOT denominators, and official activity splitters where available.
   - China and ROW: official aggregate production-tax/subsidy levels where
     possible, with sector weights from NBS/UNSD/OECD/MRIO structures and
     explicit allocated/proxy quality flags.
3. Hierarchical Bayesian bridge:
   - Aggregate quarterly data provide conditional moments for country-level
     dynamics for `tau_C`, `tau_N`, and `tau_Y` under the stated rule, timing,
     measurement, and fiscal-shock orthogonality assumptions.
   - For data-rich countries, the aggregate layer can estimate the
     cross-instrument shock covariance among `tau_C`, `tau_N`, and `tau_Y`.
   - Annual sectoral data provide accounting weights for `tau_Y`, not free
     sectoral fiscal-rule dynamics.
   - Shrinkage and measurement error prevent allocated sectoral weights
     from being interpreted as precise direct sectoral fiscal responses.
4. Frequency bridge:
   - Aggregate quarterly posterior draws discipline country-level persistence,
     feedbacks, shock scales, and cross-instrument covariance.
   - Annual sectoral production weights allocate `tau_Y` levels and exposures
     across sectors.
   - In the implemented mixed-frequency bridge, annual aggregate fiscal
     instruments are first smoothed into latent quarterly states with
     annual-average measurement equations. Annual sectoral production weights
     remain a deterministic/proxy allocation layer rather than a jointly
     estimated production-weight state.

A central limitation is fiscal closure. Empirical production-wedge debt
responses can be negative or otherwise incompatible with a stable model
closure. Runtime use therefore requires either explicit admissibility
restrictions or a draw-level model-solution filter, and neither a nonnegative
debt response nor a clipped coefficient is by itself a proof of determinacy.

The recommended four-stage roadmap is:

1. Estimate a quarterly aggregate Bayesian fiscal-rule block for `tau_C`,
   `tau_N`, and `tau_Y`.
2. Build annual sectoral production-tax and production-subsidy weights for
   `tau_Y`; keep `tau_C` and `tau_N` aggregate.
3. Replace the approximation with a mixed-frequency fiscal-rule state-space
   estimator.
4. Embed the fiscal-rule block in the full MCMS DSGE likelihood.

Stage 1-2 outputs are not runtime-ready by default. To match the ambition of
the design, the baseline target should be Stage 3 unless a shorter prototype is
explicitly labeled as a validation exercise. Stage 1-2 outputs become runtime
candidates only after either (i) a latent quarterly state-space annualization
operator has been implemented, or (ii) a documented approximation validation
shows that annual production weights can allocate aggregate quarterly `tau_Y`
dynamics without materially changing model outcomes.

## Estimator labels

The project should keep four labels separate:

| Stage | Allowed label | What is estimated | What must not be claimed |
| --- | --- | --- | --- |
| Current C2-SUT runtime | calibrated point runtime | point matrices from reduced-form estimates and scaling | posterior estimation |
| Stage 1-2 | Bayesian fiscal-rule-block calibration posterior | fiscal-rule parameters outside the full DSGE likelihood | full LPT replication or runtime readiness |
| Stage 3 | mixed-frequency fiscal-rule state-space posterior | fiscal-rule block with quarterly aggregate and annual sectoral measurements | full DSGE posterior unless MCMS equilibrium is included |
| Stage 4 | full structural DSGE posterior | MCMS private-sector and fiscal-rule parameters jointly | direct quarterly sectoral fiscal observations |

## Why the problem is mixed-frequency

The fiscal rules in the model are quarterly state equations. In the updated
estimation structure, the Bayesian rule is estimated at the aggregate country
level for instruments `j in {C, N, Y}`:

```text
x_{j,c,t} =
    rho_{j,c} x_{j,c,t-1}
  + (1 - rho_{j,c})[
        Phi_y_{j,c} y_{c,t}
      + Phi_b_{j,c} b_{c,t-1}
    ]
  + eps_{j,c,t}.
```

The existing MCMS code uses this normalization for the fiscal wedge. In this
form, `Phi_y` and `Phi_b` are long-run target responses. The one-period
reduced-form slope on `y` is `(1 - rho) Phi_y`, and the one-period slope on
debt is `(1 - rho) Phi_b`.

The data do not naturally arrive at the same frequency or level of
disaggregation. For the United States and the euro area, public official
sources can provide quarterly aggregate fiscal objects, but clean industry-
level production tax/subsidy weights are annual. This creates three separate
objects:

```text
observed quarterly aggregate country wedges:
    x^Q_{C,c,t}, x^Q_{N,c,t}, x^Q_{Y,c,t}

observed or allocated annual sectoral production weights:
    w_T_{c,s,a}, w_S_{c,s,a}

candidate quarterly sectoral production wedge used by the model:
    x^Q_{Y,c,s,t}
```

The proposed estimator therefore cannot simply run separate quarterly OLS
rules by sector. Those series do not exist as observed official data. Instead,
it estimates aggregate fiscal dynamics and uses annual sectoral production
weights to allocate only `tau_Y`:

1. Quarterly aggregate country dynamics for `tau_C`, `tau_N`, and `tau_Y`.
2. Annual sectoral accounting weights for production taxes and subsidies.

## Available observations

The observation count determines how aggressive the inference can be.

For the current source design:

```text
United States aggregate quarterly:
    approximately 83 usable production-wedge observations, 2005Q2-2025Q4.

Euro area aggregate quarterly:
    approximately 95 usable production-wedge observations, 2002Q2-2025Q4.

Consumption and income/labour aggregate quarterly panels:
    currently generated from Benchmark B annual revenue data and, where
    coverage permits, smoothed through the latent-quarterly bridge. Direct
    quarterly receipt layers remain a future improvement. They stay aggregate
    country instruments rather than sectoral panels.

United States annual sectoral BEA/SUT:
    28 raw annual observations per model sector, 1997-2024.
    27 usable observations per sector once the lagged rule is used.

Euro area annual sectoral Eurostat D29X39:
    mostly 30 raw annual observations, 1995-2024.
    mostly 29 usable observations with a lag.
    some detailed NACE sectors have materially shorter histories.
```

The evidence table is:

| Source block | Raw coverage | Raw rows | Usable lagged rows | Evidence file or query |
| --- | --- | ---: | ---: | --- |
| U.S. aggregate quarterly | 2005Q2-2025Q4 | 84 complete quarters before lag | 83 | `MCMS-private/input_data/fiscal_rules_quarterly_c2/quarterly_c2_us_estimate.csv` |
| EA aggregate quarterly | 2002Q1-2025Q4 | 96 complete quarters before lag | 95 | `MCMS-private/input_data/fiscal_rules_quarterly_c2/quarterly_c2_ea_estimate.csv` |
| U.S. annual sectoral BEA/SUT | 1997-2024 | 28 per model sector | 27 | `MCMS-private/input_data/fiscal_rules_sectoral_c2_sut/us_model_sector_c2_sut_rule_estimates.csv` |
| EA annual sectoral Eurostat `D29X39` | 1995-2024 for best-covered NACE sectors | 20-30 by NACE sector | 19-29 by NACE sector | `claude-code-my-workflow/docs/model specifics/eurostat_ea20_nama_10_a64_d29x39_coverage.csv` |

The Eurostat sectoral coverage artifact is generated from:

```text
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_a64?lang=en&freq=A&unit=CP_MEUR&na_item=D29X39&geo=EA20
```

Here `D29X39` is Eurostat's net other taxes on production item, equal to
other taxes on production less other subsidies on production. It is not a
quarterly sectoral series. The annual coverage table must be mapped from NACE
to MCMS model sectors before the EA sectoral layer is used in runtime
calibration.

The coverage artifact is not yet a model-ready EA sectoral panel. Before the
EA annual sectoral layer can enter the estimator, the repository needs a
reproducible input directory under:

```text
MCMS-private/input_data/fiscal_rules_ea_sectoral_d29x39
```

with:

```text
raw Eurostat D29, D39, and D29X39 snapshots
sector denominators, preferably output at basic prices or documented fallback
NACE-to-MCMS concordance
sector-level transformed wedges
missingness and aggregation rules
source update timestamps and file hashes
```

Until those artifacts exist, EA sectoral evidence should enter only as a
planned direct-data source, not as already integrated sectoral calibration
data. The statistical design below nevertheless specifies how it should enter
once the panel is built.

These counts are enough to estimate compact conditional fiscal-rule moments
under predetermined-state and fiscal-shock orthogonality assumptions. They are
enough to support annual sectoral production-weight construction and
measurement-error checks. They are not enough for 44 fully independent sectoral
dynamic rules per country without strong priors, instruments, or the full DSGE
likelihood. For sectoral production weights, the estimator must report source
quality, benchmark closure, prior/proxy sensitivity, and a pooled-null
comparison in which all sectors inherit the aggregate `tau_Y` dynamics.

## Relationship to LPT

LPT estimate fiscal policy rules jointly in a DSGE model. The posterior is a
posterior over structural model parameters and fiscal-rule parameters, not a
collection of reduced-form regressions estimated outside the model.

The present proposal borrows three LPT principles:

1. Fiscal rules are dynamic policy rules with persistence.
2. Fiscal instruments respond systematically to fiscal and macro states,
   especially output and government debt.
3. The parameters should be disciplined by a likelihood and priors rather than
   chosen by hand.

It differs from LPT in four important ways:

1. It uses sectoral production-wedge data, whereas LPT is aggregate.
2. It combines quarterly aggregate data with annual sectoral data.
3. It has multiple countries, including countries without comparable direct
   sectoral fiscal data.
4. In its first feasible implementation, it estimates the fiscal-rule block
   outside the full DSGE model unless the complete MCMS likelihood is added.

The accurate label for Stage 1-3 is therefore an LPT-motivated calibration
bridge. It is not fully LPT until the MCMS equilibrium conditions, observation
equations, and fiscal rules are jointly estimated in a single posterior.

## Measurement equations

### Quarterly aggregate measurement

Let `x^Q_{j,c,t}` be the observed quarterly aggregate country wedge for
instrument `j`, expressed in model units:

```text
j in {C, N, Y}

x^Q_{C,c,t} =
    log(1 + T^Q_{C,c,t}) - log(1 + Tbar_C,c)

x^Q_{N,c,t} =
    log((1 - T^Q_{N,c,t})^(-1))
  - log((1 - Tbar_N,c)^(-1))

x^Q_{Y,c,t} =
    log(1 + T^Q_{Y,c,t}) - log(1 + Tbar_Y,c).
```

The aggregate layer estimates these three country instruments. `tau_C` is a
receipt-based consumption-tax object; `tau_N` is a receipt-based income/labour
tax object; `tau_Y` is the production-tax/subsidy object. Only `tau_Y` is
later allocated across sectors. `tau_C` and `tau_N` remain aggregate country
fiscal instruments in both estimation and runtime handoff.

For the U.S. aggregate production layer, the current C2 source object is:

```text
BEA/FRED quarterly TOPI less subsidies
- federal excise taxes
- customs duties
- state/local sales taxes
------------------------------------------------
non-product production-wedge numerator

divided by BEA/FRED all-industries gross output.
```

The FRED/BEA series currently used by the quarterly C2 audit are:

```text
W254RC1Q027SBEA: taxes on production and imports less subsidies
B234RC1Q027SBEA: federal excise taxes
B235RC1Q027SBEA: customs duties
B248RC1Q027SBEA: state and local sales taxes
GOAI: all-industries gross output
GDP: nominal GDP
GDPC1: real GDP
GFDEGDQ188S: federal debt percent of GDP
```

For the EA aggregate layer, the current quarterly source is Eurostat
government finance and national accounts data, with D29/D39-style production
tax/subsidy objects where available:

```text
gov_10q_ggnfa: quarterly general-government revenue/expenditure functions
gov_10q_ggdebt: quarterly government debt
namq_10_gdp: quarterly real GDP
```

The downloaded raw files in the current workflow are:

```text
MCMS-private/input_data/fiscal_rules_quarterly_c2/raw_us_quarterly_c2_panel.csv
MCMS-private/input_data/fiscal_rules_quarterly_c2/raw_ea_quarterly_c2_panel.csv
```

Downloaded timestamps and source endpoints must be stored in the dataset
metadata. Eurostat live APIs are not a substitute for preserving the exact
downloaded raw file and update timestamp used by an audited calibration.

The current aggregate builder generates `tau_C` and `tau_N` from Benchmark B
annual revenue data and passes eligible annual-observed instruments through
the latent quarterly bridge. Direct quarterly receipt-based objects for
`tau_C` and `tau_N` remain a future improvement for USA and EA. For China and
ROW, the current implementation uses aggregate mixed-frequency proxies where
coverage permits and transfer-prior observations where it does not.

The source objects are not conceptually identical across all layers. The U.S.
quarterly object is a major-product-tax exclusion from aggregate TOPI less
subsidies; it is not the same clean object as the annual SUT sectoral
allocation. The U.S. annual SUT object uses annual supply-use rows and
basic-price output. The EA quarterly object comes from quarterly government
finance/national accounts aggregates, while the EA annual sectoral object is
raw NACE `D29X39` coverage that still requires a documented NACE-to-MCMS
concordance and missingness rule before it can be used as an MCMS-sector input.
China and ROW have no direct integrated sectoral source in this design and
must remain transfer-prior cases.

The estimator must therefore include source-specific measurement equations.
The minimal harmonized form for aggregate fiscal instruments is:

```text
x_obs_{j,c,t}
  = alpha_{j,c,source}
  + lambda_{j,c,source} x_true_{j,c,t}
  + measurement_error_{j,c,t},

measurement_error_{j,c,t} ~ Normal(0, sigma_meas_{j,c,source}^2),
```

where `j` now indexes the fiscal instrument, and `source` indexes the source
family. The scale term is fixed to one only when the numerator, denominator,
timing, and convention match the model object. Otherwise it is either estimated
with an informative prior or fixed by a documented accounting conversion. This
is the place where the U.S. gross-output denominator, the EA GDP denominator,
tax-inclusive versus pre-tax consumption conventions, and labour-tax base
choices must be reconciled rather than silently pooled.

### Runtime units and steady states

The estimator must separate three objects:

```text
source fiscal ratio:
    T_source = fiscal_flow / denominator_flow

estimation deviation:
    tau_dev = transform(T_source) - transform(T_reference)

runtime steady-state wedge:
    Tbar_C, Tbar_N, or Tbar_Y in MCMS calibration
```

The live MCMS runtime currently carries separate steady-state fiscal wedges for
consumption, income/labour, and production. Fiscal accounts discipline dynamic
deviations and validation moments, but they do not automatically estimate a
normative or model-implied steady state. Each calibration must classify
`Tbar_C`, `Tbar_N`, and `Tbar_Y` as observed, benchmarked, proxy, or normative.

The debt variable must also be normalized before `Phi_b` is interpretable.
For the current fiscal-rule data builders, the empirical debt control is an
additive debt-to-GDP deviation from an empirical source baseline:

```text
b_emp_{c,t} = debt_gdp_{c,t} - Bgov_emp_ss_c.
```

For the current quarterly builder, `Bgov_emp_ss_c` is the latest-window sample
average used by the data builder, not necessarily the runtime `Bgov_ss` in
`calibration.jl`. If the estimator uses a no-intercept fiscal rule, this
baseline distinction is not cosmetic: shifting the empirical debt baseline
changes the estimated debt coefficient. The HMF builder must therefore write
both baselines:

```text
Bgov_emp_ss_c: empirical centering baseline used in estimation
Bgov_runtime_ss_c: model steady-state government debt used in MCMS runtime
```

and record whether the runtime handoff re-centers coefficients or uses the
empirical baseline directly. The rule uses lagged debt:

```text
b_{c,t-1}.
```

`Phi_b` is therefore a long-run response of the transformed fiscal wedge to a
one-unit empirical debt/GDP deviation. LPT coefficients are not portable unless
the debt definition, debt baseline, GDP denominator, timing, and fiscal
instrument transform match.

The aggregate country rule is:

```text
x^Q_{j,c,t} =
    rho_{j,c} x^Q_{j,c,t-1}
  + (1 - rho_{j,c})(
        Phi_y_{j,c} y^Q_{c,t}
      + Phi_b_{j,c} b^Q_{c,t-1}
    )
  + eps^Q_{j,c,t}.

eps^Q_{c,t} =
    [eps^Q_{C,c,t}, eps^Q_{N,c,t}, eps^Q_{Y,c,t}]'
    ~ Normal(0, Sigma_eps,c).
```

The aggregate layer estimates the following conditional fiscal-rule parameter
vector under the specified timing, measurement, and fiscal-shock orthogonality
assumptions:

```text
theta_{j,c} = {rho_{j,c}, Phi_y_{j,c}, Phi_b_{j,c}}
Sigma_eps,c = cross-instrument shock covariance.
```

For USA and EA, the baseline can estimate a regularized 3-by-3
cross-instrument covariance matrix for fiscal shocks. For China and ROW, the
covariance should be shrunk toward the pooled USA/EA structure or imposed as a
structured prior rather than estimated freely.

These Stage 1 coefficients are not causal fiscal responses unless an exclusion
restriction, an instrument strategy, or the full DSGE likelihood justifies that
interpretation. The limited-information identifying assumption is:

```text
E[eps^Q_{c,t} | tau^Q_{c,t-1}, b^Q_{c,t-1}, y^Q_{c,t}, information_{t-1}] = 0
```

under the stated timing convention. The baseline timing is that debt is
predetermined and lagged, while the output control is either contemporaneous
but predetermined with respect to the fiscal innovation, or replaced by
`y_{t-1}` in a robustness specification. If fiscal foresight or contemporaneous
policy endogeneity is material, Stage 1 must use instruments or move directly
to the DSGE/state-space likelihood.

### Annual sectoral production-weight measurement

The annual sectoral layer is now an allocation layer for `tau_Y`, not an
estimation layer for free sectoral fiscal-rule dynamics. It constructs two
separate annual weights:

```text
w_T_{c,s,a}: annual sector share of other taxes on production
w_S_{c,s,a}: annual sector share of other subsidies on production
```

The weights are then applied to official aggregate annual controls:

```text
D29_{c,s,a} = w_T_{c,s,a} * D29_{c,a}
D39_{c,s,a} = w_S_{c,s,a} * D39_{c,a}

NETPROD_{c,s,a} = D29_{c,s,a} - D39_{c,s,a}
T^A_{Y,c,s,a} = NETPROD_{c,s,a} / GO_basic_{c,s,a}.
```

The annual sectoral production wedge in model units is:

```text
x^A_{Y,c,s,a} =
    log(1 + T^A_{Y,c,s,a}) - log(1 + T_reference_{Y,c,s}).
```

`T_reference_{Y,c,s}` must be recorded separately from runtime `Tbar_Y` when
the runtime steady state is model-implied rather than observed in source data.

The core accounting constraints are:

```text
sum_s w_T_{c,s,a} = 1
sum_s w_S_{c,s,a} = 1

sum_s D29_{c,s,a} = D29_{c,a}
sum_s D39_{c,s,a} = D39_{c,a}
sum_s NETPROD_{c,s,a} = D29_{c,a} - D39_{c,a}.
```

Tax and subsidy weights should be separate because net production-tax values
can be small, negative, or volatile. Allocating `D29 - D39` directly would let
large positive tax weights cancel large subsidy weights and would make the
sectoral wedge unstable in exactly the sectors where the measurement is most
important.

For the United States, the preferred annual inputs are BEA SUT or industry
accounts. In the existing SUT builder, the relevant annual rows are:

```text
T018:    total industry output at basic prices
T00OTOP: other taxes on production
T00OSUB: other subsidies on production
T00TOP:  taxes on products and imports
T00SUB:  subsidies on products
```

The strict production-wedge weights should use:

```text
w_T_{USA,s,a} =
    sum_BEAmapped(T00OTOP_{s,a})
    / sum_all_model_sectors sum_BEAmapped(T00OTOP_{s,a})

w_S_{USA,s,a} =
    sum_BEAmapped(T00OSUB_{s,a})
    / sum_all_model_sectors sum_BEAmapped(T00OSUB_{s,a}).
```

Then `D29` and `D39` should be benchmarked to the official aggregate annual
controls. Product taxes/import duties (`T00TOP`) and product subsidies
(`T00SUB`) should remain outside the strict `D29 - D39` production-wedge
target unless a broader producer-price wedge is explicitly selected and
renamed.

For the euro area, aggregate controls come from Eurostat government finance
accounts. Sectoral annual weights should be built from the best available
official activity information:

```text
1. direct NACE-level D29 and D39 where separately available;
2. D29X39 only as a net validation object, not as the preferred allocation
   primitive when separate D29/D39 can be obtained;
3. env_ac_taxind2 for environmental/energy tax components by activity;
4. ESA SUT/IOT gross output, value added, payroll, land/property, energy, or
   other tax-base proxies when direct sectoral tax/subsidy rows are missing.
```

For China, the annual aggregate level should come from MOF/NBS-compatible
production-tax and subsidy categories where possible. Sector weights should
come from NBS output/value added, resource-tax exposure, energy/environmental
exposure, payroll or land/property proxies, and documented policy weights. All
unobserved sectoral allocations should carry `A` or `P` quality flags:
allocated or proxy.

For ROW, official fiscal data should control aggregate levels and MRIO/SUT
structures should control sectoral shares:

```text
official IMF/UNSD/OECD/GFS levels -> D29_{ROW,a}, D39_{ROW,a}
OECD ICIO / FIGARO / GTAP / Eora / EXIOBASE -> w_T, w_S
```

The annual sectoral output file should contain at least:

```text
country
year
sector44
GO_basic
D29_aggregate_control
D39_aggregate_control
tax_weight
subsidy_weight
D29_sector
D39_sector
NET_D29_D39_sector
tau_Y_sector
source_tax_weight
source_subsidy_weight
quality_flag_tax
quality_flag_subsidy
benchmark_error_D29
benchmark_error_D39
```

### Aggregation consistency

The annual sectoral weights must close in levels, not only in transformed log
wedges. The exact aggregate production wedge for a country-year is:

```text
T^A_{Y,c,a}
  = [sum_s NETPROD_{c,s,a}] / [sum_s GO_basic_{c,s,a}]
  = [D29_{c,a} - D39_{c,a}] / GO_basic_{c,a}.
```

If the estimator works in transformed log wedges, aggregation is only a
first-order approximation. Runtime matrices should therefore be generated from
the level allocations first, then transformed to model units. In MCMS
implementation, these weights must be reconciled with the fiscal revenue
weights used in the model, including the `S_MCY = Lambda ./ M` term that
enters production-tax revenue.

BEA-to-MCMS, NACE-to-MCMS, NBS-to-MCMS, and MRIO-to-MCMS mapping error must be
part of the measurement system. When the model sector and source sector are
not one-to-one, the output should either:

```text
1. collapse sectors to a source-consistent estimation aggregation; or
2. keep 44 runtime sectors but mark mapped, duplicated, or proxy sectors with
   larger measurement-error and quality flags.
```

## Hierarchical fiscal-rule structure

### Country aggregate parameters

The aggregate country parameter vector is indexed by instrument:

```text
theta_{j,c} = (rho_{j,c}, Phi_y_{j,c}, Phi_b_{j,c})
j in {C, N, Y}.
```

The fiscal shock vector for a country is:

```text
eps_{c,t} = [eps_{C,c,t}, eps_{N,c,t}, eps_{Y,c,t}]'
eps_{c,t} ~ Normal(0, Sigma_eps,c).
```

For the U.S. and EA, these aggregate parameters are estimated from quarterly
aggregate data. The 3-by-3 covariance `Sigma_eps,c` should be estimated with
regularization, not as an unrestricted object with no prior discipline. For
China and ROW, parameters can be estimated only if credible aggregate
quarterly or mixed-frequency fiscal observables exist. Otherwise they must be
transferred with explicit priors:

```text
theta_{j,c} ~ TransferPrior(theta_{j,US}, theta_{j,EA}, macro_fiscal_scale_c)
Sigma_eps,c ~ ShrinkagePrior(Sigma_eps,US, Sigma_eps,EA, data_quality_c).
```

This transfer must be reported as a prior/calibration, not as a direct
country-specific estimate.

### Sectoral production weights

The updated baseline does not estimate free sectoral fiscal-rule parameters.
Sectoral production wedges inherit the aggregate `tau_Y` dynamics and differ
through annual production-tax and subsidy weights.

```text
D29_{c,s,a} = w_T_{c,s,a} D29_{c,a}
D39_{c,s,a} = w_S_{c,s,a} D39_{c,a}
T^A_{Y,c,s,a} = (D29_{c,s,a} - D39_{c,s,a}) / GO_basic_{c,s,a}.
```

The dynamic quarterly component is:

```text
x^Q_{Y,c,t} =
    rho_{Y,c} x^Q_{Y,c,t-1}
  + (1 - rho_{Y,c})(
        Phi_y_{Y,c} y^Q_{c,t}
      + Phi_b_{Y,c} b^Q_{c,t-1}
    )
  + eps^Q_{Y,c,t}.
```

The sectoral runtime layer then combines an annual sectoral level/exposure
component with the aggregate country dynamic component. The conservative
default is:

```text
x^Q_{Y,c,s,t}
  = xbar^A_{Y,c,s,a(t)} + x^Q_{Y,c,t},
```

where `xbar^A_{Y,c,s,a}` is the annual sectoral production-wedge level
relative to the country reference. A richer but still disciplined option is:

```text
x^Q_{Y,c,s,t}
  = xbar^A_{Y,c,s,a(t)} + lambda_{Y,c,s} x^Q_{Y,c,t},

lambda_{Y,c,s} ~ Normal(1, sigma_lambda_c),
```

but `lambda_{Y,c,s}` should not be freely estimated unless annual sectoral
variation and validation tests actually identify it. The default `lambda=1`
means that sectors have different production-wedge levels and exposures but
share country aggregate fiscal-rule dynamics.

The pooled-null comparison is now:

```text
H0: lambda_{Y,c,s} = 1 and sectoral heterogeneity enters only through
    annual D29/D39 weights.
```

The paper should report whether any richer sectoral dynamic loading improves
posterior predictive fit relative to this pooled null after accounting for
measurement error and prior shrinkage.

### Sectoral persistence

Sectoral persistence is not identified in the updated baseline because annual
sectoral production weights are accounting objects, not sectoral quarterly
policy rules. The audit-ready default is:

```text
rho_{Y,c,s} = rho_{Y,c}.
```

Any sector-class or sector-specific persistence is a sensitivity analysis, not
the baseline. It would require direct sectoral time-series evidence or a
separate state-space identification argument.

### Debt response

The debt response is the most delicate parameter. The current reduced-form
work found negative production-wedge debt responses in some aggregate
quarterly estimates, and the runtime sign restriction clipped them to zero as
a determinacy-oriented admissibility restriction. A hierarchical Bayesian
version should not hide this issue.

Recommended prior:

```text
Phi_b_{Y,c} >= 0
```

or, if allowing negative empirical evidence:

```text
Phi_b_{Y,c} ~ Normal(m_b,Y, s_b,Y)
model solution filter: accept only draws that satisfy determinacy.
```

The first option is simpler and more transparent for a production-wedge rule
that is meant to help close fiscal debt. It is not by itself a determinacy
proof. Determinacy depends on the full linear system, the government budget
equation, monetary policy, other fiscal instruments, debt-spread terms, and
the model's timing conventions. The second option is closer to a structural
posterior but computationally more costly, because the DSGE solution must be
checked inside the sampler or in a posterior accept/reject stage.

The restricted object must be named differently from the unrestricted
empirical posterior. The estimator should carry three posterior targets:

```text
unrestricted empirical posterior:
    p(theta | data)

policy-admissible posterior:
    p(theta | data, policy restrictions)

solution-filtered posterior:
    p(theta | data, solve)
      proportional to L(data | theta) p(theta) 1{Solve(theta)=pass}
```

The last object is a posterior conditional on the model-solution event, not a
casual trimming of inconvenient draws. Reported summaries must state which of
these targets they describe.

## Priors

A defensible prior set is:

```text
rho_{j,c} ~ Beta(a_rho,j, b_rho,j), mapped to (0, 0.99)

Phi_y_{j,c} ~ Normal(m_y,j, s_y,j)

Phi_b_{j,c} ~ Normal(m_b,j, s_b,j)

diag(Sigma_eps,c)^(1/2) ~ HalfNormal(s_sigma,j)

Corr(Sigma_eps,c) ~ LKJ(eta_corr)

w_T_{c,s,a}, w_S_{c,s,a}: observed, benchmarked, allocated, or proxy weights
with source-specific measurement error, not free fiscal-rule parameters.
```

The prior means should be documented separately for each instrument. For
`tau_C` and `tau_N`, the priors discipline aggregate country rules only. For
`tau_Y`, the priors discipline the aggregate production-wedge rule; annual
sectoral production weights allocate the aggregate production wedge across
sectors but do not create independent sectoral `Phi` or `rho` priors in the
baseline.

If the runtime imposes a nonnegative production-wedge debt response for
determinacy, the estimator should report both the unrestricted empirical
posterior and the policy-admissible or solution-filtered posterior. The
restricted object must be named differently from the unrestricted posterior.

Prior scales such as `s_y`, `s_b`, and `s_sigma` must be reported in the same
units as the transformed fiscal wedge and debt/output controls. A practical
implementation should use non-centered hierarchical parameters for country
pooling and report sensitivity to the cross-country shrinkage and covariance
priors.

## Likelihood

### Aggregate quarterly likelihood

For countries with direct quarterly aggregate data:

```text
resid_{j,c,t}
  = x^Q_{j,c,t}
    - rho_{j,c} x^Q_{j,c,t-1}
    - (1 - rho_{j,c})(
          Phi_y_{j,c} y^Q_{c,t}
        + Phi_b_{j,c} b^Q_{c,t-1}
      )

resid_{c,t} = [resid_{C,c,t}, resid_{N,c,t}, resid_{Y,c,t}]'
resid_{c,t} ~ Normal(0, Sigma_eps,c).
```

This gives:

```text
log L_Q
  = sum_c sum_t log MVN(resid_{c,t}; 0, Sigma_eps,c).
```

The covariance determinant matters because `Sigma_eps,c` is estimated. In the
state-space version, the corresponding term is the innovation or measurement
covariance determinant in the Kalman likelihood.

### Annual production-weight likelihood and validation

In the updated baseline, annual sectoral data do not estimate sectoral
fiscal-rule dynamics. They enter as a benchmarked measurement/allocation layer
for production taxes and production subsidies:

```text
w_T_{c,s,a} = observed_or_allocated_tax_weight_{c,s,a}
w_S_{c,s,a} = observed_or_allocated_subsidy_weight_{c,s,a}
```

The likelihood contribution, where a statistical likelihood is needed, is a
measurement-error model around the allocation weights or sectoral levels:

```text
w_T_obs_{c,s,a} ~ Normal(w_T_true_{c,s,a}, sigma_wT_source^2)
w_S_obs_{c,s,a} ~ Normal(w_S_true_{c,s,a}, sigma_wS_source^2),
```

with simplex constraints:

```text
sum_s w_T_true_{c,s,a} = 1
sum_s w_S_true_{c,s,a} = 1
w_T_true_{c,s,a} >= 0
w_S_true_{c,s,a} >= 0.
```

If the source gives sectoral tax or subsidy levels directly, the measurement
can instead be placed on `D29_{c,s,a}` and `D39_{c,s,a}` before normalizing to
weights. If the source gives only net `D29X39`, that net object should be used
as a validation target or as a fallback with a larger error variance, because
it does not separately identify tax and subsidy weights.

The key validation equations are deterministic accounting constraints:

```text
D29_{c,s,a} = w_T_{c,s,a} D29_{c,a}
D39_{c,s,a} = w_S_{c,s,a} D39_{c,a}

sum_s D29_{c,s,a} = D29_{c,a}
sum_s D39_{c,s,a} = D39_{c,a}
sum_s (D29_{c,s,a} - D39_{c,s,a}) = D29_{c,a} - D39_{c,a}.
```

This is the reason Stage 2 is better described as a sectoral production-weight
layer than as an annual sectoral fiscal-rule likelihood. A richer
state-space version may let annual weights evolve smoothly over time, but it
still should not infer 44 independent quarterly production-tax policy shocks
without direct evidence.

## Recommended estimator path

The project should proceed in stages.

### Stage 1: exact fiscal-rule Bayesian block

Estimate the aggregate quarterly rules outside the full DSGE model:

```text
theta_{j,US}, theta_{j,EA}, Sigma_eps,US, Sigma_eps,EA
    | quarterly aggregate tau_C, tau_N, tau_Y data.
```

Use the exact model normalization and emit posterior draws. This replaces
point-estimate OLS calibration with a posterior over the aggregate fiscal-rule
block and its cross-instrument shock covariance.

### Stage 2: annual sectoral production-weight layer

Build annual sectoral `tau_Y` weights:

```text
w_T_{c,s,a}, w_S_{c,s,a}
    | BEA/Eurostat/NBS/UNSD/MRIO production-tax and subsidy allocation data.
```

Use separate tax and subsidy weights. Do not estimate all sectoral fiscal-rule
parameters independently. In the minimal implementation, annual sectoral data
inform sectoral production-wedge levels/exposures, while persistence,
output-gap feedback, debt feedback, and shock covariance remain aggregate
country objects.

### Stage 3: mixed-frequency state-space version

Replace the separate aggregate-rule plus annual-weight approximation with a
state-space system that jointly tracks aggregate fiscal states and annual
production-weight measurements. This is the first version that deserves the
label "mixed-frequency fiscal-rule state-space estimator." Reserve
"structural DSGE posterior" language for Stage 4, where MCMS equilibrium
conditions are included in the likelihood.

### Stage 4: DSGE embedding

Embed the fiscal-rule block inside the MCMS model likelihood. This is the step
that would move the project closest to LPT. It requires:

1. A solved linear state-space representation of MCMS.
2. Observation equations for the macro and fiscal series.
3. Priors for private-sector and fiscal-rule parameters.
4. A determinacy/stability filter.
5. MCMC, SMC, or another posterior simulation method.

Only Stage 4 is truly LPT-equivalent structural posterior estimation.

## Estimation and identification

### Identification status

The following table is the intended audit classification.

| Object | Evidence source | Status | Main condition |
| --- | --- | --- | --- |
| Aggregate U.S./EA `tau_C`, `tau_N`, `tau_Y` persistence and response moments | quarterly aggregate fiscal and macro data | conditionally estimated | requires predetermined-state timing and fiscal-shock orthogonality |
| Aggregate U.S./EA fiscal-shock covariance | quarterly aggregate fiscal-rule residuals | conditionally estimated with shrinkage | feasible only with regularized covariance priors |
| Aggregate U.S./EA structural fiscal-rule parameters | full MCMS likelihood with observation equations | not identified in Stage 1-3 | requires Stage 4 |
| Sectoral production-tax and subsidy weights for U.S./EA | annual BEA/Eurostat sectoral accounts and SUT/IOT | benchmarked or directly measured allocation | separate D29 and D39 weights; annual closure required |
| Sectoral `tau_Y` dynamics | aggregate `tau_Y` posterior plus annual weights | allocated runtime construction | sectoral dynamics inherit aggregate country rule unless richer evidence is added |
| Sectoral quarterly persistence | annual sectoral accounts | not identified in Stage 1-2 | use country persistence |
| Sectoral quarterly shock variances | annual sectoral accounts | not identified in Stage 1-2 | use aggregate scale or explicit sensitivity |
| China/ROW sectoral weights | official aggregate levels plus external allocation proxies | allocated/proxy calibration | uncertainty must be wider than direct U.S./EA cases |
| Runtime-ready HMF matrices | posterior draws plus model solution filter | not available until feasibility gate passes | requires matrix handoff and BK/stability evidence |

### What the quarterly aggregate data provide

Quarterly aggregate data provide conditional moments for country aggregate
parameters such as `rho_{j,c}`, `Phi_y_{j,c}`, `Phi_b_{j,c}`, and
`Sigma_eps,c`, under the specified fiscal-rule equation, timing conventions,
measurement equations, and fiscal-shock orthogonality assumptions. With
approximately 83-95 observations for the U.S. and EA, this is feasible for a
compact conditional equation and a regularized three-instrument covariance. It
is still not large-sample inference and should not be described as structural
identification unless the full DSGE likelihood is included. Posterior
uncertainty, prior sensitivity, and weak-identification diagnostics should be
shown.

### What annual sectoral data provide

Annual sectoral data provide low-frequency production-tax and production-
subsidy allocation weights:

```text
w_T_{c,s,a}
w_S_{c,s,a}
```

under source-specific measurement and allocation assumptions. The annual
sectoral data are useful for saying that sector `s` carries a larger or
smaller share of production taxes and subsidies, and therefore a different
production-wedge level/exposure. They are not strong enough to claim precise
independent quarterly sectoral dynamics, free sectoral persistence, sectoral
debt/output feedbacks, or sectoral quarterly shock variances.

### What is not identified

The following are not identified without additional data or stronger structure:

1. Fully independent quarterly sectoral fiscal shocks.
2. Fully independent sectoral persistence parameters for every sector.
3. China and ROW sectoral production-wedge rules from direct official
   production-tax/subsidy observations.
4. A full structural DSGE posterior if the private-sector model is omitted from
   the likelihood.

## Treatment of China and ROW

China and ROW should be modeled as transfer-prior countries unless direct
quarterly and annual sectoral fiscal sources are found.

For China and ROW:

```text
theta_{j,c} ~ TransferPrior(theta_{j,US}, theta_{j,EA}, scale_{j,c})
Sigma_eps,c ~ ShrinkagePrior(Sigma_eps,US, Sigma_eps,EA, data_quality_c).
```

A concrete prior family is:

```text
theta_{j,c} = mu_transfer_{j,c} + H_{j,c} z_{j,c},

z_{j,c} ~ StudentT(nu_transfer, 0, I),

mu_transfer_{j,c}
  = w_US,c theta_{j,US} + w_EA,c theta_{j,EA} + X_c gamma_j,

H_{j,c} = diag(h_rho_{j,c}, h_y_{j,c}, h_b_{j,c}).
```

The weights and scale terms should be built from observable fiscal-capacity
and macro-finance proxies, not chosen after seeing runtime performance.
Examples are government revenue/GDP, debt/GDP, output cyclicality, tax mix,
sector shares, and IO benchmark fiscal shares. The Student-t tail is deliberate:
it makes transferred countries more uncertain than direct-data countries and
reduces false precision.

The scale can use:

1. Aggregate fiscal responsiveness proxies.
2. Government revenue/debt cyclicality proxies.
3. Sectoral IO or GDP shares.
4. GTAP/OECD/ICIO benchmark tax/subsidy shares if available.

The posterior should widen uncertainty for transferred countries:

```text
sigma_transfer_CN > sigma_direct_US
sigma_transfer_ROW > sigma_direct_US
```

This prevents the calibration from pretending that scaled China/ROW values are
as data-rich as U.S. or EA values.

Rows for China and ROW in generated sectoral production-weight files should be
named as allocated or transferred-weight objects. They should not be described
as direct China-sector or ROW-sector estimates unless direct official sectoral
production-tax/subsidy observations enter the likelihood.

## Frequency transformation

The updated baseline no longer transforms annual sectoral fiscal-rule
coefficients to quarterly frequency, because it does not estimate annual
sectoral fiscal rules. The quarterly fiscal-rule parameters come from the
aggregate Bayesian block:

```text
rho_{j,c}, Phi_y_{j,c}, Phi_b_{j,c}, Sigma_eps,c
    for j in {C, N, Y}.
```

Annual sectoral information enters only through `tau_Y` production weights:

```text
w_T_{c,s,a}, w_S_{c,s,a}.
```

The quarterly sectoral production-wedge construction is therefore:

```text
aggregate quarterly tau_Y dynamics
    + annual sectoral production-tax/subsidy level or exposure weights
    -> sectoral quarterly tau_Y runtime matrix.
```

The conservative audit-ready default is:

```text
rho_{Y,c,s} = rho_{Y,c}
Phi_y_{Y,c,s} = Phi_y_{Y,c}
Phi_b_{Y,c,s} = Phi_b_{Y,c}
Sigma_{Y,c,s} = Sigma_{Y,c}
```

with sectoral heterogeneity entering through the annual `D29`/`D39` weights
and the sectoral steady/exposure component, not through sector-specific
dynamic coefficients. The current HMF implementation uses the richer but still
restricted loading version:

```text
rho_{Y,c,s} = rho_{Y,c}
Phi_y_{Y,c,s} = loading_s Phi_y_{Y,c}
Phi_b_{Y,c,s} = max(0, abs(loading_s) Phi_b_{Y,c})
Sigma_{Y,c,s} = Sigma_{Y,c} max(0.25, abs(loading_s)) measurement_error_s
```

where `loading_s` is computed from revenue-based annual production-tax/subsidy
exposure. These are allocated sectoral rule matrices, not separately estimated
sectoral rules. If a richer version introduces latent sectoral loadings:

```text
x^Q_{Y,c,s,t} = xbar^A_{Y,c,s,a(t)} + lambda_{Y,c,s} x^Q_{Y,c,t},
```

then `lambda_{Y,c,s}` is a loading on aggregate dynamics, not a separately
estimated fiscal-rule response. It must be identified from annual validation
or imposed with strong shrinkage around one.

For the current sectoral C2-SUT baseline, annual residual standard deviations
are already generated and passed through a runtime field named `Sigma_tau_Y`.
The HMF design should not inherit that convention without a frequency mapping.
An HMF runtime candidate must either:

```text
1. use the aggregate quarterly `Sigma_eps,c` from the Bayesian block;
2. use aggregate quarterly `Sigma_eps,c` times an audited sectoral loading
   sensitivity; or
3. label any annual residual scale as annual and block it from runtime use.
```

The implemented HMF candidate follows option 2 and additionally emits
`sectoral_tau_y_factor_covariance.csv`, a restricted sectoral covariance
diagnostic:

```text
eps_{Y,c,s,t} = loading_s u_{Y,c,t} + eta_{Y,c,s,t}
Cov(eps_s, eps_r) =
    loading_s loading_r Var(u_{Y,c,t})
  + 1{s=r} Var(eta_{Y,c,s,t}).
```

This is the appropriate role for the revenue-based system in the current data
environment: it improves sectoral exposure, shock dispersion, and a disciplined
covariance prior, but it does not identify an unrestricted sectoral covariance
matrix or free sectoral `rho`, `Phi_y`, and `Phi_b`.

It should not expose annual residual scales under a quarterly runtime name.

## Determinacy and model-solution filtering

A fiscal-rule posterior is not runtime-ready merely because the statistical
block estimates. The draw must also be compatible with model solution.

There are three options:

1. Ex ante restrictions:
   - impose nonnegative debt feedback as an admissibility restriction;
   - restrict persistence below one;
   - restrict volatility and response magnitudes.
2. Ex post posterior filtering:
   - estimate fiscal-rule posterior;
   - solve the DSGE model for each posterior draw;
   - retain or weight draws that solve and satisfy BK/stability checks and
     bounded debt dynamics.
3. Joint structural posterior:
   - include the DSGE solution inside the likelihood;
   - reject nonsolving draws during posterior simulation.

The first option is easiest. The third is closest to LPT. The second is a
practical bridge.

For the current project, a credible sequence is:

```text
statistical posterior -> determinacy filter -> runtime posterior summary.
```

The model calibration should report:

```text
share of posterior draws solving the DSGE model
filtered effective sample size
share satisfying bounded-debt diagnostics
posterior means/medians before filtering
posterior means/medians after filtering
reason for rejected draws
```

The feasibility gate should set a minimum solution mass before any runtime
summary is reported as a full filtered-posterior runtime baseline. A practical
default is:

```text
Pr(Solve(theta)=pass | data) >= 0.50
filtered effective sample size >= 100
```

for a prototype posterior, with tighter thresholds for reported paper results.
If the solve probability is below the pre-specified threshold, selecting one
passing draw is a diagnostic exercise, not a supported runtime baseline.
The current checksum-bound anchored HMF/C2-SUT candidate is narrower than that
full posterior standard: it is runtime-selectable after a summary solve-status
gate and a five-draw diagnostic filter, but it is not a full filtered-posterior
runtime baseline until the larger ESS/solve-mass gate is met.
Bounded-debt diagnostics should be defined before filtering. The default test
is: after each fiscal shock or selected policy experiment, the government-debt
state must not display explosive growth over the reported IRF horizon and must
have a stable linear transition under the solved model. The harness should
record the maximum absolute debt deviation over the horizon, the terminal debt
deviation, and the relevant transition spectral-radius diagnostic when
available.

The selected runtime matrix cannot be an unchecked componentwise posterior
median. Componentwise medians can violate aggregation, admissibility, or
solution constraints even when many individual posterior draws pass. The HMF
handoff should either:

```text
1. select a representative passing draw, such as the filtered-posterior draw
   closest to the filtered posterior median vector under a documented metric;
2. compute a constrained summary and then solve-check that summary; or
3. report model objects as posterior distributions over filtered draws rather
   than collapsing immediately to one matrix.
```

In all cases, the selected point runtime must have its own solve status.

## How this differs from current C2-SUT runtime

The current default C2-SUT runtime is a calibrated dataset:

1. Sectoral U.S. coefficients come from annual BEA/SUT sectoral regressions.
2. EA, China, and ROW are scaled or transferred.
3. Runtime coefficients are point values.
4. Negative debt feedback is clipped as a determinacy-oriented admissibility
   restriction, not as a proof of determinacy.
5. Full posterior uncertainty is not propagated.

The first implemented HMF prototype now adds:

1. `scripts/build_hmf_fiscal_rule_estimator.py`, which generates 500
   posterior or pseudo-posterior fiscal-rule-block draws.
2. Aggregate HMF vectors for `tau_C` and `tau_N`, loaded through
   `calibration.jl` when `fiscal_rule_layer=:hmf_candidate`.
3. Annual production-tax and production-subsidy weights for the U.S. BEA SUT
   sectoral layer.
4. A sectoral HMF `tau_Y` allocation artifact for comparison.
5. A solve-filtered runtime handoff that uses a 75 percent HMF sectoral
   `tau_Y` allocation and a 25 percent C2-SUT production-wedge solution
   anchor. The pure unanchored HMF sectoral `tau_Y` allocation fails the BK
   filter.

The full structural version would extend this with a larger solve-filtered
posterior and DSGE likelihood embedding. The current implementation already
emits:

1. Posterior distributions for aggregate country rules for `tau_C`, `tau_N`,
   and `tau_Y`.
2. A posterior or shrinkage-regularized covariance matrix for aggregate
   fiscal shocks.
3. Annual sectoral production-tax and production-subsidy weights for `tau_Y`,
   with exact annual accounting closure.
4. Explicit uncertainty widening for transferred countries.
5. A checksum-bound summary solve-status gate and a five-draw diagnostic
   posterior solve filter before runtime use.

## Runtime handoff

The runtime handoff must match the existing MCMS architecture. The current
runtime loads generated Julia include files from `MCMS-private/input_data` and
assigns:

```text
Rho_tau_Y
Phi_tau_Y_y
Phi_tau_Y_b
Sigma_tau_Y
```

inside `MCMS-private/src/calibration.jl`.

The hierarchical estimator should therefore emit either:

```text
MCMS-private/input_data/fiscal_rules_hmf/hmf_runtime.jl

function hmf_runtime_matrices()
    return (Rho_tau_Y = ..., Phi_tau_Y_y = ...,
            Phi_tau_Y_b = ..., Sigma_tau_Y = ...)
end
```

or an explicitly named posterior-candidate loader that `calibration.jl` can
select without ambiguity. This requires an explicit runtime selector, for
example:

```text
calibrate(; fiscal_rule_layer = :sectoral_c2_sut)
calibrate(; fiscal_rule_layer = :hmf_candidate)
```

The default must remain the audited baseline until the HMF candidate passes
the feasibility gate. HMF output is opt-in candidate infrastructure, not an
implicit replacement merely because a generated file exists. The output must
distinguish:

```text
unrestricted_empirical_posterior
determinacy_filtered_posterior
runtime_selected_summary
```

As of the first implementation, `:hmf_candidate` is opt-in and passes the
summary-level solve-status gate with:

```text
status = passed_solve_status_only
stage = solve
tau_y_solution_anchor_weight = 0.25
tau_y_hmf_allocation_weight = 0.75
elapsed_seconds = 961.1969997882843
stable_eigenvalues = 1885
required_stable = 1885
unstable_eigenvalues = 723
required_unstable = 723
posterior_target = aggregate_hmf_with_c2_sut_tau_y_anchor_pending_draw_filter
runtime_readiness_flag = point_runtime_solve_ready
point_runtime_solve_ready = true
posterior_filter_ready = false
```

The pass should be interpreted narrowly: the aggregate HMF `tau_C` and
`tau_N` vectors are active, and sectoral `tau_Y` uses a solve-filtered blend.
The pure annual-weight sectoral HMF `tau_Y` allocation exists as an audited
candidate and comparison object. In the current five-draw diagnostic, pure HMF
passes for draws 1, 3, 4, and 5, but draw 2 has a BK shortfall at pure HMF and
passes only after the 25 percent C2-SUT anchor is applied.

Matrix files should use unambiguous names, for example:

```text
Rho_tau_Y_hmf_quarterly_matrix.csv
Phi_tau_Y_y_hmf_quarterly_matrix.csv
Phi_tau_Y_b_hmf_quarterly_matrix.csv
Sigma_tau_Y_hmf_quarterly_matrix.csv
```

Draw-level determinacy filtering is now implemented by
`prepare_hmf_posterior_draw_filter_candidates.py` and
`check_hmf_posterior_draw_filter.jl`. The remaining task is scaling from the
five-draw diagnostic subset to a larger thinned or full posterior. The harness:

1. load posterior draws or thinned posterior draws;
2. inject each draw into the fiscal-rule matrices;
3. run the same QZ/BK and model-export checks used by the full model;
4. record solve status, failed condition, and rejected-draw reason;
5. export filtered posterior summaries and a selected runtime draw or
   solve-checked constrained summary.

The harness should be solve-only by default. It now returns QZ/BK counts,
solution status, timeout-enforcement status, and failure reason without running
IRF generation or export for every posterior draw. IRFs should be computed only
for the selected runtime draw or for a small filtered-posterior subset.
Bounded-debt diagnostics remain a required next extension; they are not yet
implemented in the draw-level filter output.

Every generated runtime object should be validated on load:

```text
validate_fiscal_rule_matrices!(
    obj,
    expected_country_order = ["EA", "China", "ROW", "USA"],
    expected_size = (4, 44),
    allowed_closures = [...],
)
```

The validation should fail on wrong dimensions, nonfinite values, missing
country order, swapped country order, unrecognized closure rule, or matrix
names that do not match the selected fiscal-rule layer. A companion
`check_hmf_runtime.jl` script should compare CSV summaries to generated Julia
matrices within tolerance and record the selected runtime layer.

For implementation, the project should choose a concrete stack. A practical
first version can be Python for posterior estimation and CSV/JL artifact
generation, because the existing builders already follow that pattern. The
full DSGE-embedded version is more naturally Julia-side because it must solve
MCMS inside the posterior loop.

## Audit outputs required

The estimator should emit the following artifacts:

```text
aggregate_quarterly_posterior_draws.csv or parquet
aggregate_quarterly_posterior_summary.csv
aggregate_shock_covariance_posterior_summary.csv
latent_quarterly_state_space_panel.csv
latent_quarterly_state_space_diagnostics.csv
sectoral_tau_y_factor_covariance.csv
annual_production_tax_weights.csv
annual_production_subsidy_weights.csv
sectoral_tau_y_annual_panel.csv
sectoral_tau_y_quarterly_candidate_summary.csv
country_transfer_prior_summary.csv
determinacy_filter_summary.csv
hmf_runtime.jl
Rho_tau_Y_hmf_quarterly_matrix.csv
Phi_tau_Y_y_hmf_quarterly_matrix.csv
Phi_tau_Y_b_hmf_quarterly_matrix.csv
Sigma_tau_Y_hmf_quarterly_matrix.csv
Rho_tau_C_hmf_quarterly_vector.csv
Phi_tau_C_y_hmf_quarterly_vector.csv
Phi_tau_C_b_hmf_quarterly_vector.csv
Sigma_tau_C_hmf_quarterly_vector.csv
Rho_tau_N_hmf_quarterly_vector.csv
Phi_tau_N_y_hmf_quarterly_vector.csv
Phi_tau_N_b_hmf_quarterly_vector.csv
Sigma_tau_N_hmf_quarterly_vector.csv
hierarchical_mixed_frequency_audit.md
```

Each artifact should include:

```text
source family
source URL or local source file
frequency
country
sector
variable definition
model transform
prior family
posterior summary
runtime readiness flag
source file hashes
generated Julia checksum
matrix schema and dimensions
selected fiscal-rule layer
posterior target: unrestricted, policy-admissible, or solution-filtered
```

## Minimal implementable version

The minimal useful implementation should still aim to deliver the promised
hierarchical mixed-frequency object, not only a downgraded descriptive
exercise. It is:

1. Build aggregate quarterly `tau_C`, `tau_N`, and `tau_Y` panels for the U.S.
   and EA, with China and ROW flagged as mixed-frequency/proxy/transfer cases
   where necessary.
2. Estimate aggregate quarterly rules with Bayesian priors and a regularized
   cross-instrument covariance matrix.
3. Build annual sectoral production-tax and production-subsidy weights in
   `MCMS-private`, using separate `D29` and `D39` controls wherever possible
   rather than a single net weight.
4. Map those weights to the 44 MCMS sectors with explicit quality flags,
   benchmark errors, and source-specific measurement-error inflation.
5. Hold China and ROW as transferred-prior or allocated-weight countries with
   Student-t transfer uncertainty and explicit provenance.
6. Combine aggregate `tau_Y` posterior draws with annual production weights to
   generate candidate sectoral `tau_Y` matrices; keep `tau_C` and `tau_N` as
   aggregate vectors.
7. Select a representative passing draw or solve-checked constrained summary,
   not unchecked componentwise medians.
8. Run the draw-level full-model solve filter, or a solve-only summary-level
   prototype as an interim diagnostic.
9. Compare four layers: current C2-SUT, aggregate-only Bayesian, annual
   production-weight allocation, and HMF candidate. Report fit, posterior
   uncertainty, solve rate, bounded-debt diagnostics, and model outcomes.
10. Document uncertainty and do not call the output direct sectoral quarterly
    evidence.

This version is not fully structural LPT. Its advantage over the current
point-calibrated C2-SUT runtime is uncertainty accounting, aggregate
cross-instrument posterior discipline, explicit production-weight accounting,
and model-solution conditioning, not structural LPT identification.

## Minimum proof-of-feasibility gate

Before any hierarchical mixed-frequency output is treated as runtime-ready,
the project should complete a small reproducible prototype:

1. generate at least 100 posterior or pseudo-posterior fiscal-rule draws for a
   harness smoke test, with a larger draw count required before reporting
   posterior summaries in the paper;
2. map each draw into aggregate `tau_C` and `tau_N` vectors plus exact
   sectoral `Rho_tau_Y`, `Phi_tau_Y_y`, `Phi_tau_Y_b`, and `Sigma_tau_Y`
   matrices generated from aggregate `tau_Y` dynamics and annual production
   weights;
3. write those matrices through the proposed `fiscal_rules_hmf` generated
   Julia API;
4. load the matrices through `calibration.jl` or a dedicated test harness;
5. record solve rate, wall time, memory use, failed BK/stability conditions,
   bounded-debt diagnostics, and rejection reasons;
6. compare current C2-SUT, aggregate-only Bayesian, annual production-weight
   allocation, and HMF candidate layers on fit, posterior uncertainty, solve
   rate, bounded-debt diagnostics, and model outcomes;
7. compare model outcomes under the approximation with the latent
   state-space/annualization benchmark or a simulation validation if the
   benchmark is not yet implemented.

Until that gate is passed, Stage 1-2 outputs should be described as posterior
calibration evidence and candidate matrices, not as the runtime baseline. The
goal is not to weaken the ambition, but to make the promised HMF runtime claim
conditional on the missing operational pieces being implemented and audited.

Current prototype status:

1. The 100-draw smoke threshold is exceeded: the builder emits 500 draws.
2. Aggregate `tau_C` and `tau_N` vectors are generated and loaded by
   `calibration.jl`.
3. Annual sectoral production-tax and production-subsidy weights are generated
   in `MCMS-private/input_data/fiscal_rules_hmf`.
4. The pure experimental sectoral HMF `tau_Y` allocation fails the solve
   filter for draw 2 with 1,884 stable eigenvalues versus 1,885 required, but
   passes for draws 1, 3, 4, and 5 in the current five-draw diagnostic subset.
5. The active HMF runtime therefore uses the strongest passing tested blend:
   75 percent HMF sectoral `tau_Y` allocation and 25 percent C2-SUT solution
   anchor.
6. `scripts/check_hmf_solve_status.jl` records the point-runtime solve gate in
   `determinacy_filter_summary.csv`; the current checksum-bound point runtime
   passes with 1,885 stable and 723 unstable eigenvalues, exactly matching the
   required BK counts. `calibration.jl` now enforces the live HMF runtime
   checksum against `metadata.json` and `determinacy_filter_summary.csv`; the
   solve script records both the pre-readiness file checksum and the post-
   readiness file checksum, plus an invariant structural runtime hash.
7. `scripts/summarize_hmf_layer_comparison.py` records matrix-distance
   comparisons across C2-SUT, the active HMF blend, and the pure unanchored
   HMF allocation in `layer_comparison_summary.csv`.
8. `latent_quarterly_state_space_panel.csv` and
   `latent_quarterly_state_space_diagnostics.csv` replace the earlier
   annual-to-quarterly coefficient shortcut for annual-observed aggregate
   instruments. The bridge treats quarterly fiscal wedges as latent random-walk
   states and annual fiscal data as annual-average measurements. Latent-state
   posterior variance enters as a first-order shock-scale inflation before the
   quarterly fiscal-rule posterior is summarized; the implementation does not
   yet simulate full latent paths through the structural MCMS equilibrium. The
   bridge is used for `tau_C` in EA, China, ROW, and USA, and for `tau_N` in EA,
   China, and USA.
   ROW `tau_N` and China/ROW `tau_Y` remain transfer-prior cases because the
   current database lacks eight annual measurements for those objects.
9. `sectoral_tau_y_factor_covariance.csv` records the restricted sectoral
   `tau_Y` shock covariance implied by revenue-based exposure loadings: one
   aggregate country `tau_Y` factor plus diagonal sectoral idiosyncratic noise.
10. `scripts/prepare_hmf_posterior_draw_filter_candidates.py` and
   `scripts/check_hmf_posterior_draw_filter.jl` implement the posterior-draw
   solve-filter harness. After the latent-state-space rebuild, the stale
   pre-state-space draw filter was overwritten by a fresh five-draw solve
   filter using the anchor grid `0.0, 0.25, 0.5, 0.75, 1.0`. The filter tested
   six candidates: draws 1, 3, 4, and 5 pass at pure HMF; draw 2 fails at pure
   HMF with a BK shortfall and passes at the active 75/25 blend. Candidate
   files carry hashes for immutable/current source inputs and C2 anchor
   matrices; the mutable `metadata.json` hash is not used as candidate
   provenance. The Julia filter validates provenance, country order, vector
   length, matrix dimensions, finite values, and anchor-weight closure before
   solving each candidate; malformed candidates are recorded as failed rows
   rather than aborting the whole batch silently.
11. The draw-filter harness is now adaptive: candidate generation supports
   anchor grids, and the Julia filter supports `--resume
   --skip-draw-after-pass` so long posterior filters can be continued without
   retesting draws that already have one passing anchor.
12. `scripts/summarize_hmf_posterior_draw_filter.py` reduces raw draw-anchor
    trials into minimum-passing-anchor summaries. In the current diagnostic
    set, all five tested latent-state-space posterior draws have at least one
    passing anchor; the minimum passing anchor is 0.0 for four draws and 0.25
    for one draw.
13. A separate fixed active-anchor filter path has been prepared for the
    100-draw posterior-readiness gate.
    `posterior_draw_filter_active_anchor_candidates.json` contains 100
    active-anchor candidates at `tau_y_solution_anchor_weight = 0.25` and
    validates with code/data provenance. A final code-bound smoke solve in
    `posterior_draw_filter_active_anchor_codebound_smoke_summary.csv` has 1
    completed active-anchor draw, passing with exact BK counts and matched
    provenance; the associated overall summary reports `filtered_ess_proxy =
    1` and `posterior_ready_gate_passed = false`.
14. `scripts/run_hmf_pipeline.py` provides a reproducible wrapper: cheap
    reporting refreshes run by default, while `--build`, `--runtime-check`,
    `--solve-check`, and `--draw-filter --resume --skip-draw-after-pass`
    opt into expensive stages.
15. `scripts/check_hmf_runtime.jl` passes and
    `scripts/check_hmf_solve_status.jl` records
    `passed_solve_status_only`. Generated HMF runtimes now start with
    `point_runtime_pending_solve_filter`; only `check_hmf_solve_status.jl` can
    mark the point runtime `point_runtime_solve_ready`. The separate
    `posterior_filter_ready` flag remains false until a larger posterior draw
    filter meets the pre-specified solve-mass and ESS gate. The determinacy row
    records the generated Julia checksum, source-hash manifest, elapsed time,
    and BK counts used for the passing point-runtime solve.

The next implementation step is continuing the fixed active-anchor posterior
solve filter from the final code-bound smoke draw to at least the 100-draw
readiness gate. The harness exists and can resume across sessions, but the
repository does not yet contain a 100-draw or 500-draw filtered posterior
because each solve is expensive in the current Julia pipeline.

## Full structural version

The full structural version embeds the mixed-frequency fiscal block into the
MCMS state-space representation. The state vector contains private-sector MCMS
states, aggregate fiscal states, and the production-wedge allocation states or
weights needed to map aggregate `tau_Y` into sectoral model wedges. The
observation equations map this state vector to quarterly aggregate observables
and annual production-tax/subsidy weight or level observables.

The likelihood is:

```text
log L(theta)
  = log p(quarterly aggregate observables,
          annual production-weight observables
          | MCMS solution, theta).
```

The posterior is:

```text
p(theta | data) proportional to L(theta) p(theta).
```

This is the object closest to LPT. It is also the most expensive because every
posterior draw must solve the model or be filtered for determinacy.

## Literature positioning

The method is a new combination rather than a direct copy of a single paper.
The closest foundations are:

1. Leeper, Plante, and Traum (2010), "Dynamics of Fiscal Financing in the
   United States." This is the LPT fiscal-rule estimation benchmark.
   Link: https://www.nber.org/papers/w15160
2. Herbst and Schorfheide (2015), "Bayesian Estimation of DSGE Models." This provides
   general Bayesian DSGE estimation machinery and discusses LPT-motivated
   applications.
   Link: https://academic.oup.com/princeton-scholarship-online/book/30660
3. Foroni and Marcellino (2014), "Mixed-Frequency Structural Models:
   Identification, Estimation, and Policy Analysis." This supports the
   mixed-frequency structural estimation logic.
   Link: https://ideas.repec.org/a/wly/japmet/v29y2014i7p1118-1144.html
4. Meyer-Gohde and Shabalina (2022), "Estimation and Forecasting Using
   Mixed-Frequency DSGE Models." This supports DSGE estimation with
   mixed-frequency observables.
   Link: https://ideas.repec.org/p/zbw/imfswp/175.html
5. Pedregal and Perez (2010), "Should Quarterly Government Finance Statistics
   Be Used for Fiscal Surveillance in Europe?" This supports mixed-frequency
   fiscal state-space methods.
   Link: https://ideas.repec.org/a/eee/intfor/v26y2010i4p794-807.html
6. Asimakopoulos, Paredes, and Warmedinger (2013), "Forecasting Fiscal Time
   Series Using Mixed Frequency Data." This supports high-frequency fiscal
   indicators combined with lower-frequency fiscal targets.
   Link: https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1550.pdf

The note should phrase the contribution as:

```text
We combine LPT-motivated fiscal-rule posterior discipline with mixed-frequency
state-space logic and annual sectoral production-weight accounting. Quarterly
aggregate data discipline country-level fiscal dynamics for consumption,
income/labour, and production instruments under explicit timing and
measurement assumptions, while annual BEA, Eurostat, and other sectoral
accounts allocate production taxes and subsidies across sectors with exact
annual accounting closure.
```

It should avoid the stronger claim:

```text
We estimate LPT sectoral fiscal rules directly from quarterly sectoral data.
```

That claim would be false because the official quarterly sectoral
production-tax/subsidy data are not observed.

## Recommended wording for the paper

The paper can say:

```text
The fiscal-rule calibration follows a hierarchical mixed-frequency design. At
the country level, quarterly aggregate fiscal observables discipline the
dynamic response of aggregate consumption, income/labour, and production
fiscal instruments to output and debt, including the covariance of their
fiscal shocks where the data support it. Consumption and income/labour taxes
remain aggregate country instruments. At the sector level, annual production-
tax and production-subsidy accounts construct separate `D29` and `D39`
weights that allocate the production wedge across sectors while preserving
official annual totals. The resulting sectoral production-wedge matrices are
posterior candidate runtime objects, not directly observed quarterly sectoral
fiscal rules.
```

It should also state:

```text
This procedure is LPT-motivated in its use of dynamic fiscal rules and posterior
discipline, but it is not a full LPT replication unless the fiscal-rule block
is estimated jointly with the DSGE equilibrium conditions.
```

## Main risks

1. Overclaiming the sectoral quarterly data.
   - Fix: always call the sectoral quarterly series latent or transformed.
2. Weak sectoral dynamic identification.
   - Fix: keep sectoralization to annual production-tax/subsidy weights unless
     new direct sectoral time-series evidence is added.
3. Debt feedback instability.
   - Fix: sign restrictions or determinacy filtering.
4. China/ROW evidence gap.
   - Fix: transfer priors with wider uncertainty.
5. Annual-to-quarterly transformation ambiguity.
   - Fix: the current HMF implementation now uses a latent quarterly
     state-space bridge with annual-average measurement equations for
     annual-observed aggregate instruments where coverage permits. Remaining
     transfer-prior cases must stay labeled as such.
6. Runtime mismatch.
   - Fix: export exact runtime matrices from posterior summaries and run model
     solution checks before using them as the baseline.

## Conclusion

A hierarchical mixed-frequency LPT-motivated calibration is feasible and
defensible. It would not create observed quarterly sectoral fiscal data, but it
would use the available official data efficiently: quarterly aggregate series
for country-level fiscal dynamics and annual sectoral accounts for production-
tax/subsidy allocation. The method is most defensible if it is presented as a
posterior-backed calibration bridge, with a clear path to full structural DSGE
estimation once the MCMS model is embedded in the likelihood.
