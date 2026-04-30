# Workflow Infrastructure Overlay

Use this overlay for changes to the workflow system itself: agents, skills, hooks, rules, templates, migration docs, repo hygiene, and upstream compatibility.

## Rules

- Preserve Claude compatibility material unless the user explicitly asks to remove it.
- Prefer Codex-native active behavior in `.codex/` while keeping `.claude/` as reference material.
- Keep main purpose-agnostic: add reusable overlays, workflows, templates, or scripts instead of baking in project assumptions.
- When importing upstream changes, record what changed and any parity gaps in `quality_reports/merges/` or a plan.
- Avoid duplicate long instructions across `AGENTS.md`, `README.md`, overlays, and workflow docs; link to the canonical source instead.

## Typical Capabilities

- update hooks and hook parity;
- add or revise Codex skills and rules;
- merge upstream workflow improvements;
- simplify redundant instructions;
- maintain branch-tailoring and overlay maps.
