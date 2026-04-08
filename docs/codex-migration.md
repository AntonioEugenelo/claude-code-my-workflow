# Codex Migration Map

This branch converts the repository from a Claude-first control plane to a Codex-first one.

## What Changed

| Previous Claude Asset | Codex Replacement |
| --- | --- |
| `CLAUDE.md` as the primary instruction file | `AGENTS.md` |
| `.claude/rules/*.md` auto-loaded rules | `docs/codex-workflows/*.md` explicit operating docs |
| `.claude/skills/*/SKILL.md` slash commands | `docs/codex-workflows/capabilities.md` plain-language recipes |
| `.claude/settings.json` permissions and hooks | Explicit verification, review, and logging procedures in `AGENTS.md` and workflow docs |
| `.claude/agents/*.md` runtime subagents | Review lenses described in `docs/codex-workflows/review-routing.md` |

## What Stayed the Same

- `scripts/` remains the automation layer.
- `templates/` remains the template library for plans, session logs, and quality reports.
- `MEMORY.md`, `quality_reports/`, and the paper/analysis folders remain the durable project state.

## Legacy Material

`.claude/` is retained for reference and for anyone who still wants to compare against the original Claude-oriented setup. It is no longer the authoritative behavior contract for this branch.

## Functional Differences

- Hook-driven enforcement is now explicit. Codex is expected to follow the procedures, not rely on runtime hook events.
- Slash commands are replaced by plain-language requests.
- Review roles are preserved as named lenses. They can be run sequentially without runtime-specific agent support.

## Recommended Use

Start each new Codex session by reading `AGENTS.md`. For non-trivial work, then read the relevant docs in `docs/codex-workflows/` before editing files.
