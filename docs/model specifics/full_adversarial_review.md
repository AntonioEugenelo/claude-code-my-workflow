# Adversarial review of `full.md`

Date: 2026-05-13

Target: `claude-code-my-workflow/docs/model specifics/full.md`

Requested reviewer set: theory critic and coding check agent only.

Loop status: complete for the requested reviewer set. Both reviewers completed independent read-only reviews, the coordinator reconciled the findings, and no edit/rereview round was triggered because `full.md` itself was not modified during this review.

Important infrastructure note: the local scripted review planner does not expose a custom two-reviewer plan for a `.md` target; it routes markdown files to proofreader/devils-advocate. To honor the user's explicit reviewer constraint, this review used the full adversarial loop structure manually with only the requested theory and code reviewers.

## Quarterly C2 calibration adversarial rereview, May 13, 2026

Request: full adversarial review of the updated calibration material after the
quarterly C2 update. Reviewer set: theory critic and code/calibration check
agent.

Loop status: complete. The two reviewers completed independent read-only
reviews. The coordinator also inspected the live generated artifacts, verified
that `src/calibration.jl` contains the quarterly C2 vectors, ran a syntax-only
AST check on the active Python builders, ran the Julia vector check, and reran
the full quarterly C2 model check. This section supersedes older C2/sectoral
comments below where they conflict with the current quarterly C2 runtime.

### Updated scores after quarterly C2

| Reviewer | Score | Verdict |
| --- | ---: | --- |
| Theory critic | 42/100 | Documentation improved, but paper/runtime/audit still conflict and the active baseline fails BK. |
| Code/calibration check agent | 56/100 | Quarterly C2 is mechanically integrated, but the model still does not solve and sectoral tax rates are not runtime-integrated. |
| Coordinator synthesis | 45/100 | Better data bridge than annual C2, but still not an editor-defensible calibrated baseline. |

Calibration-specific score after quarterly C2:

| Calibration object | Score | Current status |
| --- | ---: | --- |
| Fiscal equations and wedge definitions | 75/100 | Equations remain coherent and `build_equations.jl` consumes the intended objects. |
| Quarterly C2 production-rule data layer | 60/100 | Major improvement over annual frequency; direct quarterly EA and USA estimates now exist. |
| Quarterly C2 runtime integration | 55/100 | Runtime vectors match generated country coefficients, but they are still manually copied into Julia. |
| Model-solution validity | 20/100 | Full current runtime check fails BK by two stable roots. |
| Sectoral tax-rate calibration | 35/100 | Sectoral/SUT and quarterly 4-by-44 files exist, but runtime uses country aggregate rates repeated across sectors. |
| Fiscal closure economics | 30/100 | Production-wedge debt feedback is negative in all countries and destabilizes the solved system. |
| LPT consistency | 30/100 | Still reduced-form OLS outside the DSGE, not an LPT structural posterior. |

### What changed

The active production-wedge calibration is now `Quarterly C2`, not annual C2.
The active artifacts are:

```text
MCMS-private/scripts/build_fiscal_rule_dataset_quarterly_c2.py
MCMS-private/input_data/fiscal_rules_quarterly_c2
MCMS-private/src/calibration.jl
```

The runtime country order remains:

```text
EA, China, ROW, USA
```

The live runtime vectors are:

```text
Rho_tau_Y   = [0.06377464862897264, 0.49268960242939547, 0.5564666371949851, 0.6888852763870515]
Phi_tau_Y_y = [0.05886484237361775, 0.012643484605117439, 0.0009611292452423523, 0.010127182982481558]
Phi_tau_Y_b = [-0.014998973569044179, -0.02884011700539614, -0.03707015920831699, -0.009242063830002782]
Sigma_tau_Y = [0.00525912488192555, 0.004784228152489203, 0.002738881214194855, 0.0034843217217488142]
```

The update resolves one prior criticism: annual production-rule estimates are no
longer the active production-wedge runtime rule. EA and USA now use direct
quarterly estimates:

```text
USA: 83 observations, 2005Q2-2025Q4, BEA/FRED quarterly C2 object
EA:  95 observations, 2002-Q2-2025-Q4, Eurostat D29REC-D39PAY
```

It also removes the previous direct-EA-plus-tax-margin double-scaling issue for
the active EA aggregate rule: the quarterly builder uses the direct EA beta and
sigma directly. China and ROW, however, remain scaled transfer calibrations from
the U.S. quarterly aggregate rule using existing C2 fiscal-responsiveness
scales.

### Verification completed in this rereview

Python syntax check:

```text
AST OK for:
MCMS-private/scripts/build_fiscal_rule_dataset_quarterly_c2.py
MCMS-private/scripts/build_fiscal_rule_dataset_sectoral_c2_sut.py
```

Julia runtime vector check:

```text
julia --project=. scripts\check_quarterly_c2_calibration.jl
```

Result: `calibrate()` completed and printed the expected quarterly C2 vectors.

Full model check:

```text
julia --project=. scripts\run_c2_full_model_check.jl
```

Fresh result from this rereview:

```text
Output MAT target: output_julia\irfs\irf_C2_FullModelCheck_2026-05-13_22-05-27.mat
equations = 6,762
variables = 6,762
shocks = 448
static elimination residual = 2.842154310930614e-14
stable eigenvalues = 1,883
required stable eigenvalues = 1,885
unstable eigenvalues = 725
required unstable eigenvalues = 723
result = BK violation, no stable solution
```

The current quarterly C2 runtime is therefore integrated but not solved. No
baseline quarterly C2 IRFs should be treated as valid.

### Major blockers after quarterly C2

#### QC2-1. Active baseline still fails BK

Severity: blocker.

The full model reaches QZ and fails:

```text
BK violation: too few stable eigenvalues (1883 < 1885). No stable solution.
```

This is a hard stop for baseline quantitative use. A paper cannot present this
as the calibrated baseline unless it either changes the fiscal closure so the
model solves or explicitly reports it as a failed candidate.

#### QC2-2. Debt feedback has the wrong stabilizing logic in the model

Severity: blocker.

The active production-wedge debt feedback is negative for all countries:

```text
Phi_tau_Y_b = [-0.014998973569, -0.028840117005, -0.037070159208, -0.009242063830]
```

The model equation is:

```text
tau_Y[k,i,t] =
    rho * tau_Y[k,i,t-1]
  + (1-rho) * (Phi_y * y[k,t] + Phi_b * bgov[k,t-1])
  + Sigma * eps[k,i,t]
```

With the model's sign convention, a negative production-wedge debt response
means higher inherited debt lowers production taxes or raises subsidies. That is
not an LPT-style stabilizing fiscal closure unless another fiscal instrument
does the debt stabilization and the solved model proves this joint mechanism.

Older diagnostics already showed that zeroing, clipping, making positive, or
shrinking the negative production-wedge debt feedbacks restores BK. The fresh
quarterly C2 run still fails with the all-negative debt-feedback vector.

#### QC2-3. Sectoral tax-rate material is not the live runtime calibration

Severity: high.

The repository now contains two kinds of 4-by-44 sectoral files:

```text
MCMS-private/input_data/fiscal_rules_sectoral_c2_sut
MCMS-private/input_data/fiscal_rules_quarterly_c2/*_matrix.csv
```

But `src/calibration.jl` still does:

```text
Rho_tau_Y = repeat(rho_tau_Y_by_country, 1, Inum)
Phi_tau_Y_y = repeat(phi_tau_Y_y_by_country, 1, Inum)
Phi_tau_Y_b = repeat(phi_tau_Y_b_by_country, 1, Inum)
Sigma_tau_Y = repeat(sigma_tau_Y_by_country, 1, Inum)
```

The quarterly sectoral file uses neutral output-share allocation, which implies
the same wedge rate for every sector inside a country. The sectoral C2-SUT file
has more genuine U.S. sectoral variation, but it is explicitly candidate-only
and not integrated into runtime.

Adversarial conclusion: the paper may say the current runtime has a
country-level production-wedge rule distributed across sectors. It should not
claim that the live model uses empirically estimated sector-specific fiscal
reaction functions.

#### QC2-4. Generated-to-runtime bridge is still manual

Severity: high.

The generated `quarterly_c2_country_coefficients.csv` values match the live
hard-coded Julia vectors, but the model does not load the CSV. Regenerating the
dataset will not change the model unless a human manually patches
`src/calibration.jl`.

