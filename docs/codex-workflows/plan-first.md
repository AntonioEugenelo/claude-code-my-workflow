# Plan-First Workflow

Use this workflow for any non-trivial task.

## When Planning Is Required

- The request is high-level or ambiguous.
- The work is likely to affect more than 3 files.
- The work is likely to take more than 30 minutes.
- The user is asking for a redesign, migration, or workflow change.

## When You Can Skip It

- The task is a clear single-file edit.
- The task is a direct question that does not require repo changes.
- The user explicitly asks for a fast one-off fix and the scope is genuinely small.

## Protocol

1. Read `MEMORY.md` for relevant prior lessons.
2. If the request is ambiguous, ask a small number of targeted clarifying questions.
3. Write a short plan to `quality_reports/plans/YYYY-MM-DD_short-description.md`.
4. Include status, scope, files likely to change, verification steps, and known assumptions.
5. For complex requests, also create a requirements note in `quality_reports/specs/` using `templates/requirements-spec.md`.
6. Execute only after the plan is clear.

## Requirements Notes

For migrations, redesigns, or vague feature requests, capture:

- `MUST`: non-negotiable outcomes
- `SHOULD`: preferred outcomes
- `MAY`: optional outcomes
- `CLEAR`: well specified
- `ASSUMED`: reasonable assumption the user can override
- `BLOCKED`: cannot proceed without an answer

## Context Survival

Before ending a long session or switching tasks:

1. Ensure the active plan is saved to disk.
2. Append key decisions to the current session log.
3. Record persistent corrections in `MEMORY.md` using `[LEARN:tag]`.
4. Note open questions instead of relying on conversation memory.
