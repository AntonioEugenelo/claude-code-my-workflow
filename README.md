# Codex Academic Workflow

This branch is the Codex-native migration of the original Claude-oriented academic workflow. It keeps the useful repository structure, templates, and automation scripts, and now combines Codex-readable workflow docs with a narrow layer of repo-local Codex hook enforcement where the current Codex runtime supports it.

## Quick Start

Open the repository in Codex and start from `AGENTS.md`. For any non-trivial task, Codex should also read the matching guide in `docs/codex-workflows/`.

Core entrypoints:

- `AGENTS.md`: primary instructions for Codex
- `docs/codex-workflows/plan-first.md`: planning and ambiguity handling
- `docs/codex-workflows/orchestrator.md`: implement, verify, review, fix loop
- `docs/codex-workflows/quality-gates.md`: authoritative thresholds and scoring expectations
- `docs/codex-workflows/review-routing.md`: review-agent routing by file type
- `docs/codex-workflows/review-agents.md`: active read-only review-agent layer
- `docs/codex-workflows/adversarial-review.md`: adversarial review loop
- `docs/codex-workflows/capabilities.md`: replacement for old slash-command skills
- `docs/codex-workflows/working-conventions.md`: source-of-truth, exploration, and reproducibility conventions
- `docs/codex-workflows/style-guides.md`: prose voice and analysis-style conventions
- `docs/codex-migration.md`: mapping from the previous Claude-first setup

## What This Repo Supports

- LaTeX and Beamer writing workflows
- Quarto translation and review workflows
- R, Python, and MATLAB analysis support
- Paper, slide, and letter review routines
- Read-only multi-agent adversarial review loops
- Durable plans, session logs, merge reports, and memory

## Codex Migration Summary

The old control layer remains in `.claude/` for reference, but this branch treats it as legacy material. The active behavior contract now lives in `AGENTS.md` and `docs/codex-workflows/`.

The migration preserves the main functional ideas:

- plan first for non-trivial work
- verify before claiming completion
- keep source files authoritative
- use explicit review passes instead of self-approval
- persist plans, logs, and lessons on disk
- keep repo-local helper state under `.codex/state/` and writable review enforcement state under `quality_reports/tmp/review_state/`

## Natural-Language Replacements for Prior Skills

Instead of Claude slash commands, ask for the task directly:

- `compile this LaTeX file`
- `proofread this section`
- `review this paper`
- `translate this Beamer deck to Quarto`
- `validate the citations`
- `run the data analysis`
- `prepare this for deployment`

Codex maps those requests through `docs/codex-workflows/capabilities.md`.

## Repository Structure

- `master_supporting_docs/`: papers, models, supporting documents, and nested repos
- `scripts/`: reusable automation
- `templates/`: plan, spec, report, session-log, and skill templates
- `quality_reports/`: plans, session logs, reviews, and merge reports
- `.codex/`: repo-local Codex helper state and notes
- `.codex/review_agents/`: active read-only review-agent prompt cards
- `docs/codex-workflows/`: Codex-native workflow documentation
- `.claude/`: legacy Claude-oriented reference material

## Notes

- This migration does not depend on Claude hooks or slash-command semantics.
- Repo-local Codex hooks live in `.codex/hooks.json`, but current Codex hook coverage is still partial and runtime-dependent.
- The current Codex hook docs state that Windows support is temporarily disabled, so the repo can be configured for hooks before every Windows client can execute them.
- Existing scripts and templates were intentionally preserved.
- Nested repositories in `master_supporting_docs/` still need careful handling.