Adversarial conclusion: this is not yet a robust calibration pipeline. The
runtime should load a frozen artifact or generated include file and record
metadata/checksums.

#### QC2-5. The paper is stale relative to the runtime

Severity: high.

`Fiscal-LPT/main.tex` still describes the production-rule table as operational
runtime calibration but reports old hand-set values:

```text
rho^Y_k = [0.80, 0.70, 0.75, 0.80]
phi^Y_y = [0.02, 0.03, 0.02, 0.01]
phi^Y_b = [0.015, 0.020, 0.015, 0.010]
```

Those do not match the live quarterly C2 runtime. The paper also contains older
language saying the numerical coefficients do not come from an estimated fiscal
reaction function. That is now inaccurate for EA and USA production-wedge
dynamics, which are estimated reduced-form quarterly rules. It remains accurate
for China and ROW and for many other fiscal objects.

Adversarial conclusion: the paper/runtime mismatch is editorially dangerous.
Before submission, the paper must either update the tables to quarterly C2 or
state that the paper tables are illustrative/non-runtime.

#### QC2-6. The steady-state production wedge is still not observed fiscal data

Severity: high.

The runtime still uses:

```text
Tbar_Y = 1.0 ./ M .- 1.0
```

This is a markup-implied steady-state wedge. It is not observed sectoral
production-tax or subsidy data. Quarterly C2 affects the dynamic rule only.

Adversarial conclusion: separate the normative markup-offsetting steady state
from the empirical/proxy fiscal-rule dynamics in every table and claim.

#### QC2-7. The quarterly U.S. object is cleaner, but not identical to annual C2

Severity: medium-high.

The U.S. quarterly object subtracts:

```text
federal excise taxes
customs duties
state/local sales taxes
```

from quarterly TOPI less subsidies over gross output. This removes customs
duties and major product-tax overlap, but the audit correctly states that the
quarterly public series do not expose every annual-style product-tax
subcomponent. The quarterly construction is better for model frequency, but not
a perfect replacement for the richer annual decomposition.

#### QC2-8. The sectoral C2-SUT object is conceptually different from quarterly C2

Severity: medium-high.

The sectoral C2-SUT candidate excludes product taxes/imports but leaves product
subsidies inside the wedge as negative subsidies. EA quarterly C2 uses
`D29REC-D39PAY`, i.e. other taxes on production net of other subsidies on
production. These are close but not identical fiscal concepts.

Adversarial conclusion: do not merge quarterly C2 and sectoral C2-SUT without a
concept bridge. If sectoral C2-SUT becomes runtime, it needs its own stability
test and paper language.

### Main points an editor would still make after quarterly C2

1. The active fiscal calibration still does not solve the model. A baseline
   that fails BK cannot support baseline IRFs or welfare results.
2. The runtime and paper tables do not match. The table claiming operational
   runtime calibration is stale.
3. The debt-feedback signs are economically suspicious and destabilizing in the
   model.
4. The live model does not use sector-specific empirical production-tax rules;
   it repeats country aggregate rates across sectors.
5. China and ROW remain transfer/fallback calibrations, not direct quarterly
   fiscal evidence.
6. The production-wedge steady state is markup-implied, not observed fiscal
   policy.
7. The calibration is reduced-form OLS outside the DSGE, not LPT-estimated.
8. The runtime does not load generated calibration artifacts, so the pipeline is
   brittle.

### Required fixes before baseline use

1. Replace the current all-negative production-wedge debt feedback with a
   determinacy-preserving fiscal closure: sign restriction, shrinkage prior,
   zero production-wedge debt feedback, or a separate stabilizing fiscal
   instrument.
2. Rerun full BK and debt-IRF checks after that change.
3. Update `Fiscal-LPT/main.tex` so the production-rule table matches quarterly
   C2, or explicitly mark the table as illustrative and not runtime.
4. Decide whether sectoral C2-SUT is a data appendix or a runtime matrix. If it
   is runtime, integrate and test it separately.
5. Make generated calibration artifacts authoritative for runtime, not manually
   copied values.
6. Keep the LPT language strictly to "LPT-style closure" unless joint DSGE
   estimation is implemented.

## Comprehensive fiscal-augmentation rereview, May 13, 2026

Request: conduct an in-depth review of the repository work toward the fiscal
augmentation of the model, with extreme attention to calibration. Reviewer set:
theory critic and code/calibration check agent.

Loop status: complete. The two reviewers completed independent read-only passes,
the coordinator checked their convergence against the live repository, and this
file was updated rather than creating a new review file.

### Updated scores

| Reviewer | Score | Verdict |
| --- | ---: | --- |
| Theory critic | 52/100 | Fiscal equations are mostly coherent; calibration is not editor-defensible as a final baseline. |
| Code/calibration check agent | 55/100 | C2 is mechanically integrated, but the live baseline fails model solution and the data-to-runtime bridge is brittle. |
| Coordinator synthesis | 48/100 | The fiscal augmentation is a useful experimental layer, but the current calibration should not be presented as a valid baseline. |

Calibration-specific score:

| Calibration object | Score | Current status |
| --- | ---: | --- |
| Fiscal equations and wedge definitions | 75/100 | Mostly internally coherent and aligned with `build_equations.jl`. |
| Consumption-tax steady state | 55/100 | Best-supported fiscal object, but live values are still hand-set and only partly aligned with generated recommendations. |
| Labour-tax wedge | 30/100 | Runtime values are hand-set and the data proxy is income/social revenue, not a clean labour wedge. |
| Production-wedge steady state | 35/100 | `Tbar_Y = 1/M - 1` is a normative markup-offsetting object, not observed fiscal policy. |
| Production-wedge dynamic rule C2 | 25/100 | Directly integrated, but fails BK in the baseline and likely has an EA double-scaling ambiguity. |
| Sectoral C2-SUT candidate layer | 45/100 | Material improvement over aggregate C2 for U.S. sectoral evidence, but not runtime-integrated and not stability-tested. |
| LPT consistency | 30/100 | LPT-style fiscal closure only; not an LPT estimation. |

### Bottom-line verdict

The fiscal augmentation is not ready to be described as a final calibrated model.
The derivations and equation integration are credible enough for an appendix and
for experimental model development, but the calibration is very likely wrong for
baseline quantitative claims unless the paper explicitly downgrades it to a
scenario/sensitivity layer.

The sharpest issue is not a small measurement caveat. The currently integrated
C2 production-wedge rule fails the model-solution check:

```text
Baseline C2 full model run:
stable eigenvalues = 1,883
required stable eigenvalues = 1,885
result = BK violation, no stable solution, no baseline C2 IRFs
```

This is fatal for using C2 as a baseline. The fact that zero, clipped, absolute,
and shrunk debt-feedback variants pass BK shows the failure is concentrated in
the calibration of production-wedge debt feedback, not in generic parser failure.

Update after the sectoral tax-rate calibration: the new sectoral C2-SUT dataset
is a real improvement over the previous aggregate-only evidence for U.S.
production wedges. It estimates 44 U.S. sectoral rules and produces 4-by-44
country-sector matrices. It does not change the baseline verdict because the
sectoral matrices are explicitly marked as candidate-only, are not loaded by
`src/calibration.jl`, inherit the C2 country-scaling assumptions, and have
larger coefficient extremes than aggregate C2.

### Main high-severity findings

#### 1. C2 is integrated but does not solve the model

Severity: blocker.

Evidence:

- `MCMS-private/src/calibration.jl` hard-codes the C2 production-rule vectors:
  `Rho_tau_Y`, `Phi_tau_Y_y`, `Phi_tau_Y_b`, and `Sigma_tau_Y`.
- `MCMS-private/output_julia/logs/c2_full_model_20260513_161623.out.log`
  reaches QZ and reports `1883` stable eigenvalues against `1885` required.
- `MCMS-private/output_julia/logs/c2_full_model_20260513_161623.err.log`
  reports `BK violation: too few stable eigenvalues (1883 < 1885). No stable
  solution.`
- This review already records the same result in the C2 implementation status
  section below.

Adversarial conclusion: an editor would not accept baseline quantitative
results from a calibration that fails BK. The calibration can remain in the repo
as an experiment, but not as the paper's baseline.

#### 2. The C2 debt-feedback coefficients are dynamically destabilizing

Severity: blocker.

