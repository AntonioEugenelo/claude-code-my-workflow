# Structural-Bayes DSGE Estimation Base

Date: 2026-05-15

Status: process note for the `full-bayes-fiscal-dsge` branch. This does not
claim that MCMS currently has an implemented structural posterior. It identifies
a Julia DSGE Bayesian-estimation package to use as the design base, then maps
that workflow onto the MCMS fiscal-rule problem.

## Package Selected

Primary base: FRBNY `DSGE.jl`

- Repository: https://github.com/FRBNY-DSGE/DSGE.jl
- Documentation: https://frbny-dsge.github.io/DSGE.jl/
- Relevant replication package:
  https://github.com/FRBNY-DSGE/Replication-of-Online-Estimation-of-DSGE-Models

Reason for selection:

- It is a Julia DSGE codebase for solving and estimating structural DSGE models.
- It implements posterior evaluation around a solved state-space system rather
  than treating fiscal coefficients as a detached reduced-form layer.
- Its estimation workflow has the pieces MCMS needs: priors, transformed data,
  model solution, likelihood evaluation, posterior sampling, draw-level output,
  and downstream summaries.
- Its Online Estimation replication package shows how to run large posterior
  exercises in reproducible chunks and how to separate raw estimation output
  from tables and figures.

Secondary reference only: `NormannR/BayesianEstimationDSGEModels`

- Repository: https://github.com/NormannR/BayesianEstimationDSGEModels
- Useful as a compact pedagogical MCMC example for a small New Keynesian model.
- Not suitable as the main base for MCMS because it is old Julia 0.6 code and
  does not provide the model infrastructure needed for MCMS-scale runtime
  validation.

## What To Borrow From DSGE.jl

The relevant design pattern is not to copy FRBNY model equations into MCMS. The
useful pattern is the estimation contract:

```text
parameter draw theta
-> build model-specific parameterization
-> solve DSGE / produce state-space representation
-> evaluate measurement system likelihood
-> return log prior + log likelihood if admissible
-> otherwise return -Inf
-> save draw-level posterior values and model objects needed downstream
```

For MCMS, the model-solution step must be stricter than a generic likelihood
call. The posterior support must reject any draw that fails:

- MCMS solution status,
- Blanchard-Kahn determinacy,
- bounded-debt diagnostics.

No failed draw should be repaired by clipping, floors, arbitrary rescaling, or
runtime anchoring.

## MCMS Translation

The MCMS version should not import the FRBNY package as the main runtime. MCMS
already has its own calibration, equation generation, QZ/BK checks, and bounded
debt diagnostic in `MCMS-private/src`. The right approach is to implement the
FRBNY-style estimation contract around the existing MCMS solver.

Target module:

```text
MCMS-private/src/fiscal_structural_estimation.jl
```

Core functions:

```julia
logprior(theta)
build_fiscal_runtime(theta)
solve_model(theta)
loglikelihood(theta, data)
logposterior(theta, data)
```

Required posterior rule:

```julia
function logposterior(theta, data)
    lp = logprior(theta)
    isfinite(lp) || return -Inf

    runtime = build_fiscal_runtime(theta)
    status = solve_model(theta; runtime=runtime)

    status.solves || return -Inf
    status.bk_passed || return -Inf
    status.bounded_debt_passed || return -Inf

    ll = loglikelihood(theta, data; runtime=runtime, status=status)
    return lp + ll
end
```

This is the Option 3 change: MCMS admissibility becomes part of posterior
support.

## Parameter Block

Start with country-level fiscal response parameters only:

```text
rho_tau_C, Phi_tau_C_y, Phi_tau_C_b, sigma_tau_C
rho_tau_N, Phi_tau_N_y, Phi_tau_N_b, sigma_tau_N
rho_tau_Y, Phi_tau_Y_y, Phi_tau_Y_b, sigma_tau_Y
```

Each object is a country vector in the current MCMS country order:

```text
EA, China, ROW, USA
```

Sectoral `tau_Y` should remain out of the first structural estimator. It can be
added later by introducing explicit sector-loading priors and expanding the
state/measurement mapping after the country-level estimator works.

## Observation System

Use the fiscal data already constructed for the HMF layer as data inputs, not as
a runtime layer:

