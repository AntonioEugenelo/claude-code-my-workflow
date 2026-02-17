# Constitutional Governance: Macro Workshop Project

**Non-negotiable principles for this project.**

---

## Article I: Single Source of Truth

Beamer `.tex` files in `Slides/` are authoritative. Quarto `.qmd` derives from them. Never edit Quarto without first verifying the Beamer source matches.

**Why:** Prevents divergence between presentation formats.

**Exceptions:** Quarto-only CSS/layout adjustments that have no Beamer equivalent.

---

## Article II: Plan-First Threshold

Enter plan mode for tasks requiring >3 files or multi-step workflows.

**Why:** Prevents mid-implementation pivots. This is a 15-minute workshop talk for a critical audience — every change matters.

**Exceptions:** Exploration folder allows fast-track. Single-file typo fixes skip planning.

---

## Article III: Quality Gate

Nothing commits below **90/100**. This project targets a rigorous and critical audience.

**Why:** High bar ensures publication-ready output from the start.

**Exceptions:** WIP branches explicitly marked. Exploratory work in `explorations/` uses 60/100.

---

## Article IV: Mathematical Rigour

All equations must be:
1. Mathematically correct (every `=` step verified)
2. Notation-consistent with the knowledge base
3. Self-contained on each slide (assumptions stated or referenced)

**Why:** The audience is rigorous macro theorists. Any error undermines credibility.

**Exceptions:** None. Fix before committing.

---

## Article V: Compilation Verification

All `.tex` files must compile with 3-pass XeLaTeX without errors before commit. Warnings are acceptable only if documented.

**Why:** Broken builds block all downstream work.

**Exceptions:** Known LaTeX warnings documented in session log.

---

## User Preferences (Override Anytime)

- Citation style (inline text vs BibTeX `\cite{}`)
- Appendix ordering and content selection
- Colour emphasis choices within the Oxford palette
- Slide ordering within sections
- Level of detail on any given slide

---

## Requesting Amendment

When deviating from an article, ask:

> "Are you **amending Article X** (permanent change) or **overriding for this task** (one-time exception)?"
