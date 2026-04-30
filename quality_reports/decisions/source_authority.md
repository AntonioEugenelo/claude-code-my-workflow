# Source Authority Guard

Use this before pull, push, Overleaf sync, branch merge, or cross-repo copy.

## Default Authorities

| Area | Default authority | Guard before write/sync |
| --- | --- | --- |
| Workflow infrastructure | Local git branch | Check `git status --short --branch` and active decision locks. |
| `.claude/` compatibility material | Preserved upstream/reference material | Do not delete or rewrite unless the task is Claude compatibility migration. |
| `.codex/` runtime material | Local Codex-first branch | Verify `codex features list` after config changes. |
| Paper source in nested Overleaf repos | Project-specific; often Overleaf remote | Check nested repo status/remotes first. Prefer status before pull/push. |
| Generated figures/PDF/HTML | Derived artifacts | Regenerate from source or document why reuse is valid. |
| Model outputs (`.mat`, `.csv`, logs) | Producing script and run card | Do not treat copied outputs as authoritative without source/run evidence. |

## Required Check Before Sync

1. Identify repository root and nested repo, if any.
2. Report current branch, HEAD, dirty files, and remote delta.
3. State which side is authoritative for this task.
4. State what could be overwritten.
5. Ask for confirmation before destructive or authority-changing actions.

## Current Known Risks

- `master_supporting_docs/` can contain nested repos/submodules.
- Overleaf source can be newer than local paper source.
- Generated outputs can look current while being produced from stale `.mat` or preprocessing inputs.
- Branch names in this workspace often encode project state; do not infer authority from branch name alone.
