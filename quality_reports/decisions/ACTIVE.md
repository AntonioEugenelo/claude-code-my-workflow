# Active Decision Locks

This file records decisions that prevent repeated rediscovery. Codex must read
this file before changing branches, syncing remotes, rerunning expensive jobs,
rewriting audit scope, or changing model specifications.

## Locked Decisions

| ID | Decision | Status | Owner | Last checked | Override rule |
| --- | --- | --- | --- | --- | --- |
| D-001 | This repository is Codex-first; `.claude/` is preserved as compatibility/reference material. | active | workflow | 2026-04-30 | User must explicitly request Claude-first behavior. |
| D-002 | The default branch should remain purpose-agnostic; project-specific assumptions activate through overlays. | active | workflow | 2026-04-30 | User must name the target project overlay. |
| D-006 | `main` is the overset workflow branch: it stores reusable capabilities for known branch uses, but a new project branch must be tailored by first prompt before assumptions become active. | active | workflow | 2026-04-30 | User may explicitly request a project-specific default branch. |
| D-003 | For Tariffs/Overleaf work, check source authority before pull, push, or edit. | active | workflow | 2026-04-30 | User may override after Codex reports the current authority/risk. |
| D-004 | Do not rerun long MATLAB/Julia/Quarto/LaTeX jobs until the rerun gate has been answered. | active | workflow | 2026-04-30 | User may override with an explicit "run anyway" instruction. |
| D-005 | Full audits require a frozen target and, for numeric paper claims, a claim ledger. | active | workflow | 2026-04-30 | User may request exploratory review, but it must be labeled exploratory. |

## Current Project Locks

| Project | Active lock | Notes |
| --- | --- | --- |
| Generic workflow base | Purpose-agnostic Codex-first workflow | No project dependency should be required for ordinary use. |
| Known project overlays | Opt-in only | Use `docs/project-overlays/branch-purpose-map.md` to choose overlays, then read the matching files before applying assumptions. |

## How To Update

When a decision changes, edit this file in the same turn as the change and add:

- the old decision,
- the new decision,
- why the override is justified,
- which outputs or branches need revalidation.
