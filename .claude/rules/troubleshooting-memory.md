# Troubleshooting Memory

**When a technical issue takes more than one attempt to resolve, save the solution to memory.**

This overrides the default guidance against saving debugging solutions. Environment and toolchain issues recur across sessions, and re-debugging them wastes compute.

---

## When to Save

- Compilation errors that required >1 attempt to fix
- Path or environment issues (fonts, packages, tools not found)
- Tool quirks (IDE behaviour, CLI flags, platform differences)
- Configuration fixes (LaTeX packages, shell setup, git config)
- Any fix where you tried something that didn't work before finding what did

## When NOT to Save

- One-shot fixes (typo in filename, missing closing brace) — too trivial
- Code logic bugs specific to one file — the fix is in the code
- Issues already documented in CLAUDE.md or project rules

## Memory Format

Save to the project memory directory as `troubleshooting_<short_slug>.md`:

```markdown
---
name: <short description>
description: <symptom in one line — this is used for relevance matching>
type: troubleshooting
---

**Symptom:** <exact error message or observed behaviour>

**Environment:** <OS, tool versions, relevant context>

**Failed attempts:**
1. <what was tried and why it didn't work>

**Solution:** <what actually fixed it>

**Why:** <root cause explanation>
```

## How to Use

Before debugging a compilation or environment issue, check existing troubleshooting memories. If a matching symptom exists, try the documented solution first.
