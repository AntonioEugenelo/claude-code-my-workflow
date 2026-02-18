---
description: Quick reference for the core workflow loop, quality gates, non-negotiables, and exploration mode.
---

# Workflow Quick Reference

**Model:** Contractor (you direct, the agent orchestrates)

---

## The Loop

```
Your instruction
    ↓
[PLAN] (if multi-file or unclear) → Show plan → Your approval
    ↓
[EXECUTE] Implement, verify, done
    ↓
[REPORT] Summary + what's ready
    ↓
Repeat
```

---

## I Ask You When

- **Design forks:** "Option A (fast) vs. Option B (robust). Which?"
- **Content ambiguity:** "Equation unclear on X. Assume Y?"
- **Scope question:** "Also refactor Y while here, or focus on X?"
- **Mathematical choices:** "Alternative derivation path available. Preference?"

---

## I Just Execute When

- Code fix is obvious (bug, pattern application)
- Verification (compilation, rendering)
- Documentation (logs, commits)
- Plotting (per established standards)
- Deployment (after you approve, I ship automatically)

---

## Quality Gates (No Exceptions)

| Score | Action |
|-------|--------|
| >= 90 | Ready to commit |
| < 90  | Fix blocking issues |

---

## Non-Negotiables

- **Paths:** Relative paths from project root; `\input{../Preambles/header.tex}` for LaTeX
- **Figures:** Publication-ready, vector format (TikZ/PDF) preferred, white background
- **Colour palette:** Oxford navy #002147, accent red #A31F34, mid blue #4B6482, grey #646464
- **Mathematical rigour:** Every equation verified, notation consistent with knowledge base
- **Compilation:** 3-pass XeLaTeX must succeed before any commit

---

## Preferences

**Visual:** Clean, minimal slides. Two-column layouts for dense content. Equations centred and prominent.
**Reporting:** Concise bullets. Details on request.
**Session logs:** Always (post-plan, incremental, end-of-session).
**Audience context:** Rigorous macro theorists. Precision over accessibility.

---

## Exploration Mode

For experimental work, use the **Fast-Track** workflow:
- Work in `explorations/` folder
- 60/100 quality threshold (vs. 90/100 for production)
- No plan needed — just a research value check (2 min)
- See `.agent/rules/exploration-fast-track.md`

---

## Next Step

You provide task → I plan (if needed) → Your approval → Execute → Done.
