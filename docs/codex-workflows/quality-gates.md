# Quality Gates

This is the authoritative source for workflow thresholds and scoring expectations on the Codex branch.

## Universal Thresholds

| Score | Gate | Meaning |
| --- | --- | --- |
| `90/100` | Commit | Minimum for production work |
| `95/100` | External review | Ready for collaborators, supervisors, or peer review |
| `98/100` | Send / deploy | Ready to publish, submit, or distribute |
| `60/100` | Exploration | Minimum for `explorations/` fast-track work |

## Enforcement

- Below `90`: do not treat the work as production-ready.
- `90-94`: commit-ready, but still below external-review quality.
- `95-97`: ready for external review.
- `98+`: ready to send, publish, or deploy.
- Overrides must be explicit and justified.

## Scoring Principle

The review pass is the scoring authority. Do not estimate a post-fix score from memory. Re-run the relevant review checklist, scorer, or verification pass on the current files.

## Typical Deductions

### Cover Letters / Proposals

| Severity | Issue | Deduction |
| --- | --- | --- |
| Critical | Wrong recipient, institution, or programme facts | `-30` to `-50` |
| Critical | Compilation failure | `-100` |
| Critical | Missing core section or length breach | `-20` to `-30` |
| Major | Generic fit, unsupported claims, tone mismatch | `-5` to `-10` |
| Minor | Grammar, typos, formatting drift | `-1` to `-2` each |

### Slides and Quarto

| Severity | Issue | Deduction |
| --- | --- | --- |
| Critical | Compilation/render failure | `-100` |
| Critical | Broken citations or equation overflow | `-15` to `-20` |
| Major | Text overflow, layout collisions, notation drift | `-3` to `-5` |
| Minor | Font-size shrinkage, avoidable formatting clutter | `-1` each |

### Research Papers

| Severity | Issue | Deduction |
| --- | --- | --- |
| Critical | Derivation error affecting results | `-50` |
| Critical | Compilation failure | `-100` |
| Critical | Literature-positioning factual error | `-30` |
| Major | Unjustified assumption, missing comparison, notation drift | `-3` to `-10` |
| Minor | Grammar and typos | `-2` each |

### Code and Analysis

| Severity | Issue | Deduction |
| --- | --- | --- |
| Critical | Syntax/runtime failure | `-100` |
| Critical | Domain bug or hard-coded path | `-20` to `-30` |
| Major | Missing reproducibility controls or missing generated output | `-5` to `-10` |
| Minor | Style and structure issues | `-1` each |

## Numerical Tolerances

Use explicit tolerances when verifying reproduced results:

| Quantity | Tolerance |
| --- | --- |
| Integer counts | Exact match |
| Point estimates | `< 0.01` unless stricter project rules apply |
| Standard errors | `< 0.05` unless bootstrap noise is expected |
| Percentages | `< 0.1pp` |
| Project-specific model moments | Use the tighter source-specific tolerance if documented |

## Reports

- Save merge-time quality reports in `quality_reports/merges/`.
- Use `templates/quality-report.md`.