The live C2 debt-feedback vector is:

```text
Phi_tau_Y_b = [0.009363564416125004,
               -0.04452161512787383,
               -0.05598147065548276,
               -0.01057010084983507]
```

The diagnostic logs show the following variants pass BK:

| Variant | BK result |
| --- | --- |
| set all production-wedge debt feedbacks to zero | pass |
| clip negative feedbacks to zero | pass |
| use absolute positive feedbacks | pass |
| scale negative feedbacks by 1/3 | pass |
| scale negative feedbacks by 1/10 | pass |

Adversarial conclusion: the unrestricted empirical debt-feedback magnitudes are
not compatible with the model's stability requirements. The negative signs are
also economically suspicious for fiscal closure: when debt is high, a negative
production-wedge debt response lowers production taxes or raises subsidies,
which worsens fiscal closure unless another instrument does the stabilizing.

#### 3. There is a likely EA C2 double-scaling error

Severity: high.

The code estimates a direct EA D29 rule:

```text
EA D29 direct beta_y = -0.00174550562561
EA D29 direct beta_b =  0.00342299891305
EA D29 direct sigma  =  0.00094252462041
```

Then `build_fiscal_rule_dataset_calibration_c2.py` computes:

```text
fiscal_y_scale = EA direct beta_y / US beta_y
fiscal_b_scale = EA direct beta_b / US beta_b
beta_country = US beta * tax_margin_scale * fiscal_scale
sigma_country = US sigma * tax_margin_scale * fiscal_sigma_scale
```

For EA, this algebra collapses to:

```text
EA beta = EA direct beta * tax_margin_scale
EA sigma = EA direct sigma * tax_margin_scale
```

with `tax_margin_scale = 1.3510766540111345`. If the direct EA D29 regression is
already in EA D29 model-deviation units, applying the EA margin scale again is
double scaling. This changes the direct EA coefficients from the direct
Eurostat estimate to the runtime C2 values:

```text
direct beta_y -0.0017455 -> runtime beta_y -0.0023583
direct beta_b  0.0034230 -> runtime beta_b  0.0046247
direct sigma   0.0009425 -> runtime sigma   0.0012734
```

Adversarial conclusion: this must be fixed or explicitly justified. Either use
the direct EA D29 beta/sigma directly, or explain why the direct EA regression
is only a responsiveness ratio and still needs a separate margin-intensity
scale. Right now the code reads like it does both.

#### 4. Annual reduced-form coefficients are hard-coded into a likely quarterly runtime

Severity: high.

The C2 builder computes quarterly approximations:

```text
rho_quarterly_approx
sigma_quarterly_innovation_approx
```

but `src/calibration.jl` consumes annual `Rho_tau_Y` and annual
`Sigma_tau_Y_calibration_c2_annual` directly. The same broader issue applies to
Benchmark A/B fiscal-rule estimates. The documentation correctly warns about
this, but the runtime still uses annual C2 values.

Adversarial conclusion: if the model period is quarterly, the current C2 runtime
calibration is period-inconsistent. At minimum, persistence and shock scales
need conversion. Output and debt feedbacks also need a stated time-aggregation
mapping, not just an AR-root transformation.

#### 5. Generated calibration artifacts are not authoritative for runtime

Severity: high.

`calibration.jl` does not load the generated C2 CSV. It manually copies the
generated values:

```text
rho_tau_Y_by_country = [...]
phi_tau_Y_y_by_country = [...]
phi_tau_Y_b_by_country = [...]
sigma_tau_Y_by_country = [...]
```

This means rerunning `build_fiscal_rule_dataset_calibration_c2.py` does not
change the model unless someone manually patches the Julia file. The generated
data and runtime can silently diverge.

Adversarial conclusion: for a serious calibration workflow, the runtime should
load a frozen calibration artifact or a generated Julia include file with
metadata, checksum, date, and model-frequency convention.

#### 6. Consumption, labour, and debt steady states are still partly hand-set

Severity: high.

The live runtime values are:

```text
Tbar_C  = [0.18, 0.12, 0.14, 0.05]
Tbar_N  = [0.38, 0.25, 0.25, 0.28]
Bgov_ss = [0.878, 0.8833, 0.94, 1.2079]
```

Benchmark B recommendations are:

```text
Tbar_C  = [0.1353297479, 0.1162832972, 0.1389145980, 0.0653347652]
Tbar_N_proxy = [0.2746, 0.0878403812, 0.1031834281, 0.1899996420]
Bgov_ss = [0.9030, 0.7880, 0.9244, 1.2380]
```

The labour proxy is not a clean labour wedge, so it should not be copied
mechanically. But the large gap between runtime `Tbar_N` and the broad
income/social proxy is still a problem: the runtime values are effectively
judgmental placeholders, not data-based fiscal calibration.

Adversarial conclusion: the paper should not imply that all fiscal steady states
come from the new dataset. It can say consumption-tax and debt benchmarks have
candidate data support; labour-tax and production-tax steady states remain
model/calibration assumptions.

#### 7. Production-wedge steady state is not observed fiscal policy

Severity: high.

The live model uses:

```text
Tbar_Y = 1.0 ./ M .- 1.0
```

This is a markup-offsetting normalization. It can be useful as a normative
efficient-steady-state device, but it is not observed sectoral production-tax or
production-subsidy data.

Adversarial conclusion: an editor would object if this is described as a fiscal
calibration. It should be described as a model-implied subsidy/tax wedge used to
offset steady-state markups, with observed fiscal production-tax evidence only
entering the dynamic C2 sensitivity.

#### 8. The runtime production rule is still not sectoral despite being used sector-by-sector

Severity: high.

The live C2 runtime remains an all-industries country-level rule repeated across
all sectors:

```text
Rho_tau_Y = repeat(rho_tau_Y_by_country, 1, Inum)
Phi_tau_Y_y = repeat(phi_tau_Y_y_by_country, 1, Inum)
Phi_tau_Y_b = repeat(phi_tau_Y_b_by_country, 1, Inum)
Sigma_tau_Y = repeat(sigma_tau_Y_by_country, 1, Inum)
```

The new sectoral C2-SUT dataset partially addresses this criticism as a
candidate layer:

```text
MCMS-private/input_data/fiscal_rules_sectoral_c2_sut
```

It estimates all 44 U.S. sectoral rules and writes 4-by-44 matrices:

```text
Rho_tau_Y_sectoral_c2_sut_matrix.csv
Phi_tau_Y_y_sectoral_c2_sut_matrix.csv
Phi_tau_Y_b_sectoral_c2_sut_matrix.csv
Sigma_tau_Y_sectoral_c2_sut_annual_matrix.csv
```

But this does not yet make the runtime calibration sectoral. The sectoral audit
file says the layer is not a runtime patch, and `src/calibration.jl` still uses
the aggregate C2 vectors repeated across sectors.

Adversarial conclusion: the previous "not sectoral" criticism should be
narrowed. It is no longer true of the new candidate dataset. It remains true of
the live runtime calibration.

#### 8a. Sectoral C2-SUT improves the data layer but introduces new risks

Severity: high for runtime use; medium for documentation.

The new builder:

```text
MCMS-private/scripts/build_fiscal_rule_dataset_sectoral_c2_sut.py
```

uses BEA `SUPPLY-USE.zip`, `Use_Summary.xlsx`, and constructs:

```text
C2_SUT_wedge =
    Other taxes on production
    - Other subsidies on production
    - Subsidies on products
```

divided by total industry output at basic prices, while excluding:

```text
Taxes on products and imports
```

The generated audit reports full coverage:

```text
US sectoral rules estimated: 44 of 44
country-sector coefficient rows: 176
```

This is a useful improvement because product taxes and import duties are no
longer removed by a proportional gross-output allocation. However, the candidate
layer is much more volatile than aggregate C2:

```text
Rho_tau_Y:     0.161373 to 0.838042
Phi_tau_Y_y:  -0.272646 to 0.007139
Phi_tau_Y_b:  -0.570264 to 0.169720
Sigma_tau_Y:   0.000234 to 0.054585
```

The most extreme debt-feedback entries are concentrated in sectors such as air
transport and accommodation/food services after country scaling. Given that the
aggregate unshrunk C2 debt feedback already fails BK, the sectoral matrix cannot
be patched into runtime without shrinkage/sign restrictions and full
determinacy/debt-IRF tests.

