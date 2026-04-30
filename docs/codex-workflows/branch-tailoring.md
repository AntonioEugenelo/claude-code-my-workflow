# Branch Tailoring Workflow

Use this workflow at the start of a new project branch created from the purpose-agnostic main branch.

## Goal

Activate only the assumptions, tools, review gates, and paths needed by the project at hand. Do not turn optional overlays into global defaults.

## First Prompt Template

```text
I am tailoring this purpose-agnostic workflow branch for <project>. Read AGENTS.md, docs/codex-workflows/branch-tailoring.md, docs/project-overlays/branch-purpose-map.md, and the relevant overlay files. Create or update quality_reports/decisions/ACTIVE.md with the active overlays, source-of-truth paths, optional dependencies, verification commands, rerun gates, and excluded overlays. Do not import project assets or dependencies unless this project needs them.
```

## Procedure

1. Identify the project and compare it with `docs/project-overlays/branch-purpose-map.md`.
2. Select the minimal overlay set from `docs/project-overlays/`.
3. Record active overlays and inactive overlays in `quality_reports/decisions/ACTIVE.md`.
4. Record source-of-truth paths, derived outputs, and protected generated artifacts.
5. Record optional dependencies that are required only for this branch.
6. Record verification commands and any rerun gate requirements.
7. If the project use is not represented by an existing overlay, add a concise overlay before continuing substantial work.

## Completion Check

The branch is tailored when a future Codex session can answer these questions without guessing:

- Which overlays are active?
- Which files are authoritative?
- Which dependencies are optional and project-specific?
- Which commands verify completion?
- Which outputs require a run card before overwrite?
