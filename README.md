# Codex Academic Workflow Starter

This repository is a Codex-first, purpose-agnostic workflow base for serious academic and research work. It keeps the full inherited Claude Code workflow as compatibility material, but `AGENTS.md` is now the active instruction surface.

Use it as a head branch for new projects: keep the shared planning, review, verification, agent, and skill library in place, then activate only the project overlay you need. The first prompt on a repurposed branch should tailor the branch using `docs/codex-workflows/branch-tailoring.md` or `templates/branch-tailoring-prompt.md`.

## Quick Start

1. Fork or clone the repo.
2. Start Codex in the repository root.
3. Read `AGENTS.md`.
4. For non-trivial work, create or update a plan in `quality_reports/plans/`.
5. On a new project branch, run the branch-tailoring prompt before substantial work.
6. Select a project overlay only when the work requires one.

The default branch should not require MCMS, Tariffs, Overleaf, MATLAB, Dynare, Quarto, LaTeX, or R just to be useful. Those capabilities remain available as opt-in project overlays or task-specific workflows.

## Active Codex Surfaces

- `AGENTS.md`: primary Codex operating instructions.
- `.codex/`: Codex-readable mirrors of agents, skills, hooks, and workflow metadata.
- `.codex/config.toml`: project metadata and active Codex hook registration.
- `.codex/rules/`: Codex-facing mirror of the preserved Claude rules and procedural checklists.
- `docs/codex-workflows/`: task recipes for planning, first-prompt branch tailoring, implementation, review, logging, and capability routing.
- `docs/project-overlays/`: optional project profiles for academic circumstances such as Antonio/Oxford, MCMS, Tariffs/Overleaf, Government Spending, Cox replication, applications, CVs, referee reviews, teaching, slide prototypes, and workflow infrastructure.
- `quality_reports/`: plans, specs, session logs, merge reports, checkpoints, and decisions.
- `quality_reports/decisions/ACTIVE.md`: active locks for branch/source/model decisions.
- `quality_reports/run_cards/`: contracts for expensive reruns and output-overwriting jobs.
- `quality_reports/claim_ledgers/`: source-to-claim ledgers for numeric and figure audits.
- `templates/`: reusable plan, spec, report, checkpoint, and preregistration templates.

## Preserved Claude Compatibility

The original `.claude/` tree is intentionally retained. It contains the canonical Claude Code versions of:

- agents,
- skills and slash-command workflows,
- hooks,
- rules,
- references,
- settings,
- status line scripts.

Codex does not expose every Claude runtime feature with identical semantics. Where exact parity is not feasible, the Codex workflow preserves the behavior as explicit procedures, mirrored reference files, and documented limitations rather than silently deleting it.

Known non-identical areas:

- Claude `PostToolUse`, `Stop`, and `SessionStart[resume]` behavior is actively wired through Codex hooks.
- Claude `Notification` and `PreCompact` have no exact Codex event in the installed runtime and remain explicit checkpoint/session-log procedures.
- Claude slash-command argument expansion.
- Claude status line rendering.
- Claude `Task(subagent_type=...)` dispatch.
- Claude permission-mode prompts.

## Purpose-Agnostic Model

The default workflow is generic:

- Plan before ambiguous or broad work.
- Treat source files as authoritative.
- Verify after edits.
- Use explicit review lenses instead of self-approval.
- Keep durable context on disk.
- Preserve project-specific assumptions in overlays.

Project-specific material is available but not default. For example, the Antonio/Oxford, MCMS, Tariffs/Overleaf, Cox replication, Government Spending, CV, cover-letter, referee-review, teaching, and slide-prototype workflows are retained for projects that need them, but ordinary forks can ignore those overlays.

Known branch purposes are mapped in `docs/project-overlays/branch-purpose-map.md`. If a future branch introduces a distinct repeatable use, add it as a small overlay, workflow, template, skill, or script rather than making `main` project-specific.

## Included Capabilities

The inherited workflow includes specialized agents and skills for:

- proofreading and editing,
- paper and referee-style review,
- methods and domain review,
- LaTeX and Quarto compilation,
- Beamer-to-Quarto translation,
- R/data-analysis review,
- bibliography and claim validation,
- reproducibility auditing,
- lecture creation,
- slide quality review,
- preregistration,
- checkpointing and session handoff,
- response-to-referees workflows.

See `docs/codex-workflows/capabilities.md` for the Codex routing map, `.codex/skills/` for preserved skill instructions, and `.codex/rules/` for the detailed workflow rules.

## Optional Dependencies

Install only what your selected project overlay or task needs.

| Capability | Typical Tools |
| --- | --- |
| Core Codex workflow | git, Python 3 |
| LaTeX/Beamer | XeLaTeX or TeX Live |
| Quarto slides/sites | Quarto |
| R analysis | R |
| MATLAB/Dynare models | MATLAB, Dynare |
| Overleaf sync | Bash-compatible shell, Overleaf git credentials |
| GitHub PR workflows | GitHub CLI |

On this Windows environment, `scripts/sync-overleaf.sh status` could not run because `bash` was not available on PATH. A Windows-native equivalent or Git Bash/WSL is required for that workflow.

## Legacy Upstream

This repository tracks upstream workflow improvements from Pedro Sant'Anna's `claude-code-my-workflow` and adapts them for Codex-first use. The original Claude-oriented guide, changelog, and `.claude/` assets are preserved so Claude users can still recover the original behavior.

## License

MIT License. See `LICENSE`.