Additional caveats:

1. The sectoral dataset still inherits the aggregate C2 country-scaling inputs,
   including the possible EA double-scaling issue.
2. China and ROW remain transfer/fallback calibrations, not direct sectoral
   country estimates.
3. BEA summary mappings do not perfectly match the 44 model sectors. Chemicals
   and pharmaceuticals both use BEA `325`; several services sectors use bundled
   or proxy BEA categories.
4. Product subsidies remain inside the wedge as negative subsidies. This may be
   intentional, but it should be justified because product subsidies are not the
   same fiscal object as other taxes/subsidies on production.
5. The coefficients are annual and still need a model-frequency decision.

#### 9. China and ROW production calibration is transferred, not estimated

Severity: high.

USA uses BEA C2 and EA uses Eurostat D29. China and ROW use broad-fiscal
absolute fallback intensities and inherit the U.S. sign. ROW is also the world
aggregate proxy, not residual ROW after removing EA, China, and USA.

Adversarial conclusion: China and ROW C2 values should be treated as scenario
parameters or shrinkage priors, not empirical production-tax estimates.

#### 10. Paper and Dynare artifacts are stale relative to the Julia runtime

Severity: high.

`Fiscal-LPT/main.tex` still reports older production-rule table values:

```text
rho^Y_k = [0.80, 0.70, 0.75, 0.80]
phi^Y_y = [0.02, 0.03, 0.02, 0.01]
phi^Y_b = [0.015, 0.020, 0.015, 0.010]
```

The live Julia runtime uses C2 values instead. The legacy Dynare declaration
file `MCMS-private/b3_declare_par_fiscal_lpt.mod` still contains placeholders:

```text
Tbar_C = 0.20
Tbar_N = 0.30
bgov_ss = 0.60
rho_tau_Y = 0.80
phi_tau_Y_y = 0.05
phi_tau_Y_b = 0.00
sigma_tau_Y = 0.01
```

Adversarial conclusion: the documentation/runtime state is not clean enough for
editorial review. The paper, Julia runtime, generated calibration artifacts, and
Dynare mirror should either be synchronized or explicitly scoped as different
objects.

### LPT consistency verdict

The repository implements an LPT-style fiscal-rule closure, not an LPT
calibration. The gap is structural:

1. LPT estimates fiscal rules jointly inside a DSGE model.
2. LPT uses U.S. quarterly observables and a Bayesian posterior.
3. This repository uses annual reduced-form OLS and transfer/scaling rules.
4. The generated coefficients are not estimated jointly with the private-sector
   model or the fiscal budget block.
5. The current C2 baseline fails BK, so it is not even a solved DSGE baseline.

Permissible claim:

```text
The fiscal block follows an LPT-style debt-feedback closure.
```

Impermissible claim:

```text
The fiscal rule coefficients are LPT-estimated or LPT-consistent estimates.
```

### Main points an editor would still make

1. The proposed baseline fiscal calibration does not solve the model. Show a BK
   pass and bounded debt IRFs before reporting quantitative results.
2. The calibration is not LPT estimation. The paper must stop implying a
   structural posterior-backed calibration unless that estimation is actually
   implemented.
3. The runtime production-subsidy calibration is not sectoral. A sectoral
   C2-SUT candidate now exists, but it is not runtime-integrated or
   stability-tested.
4. The production-wedge steady state is a markup-offsetting model normalization,
   not observed subsidy policy.
5. The annual fiscal-rule estimates are not consistently converted to the model
   period.
6. EA C2 appears to combine a direct D29 regression with an additional
   tax-margin scale. This may double-scale both the aggregate and sectoral EA
   production rules.
7. China and ROW production-rule values are transferred fallback parameters, not
   direct evidence.
8. Labour-tax calibration is weak because the proxy is broad income/social
   revenue rather than a labour wedge.
9. The generated calibration tables are not loaded by runtime, so the workflow
   is not reproducible enough.
10. The paper and Dynare mirror are stale relative to the Julia runtime.

### Required fixes before baseline use

1. Decide the baseline: either remove C2 from runtime and keep it as a
   sensitivity, or make C2 solve the model.
2. Fix or justify the EA C2 double-scaling issue.
3. Convert annual rule objects to the model frequency or declare the model
   annual and adjust all other timing accordingly.
4. Replace destabilizing production-wedge debt feedback with a theoretically
   disciplined closure: sign restriction, shrinkage prior, zero production-debt
   feedback, or a separate stabilizing fiscal instrument.
5. Test the sectoral C2-SUT matrices separately before any runtime patch. Do not
   infer validity from aggregate C2 diagnostics.
6. Make generated calibration artifacts authoritative for runtime.
7. Update `Fiscal-LPT/main.tex` and the Dynare mirror, or explicitly mark them
   as stale/non-runtime.
8. Re-run parser/Jacobian, equation-count, BK, state-transition eigenvalue, and
   debt-IRF checks after every calibration change.

## Scores

| Reviewer | Score | Verdict |
| --- | ---: | --- |
| Theory critic | 70/100 | Strong audit note, not yet a defensible calibration argument. |
| Coding check agent | 70/100 | Source files and schemas are coherent, but empirical outputs are not model-ready. |
| Coordinator synthesis | 70/100 | Useful documentation, but the dynamic calibration interface is not safe to patch into runtime without normalization fixes. |

## Stop rule used

The review stops only after:

1. Both requested reviewers finish independent reviews.
2. The coordinator checks whether their findings conflict or converge.
3. High-severity issues are mapped to exact document/code locations.
4. A final verdict distinguishes usable content from content that must not be used as runtime calibration.

This stop rule was met. The two reviewers strongly converged on the same core issue: the empirical fiscal-rule regressions in `full.md` are not normalized into the implemented Julia fiscal-rule form.

## Highest-severity findings

### 1. The dynamic rule coefficients are not directly compatible with the Julia model

Severity: high.

`full.md` describes reduced-form estimates of the form:

```text
tau_t = const + rho tau_{t-1} + phi_y output_gap_t + phi_b debt_gdp_{t-1} + residual_t
```

This appears in `full.md` around the reduced-form estimation section and is implemented in `MCMS-private/scripts/build_fiscal_rule_dataset.py`.

The Julia model rule instead uses:

```text
tau_t = rho tau_{t-1} + (1-rho) * (Phi_y y_t + Phi_b bgov_{t-1}) + Sigma eps_t
```

This is the form generated in `MCMS-private/src/build_equations.jl`.

Therefore, the regression coefficient `phi_y` is not generally equal to the model parameter `Phi_y`; the corresponding model object is:

```text
Phi_y = phi_y / (1-rho)
Phi_b = phi_b / (1-rho)
```

unless the regression is re-estimated in the same normalized form as the model.

Impact: any direct patch from `fiscal_rule_estimates.csv` or `benchmark_b_rule_estimates.csv` into `Phi_tau_*` would understate the implemented output/debt response by a factor of `(1-rho)`. This is especially severe when `rho` is close to one. The code critic flagged Benchmark B USA VAT as an example: with `rho = 0.9755`, a debt coefficient of about `0.0003146` would be implemented as roughly `0.0000077` if pasted directly.

Required fix before model use:

- Either estimate the empirical equation in the model-normalized form, or
- Add transformed columns such as `Phi_model_y = phi_y / (1-rho)` and `Phi_model_b = phi_b / (1-rho)`, plus explicit handling when `rho` is close to one.

### 2. The estimated variables are observed tax-rate proxies, while the model uses fiscal wedge deviations

Severity: high.

`full.md` correctly states that the model objects `tau_C`, `tau_N`, and `tau_Y` are wedge deviations, but the empirical builders estimate rules on observed effective tax rates or revenue-share proxies:

- consumption tax: goods/services tax revenue divided by household consumption;
- income/labour proxy: income tax plus social contributions as a GDP share;
- production proxy: net product taxes or subsidies/transfers as GDP shares.

These are not automatically in the same units as the model states.

For model use, the transformation should be explicit. At minimum:

- consumption taxes should be mapped to gross consumption wedge deviations, for example deviations in `log(1 + T_C)`;
- labour taxes need the model's inverse after-tax labour wedge convention, not just an income/social revenue share;
- production taxes need a marginal-cost wedge consistent with `1 + Tbar_Y`, not an aggregate production/import tax share of GDP;
- shock standard deviations must be transformed into the same units as the model wedge variable.

