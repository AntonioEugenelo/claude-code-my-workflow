# Response to adversarial review

Date: 2026-05-14

Scope:

- `docs/model specifics/full_adversarial_review.md`
- `docs/model specifics/full.md`
- `docs/model specifics/fiscal_lpt_derivations.md`
- `MCMS-private/src/calibration.jl`
- `MCMS-private/scripts/build_fiscal_rule_dataset_quarterly_c2.py`
- `MCMS-private/input_data/fiscal_rules_quarterly_c2`
- `Fiscal-LPT/main.tex`

## Bottom line

I accepted the review's central critique. The unrestricted quarterly C2
production-wedge rule was not a valid baseline because all four empirical
production-wedge debt feedbacks were negative and the full model failed BK. I
implemented a determinacy-preserving runtime closure:

```text
debt_feedback_closure = clip_negative_phi_b_to_zero
```

The active runtime now keeps the quarterly C2 persistence, output response, and
shock scale, but clips negative production-wedge debt feedbacks to zero. The
unrestricted empirical debt coefficients remain in the generated CSV files as
audit columns.

The full model now solves:

```text
stable eigenvalues = 1,885
required stable eigenvalues = 1,885
unstable eigenvalues = 723
required unstable eigenvalues = 723
output = output_julia\irfs\irf_C2_FullModelCheck_2026-05-14_13-48-45.mat
```

This is still not an LPT posterior calibration. It is a quarterly reduced-form
calibration with a sign-restricted fiscal closure.

## Accepted and implemented

### 1. Active baseline failed BK

Accepted.

The unrestricted quarterly C2 runtime failed:

```text
stable eigenvalues = 1,883
required stable eigenvalues = 1,885
```

The review was right that this cannot be presented as a baseline. I changed the
runtime closure by clipping negative production-wedge debt feedbacks to zero.
After the change, the model solved and exported IRFs.

### 2. Negative production-wedge debt feedback was destabilizing

Accepted.

The unrestricted empirical quarterly debt-feedback vector was:

```text
Phi_tau_Y_b_empirical =
[-0.014998973569, -0.028840117005, -0.037070159208, -0.009242063830]
```

Under the model sign convention, a negative response means higher inherited
debt lowers production taxes or raises production subsidies. That is not a
debt-stabilizing production-wedge closure. The runtime now uses:

```text
Phi_tau_Y_b = [0, 0, 0, 0]
```

The empirical values are retained in:

```text
MCMS-private/input_data/fiscal_rules_quarterly_c2/quarterly_c2_country_coefficients.csv
```

as:

```text
Beta_tau_Y_b_empirical_quarterly_c2
Phi_tau_Y_b_empirical_quarterly_c2
```

### 3. Generated-to-runtime bridge was manual

Accepted and fixed.

The quarterly C2 builder now writes a generated Julia runtime artifact:

```text
MCMS-private/input_data/fiscal_rules_quarterly_c2/quarterly_c2_runtime.jl
```

`src/calibration.jl` now includes this generated artifact:

```julia
include(joinpath(@__DIR__, "..", "input_data", "fiscal_rules_quarterly_c2", "quarterly_c2_runtime.jl"))
```

and loads:

```julia
quarterly_c2 = quarterly_c2_runtime_vectors()
rho_tau_Y_by_country = quarterly_c2.rho_tau_Y_by_country
phi_tau_Y_y_by_country = quarterly_c2.phi_tau_Y_y_by_country
phi_tau_Y_b_by_country = quarterly_c2.phi_tau_Y_b_by_country
sigma_tau_Y_by_country = quarterly_c2.sigma_tau_Y_by_country
```

Regenerating the quarterly C2 dataset now regenerates the runtime include file.
This removes the manual copy-paste bridge.

### 4. Paper/runtime mismatch

Accepted and fixed.

`Fiscal-LPT/main.tex` no longer reports the old production-rule values:

```text
rho^Y = [0.80, 0.70, 0.75, 0.80]
phi^Y_y = [0.02, 0.03, 0.02, 0.01]
phi^Y_b = [0.015, 0.020, 0.015, 0.010]
```

It now reports the active quarterly C2 runtime values:

