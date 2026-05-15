# Agent plan: move Fiscal-MCMS calibration closer to LPT estimation

Date: 2026-05-13

Objective: replace the current calibration-only fiscal-rule workflow with a staged LPT-style estimation workflow, using the available annual public data while preserving clear boundaries between candidate data, estimated parameters, and runtime calibration.

## Operating rules

1. Work in `C:\CustomTools\MCMS_gvt`.
2. Keep documentation and review outputs for this task inside:

```text
claude-code-my-workflow/docs/model specifics
```

3. Do not treat generated estimates as baseline runtime calibration until model-solution checks pass.
4. Do not overwrite user changes or revert unrelated files.
5. Before changing `MCMS-private/src/calibration.jl`, produce a written patch plan and verify that the current C2 problems have been fixed.
6. All generated datasets must carry source metadata, formula definitions, package versions, and row-level status flags.

## Current problem

The existing workflow is LPT-style but not LPT-estimated.

LPT estimates fiscal policy rules inside a DSGE model using quarterly U.S. data and Bayesian estimation. The current Fiscal-MCMS workflow instead uses annual public fiscal data, reduced-form regressions, and transfer/scaling rules across countries. This is useful, but it should not be described as LPT posterior estimation.

The immediate target is to move from:

```text
annual OLS calibration artifacts
```

to:

```text
model-consistent transformed fiscal observables
+ exact model-form fiscal-rule estimation
+ Bayesian posterior estimates
+ model-solution validation
```

## Stage 0: repair C2 before further use

Files:

```text
MCMS-private/scripts/build_fiscal_rule_dataset_calibration_c2.py
MCMS-private/input_data/fiscal_rules_calibration_c2/*
MCMS-private/src/calibration.jl
claude-code-my-workflow/docs/model specifics/full.md
claude-code-my-workflow/docs/model specifics/full_adversarial_review.md
```

Tasks:

1. Fix the C2 product-tax subtraction.
   - Current code appears to subtract BEA NIPA Table 3.5 line 3 only.
   - Verify whether this is only federal product taxes.
   - If so, replace it with a full product-tax aggregate including state/local product taxes.
   - If a full aggregate cannot be built, rename the current object so it does not claim to remove all product taxes.

2. Fix denominator consistency.
   - Do not compare U.S. C2 wedge over gross output to EA D29 over GDP.
   - Put both on gross output or both on GDP before computing `tax_margin_scale`.

3. Fix the `rho`/`Phi` transfer rule.
   - Decide whether C2 transfers reduced-form `beta` or model target `Phi`.
   - If transferring reduced-form response:

```text
Phi_country = beta_country_scaled / (1 - rho_country)
```

   - If transferring `Phi`, explicitly document why the implied country-specific beta is intended.

4. Fix sign handling.
   - Stop silently converting fiscal-response proxies to absolute values.
   - Emit signed and absolute variants.
   - Make the chosen sign convention explicit.

5. Reconcile runtime status.
   - Either remove C2 from `calibration.jl` until checks pass, or clearly mark the runtime as experimental.
   - Update `full.md` and `full_adversarial_review.md` so they do not contradict the live code.

Acceptance criteria:

- C2 source formulas are source-accurate.
- U.S./EA scaling uses compatible denominators.
- Country coefficient construction identifies whether it transfers `beta` or `Phi`.
- `calibration.jl` status is consistent with the documentation.

## Stage 1: build model-consistent fiscal observables

Files:

```text
MCMS-private/scripts/build_fiscal_rule_dataset.py
MCMS-private/scripts/build_fiscal_rule_dataset_benchmark_b.py
MCMS-private/scripts/build_fiscal_rule_dataset_calibration_c2.py
```

Tasks:

1. Keep raw proxy rows, but make `_model_dev` rows the primary estimation rows.
2. Ensure every `_model_dev` object matches the model state:

```text
tau_C_model_dev = log(1 + T_C_t) - log(1 + Tbar_C)
tau_N_model_dev = log((1 - T_N_t)^(-1)) - log((1 - Tbar_N)^(-1))
tau_Y_model_dev = log(1 + T_Y_t) - log(1 + Tbar_Y)
bgov_dev        = debt_gdp_t - Bgov_ss
```

3. Add clear row-level flags:

```text
source_family
model_state_transform
steady_state_source
frequency
proxy_quality
runtime_ready
```

4. Separate instruments into quality tiers:

```text
tier_1: consumption/VAT where denominator and tax concept are clean
tier_2: income/social proxy, labelled non-labour-clean
tier_3: production wedge, C2 only after Stage 0 repair
```

Acceptance criteria:

- One panel exists with raw variables and model-dev variables.
- Every model-dev variable has a documented formula.
- No proxy row is marked runtime-ready by default.

## Stage 2: estimate the exact MCMS fiscal-rule form

Target equation:

```text
tau_t = rho tau_{t-1}
      + (1-rho)(Phi_y y_t + Phi_b bgov_{t-1})
      + Sigma eps_t
```