- `tau_C`: revenue/base effective consumption-tax wedge,
- `tau_N`: income/social-contribution effective labour wedge,
- `tau_Y`: production-tax/subsidy wedge,
- output/activity measure,
- debt measure.

Measurement equations:

```text
observed fiscal wedge =
    model-implied fiscal wedge
    + measurement error

annual observation =
    annual aggregation of quarterly model object
    + measurement error

quarterly observation =
    quarterly model object
    + measurement error
```

The likelihood should make measurement errors explicit. Mixed-frequency handling
belongs in the observation system, not in post-estimation fixes to runtime
matrices.

## Priors And Support

Restrictions should be encoded as priors or support:

- `rho` inside stationary support,
- `sigma` positive,
- debt feedback prior centered on stabilizing values,
- sector loadings, once added, with explicit prior distribution.

Forbidden in the new structural estimator:

- clipping exposure loadings to fixed ranges,
- mechanically setting `sigma` from clipped loadings,
- post-estimation coefficient scaling,
- runtime anchoring to C2-SUT matrices,
- hidden floors or arbitrary rescaling.

HMF outputs may still be used as:

- data construction,
- prior/proposal centers,
- benchmark comparison.

They should not be relabeled as structural posterior draws.

## Sampler Process

Use a staged sampler implementation:

1. Build deterministic data loading from `input_data/fiscal_rules_hmf/`.
2. Define `theta` packing/unpacking with named parameters and country order.
3. Implement `logprior` and support checks.
4. Implement `build_fiscal_runtime(theta)` to produce an in-memory fiscal rule
   object with `selected_fiscal_rule_layer = structural_bayes_fiscal`.
5. Thread the in-memory runtime into `calibrate` and `solve_status_only`.
6. Implement `loglikelihood` from explicit fiscal/macro measurement equations.
7. Start with adaptive random-walk Metropolis-Hastings.
8. Record every attempted draw, including rejection reason.
9. Summarize only accepted structural posterior draws.
10. Compare accepted posterior summaries against `:hmf_candidate`.

DSGE.jl's default workflow estimates a mode, constructs a proposal covariance,
then runs posterior sampling. MCMS can start simpler with adaptive random-walk
MH, then add mode/Hessian or SMC once the structural likelihood is correct.

## Output Contract

Write structural-Bayes outputs only under:

```text
MCMS-private/input_data/fiscal_rules_structural_bayes/
```

Required artifacts:

```text
posterior_draws.csv
accepted_draws.csv
rejection_summary.csv
posterior_summary.csv
runtime_posterior_mean.jl
runtime_posterior_median.jl
estimation_audit.md
metadata.json
```

Do not mix these with:

```text
MCMS-private/input_data/fiscal_rules_hmf/
```

Runtime metadata should identify:

```text
selected_fiscal_rule_layer = structural_bayes_fiscal
posterior_target = full_mcms_likelihood_fiscal_response_posterior
runtime_readiness_flag = structural_posterior_runtime_ready
```

Only accepted posterior draws can enter runtime mean/median matrices.

## Validation Gate

Do not use Option 3 paper language until the branch has:

- at least 1,000 attempted draws,
- nonzero accepted draws,
- reported acceptance rate,
- reported BK failure rate,
- reported bounded-debt failure rate,
- posterior summaries computed only from accepted draws,
- comparison against `:hmf_candidate`,
- fixed seed recorded,
- source hashes recorded.

## Implementation Order

Recommended file order:

1. `src/fiscal_structural_estimation.jl`
   - parameter packing, priors, data loading, likelihood, posterior contract.
2. `src/calibration.jl`
   - add `:structural_bayes_fiscal` loader support without changing
     `:hmf_candidate`.
3. `src/solve_onkio.jl`
   - expose a lightweight solve-status call that accepts an in-memory fiscal
     runtime object, or a generated structural runtime file.
4. `scripts/run_structural_bayes_fiscal_estimator.jl`
   - sampler entry point with fixed seed and output writer.
5. `scripts/check_structural_bayes_runtime.jl`
   - validates metadata, accepted-draw summaries, hashes, solve/BK/debt failure
     accounting, and runtime handoff files.

This keeps the HMF/LPT layer intact and creates a separate structural-Bayes
layer whose posterior support is defined by the solved MCMS model.
