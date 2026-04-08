# Session Log: Codex Migration

## Goal

Migrate the branch from Claude-first workflow control to Codex-first instructions without disturbing existing project content or unrelated local edits.

## Key Decisions

- Added `AGENTS.md` as the new root behavior contract.
- Replaced hook-driven and slash-command-oriented guidance with explicit workflow documents in `docs/codex-workflows/`.
- Kept `.claude/` in place as legacy reference instead of deleting it.
- Rewrote `README.md` and reduced `CLAUDE.md` to a legacy pointer.

## Verification

- Read back `AGENTS.md` and `README.md`.
- Listed the new files in `docs/codex-workflows/`.
- Confirmed the branch name is `codex-migration`.
- Regenerated `guide/workflow-guide.html` from the rewritten `guide/workflow-guide.qmd`.
- Synced the regenerated guide to `docs/workflow-guide.html`.
- Rewrote `docs/index.html` to match the Codex-first branch narrative.

## Open Items

- Existing `.claude/` rules, hooks, and skills remain in the repo for reference and are not functionally consumed by Codex.
