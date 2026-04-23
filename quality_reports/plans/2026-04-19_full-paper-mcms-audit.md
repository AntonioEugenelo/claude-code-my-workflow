# Plan: Full Paper MCMS Audit

**Date:** 2026-04-19
**Status:** IN PROGRESS

## Scope

Run a deep audit of the tariff paper against the MCMS model and figure-generation pipeline.

This task has three linked outputs:

1. a numbers audit for manuscript claims
2. a figure/pipeline alignment audit for what each picture represents, what shock it uses, and what the surrounding text says about it
3. an adversarial code review of the MCMS generation pipeline itself

## Constraints

- Use the MCMS model and generation pipeline as the source of truth.
- Do not validate claims by citing the paper back to itself.
- Keep the audit evidence on disk under `quality_reports/`.
- Treat the current dirty worktree as pre-existing; avoid unrelated edits.
- Use read-only review agents for the adversarial review phases.

## Likely Files

- `master_supporting_docs/Tariffs_ECB/0_clean/**/*.tex`
- `master_supporting_docs/MCMS/**/*.py`
- `master_supporting_docs/MCMS/**/*.m`
- `master_supporting_docs/MCMS/output_python/**/*`
- `master_supporting_docs/MCMS/output_matlab/**/*`
- `quality_reports/specs/2026-04-19_full-paper-mcms-audit.md`
- `quality_reports/reviews/2026-04-19_full-paper-mcms-audit_adversarial.md`
- `quality_reports/reviews/2026-04-19_mcms-code-adversarial.md`
- `quality_reports/session_logs/2026-04-19_full-paper-mcms-audit.md`

## Work Plan

1. Inventory manuscript claims and figure references that need model-backed checking.
2. Map each figure/table claim to the MCMS code path, saved outputs, and shock definition.
3. Recompute or verify quoted numbers directly from MCMS-generated data wherever possible.
4. Write an audit memo that records each checked claim, verdict, evidence path, and any discrepancy.
5. Run the adversarial review loop on the audit memo.
6. Run an adversarial code review on the MCMS generation code with read-only code reviewers.
7. Update the audit memo with any live reviewer findings and save the final state.

## Verification

- `git status --short`
- `./scripts/sync-overleaf.sh status`
- local extraction of manuscript numbers and figure references from `0_clean/sections/*.tex`
- local inspection of MCMS `.m`, `.py`, `.csv`, and `.mat` sources
- `python scripts/review_plan.py ... --adversarial`
- `./scripts/review-mode.sh start ...`
- read-only reviewer passes for document and code audit outputs

## Assumptions

- "All the numbers quoted in the paper" means numerically explicit manuscript claims in the active `0_clean/sections/*.tex` source, excluding bibliography metadata and author affiliations.
- "Pictures" means manuscript figures generated from the MCMS pipeline or included from MCMS-produced outputs; if a figure is hand-authored or external, the audit will flag it separately.
- The deliverable is an audit report, not manuscript edits, unless a later user instruction asks for fixes.
