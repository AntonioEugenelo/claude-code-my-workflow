# Quality Gates & Scoring Rubrics

**Single authoritative source for all quality thresholds. Referenced by orchestrator, agents, and CLAUDE.md.**

---

## Universal Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| **90/100** | Commit | Minimum for production work |
| **95/100** | Review | Ready for supervisor/peer review |
| **98/100** | Send/Deploy | Ready to submit or publish |
| **60/100** | Exploration | Minimum for `explorations/` folder (fast-track) |

## Enforcement

- **Score < 90:** Block commit. List blocking issues.
- **Score 90--94:** Allow commit, flag for review before sending/deploying.
- **Score >= 95:** Ready for external review.
- **Score >= 98:** Ready to send/deploy.
- User can override with justification.

## Scoring Method

Start at 100. Deduct for issues found using the document-specific rubric below.

---

## Cover Letters & Proposals (`Letters/**/*.tex`)

### Critical (any one blocks submission)

| Issue | Deduction |
|-------|-----------|
| Wrong recipient name or institution | -50 |
| Factual error (dates, programme name, faculty name) | -30 |
| Compilation failure | -100 |
| Exceeds target length (1 page for letters; 2pp body + 1pp refs for proposals) | -30 |
| Missing key section (purpose / fit / qualifications) | -20 |

### Major

| Issue | Deduction |
|-------|-----------|
| Generic opening ("To Whom It May Concern") | -10 |
| No specific faculty or programme mentioned | -10 |
| Tone mismatch (too casual or too stiff) | -5 |
| Unfilled TODO/placeholder in final version | -15 |
| Paragraph with no substantive content | -5 |
| Claims without evidence | -5 |

### Minor

| Issue | Deduction |
|-------|-----------|
| Grammar error | -2 each |
| Typo | -2 each |
| Inconsistent formatting (dates, titles) | -1 each |
| Overly long sentence (>40 words) | -1 each |
| Passive voice where active is stronger | -1 each |

### Anti-Patterns

| Pattern | Why It's Bad |
|---------|-------------|
| "I am passionate about..." | Cliche, says nothing specific |
| "I believe I am the ideal candidate" | Presumptuous |
| Listing courses taken | Not relevant for research exchange |
| Name-dropping without substance | Transparent and unconvincing |
| "As you can see from my CV..." | The letter should stand alone |
| Copy-pasting from another application | Generic, tone-deaf |

---

## Beamer Slides (`Slides/**/*.tex`)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | XeLaTeX compilation failure | -100 |
| Critical | Undefined citation | -15 |
| Critical | Overfull hbox > 10pt | -10 |
| Critical | Equation overflow | -20 |
| Major | Text overflow | -5 |
| Major | TikZ label overlap | -5 |
| Major | Notation inconsistency | -3 |
| Minor | Font size reduction | -1 per slide |

---

## Quarto Slides (`Quarto/**/*.qmd`)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Compilation failure | -100 |
| Critical | Equation overflow | -20 |
| Critical | Broken citation | -15 |
| Critical | Typo in equation | -10 |
| Major | Text overflow | -5 |
| Major | TikZ label overlap | -5 |
| Major | Notation inconsistency | -3 |
| Minor | Font size reduction | -1 per slide |
| Minor | Long lines (>100 chars) | -1 (EXCEPT documented math formulas) |

---

## R Scripts (`scripts/**/*.R`)

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Syntax errors | -100 |
| Critical | Domain-specific bugs | -30 |
| Critical | Hardcoded absolute paths | -20 |
| Major | Missing set.seed() | -10 |
| Major | Missing figure generation | -5 |

---

## Research Papers

| Severity | Issue | Deduction |
|----------|-------|-----------|
| Critical | Derivation error that propagates to main results | -50 |
| Critical | Compilation failure | -100 |
| Critical | Factual error in literature positioning | -30 |
| Major | Unjustified assumption | -10 |
| Major | Missing comparative static | -5 |
| Major | Notation inconsistency | -3 |
| Minor | Grammar error | -2 each |
| Minor | Typo | -2 each |

---

## Tolerance Thresholds (Numerical Research)

| Quantity | Tolerance | Rationale |
|----------|-----------|-----------|
| IRF peak responses | 1e-6 | Dynare numerical precision |
| Welfare losses | 1e-8 | Second-order approximation accuracy |
| Steady-state values | 1e-10 | Solver convergence criterion |
| Calibrated parameters | Exact match to source | No rounding unless stated |

---

## Quality Reports

Generated **only at merge time**. Use `templates/quality-report.md` for format.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md`.
