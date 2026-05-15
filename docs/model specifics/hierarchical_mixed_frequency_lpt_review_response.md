# Review response: hierarchical mixed-frequency LPT-motivated calibration note

Date: 2026-05-14

Target file:

```text
claude-code-my-workflow/docs/model specifics/hierarchical_mixed_frequency_lpt_note.md
```

This file records the adversarial review loop requested by the user. Review
agents are read-only. The main agent is responsible for integrating fixes and
rerunning the review until the note receives a passing grade or an unresolved
material disagreement must be escalated.

## Passing rule

The note is considered passing when all rerun reviewers score the revised note
above 95/100 and no critical/blocking findings remain. This supersedes the
earlier 90/100 stopping rule.

## Round 0 draft status

The initial draft explains:

1. the mixed-frequency data structure;
2. the relationship to LPT;
3. quarterly aggregate and annual sectoral measurement equations;
4. hierarchical pooling across sectors;
5. frequency transformation from annual to quarterly parameters;
6. determinacy filtering before runtime use;
7. required audit outputs and recommended paper wording.

## Review log

Review rounds will be appended below.

## Round 1 baseline specialist review

Agents completed:

```text
proofreader: fail, 86/100
DSGE/fiscal theory critic: fail, 87/100
derivation auditor: fail, 84/100
Bayesian/mixed-frequency econometrics reviewer: fail, 82/100
data-accounting reviewer: fail, 82/100
implementation/runtime alignment critic: fail, 82/100
```

Main findings:

1. The note overused "identify" for quantities that are only estimated under
   timing and orthogonality assumptions or disciplined by the hierarchical
   prior.
2. The annual-to-quarterly mapping `rho_Q = rho_A^(1/4)` and
   `sigma_Q = sigma_A/sqrt(4)` was too strong for annual average or flow-ratio
   sectoral accounts.
3. Debt normalization and determinacy language were underspecified.
4. BEA/FRED and Eurostat source definitions lacked enough row/series detail.
5. The Eurostat annual sectoral coverage claim needed a local coverage
   artifact.
6. Runtime handoff needed to match the current generated-Julia-matrix pattern.

Actions taken:

1. Added notation and acronym definitions.
2. Replaced "strongest feasible" and "identify" language with narrower
   "discipline/estimate under assumptions" language.
3. Added estimator-label taxonomy separating current runtime calibration,
   fiscal-rule-block posterior, mixed-frequency state-space posterior, and
   full DSGE posterior.
4. Added a data evidence table and generated:

```text
claude-code-my-workflow/docs/model specifics/eurostat_ea20_nama_10_a64_d29x39_coverage.csv
```

5. Added exact U.S. FRED series IDs and Eurostat source endpoints used in the
   current quarterly C2 layer.
6. Added runtime units, `Tbar_Y`, debt/GDP normalization, and lag timing.
7. Rewrote aggregation to prefer level aggregation and defined log-linear
   weights with the relative gross-wedge term.
8. Rewrote the annual sectoral layer so the minimal implementation estimates
   low-frequency sectoral response deviations, not free sectoral quarterly
   persistence or quarterly shock variances.
9. Demoted fourth-root persistence and square-root volatility conversion to
   heuristic point-in-time approximations, not the audit-ready default for
   annual BEA/Eurostat flow accounts.
10. Replaced "clipped for determinacy" with "determinacy-oriented
    admissibility restriction" and required BK/stability and bounded-debt
    checks.
11. Added a runtime handoff section specifying the generated Julia API,
    unambiguous quarterly matrix names, unrestricted/filtered/runtime posterior
    categories, and the need for a draw-level determinacy harness.

Reviewer pushback:

None of the Round 1 major findings should be rejected. The only partial pushback
is on implementation storage: the note permits CSV or parquet because the
current repository already uses CSV/JL generated artifacts, while parquet is
useful but not required for a first implementation.

## Round 2 full adversarial loop

User instruction during this round:

