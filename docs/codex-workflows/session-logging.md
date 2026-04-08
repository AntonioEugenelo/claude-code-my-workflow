# Session Logging

Use `quality_reports/session_logs/YYYY-MM-DD_description.md` with `templates/session-log.md`.

## Required Logging Moments

1. After a plan is settled for non-trivial work.
2. When a meaningful design decision or correction changes the approach.
3. At session end with outcome, verification state, and open questions.

## What to Capture

- Goal and scope
- Key decisions and rationale
- Files changed
- Verification commands and results
- Open issues, blockers, or follow-up work

## Merge Reports

Create merge reports only at merge time, not for every intermediate commit.

- Location: `quality_reports/merges/YYYY-MM-DD_branch-name.md`
- Template: `templates/quality-report.md`

## Repo Map Maintenance

When structure changes materially, especially in `master_supporting_docs/MCMS/` or `master_supporting_docs/Tariffs_ECB/`, update any repo map or equivalent structure notes instead of leaving that knowledge only in chat.