Impact: even if the `(1-rho)` normalization is fixed, the coefficients and residual standard deviations are still mis-scaled unless the observed tax variables are converted into model-state units.

Required fix before model use:

- Add a section in `full.md` that derives the empirical-to-model transformation for each fiscal object.
- Add transformed model-ready columns to the generated CSVs instead of treating the raw regression coefficients as final candidates.

### 3. The intercept and steady-state mapping are under-specified

Severity: high.

The OLS regressions include a constant, while the Julia fiscal rules are written as deviations around steady state with no intercept. `full.md` does not yet fully explain how the empirical intercept is absorbed into the steady-state tax object or removed by demeaning.

This matters because the regression is estimated in observed levels/proxies, while the model equation is a deviation equation. A valid bridge must specify whether:

- the regression should be estimated on deviations from the recommended `Tbar_*`;
- the intercept should be discarded after centering;
- the intercept is used to back out a steady-state level; or
- a different empirical specification should be used.

Impact: without this mapping, `rho`, `phi_y`, `phi_b`, and `sigma` are not guaranteed to describe the same state variable that the model evolves.

Required fix before model use:

- Define the centering convention.
- Show the algebra from the level regression to the deviation-form fiscal rule.
- Recompute or transform the reported coefficients accordingly.

### 4. Benchmark B weakens the original uniform-source standard

Severity: medium-high.

The request recorded in `full.md` emphasizes uniform sources for country-varying parameters. Benchmark A follows that logic more closely by relying on WDI/IMF style cross-country coverage. Benchmark B instead uses:

- Eurostat for EA;
- OECD for USA;
- WDI/IMF fallback for China and ROW.

That may be economically preferable for some objects, but it is not the same source discipline. The current phrasing that Benchmark B is "not less disciplined" is too strong unless the document defines a hierarchy where concept fit dominates source uniformity and then validates cross-source comparability.

Impact: Benchmark B may improve concept fit for EA/USA taxes while reducing cross-country comparability. That tradeoff should be made explicit rather than presented as unambiguously superior.

Required fix:

- Label Benchmark A as the uniform-source benchmark.
- Label Benchmark B as the concept-priority benchmark.
- Add a short decision rule for when each should be used.

### 5. `Tbar_N_proxy` is not a clean labour-tax wedge

Severity: medium-high.

The document is appropriately cautious, but it still leaves open a path where `Tbar_N_proxy` may be used as a provisional `Tbar_N`. This is economically fragile.

The proxy mixes income taxes and social contributions and can include taxes on labour, profits, capital income, and other bases. The model's labour wedge enters wage setting and fiscal revenue through a specific after-tax labour wedge convention. A GDP-share tax revenue measure is not directly that wedge.

Impact: using `Tbar_N_proxy` as a labour tax can distort labour supply/wage dynamics and government revenue feedbacks.

Required fix:

- Do not label `Tbar_N_proxy` as model-ready.
- If it is used, call it an income/social revenue proxy.
- Prefer a compensation-of-employees denominator or an explicit labour-tax wedge source before mapping into `Tbar_N`.

### 6. Production-tax/subsidy calibration remains scenario-only

Severity: medium-high.

`full.md` is strongest where it says production subsidies are not identified. That statement should be even sharper.

Benchmark B adds an EA aggregate `D2` production/import tax estimate, but the runtime object is a sector-country marginal-cost wedge. The EA aggregate is not sectoral, not cleanly net of subsidies in the required model sense, and not mapped to the model's sectoral base.

Impact: production-tax results should not be described as calibrated from the generated datasets. They are scenario or sensitivity parameters unless a sectoral source and mapping are added.

Required fix:

- Replace phrases like "clean EA production-tax estimate" with "aggregate EA production/import tax proxy."
- State that `Tbar_Y`, `Rho_tau_Y`, `Phi_tau_Y_*`, and `Sigma_tau_Y` remain scenario parameters unless a sectoral data source is introduced.

### 7. ROW is not a residual ROW

Severity: medium.

`full.md` flags this limitation, but it should be elevated in the decision summary. The ROW series use world aggregates such as WLD/WEOWORLD, not aggregates excluding EA, China, and USA.

Impact: if the model contains EA, China, USA, and ROW separately, then world aggregates contaminate ROW with the countries already represented as separate blocks. This can affect both steady-state tax/debt levels and fiscal feedback estimates.

Required fix:

- Do not treat ROW estimates as a clean calibration for the residual model block.
- Build residual ROW where possible, or label ROW as a world-proxy sensitivity.

## Medium-severity findings

### 8. Annual-to-model-frequency conversion is unresolved

`full.md` correctly flags annual frequency, but the mapping section still reads as though annual coefficients can be used directly. If the model is quarterly, persistence, feedback, and shock scale all need frequency treatment.

Required fix:

- Add a frequency-conversion table before any model-use recommendation.
- Convert `rho` explicitly.
- State how `Sigma` scales across frequencies.
- Clarify whether output and debt feedback coefficients are annual-response coefficients or per-period model coefficients.

### 9. The output gap is a fragile linear-trend residual

The builders use log real GDP residualized on a linear time trend over the available sample. This is transparent but fragile. Crises, post-2020 observations, and country-specific trend breaks can materially alter `phi_y`.

Required fix:

- Add at least one robustness gap measure before treating `phi_y` as a candidate policy coefficient.
- At minimum, report whether coefficient signs and magnitudes survive an alternative detrending method or a restricted sample.

### 10. Benchmark B is not fully standalone reproducible from its output directory

Benchmark B writes Eurostat/OECD raw files, but it refetches WDI/IMF components through Benchmark A logic and does not store every raw input in the Benchmark B output directory. It also lacks package versions and complete request metadata.

Impact: reruns can drift if APIs revise data or change availability.

Required fix:

- Save raw WDI and IMF inputs used by Benchmark B into the Benchmark B artifact directory, or include hashes/paths to the exact Benchmark A raw files used.
- Add package versions and request metadata.
- Add a Benchmark B command and output checklist to the reproducibility section.

### 11. Partial missing tax components can be treated as zero in Benchmark B

The Benchmark B script sums EA/USA income and social components using zero-fill logic when at least one component is present. The current generated artifacts may not exhibit partial missingness, but the code path would understate the combined proxy if one component disappears in a future API response.

Required fix:

- Require all intended components to be present, or
- Add an explicit `partial_source_flag` and exclude partial rows from estimation by default.

### 12. Generated datasets are not wired into the live Julia calibration

The generated CSVs are candidate calibration artifacts. The live Julia calibration still has hand-set fiscal values unless manually patched or connected through a loader.

Impact: any claim that the current model "uses" Benchmark A or Benchmark B is false until the runtime calibration is updated and verified.

Required fix:

- Keep wording as "candidate calibration recommendations" until code integration is done.
- If integrated, record the exact CSV row/source used for each patched parameter and rerun parser/BK/model checks.

## Things `full.md` does well

- It is unusually transparent about source limitations.
- It separates Benchmark A and Benchmark B rather than hiding source heterogeneity.
- It correctly warns that production subsidies are not identified by the current public data.
- It records that reduced-form regressions are not structural fiscal rules.
- It gives reproducibility steps for the Benchmark A builder and documents the generated artifact schema.

These strengths should be preserved. The main required change is not to make the document less cautious; it is to move the most important caution into the model-use recommendation and to add the missing algebra between empirical proxies and model states.

## Required changes before using the estimates in the model

1. Add a model-normalized fiscal-rule mapping:

```text
Empirical: tau_t = a + rho tau_{t-1} + beta_y y_t + beta_b b_{t-1} + u_t
Model:     tau_t = rho tau_{t-1} + (1-rho)(Phi_y y_t + Phi_b b_{t-1}) + Sigma eps_t

Therefore:
Phi_y = beta_y / (1-rho)
Phi_b = beta_b / (1-rho)
```

2. Define the tax-wedge transformation for `tau_C`, `tau_N`, and `tau_Y`.

3. Explain how the intercept is removed or absorbed into steady-state tax levels.

4. Add frequency conversion if the runtime model is not annual.

5. Downgrade dynamic coefficients from "usable" to "candidate, unverified, not runtime-ready."

6. Keep production-tax and ROW estimates out of baseline calibration unless stronger data are added.

7. Add Benchmark B reproducibility commands and raw-input provenance.

