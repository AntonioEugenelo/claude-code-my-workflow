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
   - Response: this is retained as a true description of the active runtime.
     The new draw filter also reports that pure HMF passes for four of the five
     diagnostic draws, while draw 2 requires the 25 percent C2-SUT anchor.
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
     anchor-matrix hashes. The mutable `metadata.json` hash was removed from
     candidate provenance. The Julia draw filter validates provenance, country
     order, vector lengths, matrix dimensions, finite values, and anchor/HMF
     weights summing to one.
3. **Anchor matrices were blended positionally after dropping labels.**
   - Fixed in code. Both the HMF builder and candidate preparer now assert
     C2-SUT country row order and consecutive sector-index columns before
     blending.
4. **A malformed candidate could abort a draw-filter batch without a row.**
   - Fixed in code. Candidate-level exceptions are caught and written as
     failed rows with stage `candidate_exception`.
5. **Filter metadata hard-coded the active anchor and did not distinguish
   candidate-file size from tested rows.**
   - Fixed in code. The summarizer now reads the active anchor from
     `metadata.json` and records candidate-file SHA, candidate count, anchor
     grid, and summary-file SHA.

Devils-advocate findings and response:

1. **`runtime_ready` conflated a point solve with posterior readiness.**
   - Fixed in code and docs. The runtime now separates
     `point_runtime_solve_ready=true` from `posterior_filter_ready=false`.
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
   - Partly fixed in code. The draw filter now writes max-resident-memory
     before/after columns and explicit `bounded_debt_status` and
     `timeout_status` fields. Bounded-debt remains marked
     `not_evaluated_solve_only` until a separate debt-dynamics diagnostic is
     implemented.

Verification after code fixes:

```text
python -B scripts/build_hmf_fiscal_rule_estimator.py --draws 500 --tau-y-anchor-weight 0.25
julia --project=. scripts/check_hmf_solve_status.jl
python -B scripts/prepare_hmf_posterior_draw_filter_candidates.py --draws 1 2 3 4 5 --tau-y-anchor-grid 0.0 0.25 0.5 0.75 1.0
julia --project=. scripts/check_hmf_posterior_draw_filter.jl --skip-draw-after-pass
python -B scripts/summarize_hmf_posterior_draw_filter.py
julia --project=. scripts/check_hmf_runtime.jl
```

Current evidence:

```text
runtime_readiness_flag = point_runtime_solve_ready
point_runtime_solve_ready = true
posterior_filter_ready = false
determinacy status = passed_solve_status_only
pre-solve checksum = 145c95dc7661c39e358dd39e31bf06d3b53a7ce0f1cb1bdc6dcceba2433433be
determinacy checksum = 1da5e950ca1213633fcdcc412025db16b129294403c64c8d82cbef62c4db4e9f
runtime structural checksum = c196eaa619ea723708665fbb3435ce4ac84a160e0b51687fedc6a2d82e5ba87f
source hash manifest = 30681530365440fa4740931ba5bdce423768fbd37f783e7711da6af828739dec
determinacy BK counts = 1885 stable / 1885 required; 723 unstable / 723 required
posterior draw filter = 6 tested candidates across 5 latent-state-space draws
posterior draw filter result = all 5 draws have at least one passing anchor
minimum passing anchor = 0.0 for draws 1, 3, 4, 5; 0.25 for draw 2
candidate file = 25 draw-anchor candidates with source and C2-anchor provenance hashes
candidate file checksum = 38c524c79996469b7a760134e5616897dd45b527bc3d4868edff1f86f6ea2568
fixed active-anchor candidate file = 100 code-bound candidates at tau_y_solution_anchor_weight 0.25
code-bound active-anchor smoke filter = 1 completed draw, 1 passing, active_anchor_solve_rate 1.0
code-bound active-anchor ESS proxy = 1 / 100; posterior_ready_gate_passed = false
```

Round 4 status:

The major code-level review findings have been addressed by code changes rather
than by weakening claims wherever feasible. The remaining unresolved issue is
substantive rather than a bug: this is still a fiscal-rule-block bridge and
filtered subset, not a full 500-draw solve-filtered posterior and not a full
structural LPT posterior. Because the reviewer scores remain below the strict
95/100 stopping threshold, the review is not recorded as fully passed.
