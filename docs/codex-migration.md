# Codex Migration Map

This branch is Codex-first, while preserving the inherited Claude Code behavior as compatibility material.

## Active Control Plane

| Purpose | Codex-First Surface |
| --- | --- |
| Primary instructions | `AGENTS.md` |
| Workflow recipes | `docs/codex-workflows/` |
| Optional project assumptions | `docs/project-overlays/` |
| Agent references | `.codex/agents/` |
| Skill references | `.codex/skills/` |
| Rule references | `.codex/rules/` |
| Active hook configuration and runtime notes | `.codex/config.toml`, `.codex/hooks/` |
| Durable context | `quality_reports/`, `MEMORY.md` |

## Preserved Claude Surface

The `.claude/` directory remains in the repository on purpose. It preserves:

- Claude settings and permission policy,
- hook scripts,
- slash-command skills,
- subagent definitions,
- rules and references,
- the status line script.

Do not delete `.claude/` when working on Codex migration. It is the source of truth for Claude parity and a regression reference for Codex equivalents.

`.codex/rules/` mirrors `.claude/rules/` for Codex-facing use. Codex should treat these as explicit procedural rules and checklists, not as implicit runtime-loaded instructions.

`.codex/config.toml` actively registers the supported Codex hooks. The installed runtime reports `codex_hooks` as stable and supports `PreToolUse`, `PermissionRequest`, `PostToolUse`, `SessionStart`, `UserPromptSubmit`, and `Stop`.

## Parity Rules

- Preserve behavior exactly when Codex can express it directly.
- Mirror behavior as a Codex procedure when Codex has no direct runtime equivalent.
- Document unavoidable differences instead of silently weakening the workflow.
- Keep project-specific assumptions in overlays rather than the generic startup path.

## Known Runtime Differences

| Claude Feature | Codex Treatment |
| --- | --- |
| Slash commands with `$ARGUMENTS` | Plain-language requests routed through `docs/codex-workflows/capabilities.md` and `.codex/skills/` |
| `Task(subagent_type=...)` | Explicit review lenses or Codex subagents when the user requests delegation |
| `PostToolUse` hooks | Active Codex hooks for context monitoring and verification reminders |
| `Stop` hook | Active Codex session-log reminder hook |
| `SessionStart[compact|resume]` | Active for Codex `SessionStart[resume]`; no Codex `compact` source was found |
| `Notification` and `PreCompact` hooks | No exact Codex event found; preserved as explicit session-log/checkpoint procedures plus reference scripts |
| Status line command | Documentation only unless the active Codex runtime supports an equivalent |
| Permission modes | Follow Codex approval/sandbox rules and record blockers in session logs |

## Purpose-Agnostic Main

The default branch should be reusable for any academic or research project. It may contain specialized capabilities, but they must not be required for ordinary use.

Project-specific material belongs in one of three places:

- `docs/project-overlays/` for instructions and activation rules,
- optional directories such as `master_supporting_docs/` or `model/` for project assets,
- project branches when the asset is too large or too specific for the generic base.

## Recommended Use

Start with `AGENTS.md`. For non-trivial work, read the relevant Codex workflow doc and only then activate a project overlay if the current task requires it.