```text
rho^Y = [0.063775, 0.492690, 0.556467, 0.688885]
phi^Y_y = [0.058865, 0.012643, 0.000961, 0.010127]
phi^Y_b = [0, 0, 0, 0]
sigma^Y = [0.005259, 0.004784, 0.002739, 0.003484]
```

The text now says the production-wedge coefficients are quarterly reduced-form
objects with a runtime sign restriction, not structural posterior estimates.

### 5. `full.md` still read as a menu of alternatives

Accepted and fixed.

`full.md` now documents only the active quarterly C2 specification. Historical
Benchmark A/B/C and annual C2 option material was removed from that file. The
note now focuses on:

- active sources,
- active formulas,
- China/ROW transfer treatment,
- runtime vectors,
- generated files,
- reproducibility,
- verification status,
- limitations.

### 6. Sectoral material was overstated

Accepted.

The runtime still repeats country aggregate production-wedge coefficients across
sectors. The quarterly sectoral file is operational as a 4-by-44 artifact, but
under neutral output-share allocation the sectoral wedge rates equal the
country aggregate wedge rate.

The current claim is therefore:

```text
country-specific production-wedge rule, repeated across sectors
```

not:

```text
empirically estimated sector-specific production-wedge reaction functions
```

### 7. `Tbar_Y` was potentially confused with observed fiscal data

Accepted as a documentation boundary.

The runtime still uses:

```text
Tbar_Y = 1 ./ M - 1
```

This is the markup-implied steady-state production wedge. Quarterly C2 affects
the dynamic rule only. I did not replace `Tbar_Y` with observed fiscal data.

## Pushbacks

### 1. I did not implement an LPT-style Bayesian posterior

Rejected as out of scope for this patch.

Quarterly data make posterior estimation more feasible, but the current
repository still lacks the estimation layer required for an LPT posterior:

- measurement equations,
- priors,
- repeated DSGE solution inside likelihood evaluation,
- Kalman or particle filtering,
- posterior sampling,
- posterior diagnostics.

The correct label remains:

```text
quarterly reduced-form calibration with a sign-restricted fiscal closure
```

not:

```text
LPT-estimated Bayesian posterior calibration
```

### 2. I did not integrate the sectoral C2-SUT candidate as runtime

Rejected for the baseline.

The sectoral C2-SUT candidate has much wider coefficient ranges than the
aggregate quarterly C2 runtime. Integrating it directly would require a separate
determinacy and debt-IRF review. The current baseline stays country-level and
sector-common.

### 3. I did not let production-wedge debt feedback be negative

Rejected for the active runtime closure.

The unrestricted negative debt feedbacks are retained as empirical audit
columns, but they are not used in the runtime because they break determinacy and
have the wrong fiscal-stabilization direction under the model's sign
convention.

## Verification performed

Quarterly C2 builder:

```text
python -B scripts\build_fiscal_rule_dataset_quarterly_c2.py
```

Runtime vector check:

```text
julia --project=. scripts\check_quarterly_c2_calibration.jl
```

Result:

```text
Rho_tau_Y[:,1] = [0.06377464862897264, 0.49268960242939547, 0.5564666371949851, 0.6888852763870515]
Phi_tau_Y_y[:,1] = [0.05886484237361775, 0.012643484605117439, 0.0009611292452423523, 0.010127182982481558]
Phi_tau_Y_b[:,1] = [0.0, 0.0, 0.0, 0.0]
Sigma_tau_Y[:,1] = [0.00525912488192555, 0.004784228152489203, 0.002738881214194855, 0.0034843217217488142]
```

Full model check:

```text
julia --project=. scripts\run_c2_full_model_check.jl
```

Result:

```text
equations = 6,762
variables = 6,762
shocks = 448
static elimination residual = 2.842154310930614e-14
stable eigenvalues = 1,885
required stable eigenvalues = 1,885
unstable eigenvalues = 723
required unstable eigenvalues = 723
IRFs exported to output_julia\irfs\irf_C2_FullModelCheck_2026-05-14_13-48-45.mat
```

## Current status

The active quarterly C2 runtime now solves. The implementation is acceptable as
a transparent reduced-form baseline closure with an explicit sign restriction.
It is not a structural LPT posterior, and China/ROW plus sectoral
heterogeneity remain transfer assumptions rather than direct evidence.