```text
Rather than solving issues by downgrading the claims, update the discussion to
match what the text had promised whenever possible.
```

The integration principle for Round 2 is therefore: fix by adding the missing
econometric, accounting, and runtime machinery first. Only downgrade language
where the live data or code cannot currently make the claim true.

Agents completed:

```text
devils-advocate: fail, 42/100
data-accounting/calibration reviewer: fail, 66/100
code/runtime alignment reviewer: fail, 72/100
Bayesian/mixed-frequency econometrics reviewer: fail, 74/100
derivation auditor: fail, 86/100
DSGE/fiscal theory critic: fail, 87/100
```

Main findings:

1. The design was still too roadmap-like relative to what it promised; Stage
   1-2 could not be treated as runtime-ready without a real annualization or
   validation gate.
2. The Stage 1 likelihood was a limited-information conditional fiscal-rule
   likelihood, not yet a full state-space likelihood with measurement equations.
3. The latent quarterly sectoral state-space version needed a low-rank or
   factor covariance structure; 44 unrelated sectoral shocks per country are
   underidentified.
4. Annualization was acknowledged but not operationalized with a concrete
   measurement-error layer.
5. Ex-post determinacy filtering needed to be defined as a posterior target,
   not casual trimming of nonsolving draws.
6. The note blurred empirical, policy-admissible, and solution-filtered
   posterior objects.
7. The C2-SUT production-wedge accounting object was under-specified: product
   taxes/import duties are removed, but product subsidies remain.
8. The empirical debt baseline was ambiguous relative to runtime `Bgov_ss`.
9. EA sectoral `D29X39` was only a coverage artifact, not yet a model-ready
   MCMS-private panel.
10. The runtime handoff lacked an explicit fiscal-rule-layer selector,
    matrix validation, CSV-to-JL consistency checks, and a solve-only posterior
    filtering harness.
11. The current sectoral runtime exposes annual residual scales as
    `Sigma_tau_Y`; the HMF design needs a proper quarterly variance mapping or
    a block on runtime use.

Actions taken:

1. Added the exact current C2-SUT source formula:

```text
Other taxes on production
- Other subsidies on production
- Subsidies on products
```

and clarified that product taxes/import duties are excluded but product
subsidies remain.

2. Added a required EA sectoral input directory and artifact set under:

```text
MCMS-private/input_data/fiscal_rules_ea_sectoral_d29x39
```

with raw snapshots, denominators, NACE-to-MCMS concordance, transformed wedges,
missingness rules, timestamps, and hashes.

3. Added a source-specific measurement-error equation:

```text
tau_obs = alpha_j + lambda_j tau_model + measurement_error
```

so denominator and source-concept mismatches are modeled instead of silently
pooled.

4. Replaced ambiguous debt centering with distinct empirical and runtime
baselines:

```text
Bgov_emp_ss_c
Bgov_runtime_ss_c
```

and noted that no-intercept estimates change when the empirical baseline
changes.

5. Added an explicit limited-information orthogonality condition for Stage 1
and stated when instruments or DSGE embedding are needed.

6. Added annualization as a level-flow/default measurement operator, with a
fallback log-average approximation only if an explicit annualization-error
variance is included.

7. Added mapped-sector measurement-error treatment or sector aggregation as the
required treatment for lossy BEA/NACE-to-MCMS concordances.

8. Added a pooled-null comparison and prior-sensitivity reporting for sectoral
deviations.

9. Added three posterior targets:

```text
unrestricted empirical posterior
policy-admissible posterior
solution-filtered posterior
```

with the solution-filtered target defined by an indicator solve event.

10. Added a low-rank/factor state-space shock structure:

```text
Q_c = Lambda_c Lambda_c' + D_c
```

to avoid an underidentified 44-sector unrestricted process covariance.

11. Added a Sigma frequency safeguard: derive quarterly `Sigma` from the
state-space covariance, use aggregate quarterly volatility times audited
sectoral relative scale, or block annual Sigma from runtime use.

