# Fiscal-LPT `main.tex` Adversarial Review

Date: 2026-05-15

Target: `C:\CustomTools\MCMS_gvt\Fiscal-LPT\main.tex`

Model evidence checked:

- `C:\CustomTools\MCMS_gvt\MCMS-private\src\calibration.jl`
- `C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_sectoral_c2_sut\sectoral_c2_sut_runtime.jl`
- `C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_hmf\determinacy_filter_summary.csv`
- `C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_structural_bayes\metadata.json`
- `C:\CustomTools\MCMS_gvt\MCMS-private\input_data\fiscal_rules_structural_bayes\estimation_audit.md`

Review plan command:

```powershell
python scripts\review_plan.py ..\Fiscal-LPT\main.tex --round 1 --adversarial
```

Planner route: `fiscal-lpt-paper`, deep tier, round 1, adversarial.

Required reviewers:

- proofreader
- derivation-auditor
- figure-reviewer
- theory-critic
- pedagogical-reviewer
- cochrane-style-reviewer
- narrative-reviewer
- devils-advocate

Note: `bash` is not available in this PowerShell environment, so
`scripts/review-mode.sh` could not be used directly. The review was still
tracked in this report and follows the same reviewer set and findings-first
loop.

## Round 1 Findings And Fixes

### Finding 1: Budget derivation mixed levels and deviations

Severity: Critical

Reviewer roles: derivation-auditor, theory-critic, devils-advocate

Problem: The nonlinear government budget parent identity used lower-case
`rev` objects even though the revenue accounting section defines those objects
as first-order deviations, not revenue levels. This made the derivation
internally inconsistent.

Fix implemented: The parent budget now uses calligraphic normalized revenue
levels, `\mathcal R^C`, `\mathcal R^N`, `\mathcal R^Y`, and
`\mathcal R^{tar}`. The text then explicitly states that the lower-case
`rev` variables in the implemented linear equation are first-order deviations
from steady state.

Status: Fixed.

### Finding 2: Manuscript overclaimed the structural-Bayes layer

Severity: Critical

Reviewer roles: claims/paper-language, theory-critic, devils-advocate

Problem: The live structural-Bayes artifacts report only four attempted draws
and zero accepted draws. The paper therefore cannot claim a completed
structural posterior or runtime-ready structural layer.

Fix implemented: The manuscript now states that `:structural_bayes_fiscal` is
in progress, has four attempted draws and zero accepted draws, is marked
`structural_posterior_not_ready`, and does not support language claiming an
accepted structural fiscal posterior.

Status: Fixed.

### Finding 3: Production-rule text was stale

Severity: High

Reviewer roles: code/runtime integration, data/measurement, devils-advocate

Problem: The old text described production-tax feedback as country-specific
but common across sectors. The live default runtime is `:sectoral_c2_sut` and
uses sectoral production-wedge matrices. The country-level restriction now
belongs only to the in-progress first-pass structural-Bayes estimator.

Fix implemented: The production-rule derivation now states that the default
operational layer is sectoral. The calibration appendix replaced the stale
country table with a matrix summary for `Rho_tau_Y`, `Phi_tau_Y_y`,
`Phi_tau_Y_b`, and `Sigma_tau_Y`. The text separately explains that the
structural-Bayes trial runtime starts from country-level `tau_Y` response
parameters and repeats them across sectors.

Status: Fixed.

### Finding 4: HMF admissibility status needed to be explicit

Severity: High

Reviewer roles: DSGE/BK/determinacy, fiscal theory/bounded-debt,
claims/paper-language

Problem: The HMF layer is data-rich but is not runtime-ready. The live
determinacy summary shows BK passes exactly, but the bounded-debt filter fails
with debt-block spectral radius above one.

Fix implemented: The manuscript now says the HMF point runtime passes the BK
count but fails bounded debt with spectral radius about 1.01215. It identifies
HMF as a candidate and benchmark layer, not as structural posterior output.

Status: Fixed.

### Finding 5: Empty introduction

Severity: Medium

Reviewer roles: proofreader, pedagogical-reviewer, narrative-reviewer,
cochrane-style-reviewer

Problem: The paper opened with an empty `Introduction` heading, then jumped
directly to the appendix. That made the calibration-state update look like an
appendix-only patch rather than a coherent current-state note.

Fix implemented: The introduction now states what the fiscal extension adds,
what the current runtime/HMF/structural-Bayes layers are, and what the paper
does not claim.

Status: Fixed.

### Finding 6: Build/layout issue after first edit

Severity: Medium

Reviewer roles: proofreader

Problem: The first edit introduced one overfull line around inline runtime
layer names.

Fix implemented: The layer-status paragraph was converted to an enumerated
list with shorter labels.

Status: Fixed.

## Round 2 Re-Review

Re-review checks performed:

- `pdflatex -interaction=nonstopmode main.tex`
- `Select-String -Path main.log -Pattern "Overfull|Undefined|LaTeX Warning|Error|Emergency"`
- targeted search for stale claims:
  - `common across sectors`
  - `completed Bayesian structural`
  - `accepted structural fiscal posterior`
  - `Option 3`

Round 2 findings:

- No LaTeX errors.
- No overfull boxes after the second build.
- No undefined-reference warnings were reported by the targeted log search.
- No remaining claim says the structural posterior is accepted or runtime
  ready.
- No remaining statement says the default production-rule coefficients are
  common across sectors.

Residual caveats:

- The structural-Bayes process itself is not complete. This is now stated in
  the manuscript rather than hidden.
- The HMF layer is not runtime-ready. This is now stated in the manuscript.
- The default `:sectoral_c2_sut` layer is an operational calibration with an
  explicit sign restriction, not a structural posterior. This is now stated in
  the manuscript.

Review outcome: Passed for the requested manuscript update. The review does
not certify the structural-Bayes validation gate; it certifies that the paper
now matches the live repo state and avoids unsupported structural-estimation
claims.
