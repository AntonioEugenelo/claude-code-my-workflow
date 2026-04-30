# Source Authority Workflow

Use this workflow before pull, push, Overleaf sync, branch merge, or copying
outputs across repositories.

## Required Inputs

- `quality_reports/decisions/ACTIVE.md`
- `quality_reports/decisions/source_authority.md`
- `git status --short --branch` for the parent repo
- nested repo status/remotes when the task touches `master_supporting_docs/`

## Procedure

1. Identify the authoritative source for this task.
2. Check dirty files and unpushed/unpulled commits.
3. State what action could overwrite or stale existing work.
4. For Overleaf, prefer `status` before `pull` or `push`.
5. Ask for confirmation before destructive or authority-changing actions.

## Report Format

- `authority`:
- `current_branch`:
- `dirty_state`:
- `remote_delta`:
- `overwrite_risk`:
- `recommended_action`:
