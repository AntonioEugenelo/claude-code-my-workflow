# Adversarial audit and step-by-step derivation of the Fiscal-LPT appendix

Date: May 13, 2026

Scope: this note audits the appendix derivations in `Fiscal-LPT/main.tex` against the live Julia implementation in `MCMS-private/src/build_equations.jl` and the current calibration block in `MCMS-private/src/calibration.jl`.

## Verdict

The equations implemented in Julia are internally coherent under a precise set of conventions. The appendix mostly reports the implemented equations correctly, but several derivation statements are too loose.

The main substantive fault is the government budget derivation: the level constraint written in the appendix is not the correct parent equation for the implemented linear budget. The implemented equation comes from a one-period discount-debt budget, not from the lagged gross-interest budget currently written in `main.tex`.

## Adversarial findings

| Severity | Location | Finding |
|---|---|---|
| Fix | Opening appendix conventions | The text says the new fiscal objects are log deviations. This is not true for `bgov`. The implemented debt variable is an additive real public-debt deviation normalized by steady-state GDP, not a log deviation. |
| Fix | Labour-tax derivation and revenue equation | The appendix must define `tau_N` as `d log((1-T_N)^(-1))`, not just as a generic labour wedge. The wage Phillips curve and labour-tax revenue equation both require this inverse after-tax wedge convention. |
| Fix | Government budget derivation | The level equation in `main.tex`, `B_t = (1+i_{t-1})B_{t-1} - P_t Y_t Rev_t`, does not linearize to the implemented budget equation. The implemented equation comes from `Q_t^g B_t^g + P_t^C \bar Y Rev_t = B_{t-1}^g`. |
| Clarify | Revenue accounting | `rev_C`, `rev_N`, `rev_Y`, and `rev_tariff` are not log revenues. They are first-order deviations of revenue scaled by steady-state GDP. |
| Clarify | Consumption-tax Euler equation | The Euler equation is correct, but the appendix should state that `i_t` is the log deviation of the gross nominal rate, or the model's first-order interest-rate gap measured in the same units as inflation. |
| Clarify | Production-subsidy experiments | A statement such as `sigma_Y_{4,21} = -0.10` is a shock-scale override. It is a ten percentage point subsidy only for a unit innovation and under the local gross-wedge mapping. |
| Verify | Dynare mirror claim | The Dynare model-equation mirror matches the fiscal structure, but the Dynare parameter file still contains older placeholders such as `Tbar_C = 0.20`, `Tbar_N = 0.30`, `bgov_ss = 0.60`, and `psi_bgov_spread = 0.01`. The current quantitative calibration is the Julia `src/calibration.jl` block unless the Dynare parameter file is regenerated or patched. |

## Conventions needed for the derivations

For strictly positive variables, lower-case variables are log deviations:

```math
x_t = \widehat X_t = \log X_t - \log \bar X.
```

Debt is different. The implemented debt state is an additive deviation:

```math
b^g_{k,t}
=
\frac{B^g_{k,t}}{P^C_{k,t}\bar Y_k}
-
\bar b^g_k.
```

It is normalized by current CPI and steady-state real GDP. This convention is forced by the implemented budget equation because no current `y_{k,t}` term appears there.

The three tax variables are log deviations of gross wedges:

```math
\tau^C_{k,t} = \widehat{(1+T^C_{k,t})},
\qquad
\tau^N_{k,t} = \widehat{(1-T^N_{k,t})^{-1}},
\qquad
\tau^Y_{ki,t} = \widehat{(1+T^Y_{ki,t})}.
```

Therefore the first-order statutory-rate changes are:

```math
dT^C_{k,t} = (1+\bar T^C_k)\tau^C_{k,t},
```

```math
dT^N_{k,t} = (1-\bar T^N_k)\tau^N_{k,t},
```

```math
dT^Y_{ki,t} = (1+\bar T^Y_{ki})\tau^Y_{ki,t}.
```

These conversion formulas are the hidden step behind the revenue equations.

## Consumption tax and the Euler equation

The household consumption FOC is:

```math
U_C(C_{k,t})
=
\Lambda_{k,t}P^C_{k,t}(1+T^C_{k,t}).
```

With CRRA utility, `U_C(C)=C^{-sigma}`:

```math
\log \Lambda_{k,t}
=
-\sigma \log C_{k,t}
-\log P^C_{k,t}
-\log(1+T^C_{k,t}).
```

