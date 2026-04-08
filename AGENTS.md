# AGENTS.md

This repository is configured for Codex-first use.

## Operating Principles

- Plan first for non-trivial tasks. If a task is likely to touch more than 3 files, take more than 30 minutes, or has multiple valid interpretations, write a plan to `quality_reports/plans/YYYY-MM-DD_short-description.md` before editing.
- Verify after edits. Do not report completion on LaTeX, Quarto, code, or data tasks until the relevant output has been compiled, rendered, executed, or otherwise checked.
- Treat source files as authoritative. For writing projects, `.tex`, `.qmd`, `.R`, `.py`, `.m`, and source figure scripts are the source of truth. PDFs, rendered HTML, and exported figures are derived artifacts.
- Keep context on disk. Plans belong in `quality_reports/plans/`, session notes in `quality_reports/session_logs/`, merge reports in `quality_reports/merges/`, and persistent lessons in `MEMORY.md`.
- Use explicit review passes instead of self-approval. After material fixes, re-run the relevant review checklist before claiming the issue is resolved.

## Startup Routine

1. Read this file.
2. If the task touches `master_supporting_docs/Tariffs_ECB/` and this is the first Codex call on the current branch/session, check Overleaf status first using the repo machinery in `scripts/sync-overleaf.sh` before editing. Prefer `status` first, then `pull` if remote changes are present or the user asks to sync.
3. For non-trivial work, read the latest relevant plan in `quality_reports/plans/`.
4. Check `git status` before editing.
5. Read the workflow docs in `docs/codex-workflows/` that match the task.

## Core Workflows

- Planning and ambiguity handling: `docs/codex-workflows/plan-first.md`
- Implement-verify-review loop: `docs/codex-workflows/orchestrator.md`
- Review lens selection by document type: `docs/codex-workflows/review-routing.md`
- Session logging and merge reporting: `docs/codex-workflows/session-logging.md`
- Capability map for common requests: `docs/codex-workflows/capabilities.md`
- Migration notes from the previous Claude-first setup: `docs/codex-migration.md`

## Repository Notes

- `master_supporting_docs/` contains active paper, model, and supporting material. Treat nested git repos and submodules carefully.
- `scripts/` contains reusable automation. Prefer using or extending these scripts over reimplementing workflow logic in prose.
- `templates/` contains plan, quality-report, and session-log templates.
- `.claude/` is retained as legacy reference material. Do not rely on its hooks, slash commands, or Claude-specific runtime semantics for Codex behavior.

## Review and Quality

- Use the quality thresholds in `docs/codex-workflows/orchestrator.md`. The inherited default gates are 90 for commit-ready work, 95 for external review, 98 for send/deploy, and 60 for exploratory work.
- When a task materially changes prose, analysis, or outputs, perform a review pass using the correct lenses from `docs/codex-workflows/review-routing.md`.
- Do not estimate post-fix scores from memory. Re-check the current files.

## Capability Triggers

If the user asks to proofread, review, compile, translate to Quarto, validate citations, draft a letter, analyze data, or prepare a deployment, follow the matching procedure in `docs/codex-workflows/capabilities.md`.