8. Add a statement that the generated CSVs are not yet wired into the live Julia calibration.

## Suggested replacement decision summary for `full.md`

The generated datasets are useful audit and candidate-calibration artifacts, but they should not be patched directly into the runtime fiscal rules. Consumption-tax steady-state recommendations are the strongest objects, especially under Benchmark B for EA/USA and Benchmark A for uniform-source comparison. Dynamic rule estimates require a transformation from the estimated reduced-form equation into the model's `(1-rho) * Phi` fiscal-rule normalization, conversion from observed tax-rate proxies into model wedge deviations, and a clear treatment of intercepts and frequency. Labour-tax estimates are income/social revenue proxies, not clean labour wedges. Production-tax estimates remain aggregate or missing and should be treated as scenario parameters, not calibrated sectoral production subsidies. ROW estimates are world-proxy estimates, not residual-ROW calibrations.

## Final verdict

`full.md` is a strong source audit and a useful calibration dossier, but it is not yet a safe model-calibration bridge. The document should be accepted as documentation of candidate data construction and rejected as a direct instruction to patch dynamic fiscal-rule parameters into the Julia model.

The critical correction is the last-mile mapping:

```text
Do not use raw phi_y, phi_b, and sigma_resid directly as model parameters.
First transform the empirical tax proxies into model wedge deviations.
Then convert reduced-form beta coefficients into model Phi coefficients using the implemented fiscal-rule normalization.
Then run determinacy and fiscal-stability checks.
```

## Rereview status, May 13, 2026

The revised `full.md`, `adversarial_review_response.md`, builder scripts, and generated artifacts substantially address the original high-severity review findings.

Verified in the current checkout:

1. `full.md` now states that Benchmark A is the uniform-source benchmark and Benchmark B is the concept-priority benchmark.
2. `full.md` now explicitly says the generated datasets are audit and candidate-calibration artifacts, not direct runtime patches.
3. `full.md` now gives the implemented Julia fiscal-rule normalization:

```text
tau = rho tau(-1) + (1-rho) * (Phi_y y + Phi_b bgov(-1)) + Sigma eps
```

and the associated empirical-to-model scaling:

```text
Phi_y = phi_y / (1-rho)
Phi_b = phi_b / (1-rho)
```

4. `MCMS-private/scripts/build_fiscal_rule_dataset.py` now creates `_model_dev` variables, lagged `bgov_dev_for_regression`, `phi_y_model_rule_scale`, `phi_b_model_rule_scale`, quarterly approximation columns, and `near_unit_rho_flag`.
5. `MCMS-private/scripts/build_fiscal_rule_dataset_benchmark_b.py` uses the same model-deviation and model-rule-scale machinery for Benchmark B.
6. Benchmark B now writes `raw_wdi_long.csv` and `raw_imf_debt.csv` into `MCMS-private/input_data/fiscal_rules_benchmark_b`.
7. Benchmark B metadata now records Python, NumPy, and pandas versions.
8. Benchmark B now adds `benchmark_b_income_partial_source_flag` and requires both income and social-contribution components to be present before forming the income-plus-social proxy.
9. The live Julia calibration was not patched with the empirical coefficients; instead, `MCMS-private/src/calibration.jl` now contains a guard comment warning that raw annual fiscal-rule estimates are not runtime `Phi_tau_*` parameters.
10. A syntax-only AST parse of both Python builders passed under `python -B`.

Updated assessment:

The original blockers about direct coefficient copying, missing wedge transformations, intercept treatment, Benchmark B reproducibility, partial missing component handling, and runtime overclaiming are addressed well enough for the document to be treated as a satisfactory audit and bridge-layer note.

Remaining caveats:

1. The `_model_dev` rows are approximate bridge objects, not validated structural estimates.
2. The labour/income proxy is still not a clean labour wedge, even after applying the inverse-after-tax transformation.
3. The production-tax objects remain aggregate proxies and should stay out of baseline sectoral production-subsidy calibration.
4. ROW remains a world proxy, not residual ROW.
5. The quarterly conversion columns are approximations and should not replace an explicit model-frequency decision.
6. No determinacy, fiscal-stability, or output-gap robustness check has been verified in this rereview.

Rereview verdict:

The changes are satisfactory for documentation, auditability, and generating model-bridge candidate artifacts. They are not sufficient to justify using the generated dynamic fiscal-rule estimates as baseline runtime calibration without the remaining model-solution and stability checks.

## C2 adversarial rereview, May 13, 2026

Targeted files:

- `MCMS-private/scripts/build_fiscal_rule_dataset_calibration_c2.py`
- `MCMS-private/input_data/fiscal_rules_calibration_c2/*`
- `MCMS-private/src/calibration.jl`
- `claude-code-my-workflow/docs/model specifics/full.md`

Rereview scope: Calibration C2, the new BEA non-product production-wedge calibration.

Verdict: C2 is a useful candidate-data layer, but the current runtime patch is not satisfactory. The construction has several high-risk source, scaling, and model-normalization problems that should be fixed or explicitly downgraded before it is treated as the operative production-wedge calibration.

Score:

| Object reviewed | Score | Verdict |
| --- | ---: | --- |
| C2 as a documented exploratory dataset | 62/100 | Useful, but source and scaling caveats need sharpening. |
| C2 as live `calibration.jl` runtime parameters | 35/100 | Not safe yet; too many unverified mapping and stability risks. |

### C2-1. The live runtime was patched despite the audit text calling C2 candidate-only

Severity: high.

`calibration.jl` now uses C2 values directly:

```text
rho_tau_Y_by_country = [0.6063427366945628, 0.383422316920768, 0.4471993516863576, 0.4703507053697966]
phi_tau_Y_y_by_country = [-0.008948991420986046, -0.015008204525235082, -0.0007943750736267994, -0.020005570704752423]
phi_tau_Y_b_by_country = [-0.01521979664503376, -0.025802037961408814, -0.026046818710710948, -0.009380640004393774]
sigma_tau_Y_by_country = [0.006230220486877279, 0.005001150526126388, 0.0028630652194631496, 0.003642304851797515]
```

But the C2 audit file says these are annual candidate coefficients and "not runtime-patched parameters." `full.md` also says C2 remains annual, reduced-form, and not patched into `src/calibration.jl`.

This is now internally inconsistent. Either the documentation is stale, or the runtime patch happened before the required stress tests.

Required correction:

- If C2 is only exploratory, revert `Phi_tau_Y_*`, `Rho_tau_Y`, and `Sigma_tau_Y` in `calibration.jl` to the previous scenario/common-rule values and keep C2 in CSV form.
- If C2 is intended to be runtime baseline, update `full.md` and `calibration_c2_audit.md` to say it is patched, then run and record model parser, equation-count, determinacy, and debt-IRF checks.

### C2-2. C2 probably does not subtract all product taxes

Severity: high.

`build_fiscal_rule_dataset_calibration_c2.py` subtracts:

```text
BEA/NIPA-T30500/LA000236-A
```

and labels it as all "taxes on product." The C2 documentation says this removes customs duties, sales taxes, excise taxes, and other product taxes.

That claim is likely too broad. The source is NIPA Table 3.5 line 3, "Taxes on product," which sits inside the federal block. The table separately lists state/local product taxes, including sales taxes on line 20 and state/local general sales taxes on lines 21 and 22. Therefore subtracting only line 3 does not remove the full product-tax component from aggregate TOPI.

Direct symptom in the generated data: for 2023, C2 subtracts `175.413` billion dollars as product taxes, while the same NIPA table reports state general sales taxes alone at `456.123` billion and local general sales taxes at `137.827` billion in DB.Nomics' table view. That makes it implausible that the C2 series has removed all product taxes or all consumption-tax overlap.

Required correction:

- Replace the current product-tax subtraction with a full product-tax aggregate: federal line 3 plus state/local line 19, or a correctly identified total product-tax series if BEA exposes one.
- At minimum, rename the current variable to `federal_product_taxes_share_go` and stop claiming that it removes state/local sales taxes.
- Recompute C2 after the source correction.

Relevant external checks:

- BEA/FRED Table 3.5 shows line 3 under the federal block and state/local product taxes separately under line 19 and sales taxes under line 20.
- BEA explains that customs duties are a detailed component of NIPA TOPI and are reported in Table 3.5.

### C2-3. EA tax-margin scaling mixes GDP and gross-output denominators