12. Added a concrete Student-t transfer-prior family for China and ROW and
required generated rows to be labeled as transferred U.S.-sector-shape priors.

13. Added an explicit runtime selector:

```text
calibrate(; fiscal_rule_layer = :sectoral_c2_sut)
calibrate(; fiscal_rule_layer = :hmf_candidate)
```

and made HMF opt-in until the feasibility gate passes.

14. Added load-time matrix validation, `check_hmf_runtime.jl`, CSV-to-Julia
matrix consistency checks, source hashes, generated-Julia checksum, matrix
schema, selected fiscal-rule layer, and posterior-target metadata.

15. Rewrote the minimal implementation so it aims to deliver the promised HMF
object: build the EA sectoral panel, estimate source-specific measurement
error, implement or validate annualization, transform posterior draws, select a
passing draw or constrained summary, and compare current C2-SUT,
aggregate-only Bayesian, annual-sectoral partial pooling, and HMF candidates.

Round 2 status after edits:

The note has been materially revised but has not yet passed the user's
95+/100 stopping rule. A rerun is required with the relevant reviewers. The
main expected residual risks are whether the note now over-specifies an
implementation plan without actual code, and whether the remaining
non-runtime-ready caveats are acceptable as feasibility gates rather than
downgrades.

## Round 3 targeted rerun and implementation fixes

Rerun scores after the Round 2 note edits:

```text
data-accounting/calibration reviewer: pass, 96/100
DSGE/fiscal theory critic: pass, 96/100
devils-advocate: pass, 96/100
derivation auditor: pass, 97/100
Bayesian/mixed-frequency econometrics reviewer: fail, 92/100
code/runtime alignment reviewer: fail, 86/100
```

The remaining failures were not handled by downgrading the note. They were
handled by adding the missing discussion and live runtime infrastructure.

Econometrics fixes added to the note:

1. Replaced the shorthand annual state-space measurement with the general
   annualization operator `A_a(.)`.
2. Added an explicit state vector, transition equation, observation equation,
   covariance structure, and Kalman likelihood recursion.
3. Added measurement-scale anchoring:

```text
alpha_anchor = 0
lambda_anchor = 1
```

with sensitivity required for freeing other `lambda_j`.

4. Added factor normalizations:

```text
Var(f) = 1
lambda_anchor > 0
rank(Lambda_c) fixed before estimation
```

5. Added minimum solve-mass and filtered effective sample-size gates:

```text
Pr(Solve(theta)=pass | data) >= 0.50
filtered effective sample size >= 100
```

for prototype posterior use, with tighter standards for paper reporting.

6. Defined bounded-debt diagnostics as horizon-level maximum/terminal debt
deviation plus a transition spectral-radius diagnostic when available.
7. Labeled the 100-draw gate as a harness smoke test, not posterior evidence.
8. Replaced remaining loose "LPT-style" wording with "LPT-motivated" where the
   claim did not immediately include the structural-posterior caveat.

Runtime/code fixes implemented:

1. Added `fiscal_rule_layer` to `calibrate` in:

```text
MCMS-private/src/calibration.jl
```

with default:

```text
:sectoral_c2_sut
```

and opt-in:

```text
:hmf_candidate
```

2. Added `validate_fiscal_rule_matrices!` to check country order, closure,
   required matrix fields, dimensions, and finite entries.
3. Added `load_fiscal_rule_matrices` so HMF artifacts can be selected only
   through a validated loader.
4. Added a blocked HMF candidate stub:

```text
MCMS-private/input_data/fiscal_rules_hmf/hmf_runtime.jl
MCMS-private/input_data/fiscal_rules_hmf/metadata.json
```

The stub establishes the generated-Julia API but has:

```text
runtime_readiness_flag = "not_runtime_ready_stub"
```

so `calibrate(fiscal_rule_layer=:hmf_candidate)` is blocked until a real
posterior-estimated, solve-filtered artifact replaces it.

5. Added:

