# Codex Academic Workflow

This branch is the Codex-native migration of the original Claude-oriented academic workflow. It keeps the useful repository structure, templates, and automation scripts, but replaces Claude-specific hooks, slash commands, and runtime conventions with Codex-readable instructions and explicit workflow documents.

## Quick Start

Open the repository in Codex and start from `AGENTS.md`. For any non-trivial task, Codex should also read the matching guide in `docs/codex-workflows/`.

Core entrypoints:

- `AGENTS.md`: primary instructions for Codex
- `docs/codex-workflows/plan-first.md`: planning and ambiguity handling
- `docs/codex-workflows/orchestrator.md`: implement, verify, review, fix loop
- `docs/codex-workflows/review-routing.md`: review lenses by file type
- `docs/codex-workflows/capabilities.md`: replacement for old slash-command skills
- `docs/codex-migration.md`: mapping from the previous Claude-first setup

## What This Repo Supports

- LaTeX and Beamer writing workflows
- Quarto translation and review workflows
- R, Python, and MATLAB analysis support
- Paper, slide, and letter review routines
- Durable plans, session logs, merge reports, and memory

## Codex Migration Summary

The old control layer remains in `.claude/` for reference, but this branch treats it as legacy material. The active behavior contract now lives in `AGENTS.md` and `docs/codex-workflows/`.

The migration preserves the main functional ideas:

- plan first for non-trivial work
- verify before claiming completion
- keep source files authoritative
- use explicit review passes instead of self-approval
- persist plans, logs, and lessons on disk

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
- `templates/`: plan, report, and session-log templates
- `quality_reports/`: plans, session logs, reviews, and merge reports
- `docs/codex-workflows/`: Codex-native workflow documentation
- `.claude/`: legacy Claude-oriented reference material

## Notes

- This migration does not depend on Claude hooks or slash-command semantics.
- Existing scripts and templates were intentionally preserved.
- Nested repositories in `master_supporting_docs/` still need careful handling.
