# Branch Tailoring Prompt

Use this as the first prompt after creating a project branch from the purpose-agnostic main branch.

```text
I am tailoring this purpose-agnostic workflow branch for <project>.

Please read:
- AGENTS.md
- docs/codex-workflows/branch-tailoring.md
- docs/project-overlays/branch-purpose-map.md
- the relevant files in docs/project-overlays/

Then create or update quality_reports/decisions/ACTIVE.md with:
- active overlays;
- source-of-truth paths;
- derived outputs;
- optional dependencies needed by this project;
- verification commands;
- rerun gates and run-card requirements;
- overlays that should stay inactive.

Do not import project assets or dependencies unless this project needs them.
```