Severity: high.

C2 defines the U.S. margin as:

```text
US non-product production wedge / US gross output
```

but defines the EA margin as:

```text
Eurostat D29 other taxes on production / EA GDP
```

The C2 tax-margin scale is then:

```text
abs(EA D29/GDP) / abs(US C2 wedge/gross output)
```

This mixes denominators. Since gross output is materially larger than GDP, the resulting EA scale is not a clean relative tax-margin intensity. The current EA scale is `0.797142585094`, but that value may be substantially overstated or understated depending on whether the model wedge should be normalized by gross output, value added, or the model's `S_MCY` base.

Required correction:

- Put both countries on the same denominator before taking ratios.
- Preferred: convert EA D29 to a gross-output denominator if the production wedge is a marginal-cost/gross-output object.
- Alternative: convert the U.S. C2 wedge to a GDP denominator if the intended country-margin scale is fiscal revenue over GDP.
- Document the chosen denominator and recompute `tax_margin_scale`.

### C2-4. Country-specific `rho` is blended, but `Phi` is scaled from the U.S. model-scale coefficient

Severity: high.

C2 estimates U.S. reduced-form coefficients and computes:

```text
Phi_US = beta_US / (1 - rho_US)
```

Then for non-U.S. countries it changes `rho` by averaging U.S. rho with a country fiscal proxy, but it keeps `Phi` equal to the scaled U.S. `Phi`. That means the actual reduced-form impact in the Julia equation becomes:

```text
beta_country_implemented = (1 - rho_country) * Phi_country
```

not the scaled U.S. beta unless `rho_country = rho_US`.

The current implemented beta distortions are:

| Country | rho | `(1-rho)/(1-rho_US)` | implemented beta-y |
| --- | ---: | ---: | ---: |
| EA | 0.606343 | 0.743241 | -0.003523 |
| China | 0.383422 | 1.164124 | -0.009254 |
| ROW | 0.447199 | 1.043711 | -0.000439 |
| USA | 0.470351 | 1.000000 | -0.010596 |

This may be intentional if C2 wants to scale long-run target `Phi` rather than reduced-form response `beta`, but the document does not state that choice. Given the previous review focused on exactly this normalization issue, this ambiguity is too risky.

Required correction:

- Decide whether the scaling transfers `beta` or `Phi`.
- If transferring empirical reduced-form responses, compute country `Phi` as:

```text
Phi_country = beta_country_scaled / (1 - rho_country)
```

- If transferring long-run target responsiveness, explicitly say so and show why the implied country betas are acceptable.

### C2-5. The fiscal-responsiveness scaling loses signs and reuses product-tax proxies

Severity: medium-high.

The helper `fiscal_proxy` returns absolute values for production and broad fiscal proxies. C2 then applies the sign of the U.S. C2 estimate to every country. This forces all country `Phi_tau_Y_y` and `Phi_tau_Y_b` values to be negative.

That is not innocuous:

- Benchmark B EA net-production model-dev coefficients are positive, but C2 turns the EA production-wedge response negative.
- China and ROW have no production estimate, so their fallback responsiveness comes from VAT/income-social rows, then inherits the U.S. C2 sign.
- The debt-feedback vector is negative for every country, which is not obviously debt-stabilizing in the government budget.

The source mix is also conceptually weak. C2 is designed to remove product-tax overlap, but its EA/USA fiscal-responsiveness ratios use Benchmark B `net_production_tax_proxy` rows, which are built from broader production/product tax proxies rather than the C2 non-product object. For China and ROW, the fallback uses VAT/income-social dynamics, which are not production-wedge dynamics.

Required correction:

- Preserve signs unless there is a theory-based reason to use absolute intensity only.
- Add columns showing both signed and absolute scaling.
- Do not use VAT/income-social dynamics as a silent production-wedge fallback; label them as a separate sensitivity.
- Re-estimate an EA D29 model-dev rule directly if EA D29 is the C2 margin source.

### C2-6. The C2 runtime patch repeats an aggregate all-industries rule across all sectors

Severity: medium-high.

The U.S. source is an all-industries aggregate. The runtime repeats the same country coefficient across every sector:

```text
Rho_tau_Y = repeat(rho_tau_Y_by_country, 1, Inum)
Phi_tau_Y_y = repeat(phi_tau_Y_y_by_country, 1, Inum)
Phi_tau_Y_b = repeat(phi_tau_Y_b_by_country, 1, Inum)
Sigma_tau_Y = repeat(sigma_tau_Y_by_country, 1, Inum)
```

This is documented, but it matters more now that the coefficients are live. In the model, `tau_Y_{k,i}` enters sector-level marginal costs and revenues. A repeated aggregate shock/rule across 44 sectors is not a sectoral calibration.

Required correction:

- Treat C2 as a country-level aggregate sensitivity unless a sector allocation is added.
- If kept in runtime, consider using a single aggregate production-wedge shock rather than sector-specific duplicated shocks, or explicitly justify the duplicated sector shocks.

### C2-7. `Tbar_Y` remains markup-implied while C2 dynamics are estimated around a different steady state

Severity: medium.

C2 estimates `tau_Y_us_bea_c2_model_dev` around a latest-five U.S. non-product wedge of about `0.0275986`. The runtime steady state remains:

```text
Tbar_Y = 1.0 ./ M .- 1.0
```

That is a model-implied markup-offsetting object, not the BEA C2 non-product tax margin. The dynamic coefficients are in log gross-wedge units, so this is not automatically fatal, but the local linearization point is different from the empirical centering point.

Required correction:

- Either keep C2 as dynamic-only and explicitly justify why the empirical centering does not affect the dynamic mapping, or
- Provide a C2-consistent `Tbar_Y` sensitivity, clearly separated from the markup-offsetting baseline.

### C2-8. No model-solution verification was found

Severity: medium.

I verified that the C2 Python script parses with `python -B` and that the generated CSV values match the values patched into `calibration.jl`. I did not find evidence that the C2-patched Julia model has passed:

- parser success after regenerating equations,
- equation/variable count consistency,
- Blanchard-Kahn determinacy,
- bounded debt IRFs,
- shock-scale sanity checks at the model frequency.

Given the negative debt-feedback coefficients now in runtime, this is not optional.

Required correction:

- Run the model with the C2 runtime patch and record the checks in `full.md` and this review file.
- If checks fail, remove C2 from runtime and keep it as an external candidate dataset.

### C2 rereview bottom line

C2 is directionally useful because it tries to remove tariff and consumption-tax overlap from the production-wedge proxy. However, the current implementation should not be accepted as final runtime calibration.

The most urgent fixes are:

1. Correct the BEA product-tax subtraction; the current line appears to omit state/local product taxes.
2. Put U.S. and EA tax-margin scales on the same denominator.
3. Decide whether C2 transfers reduced-form `beta` or model `Phi` when country-specific `rho` changes.
4. Stop silently losing fiscal-response signs through absolute-value scaling.
5. Reconcile the documentation with the fact that C2 is now patched into `calibration.jl`.
6. Run model determinacy and debt-stability checks before calling C2 a baseline.

Until those are done, C2 should be described as a candidate sensitivity layer, not as the new accepted calibration.

## Pre-C2 implementation status, May 13, 2026

The core review findings from the Benchmark A/B bridge-layer review had been addressed in code and documentation before the later C2 runtime patch.

Accepted and patched:

1. `MCMS-private/scripts/build_fiscal_rule_dataset.py` and `MCMS-private/scripts/build_fiscal_rule_dataset_benchmark_b.py` now emit `phi_y_model_rule_scale = phi_y / (1-rho)` and `phi_b_model_rule_scale = phi_b / (1-rho)`.
2. Both builders now emit `_model_dev` dependent-variable rows using approximate model-state transformations, lagged `bgov_dev_for_regression`, and no intercept.
3. Benchmark B now writes `raw_wdi_long.csv` and `raw_imf_debt.csv` into its own output directory and records Python, NumPy, and pandas versions in `metadata.json`.
4. Benchmark B no longer zero-fills a missing income/social component; both components must be present, and `benchmark_b_income_partial_source_flag` records partial-source rows.
5. `full.md` now labels Benchmark A as the uniform-source benchmark and Benchmark B as the concept-priority benchmark.
6. `full.md` now says dynamic estimates are candidate annual model-deviation estimates, not automatic runtime replacements.
7. `MCMS-private/src/calibration.jl` now has a guard comment warning that raw annual fiscal-rule estimates are not runtime `Phi_tau_*` parameters.

