# Claim Ledger Workflow

Use a claim ledger for result audits, figure audits, numeric-claim checks, and
paper revisions that depend on generated outputs.

## When Required

Create or update `quality_reports/claim_ledgers/<date>_<scope>.md` when the
user asks to:

- check all numbers in text,
- compare figures against captions or prose,
- verify whether text should change after regenerated figures,
- audit results across model specifications,
- prepare submission-ready empirical or computational claims.

## Procedure

1. Freeze the target: branch, commit, manuscript path, active figure/table list.
2. Extract claims only from live source files, not draft-only material.
3. For each claim, identify the supporting artifact and source data.
4. Write the formula/check and tolerance before computing.
5. Mark each claim `pass`, `fail`, `blocked`, or `stale`.
6. Update prose only after the ledger identifies the necessary changes.

## Rule

Do not answer "is the text correct?" globally. Answer from the ledger: which
claims pass, which fail, and which are blocked.
