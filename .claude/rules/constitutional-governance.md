# Constitutional Governance: DSGE Model Replication Project

**Non-negotiable principles for this project.**

---

## Article I: Single Source of Truth

Cox et al. (2025) PDF is authoritative for the baseline model specification. Eugenelo `.tex` files are authoritative for extensions. Dynare `.mod` files in `model/` are authoritative for implementation.

**Why:** Three-layer traceability: paper → theory → code. Every model equation must trace to a numbered equation in the source paper.

**Exceptions:** Shock processes (AR(1) specification) not fully specified in Cox et al. — document any additions explicitly.

---

## Article II: Plan-First Threshold

Enter plan mode for tasks requiring >3 files or multi-step workflows.

**Why:** DSGE model implementation involves tightly coupled equations — a change to one equation cascades. Planning prevents mid-implementation pivots.

**Exceptions:** Exploration folder allows fast-track. Single-file typo fixes skip planning.

---

## Article III: Quality Gate

Nothing commits below **90/100**. Numerical tolerances from `quality-gates.md`: steady-state 1e-10, IRF 1e-6, welfare 1e-8, special-case nesting exact.

**Why:** Replication requires exact match to published results. Numerical errors propagate through the Ramsey solution.

**Exceptions:** WIP branches explicitly marked. Exploratory work in `explorations/` uses 60/100.

---

## Article IV: Mathematical Rigour

All model equations must be:
1. Traceable to a numbered equation in Cox et al. (2025) or Eugenelo extension paper
2. Notation-consistent across the entire model (paper notation → Dynare variable names documented)
3. Verified via special-case nesting: setting extension parameters to baseline values (kappa=0, sigma=1) must reproduce Cox et al. exactly

**Why:** The model extends a published paper. Any deviation from the source must be intentional and documented.

**Exceptions:** None. Fix before committing.

---

## Article V: Compilation Verification

Dynare must solve before commit: Blanchard-Kahn conditions satisfied, steady state exists, no NaN/Inf in policy functions. For LaTeX files, standard compilation rules apply.

**Why:** A model that doesn't solve is worse than no model — it gives false confidence.

**Exceptions:** Known Dynare warnings documented in session log.

---

## User Preferences (Override Anytime)

- Number of sectors K for test runs
- Calibration parameter choices within standard ranges
- Solution method (direct FOCs vs. `ramsey_model`)
- Output format (figures, tables, log files)
- Extension ordering (kappa first vs. CRRA first vs. constrained G first)

---

## Requesting Amendment

When deviating from an article, ask:

> "Are you **amending Article X** (permanent change) or **overriding for this task** (one-time exception)?"
