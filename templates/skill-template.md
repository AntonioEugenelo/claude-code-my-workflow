# Skill Creation Template

Use this template to create Codex skills for repeated domain workflows.

## When to Create a Skill

Create a skill when you repeatedly need:

- the same multi-step workflow
- the same domain-specific checks
- the same bundled references, scripts, or assets

Do not create a skill for one-off tasks or workflows that change every time.

## Where Codex Skills Live

Create skills in `${CODEX_HOME:-$HOME/.codex}/skills/[skill-name]/`.

A minimal skill looks like:

```text
[skill-name]/
  SKILL.md
```

Optional resources:

```text
[skill-name]/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  assets/
```

## Minimal `SKILL.md`

Use only `name` and `description` in YAML frontmatter.

```markdown
---
name: your-skill-name
description: What the skill does and when to use it. Include the user phrases or situations that should trigger it.
---

# Your Skill Name

State the job in one sentence.

## Instructions

1. Do the first essential step.
2. Do the second essential step.
3. Verify the result and report the outcome.

## References

- Read `references/...` when you need detailed domain material.

## Examples

- User says: "..."
- User says: "..."

## Troubleshooting

- If X happens, check Y.
- If Z fails, do W.
```

## Description Writing Rule

The `description` field is the trigger surface. Make it precise.

Good pattern:

```yaml
description: Reviews econometric specifications for common errors. Use when the user asks to "check the regression", "review the model spec", or shares R, Stata, or LaTeX output for an empirical paper.
```

Bad pattern:

```yaml
description: Helps with regressions.
```

## Resource Design

- Put detailed schemas, policies, and domain notes in `references/`.
- Put deterministic helpers in `scripts/`.
- Put templates and reusable files in `assets/`.
- Keep `SKILL.md` short and procedural; do not duplicate long references in it.

## Academic Example

```markdown
---
name: validate-citations
description: Cross-checks in-text citations against bibliography files. Use when the user asks to "check citations", "validate references", or is editing `.tex`, `.qmd`, or `.md` files with bibliographies.
---

# Validate Citations

## Instructions

1. Extract citation keys from the source files.
2. Parse the bibliography entries.
3. Report missing entries, unused entries, and obvious formatting issues.
4. Save the findings if the repo workflow expects a report on disk.
```

## Validation Checklist

- The skill name is short, lowercase, and hyphenated.
- The description says both what the skill does and when it should trigger.
- `SKILL.md` stays lean; detailed material lives in `references/`.
- Any bundled script is runnable and tested.
- The skill can be understood without auxiliary README files.

## Notes

- Prefer the system `skill-creator` workflow when available.
- If you add `agents/openai.yaml`, keep it consistent with `SKILL.md`.
- Do not carry over Claude-only frontmatter, hook wiring, or slash-command assumptions.