```text
MCMS-private/scripts/check_hmf_runtime.jl
MCMS-private/scripts/check_fiscal_rule_selector.jl
MCMS-private/scripts/check_solve_status_only.jl
```

6. Added `solve_status_only` to:

```text
MCMS-private/src/solve_onkio.jl
```

This returns solve status and failure reason without IRF export.

Verification:

```text
julia-1.11.1 --project=. scripts/check_hmf_runtime.jl
```

passed and reported the HMF stub as blocked from runtime use.

```text
julia-1.11.1 --project=. scripts/check_fiscal_rule_selector.jl
```

passed: the default layer loaded a 4-by-44 matrix and the HMF candidate was
blocked by the readiness guard.

```text
julia-1.11.1 --project=. scripts/check_solve_status_only.jl
```

reached `solves: true` and `stage: solve`, but the command exceeded the tool
timeout after the expensive parse/solve path. Treat this as behavioral
verification with a timeout caveat, not as a clean fast CI check.

## Round 3 final reviewer status and user override

Final rerun scores:

```text
data-accounting/calibration reviewer: pass, 96/100
DSGE/fiscal theory critic: pass, 96/100
devils-advocate: pass, 96/100
derivation auditor: pass, 97/100
Bayesian/mixed-frequency econometrics reviewer: pass, 96/100
code/runtime alignment reviewer: fail under strict threshold, 93/100
```

The final code/runtime reviewer agreed that the major unsafe runtime path was
fixed: `calibrate` now has a fiscal-rule-layer selector, runtime matrices are
validated on load, the HMF candidate is guarded by `runtime_readiness_flag`,
and the HMF stub is blocked from silent runtime promotion.

Residual code/runtime findings at 93/100:

1. `solve_status_only` avoids IRF export but still computes decision rules and
   does not yet return explicit QZ/BK counts or bounded-debt diagnostics.
2. `check_hmf_runtime.jl` validates the HMF stub API and readiness guard, but
   cannot yet compare HMF CSV summaries to generated Julia matrices because no
   real posterior HMF matrix CSVs exist.
3. The HMF artifact directory is a guarded API stub, not a full prototype
   output set with posterior summaries, draw summaries, and determinacy-filter
   summaries.

User instruction after the 93/100 runtime result:

```text
stop it and continue as if it was passing
```

Loop status:

The adversarial loop is stopped by user instruction. For subsequent work, this
review is to be treated as operationally passing, with the documented caveat
that the strict 95+/100 threshold was achieved by all lanes except the
code/runtime lane, which stopped at 93/100 after the user override.

## Round 4 latent-state-space implementation review

Date: 2026-05-15

User instruction during this round:

```text
Once you have a working version, work towards replace the annual-to-quarterly
shortcut with a latent quarterly state-space layer for tau_C, tau_N, and tau_Y,
then run a meaningful solve filter over posterior draws rather than selecting
one anchored point runtime. Once achieved, document it into the .md file, then
run a full adversarial review, address the comments by changing the code
whenever possible, only weakening claims when code fixes are not possible.
```

Implementation status before review:

1. `scripts/build_hmf_fiscal_rule_estimator.py` now builds
   `latent_quarterly_state_space_panel.csv` and
   `latent_quarterly_state_space_diagnostics.csv`.
2. Annual-observed aggregate instruments use a latent quarterly random-walk
   state with annual-average measurement equations where at least eight annual
   observations exist.
3. Latent-state posterior variance enters as a first-order shock-scale
   inflation before posterior summaries are selected. The implementation does
   not yet simulate full latent paths through the structural MCMS equilibrium.
4. Direct quarterly `tau_Y` remains in place for EA and USA. ROW `tau_N` and
   China/ROW `tau_Y` remain transfer-prior cases because the current database
   lacks the minimum annual coverage.
5. The active 75/25 HMF/C2-SUT runtime solves.
6. A fresh five-draw posterior solve filter was run after the latent-state
   rebuild using the grid `0.0, 0.25, 0.5, 0.75, 1.0`. Draws 1, 3, 4, and 5
   solve at pure HMF; draw 2 fails pure HMF and passes at the active 75/25
   blend.