Subtract the steady state:

```math
\lambda_{k,t}
=
-\sigma c_{k,t}
-p^C_{k,t}
-\tau^C_{k,t}.
```

The nominal bond FOC is:

```math
\Lambda_{k,t}
=
\beta R_{k,t} E_t \Lambda_{k,t+1},
\qquad R_{k,t}=1+i^{level}_{k,t}.
```

At first order, using `beta * Rbar = 1` and ignoring Jensen terms:

```math
\lambda_{k,t}
=
i_{k,t}
+
E_t \lambda_{k,t+1},
```

where `i_{k,t}` is the log deviation of the gross nominal rate.

Substitute the multiplier expression:

```math
-\sigma c_{k,t}-p^C_{k,t}-\tau^C_{k,t}
=
i_{k,t}
+
E_t[-\sigma c_{k,t+1}-p^C_{k,t+1}-\tau^C_{k,t+1}].
```

Move terms and use `pi^C_{k,t+1}=p^C_{k,t+1}-p^C_{k,t}`:

```math
\sigma c_{k,t}
=
\sigma E_t c_{k,t+1}
-i_{k,t}
+E_t\pi^C_{k,t+1}
+E_t\tau^C_{k,t+1}
-\tau^C_{k,t}.
```

Divide by `sigma`:

```math
c_{k,t}
=
E_t c_{k,t+1}
-
\frac{1}{\sigma}
\left(
i_{k,t}
-E_t\pi^C_{k,t+1}
-E_t\tau^C_{k,t+1}
+\tau^C_{k,t}
\right).
```

This matches the implemented Julia equation:

```text
c_k[0] = c_k[1] - 1/sigma * (i_k[0] - pi_C_k[1] - tau_C_k[1] + tau_C_k[0])
```

## Labour tax and the wage Phillips curve

The static labour condition is:

```math
\frac{W_{k,t}}{P^C_{k,t}}
=
\frac{1+T^C_{k,t}}{1-T^N_{k,t}}
C_{k,t}^{\sigma}N_{k,t}^{\varphi}.
```

Taking deviations:

```math
w^{flex}_{k,t}
=
\sigma c_{k,t}
+\varphi n_{k,t}
+\tau^C_{k,t}
+\tau^N_{k,t}.
```

The sign on `tau_N` is positive because `tau_N` is the log deviation of the inverse after-tax labour wedge. A higher labour tax raises the pre-tax wage required by households.

The Calvo wage block uses the desired real-wage gap:

```math
\pi^w_{k,t}
=
\kappa^w_k(w^{flex}_{k,t}-w_{k,t})
+\beta E_t\pi^w_{k,t+1}.
```

Substitution gives:

```math
\pi^w_{k,t}
=
\kappa^w_k
\left(
\sigma c_{k,t}
+\varphi n_{k,t}
-w_{k,t}
+\tau^C_{k,t}
+\tau^N_{k,t}
\right)
+\beta E_t\pi^w_{k,t+1}.
```

This matches the implementation. The appendix problem is definitional: without the inverse after-tax wedge convention, the sign is not well-defined.

## Production tax and price setting

The selected instrument is a marginal-cost wedge:

```math
MC^{tax}_{ki,t}
=
(1+T^Y_{ki,t})MC_{ki,t}.
```

Taking log deviations:

```math
mc^{tax}_{ki,t}
=
mc_{ki,t}
+
\tau^Y_{ki,t}.
```

Hence every price Phillips-curve marginal-cost gap receives the same `+ tau_Y` term. For producer-currency pricing:

```math
\pi_{lki,t}
=
\kappa^p_{ki}(mc_{ki,t}+\tau^Y_{ki,t}-p_{lki,t})
+\beta E_t\pi_{lki,t+1}.
```

For local-currency pricing with `l != k`, the implemented relative-price term also includes the bilateral real exchange rate:

```math
\pi_{lki,t}
=
\kappa^p_{ki}(mc_{ki,t}+\tau^Y_{ki,t}-p_{lki,t}-q_{kl,t})
+\beta E_t\pi_{lki,t+1}.
```

For dominant-currency pricing, the `q` term is relative to the dominant-currency country. The appendix is acceptable because it says it suppresses currency-pricing indicators, but a fully self-contained derivation should mention these branches.

## Fiscal rules