Tasks:

1. Add a new estimator script:

```text
MCMS-private/scripts/estimate_fiscal_rules_model_form.py
```

2. Estimate the model-form equation directly using nonlinear least squares or constrained optimization.
3. Do not estimate `phi_y` and later divide unless this is included only as a diagnostic.
4. Impose defensible parameter bounds:

```text
0 <= rho < 0.99
Sigma > 0
Phi_y and Phi_b bounded by economically plausible intervals
```

5. Emit:

```text
model_form_estimates.csv
model_form_diagnostics.csv
model_form_estimation_audit.md
```

6. Include diagnostics:

```text
obs
sample years
objective value
residual std
condition number or optimizer status
near-unit-rho flag
sign flags
debt-stabilization warning
```

Acceptance criteria:

- The estimator estimates `rho`, `Phi_y`, `Phi_b`, and `Sigma` in the same normalization used by `build_equations.jl`.
- Output includes both estimates and diagnostics.
- Estimates are still labelled candidate until model checks pass.

## Stage 3: Bayesian fiscal-rule estimation

Purpose: get closer to LPT without immediately estimating the full MCMS model.

Add:

```text
MCMS-private/scripts/estimate_fiscal_rules_bayesian.py
```

Tasks:

1. Define priors:

```text
rho ~ Beta, mapped to [0, 0.99]
Phi_y ~ Normal or Student-t
Phi_b ~ Normal or Student-t
Sigma ~ HalfNormal or InverseGamma
```

2. Use model-dev data and the exact model-form equation.
3. Estimate separate country/instrument equations first.
4. Then add a hierarchical version:

```text
Phi_y,k ~ common distribution
Phi_b,k ~ common distribution
rho_k   ~ common distribution
Sigma_k ~ common distribution
```

5. Use shrinkage for weak-data countries such as China/ROW.
6. Emit posterior summaries:

```text
posterior_mean
posterior_median
credible_interval_5
credible_interval_95
posterior_sd
rhat or convergence diagnostic
effective_sample_size
```

Acceptance criteria:

- Posterior results exist for at least `tau_C`.
- `tau_N` is estimated only as a proxy and labelled accordingly.
- `tau_Y` is included only if C2 has passed Stage 0 repairs.
- Results include uncertainty intervals, not only point estimates.

## Stage 4: annual-to-model-frequency bridge

Tasks:

1. Decide whether the model is interpreted annually or quarterly for fiscal rules.
2. If quarterly, add a frequency-conversion module.
3. Convert persistence:

```text
rho_quarterly = rho_annual^(1/4)
```

4. Define the shock-scale conversion explicitly.
5. Do not blindly divide all annual shocks by `sqrt(4)` unless the innovation aggregation assumption is stated.
6. Document whether feedback coefficients represent annual or per-period responses.

Acceptance criteria:

- The frequency bridge is explicit and reproducible.
- Runtime coefficients are tagged as annual or quarterly.

## Stage 5: MCMS model-solution validation

Files:

```text
MCMS-private/src/calibration.jl
MCMS-private/src/build_equations.jl
```

Tasks:

1. Add candidate fiscal-rule coefficients through a controlled loader or clearly labelled patch.
2. Regenerate equations.
3. Run:

```text
parser success
equation/variable count consistency
Blanchard-Kahn determinacy
bounded debt IRFs
shock-scale sanity checks
baseline IRF comparison
```

4. Compare:

```text
old hand-set baseline
Benchmark A/B model-form estimates
Bayesian posterior mean
Bayesian posterior conservative/shrinkage draw
C2 production-wedge sensitivity
```

Acceptance criteria:

- No candidate becomes baseline unless it passes model solution and debt-stability checks.
- The selected runtime calibration is reproducible from a named output row or posterior summary.

## Stage 6: documentation update

Update:

```text
claude-code-my-workflow/docs/model specifics/full.md
claude-code-my-workflow/docs/model specifics/full_adversarial_review.md
```

Required language:

```text
These are LPT-style fiscal-rule estimates, not LPT posterior estimates.
They use public annual fiscal data transformed into MCMS model-state units.
The dynamic coefficients are estimated in the same normalization as the MCMS fiscal-rule equation.
Runtime use requires model-frequency conversion, determinacy checks, and debt-stability checks.
```

Acceptance criteria:

- The document clearly separates:

```text
raw data
model-dev observables
model-form estimates
Bayesian estimates
runtime calibration
scenario/sensitivity calibration
```

- No section claims that the workflow replicates LPT Bayesian DSGE estimation unless full model estimation has actually been implemented.

## Recommended first implementation pass

Do this first:

1. Fix C2 Stage 0 issues.
2. Add `estimate_fiscal_rules_model_form.py`.
3. Estimate exact model-form rules for `tau_C` only.
4. Produce diagnostics and compare to the current transformed OLS rows.
5. Do not touch `calibration.jl` until the model-form estimates have diagnostics.

This gives the largest movement toward LPT with the least risk.