Round 4 reviewers completed so far:

```text
theory-critic: fail, 72/100 as calibration bridge; 55/100 if judged as full structural LPT
code-critic: fail, 72/100
proofreader: pass, 88/100
code-structurer: fail, 84/100
devils-advocate: fail, 78/100
```

Theory-critic findings and response:

1. **Latent state-space bridge too mechanical.**
   - Code response: latent-state posterior variance is now used as
     first-order shock-scale inflation before posterior summary selection, so
     the smoothed quarterly series no longer enters as if observed without
     uncertainty.
   - Remaining caveat: the state equation is still a deliberately simple
     random-walk bridge, not a full structural fiscal state-space likelihood.
2. **Five posterior draws are not a full filtered posterior.**
   - Code response: no claim of a full 500-draw filtered posterior is made.
     The current result is a validated filtered subset.
   - Remaining caveat: the full posterior filter remains computationally
     expensive.
3. **Anchored HMF/C2-SUT runtime is not pure HMF.**
   - Superseded by the 2026-05-15 cleanup. The active runtime is no longer an
     ex-post HMF/C2-SUT blend; C2-SUT enters through a configurable prior
     strength, and the no-C2-prior case is explicitly available.
4. **Sectoral production-weight state is not jointly estimated.**
   - Documentation response: the note now says annual sectoral weights remain
     a deterministic/proxy allocation layer; only aggregate annual fiscal
     instruments go through the latent quarterly bridge.

Code-critic findings and code response:

1. **Runtime readiness could inherit stale solve evidence.**
   - Fixed in code. Generated HMF runtimes now start as
     `point_runtime_pending_solve_filter`. `check_hmf_solve_status.jl` is
     allowed to solve a pending candidate and marks the runtime
     `point_runtime_solve_ready` only after a passing point-runtime solve. The
     separate `posterior_filter_ready` flag remains false until the draw-level
     posterior gate is met. The determinacy row records
     `generated_julia_checksum`, `source_hash_manifest_sha256`, and BK counts.
2. **Candidate JSON lacked schema/provenance validation.**
   - Fixed in code. Candidate payloads now carry posterior, exposure, and C2
     prior-center hashes. The mutable `metadata.json` hash was removed from
     candidate provenance. The Julia draw filter validates provenance, country
     order, vector lengths, matrix dimensions, finite values, and nonnegative
     C2 prior strength.
3. **Anchor matrices were blended positionally after dropping labels.**
   - Fixed in code and then superseded. Both the HMF builder and candidate
     preparer assert C2-SUT country row order and consecutive sector-index
     columns before using C2-SUT as a prior center.
4. **A malformed candidate could abort a draw-filter batch without a row.**
   - Fixed in code. Candidate-level exceptions are caught and written as
     failed rows with stage `candidate_exception`.
5. **Filter metadata hard-coded the active prior setting and did not distinguish
   candidate-file size from tested rows.**
   - Fixed in code. The summarizer now reads the active prior strength from
     `metadata.json` and records candidate-file SHA, candidate count, prior
     grid, and summary-file SHA.

Devils-advocate findings and response:

1. **`runtime_ready` conflated QZ/BK solution, bounded debt, and posterior
   readiness.**
   - Fixed in code and docs. The runtime now separates QZ/BK `solves=true`
     from strict `admissible=true`. The current candidate solves in QZ/BK but
     fails bounded debt, so `point_runtime_solve_ready=false` and
     `posterior_filter_ready=false`.
2. **Candidate provenance included a mutable metadata hash that the validator
   did not check.**
   - Fixed in code. Candidate provenance now covers the posterior draw file,
     sectoral exposure loadings, and C2 anchor matrices only.
3. **The review response carried a stale checksum.**
   - Fixed in this file. Current checksums are reported from the latest
     regenerated artifacts below.