For a generic wedge `x_{k,t}`, define:

```math
x^{target}_{k,t}
=
\phi^x_{y,k}y_{k,t}
+
\phi^x_{b,k}b^g_{k,t-1}.
```

Partial adjustment gives:

```math
x_{k,t}
=
\rho^x_k x_{k,t-1}
+
(1-\rho^x_k)x^{target}_{k,t}
+
\sigma^x_k\varepsilon^x_{k,t}.
```

Therefore:

```math
\tau^C_{k,t}
=
\rho^C_k\tau^C_{k,t-1}
+
(1-\rho^C_k)(\phi^C_{y,k}y_{k,t}+\phi^C_{b,k}b^g_{k,t-1})
+
\sigma^C_k\varepsilon^C_{k,t}.
```

```math
\tau^N_{k,t}
=
\rho^N_k\tau^N_{k,t-1}
+
(1-\rho^N_k)(\phi^N_{y,k}y_{k,t}+\phi^N_{b,k}b^g_{k,t-1})
+
\sigma^N_k\varepsilon^N_{k,t}.
```

```math
\tau^Y_{ki,t}
=
\rho^Y_{ki}\tau^Y_{ki,t-1}
+
(1-\rho^Y_{ki})(\phi^Y_{y,ki}y_{k,t}+\phi^Y_{b,ki}b^g_{k,t-1})
+
\sigma^Y_{ki}\varepsilon^Y_{ki,t}.
```

These equations match the Julia implementation. The convention issue is again that `bgov` is an additive normalized debt deviation, not a log deviation.

## Revenue linearizations

The implemented revenue variables are additive deviations normalized by steady-state GDP. They are not logs.

### Consumption-tax revenue

Define:

```math
s^C_k
=
\frac{\bar P^C_k\bar C_k}{\bar P^C_k\bar Y_k}
=
\frac{\bar C_k}{\bar Y_k}.
```

Revenue is:

```math
\mathcal R^C_{k,t}
=
T^C_{k,t}P^C_{k,t}C_{k,t}.
```

Scaled by steady-state nominal GDP, with the common CPI level handled in the real budget normalization:

```math
rev^C_{k,t}
=
s^C_k
\left[
dT^C_{k,t}
+
\bar T^C_k c_{k,t}
\right].
```

Using `dT_C = (1+Tbar_C) tau_C`:

```math
rev^C_{k,t}
=
s^C_k
\left[
(1+\bar T^C_k)\tau^C_{k,t}
+
\bar T^C_k c_{k,t}
\right].
```

### Labour-tax revenue

Define:

```math
s^L_k
=
\frac{\bar W_k\bar N_k}{\bar P^C_k\bar Y_k}.
```

Revenue is:

```math
\mathcal R^N_{k,t}
=
T^N_{k,t}W_{k,t}N_{k,t}.
```

The first-order scaled deviation is:

```math
rev^N_{k,t}
=
s^L_k
\left[
dT^N_{k,t}
+
\bar T^N_k(w_{k,t}+n_{k,t})
\right].
```

Using `dT_N = (1-Tbar_N) tau_N`:

```math
rev^N_{k,t}
=
s^L_k
\left[
(1-\bar T^N_k)\tau^N_{k,t}
+
\bar T^N_k(w_{k,t}+n_{k,t})
\right].
```

### Production-tax revenue

Define:

```math
s^{MCY}_{ki}
=
\frac{\overline{MC}_{ki}\bar Y_{ki}}{\bar P^C_k\bar Y_k}.
```

Revenue is:

```math
\mathcal R^Y_{k,t}
=
\sum_i T^Y_{ki,t}MC_{ki,t}Y_{ki,t}.
```

The first-order scaled deviation is:

```math
rev^Y_{k,t}
=
\sum_i s^{MCY}_{ki}
\left[
dT^Y_{ki,t}
+
\bar T^Y_{ki}(mc_{ki,t}+y_{ki,t})
\right].
```

Using `dT_Y = (1+Tbar_Y) tau_Y`:

```math
rev^Y_{k,t}
=
\sum_i s^{MCY}_{ki}
\left[
(1+\bar T^Y_{ki})\tau^Y_{ki,t}
+
\bar T^Y_{ki}(mc_{ki,t}+y_{ki,t})
\right].
```

This matches the implemented equation. If `Tbar_Y < 0`, the base-effect term has the sign of a subsidy: higher marginal-cost output makes the subsidy more expensive.

