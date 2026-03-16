# Troubleshooting Memory

**When a technical issue takes 2 or more attempts to resolve, save the solution to memory.**

This overrides the default guidance against saving debugging solutions. Environment and toolchain issues recur across sessions, and re-debugging them wastes compute.

---

## When to Save

Save when ALL of the following are true:
1. The issue required **at least 2 failed attempts** before finding the fix
2. The issue is environmental or toolchain-related (not a one-off code bug)

Common categories:
- Compilation errors that required multiple attempts to fix
- Path or environment issues (fonts, packages, tools not found)
- Tool quirks (IDE behaviour, CLI flags, platform differences)
- Configuration fixes (LaTeX packages, shell setup, git config)

## When NOT to Save

- Fixed on the first attempt — not worth storing
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