4. **Draw-filter rows lacked BK counts.**
   - Fixed in code. `solve_status_only`, the point-runtime determinacy row, and
     posterior-draw filter rows now record stable/unstable eigenvalue counts
     and required BK counts.
5. **Latent-state uncertainty was overstated.**
   - Documentation fixed. The implemented bridge is now described as
     first-order shock-scale inflation, not full propagation of latent paths
     through the equilibrium.
6. **The active runtime is a solve-checked posterior median summary, not a
   selected filtered posterior draw.**
   - Fixed in code/docs by adding `runtime_selection_basis =
     posterior_median_point_solve_with_c2_sut_tau_y_anchor`.
7. **The draw grid omitted pure HMF.**
   - Fixed in code and rerun. Default grids now include `0.0`; the latest
     five-draw diagnostic actually tested pure HMF first.

Code/runtime re-review findings and response:

1. **Checksum-bound readiness was asserted but not enforced at load time.**
   - Fixed in code. `calibration.jl` now validates the live `hmf_runtime.jl`
     checksum and structural runtime hash against `metadata.json` and
     `determinacy_filter_summary.csv` before allowing normal
     `fiscal_rule_layer=:hmf_candidate` use.
2. **The solve script solved a pending runtime and then mutated the readiness
   marker, so the solved file checksum and ready file checksum differed.**
   - Fixed in code. `check_hmf_solve_status.jl` now records both
     `pre_solve_julia_checksum` and `generated_julia_checksum`, plus pre/post
     structural runtime hashes. It errors if the structural hash changes while
     marking readiness.
3. **Provenance did not bind the code used to produce artifacts.**
   - Fixed in code. The HMF source-hash manifest now includes the HMF builder,
     solve-status checker, candidate preparer, draw-filter checker,
     draw-filter summarizer, fiscal-rule loader, and solver source files in
     addition to upstream data files.
4. **Draw-level diagnostics still lacked memory and bounded-debt columns.**
   - Fixed in code. The draw filter now writes max-resident-memory
     before/after columns, explicit `bounded_debt_status`, debt-block spectral
     radius, and a strict `admissible` column. Draws that solve but fail the
     debt-block diagnostic are recorded as `failed_bounded_debt_filter`.

Verification after code fixes:

```text
python -B scripts/build_hmf_fiscal_rule_estimator.py --draws 500 --tau-y-c2-prior-obs-equiv 25
julia --project=. scripts/check_hmf_solve_status.jl
python -B scripts/prepare_hmf_posterior_draw_filter_candidates.py --draws 1 2 3 4 5 --tau-y-c2-prior-grid 0 5 10 25 50 100
julia --project=. scripts/check_hmf_posterior_draw_filter.jl input_data/fiscal_rules_hmf/posterior_draw_filter_candidates.json --validate-only
python -B scripts/summarize_hmf_posterior_draw_filter.py
julia --project=. scripts/check_hmf_runtime.jl
```

Current evidence:

