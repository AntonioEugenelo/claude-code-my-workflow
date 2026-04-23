# Codex Migration Map

This branch converts the repository from a Claude-first control plane to a Codex-first one.

## What Changed

| Previous Claude Asset | Codex Replacement |
| --- | --- |
| `CLAUDE.md` as the primary instruction file | `AGENTS.md` |
| `.claude/rules/*.md` auto-loaded rules | `docs/codex-workflows/*.md` explicit operating docs |
| `.claude/skills/*/SKILL.md` slash commands | `docs/codex-workflows/capabilities.md` plain-language recipes |
| `.claude/settings.json` permissions and hooks | Repo-local Codex config in `.codex/config.toml`, experimental Codex hooks in `.codex/hooks.json`, plus explicit workflow docs |
| `.claude/agents/*.md` runtime subagents | Review lenses described in `docs/codex-workflows/review-routing.md` |
| `.claude/state/*` repo-local helper state | `.codex/state/*` plus `quality_reports/tmp/review_state/` for writable review enforcement state |
| Selected legacy rules (`quality-gates`, `single-source-of-truth`, `replication`, `exploration`, `writing-style`, `r-code-conventions`) | Active Codex docs under `docs/codex-workflows/` |
| Claude review subagents | Read-only Codex explorer review agents under `.codex/review_agents/` plus `scripts/review_plan.py` |

## What Stayed the Same

- `scripts/` remains the automation layer.
- `templates/` remains the template library for plans, session logs, and quality reports.
- `MEMORY.md`, `quality_reports/`, and the paper/analysis folders remain the durable project state.

## Legacy Material

`.claude/` is retained for reference and for anyone who still wants to compare against the original Claude-oriented setup. It is no longer the authoritative behavior contract for this branch.

## Functional Differences

- Some hook-driven enforcement has been restored through Codex's experimental hook system, but only for currently supported events.
- The main workflow is still procedural because current Codex hooks do not yet cover all tool types or all of the old Claude lifecycle surfaces.
- Slash commands are replaced by plain-language requests.
- Review roles are preserved as named lenses. They can be run sequentially without runtime-specific agent support.
- Repo-local workflow state and helper bookkeeping now live under `.codex/state/`, with writable review enforcement state under `quality_reports/tmp/review_state/`.

## Recommended Use

Start each new Codex session by reading `AGENTS.md`. For non-trivial work, then read the relevant docs in `docs/codex-workflows/` before editing files.