## Government borrowing spread

The spread equation is:

```math
i^g_{k,t}
=
i_{k,t}
+
\psi^g_k b^g_{k,t-1}.
```

The current Julia baseline sets `psi_bgov_spread = 0` for all countries. The spread channel is present as an equation but shut down quantitatively in the current Julia baseline.

## Government budget constraint

The implemented budget is a discount-debt equation. Start from:

```math
Q^g_{k,t}B^g_{k,t}
+
P^C_{k,t}\bar Y_k
\left(
rev^C_{k,t}+rev^N_{k,t}+rev^Y_{k,t}+rev^{tar}_{k,t}
\right)
=
B^g_{k,t-1}.
```

Divide by `P^C_{k,t} \bar Y_k`:

```math
Q^g_{k,t}
\frac{B^g_{k,t}}{P^C_{k,t}\bar Y_k}
+
rev^C_{k,t}+rev^N_{k,t}+rev^Y_{k,t}+rev^{tar}_{k,t}
=
\frac{B^g_{k,t-1}}{P^C_{k,t}\bar Y_k}.
```

Use:

```math
\frac{B^g_{k,t}}{P^C_{k,t}\bar Y_k}
=
\bar b^g_k+b^g_{k,t},
```

and:

```math
\frac{B^g_{k,t-1}}{P^C_{k,t}\bar Y_k}
=
\frac{P^C_{k,t-1}}{P^C_{k,t}}
\frac{B^g_{k,t-1}}{P^C_{k,t-1}\bar Y_k}.
```

At first order:

```math
\frac{P^C_{k,t-1}}{P^C_{k,t}}(\bar b^g_k+b^g_{k,t-1})
=
\bar b^g_k+b^g_{k,t-1}-\bar b^g_k\pi^C_{k,t}.
```

For discount debt, `Q^g_{k,t}=1/R^g_{k,t}`. With `Qbar = beta` and `i^g_{k,t}` as the log deviation of the gross government rate:

```math
Q^g_{k,t}(\bar b^g_k+b^g_{k,t})
=
\beta\bar b^g_k
+
\beta b^g_{k,t}
-
\beta\bar b^g_k i^g_{k,t}.
```

Subtract the steady-state identity. The first-order budget is:

```math
\beta b^g_{k,t}
-
\beta\bar b^g_k i^g_{k,t}
+
rev^C_{k,t}+rev^N_{k,t}+rev^Y_{k,t}+rev^{tar}_{k,t}
=
b^g_{k,t-1}
-
\bar b^g_k\pi^C_{k,t}.
```

This is the implemented equation.

The current appendix should use the discount-debt parent equation. Starting from a lagged gross-interest budget is not a harmless alternative presentation; it changes the timing and linear coefficients.

## Minimum recommended edits to `main.tex`

1. Define `tau_C`, `tau_N`, and `tau_Y` exactly as gross-wedge log deviations.
2. State that `bgov` is an additive debt-ratio deviation, not a log deviation.
3. Replace the government budget parent equation with `Q_t^g B_t^g + P_t^C \bar Y Rev_t = B_{t-1}^g`.
4. Say explicitly that revenue variables are first-order GDP-normalized deviations, not log revenue variables.
5. Qualify the Dynare-mirror sentence: the equation mirror matches the fiscal structure, but the current quantitative calibration is the Julia `src/calibration.jl` block unless the Dynare parameter file is updated.
6. In the policy-experiment paragraph, distinguish a wedge shock scale from a statutory-rate change.

## Implementation status, May 13, 2026

These recommended edits have been implemented in `Fiscal-LPT/main.tex`.

Accepted and patched:

1. The appendix now defines `tau_C`, `tau_N`, and `tau_Y` as gross-wedge log deviations.
2. The appendix now states that `bgov` is an additive normalized debt deviation, not a log deviation.
3. The government budget derivation now starts from the discount-debt parent equation.
4. The revenue variables are now identified as GDP-normalized first-order revenue deviations.
5. The Dynare-mirror sentence now says the Julia calibration block is the quantitative baseline.
6. The US automotive subsidy example now describes `sigma_Y_4_21 = -0.10` as a shock-scale convention under a unit innovation, not as an observed statutory subsidy rate.

Verification:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build completed successfully and produced `Fiscal-LPT/main.pdf`.
