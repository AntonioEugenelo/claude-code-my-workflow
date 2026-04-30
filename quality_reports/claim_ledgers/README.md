# Claim Ledgers

Claim ledgers bind manuscript claims to figures, tables, data files, and
verification formulas. Use a ledger before broad result audits, figure audits,
or text updates that depend on generated outputs.

## Required Columns

| Column | Purpose |
| --- | --- |
| `claim_id` | Stable identifier, e.g. `S5-F3-C02`. |
| `location` | Source text path and line/section. |
| `claim_text` | Exact claim or concise paraphrase. |
| `artifact` | Figure/table/output that supports the claim. |
| `source_data` | `.mat`, `.csv`, `.tex`, log, or script output used to verify. |
| `formula_or_check` | Computation or comparison rule. |
| `current_value` | Verified value or qualitative status. |
| `tolerance` | Numeric tolerance or qualitative acceptance criterion. |
| `status` | `pending`, `pass`, `fail`, `blocked`, or `stale`. |
| `last_checked` | Date and command/reference used. |

Start from `TEMPLATE.md` for new audits.