Rejected:

1. At this pre-C2 point, the generated Benchmark A/B coefficients were not patched into `src/calibration.jl`, because the review correctly said they were not runtime-ready without frequency conversion and model stability checks.
2. `Tbar_N_proxy` was not promoted to baseline `Tbar_N`.
3. Aggregate production-tax proxies were not promoted to sectoral production-subsidy calibration.
4. ROW was not relabeled as residual ROW.

The detailed response is recorded in:

```text
claude-code-my-workflow/docs/model specifics/adversarial_review_response.md
```

Current status after the C2 update: this pre-C2 statement no longer applies to production-wedge dynamics. `src/calibration.jl` now contains C2 production-wedge rule coefficients, and the C2 rereview above treats that runtime patch as unsafe until the product-tax source, denominator scaling, rho/Phi mapping, sign handling, and model-solution checks are corrected.

## C2 response rereview, May 13, 2026

The response in `adversarial_review_response.md` materially addresses the C2 adversarial review. The implementation is now satisfactory as an experimental runtime bridge, but not yet as a final DSGE/LPT-style calibrated production-rule block.

Verified fixes:

1. Product-tax subtraction now uses both BEA/DB.Nomics NIPA Table 3.5 series:

```text
LA000236-A federal taxes on product
LA000238-A state/local taxes on product
```

The generated raw C2 file now contains:

```text
federal_taxes_on_product_millions_current_usd
state_local_taxes_on_product_millions_current_usd
taxes_on_product_total_millions_current_usd
taxes_on_product_total_share_go
topi_less_subsidies_less_total_product_taxes_share_go
```

2. EA scaling now uses a consistent GDP denominator:

```text
EA scale = abs(EA D29 / GDP) / abs(US C2 non-product wedge / GDP)
```

The generated EA tax-margin scale is now `1.3510766540111345`.

3. C2 now transfers reduced-form annual betas before computing country-specific `Phi`:

```text
beta_country = beta_US * tax_margin_scale * fiscal_responsiveness_scale
Phi_country = beta_country / (1 - rho_country)
```

The output CSV now contains both:

```text
Beta_tau_Y_y_calibration_c2
Beta_tau_Y_b_calibration_c2
Phi_tau_Y_y_calibration_c2
Phi_tau_Y_b_calibration_c2
```

4. EA now uses a direct Eurostat D29 model-deviation estimate rather than a Benchmark B product-tax proxy for the C2 response scale.

5. China and ROW still use broad-fiscal absolute fallback intensities, but this is now explicitly flagged with:

```text
fiscal_proxy_type = broad_fiscal_abs_fallback
fallback_flag = True
sign_policy = inherits US sign under absolute fallback
```

6. `calibration.jl` now accurately documents that C2 is a runtime production-wedge bridge, repeated across sectors, while `Tbar_Y` remains the markup-implied steady state.

7. The generated C2 vectors in `calibration_c2_scaled_tau_y_coefficients.csv` match the live vectors in `MCMS-private/src/calibration.jl`.

8. `build_fiscal_rule_dataset_calibration_c2.py` passes a syntax-only AST check with `python -B`.

Updated C2 assessment:

The previous high-severity source, denominator, beta/Phi, and documentation inconsistencies are addressed. The response is technically coherent enough to keep C2 in `calibration.jl` as an explicitly experimental annual production-wedge rule.

Remaining blockers before calling it final:

1. Full parser/Jacobian now passes, but Blanchard-Kahn determinacy fails by two stable eigenvalues in the no-timeout full run.
2. Annual-to-quarterly frequency conversion remains unresolved.
3. China and ROW remain transfer/fallback calibrations, not direct production-tax evidence.
4. The rule is still aggregate country-level evidence repeated across sectors, not sectoral production-subsidy calibration.
5. The workflow is still LPT-style, not LPT-estimated, because the coefficients are not estimated jointly inside a DSGE posterior.

Rereview verdict:

Satisfactory for an experimental C2 runtime bridge. Not satisfactory for a final baseline calibration claim until the model-solution and frequency checks pass.

## C2 rereview implementation status, May 13, 2026

Accepted and patched:

1. Product-tax subtraction now uses both BEA NIPA-T30500 `LA000236-A` federal taxes on product and `LA000238-A` state/local taxes on product.
2. EA tax-margin scaling now compares Eurostat D29 over GDP with the U.S. C2 wedge converted to a GDP denominator.
3. C2 now transfers reduced-form annual betas first and then computes `Phi = beta / (1-rho)` by country.
4. EA fiscal responsiveness now comes from a direct signed Eurostat D29 model-deviation rule estimate.
5. China and ROW fallback responsiveness is explicitly labeled as `broad_fiscal_abs_fallback`, with sign policy `inherits US sign under absolute fallback`.
6. `full.md`, `calibration_c2_audit.md`, and `adversarial_review_response.md` now state that C2 is integrated into the Julia runtime only for the dynamic production-wedge rule.
7. `src/calibration.jl` now documents that C2 is an aggregate country-level rule repeated across sectors and that `Tbar_Y` remains markup-implied.

Updated C2 runtime vectors, country order EA, China, ROW, USA:

```text
Rho_tau_Y = [0.5060925826316961, 0.3998557985336169, 0.4636328332992065, 0.5032176685954944]
Phi_tau_Y_y = [-0.004774805595688503, -0.03767679461158851, -0.0028017857032894967, -0.022357955888684028]
Phi_tau_Y_b = [0.009363564416125004, -0.04452161512787383, -0.05598147065548276, -0.01057010084983507]
Sigma_tau_Y = [0.001273423010466095, 0.005148906693406413, 0.002947652864104247, 0.003749914691204584]
```

Verification completed:

```text
python -B MCMS-private\scripts\build_fiscal_rule_dataset_calibration_c2.py
julia --project=. -e "include(\"src/calibration.jl\"); c=calibrate(); ..."
julia --project=. -e "include(\"src/solve_onkio.jl\"); ... equation count ..."
julia --project=. scripts/run_c2_full_model_check.jl
```

Results:

```text
C2 dataset regenerated successfully.
calibrate() completed and printed the integrated C2 vectors.
Equation count check completed: 6,762 equations, 6,762 variables, 448 shocks.
Full model run reached QZ and failed BK:
  stable eigenvalues = 1,883
  required stable eigenvalues = 1,885
```

Still not passed:

```text
Debt-IRF boundedness
Annual-to-quarterly frequency conversion
```

The no-timeout run shows that C2 is integrated because it was explicitly requested, but it is not a valid baseline under the current model solution: parser/Jacobian and static elimination pass, then QZ fails the BK count by two stable eigenvalues. No C2 IRFs were exported.

## C2 debt-feedback diagnostic status, May 13, 2026

The full C2 failure is not a generic parser or fiscal-block construction
failure. It is concentrated in the production-wedge debt feedback magnitudes.

Baseline C2 fails:

```text
Phi_tau_Y_b = [0.009363564416125004, -0.04452161512787383, -0.05598147065548276, -0.01057010084983507]
stable eigenvalues = 1,883
required stable eigenvalues = 1,885
```

These variants pass BK:

| Variant | `Phi_tau_Y_b` country vector | BK result |
| --- | --- | --- |
| zero all | `[0, 0, 0, 0]` | pass, 1,885 stable |
| clip negatives to zero | `[0.009363564416125004, 0, 0, 0]` | pass, 1,885 stable |
| absolute positives | `[0.009363564416125004, 0.04452161512787383, 0.05598147065548276, 0.01057010084983507]` | pass, 1,885 stable |
| negatives scaled by 1/3 | `[0.009363564416125004, -0.014840538375957942, -0.018660490218494252, -0.003523366949945023]` | pass, 1,885 stable |
| negatives scaled by 1/10 | `[0.009363564416125004, -0.004452161512787383, -0.005598147065548276, -0.001057010084983507]` | pass, 1,885 stable |

Therefore, the negative debt feedbacks are not mechanically impossible, but the
unshrunk C2 magnitudes are too destabilizing. The next calibration decision is
not whether C2 can enter the model at all, but whether the baseline should use
sign restrictions, shrinkage of negative production-wedge debt responses, or a
separate fiscal-stabilization instrument.