```text
runtime_readiness_flag = point_runtime_pending_solve_filter
point_runtime_solve_ready = false
posterior_filter_ready = false
determinacy status = failed_bounded_debt_filter
solves = true
admissible = false
debt_feedback_closure = none
runtime_selection_basis = posterior_summary_with_c2_sut_tau_y_prior
tau_y_c2_prior_obs_equiv = 25.0
pre-solve checksum = a3e85233ba7c4d4d1d5eb1be60561768719111ed08fb5253977008748336f76e
determinacy checksum = a3e85233ba7c4d4d1d5eb1be60561768719111ed08fb5253977008748336f76e
runtime structural checksum = 764e9ea95b74aa901e82903595c595c8f07921cb3ba1bef982596a19d6dc6e36
source hash manifest = 36e3eb35ba38aff9854c5f0cbbe76c10412233e2cb942a26156c2c96ad4ac426
determinacy BK counts = 1885 stable / 1885 required; 723 unstable / 723 required
bounded debt status = failed_debt_block_spectral_radius
point runtime debt-block spectral radius = 1.01214862942549
posterior draw filter = strict admissibility harness validated with code/data provenance
candidate file = 30 draw/prior candidates over C2 prior strengths 0, 5, 10, 25, 50, 100
candidate file checksum = 79f44e7c017522e9ee34cf7897b96df88d6e42650441e0308fb2f0d82497ef0c
fixed active-prior candidate file = 100 code-bound candidates at tau_y_c2_prior_obs_equiv 25
code-bound active-prior smoke filter = 1 completed draw, QZ/BK solves but admissible=false
smoke draw debt-block spectral radius = 1.009976083688932
smoke candidate file checksum = 83bd9bc6cfef372e2102657a4cb0bd7270b88b7b43b2a3ec1d460e529aacc438
smoke summary checksum = f03504f2f3a5e481111f6581c44662fc63ea63f2810ec5f0a62bd445ea73c997
code-bound active-prior ESS proxy = 0 / 100; posterior_ready_gate_passed = false
```

Round 4 status:

The major code-level review findings have been addressed by code changes rather
than by weakening claims wherever feasible. The new substantive finding is that
the clean unscaled Bayesian path rejects the current active runtime under the
bounded-debt admissibility filter. The next fix should condition posterior
summaries on accepted draws, or change the model closure/prior so accepted
draws exist without ex-post debt-feedback scaling. Because the reviewer scores
remain below the strict 95/100 stopping threshold, the review is not recorded
as fully passed.

## Clean Bayesian admissibility update, 2026-05-15

The debt-feedback runtime scaling has been removed from the estimator, candidate
generator, generated runtime metadata, and Julia provenance validator. `Phi_b`
is now selected by the declared posterior rule with `debt_feedback_closure =
none`; there is no hidden multiplication by 2, 5, or any other runtime factor,
and no nonnegative debt-feedback clipping.

The admissibility filter now treats QZ/BK and bounded debt separately. The
current point runtime has:

```text
solves = true
admissible = false
status = failed_bounded_debt_filter
debt_block_spectral_radius = 1.01214862942549
```

The one-draw active-prior smoke filter has:

```text
solves = true
admissible = false
status = failed_bounded_debt_filter
debt_block_spectral_radius = 1.009976083688932
provenance_status = matched
```

This is the correct failure mode for the clean Bayesian version: runtime
parameters must be posterior summaries conditional on stationary `rho`,
hierarchical transfer priors, sectoral `tau_Y` measurement error, QZ/BK
solution, and bounded debt. The current artifacts provide the machinery, but
not yet an admissible filtered posterior.

## Issues 1-4 calibration cleanup, 2026-05-15

1. C2-SUT prior strength is now an explicit hyperparameter:
   `--tau-y-c2-prior-obs-equiv`. The baseline remains 25 observation-equivalents
   and is labelled as a prior choice, not data evidence.
2. Zero C2 prior is allowed. `--tau-y-c2-prior-obs-equiv 0` runs, candidate
   validation accepts 0, and `posterior_draw_filter_candidates.json` includes
   the grid `0, 5, 10, 25, 50, 100`.
3. Silent persistence caps were removed from selected runtime summaries and
   draw-filter candidates. `rho_selected` now equals `rho_p50`; stationarity and
   determinacy are filter outcomes.
4. Silent output-response clipping for `tau_C` and `tau_N` was removed.
   `Phi_y_selected` now equals `Phi_y_p50`; sign/range failures are left to the
   explicit admissibility filter.

Additional hidden tricks removed while addressing these issues:

- `debt_feedback_closure` is now `none`.
- `Phi_b_selected` now equals `Phi_b_p50`.
- The sectoral `tau_Y` runtime is no longer an ex-post HMF/C2 coefficient blend;
  C2-SUT enters as a configurable prior center and prior precision.

The cleaned active runtime still fails bounded debt, so this is a more honest
candidate, not a solved baseline.
