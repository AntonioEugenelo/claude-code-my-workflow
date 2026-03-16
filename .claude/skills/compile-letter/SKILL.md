---
name: compile-letter
description: Compile a cover letter with single-pass XeLaTeX. Verifies compilation, checks page count, and reports any warnings. Use after editing any letter .tex file.
disable-model-invocation: true
argument-hint: "[filename or path to .tex file]"
allowed-tools: ["Bash", "Read", "Glob"]
---

# Compile Cover Letter

Single-pass XeLaTeX compilation for cover letters.

## Steps

1. **Identify file to compile:**
   - If `$ARGUMENTS` is a full path: use it directly
   - If `$ARGUMENTS` is a filename: search in `Letters/` for it
   - If `$ARGUMENTS` is empty: compile the most recently modified `.tex` file in `Letters/`

2. **Compile with XeLaTeX:**

```bash
cd <directory-containing-file> && xelatex -interaction=nonstopmode <filename>.tex
```

3. **Verify compilation:**
   - Check exit code (0 = success)
   - Search log for `! ` (LaTeX errors)
   - Search log for `Overfull \\hbox` warnings
   - Report any issues

4. **Check page count:**
   - Cover letters: exactly 1 page. Proposals of academic work: 3 pages (2 body + 1 references)
   - If exceeding target, report as a CRITICAL issue

5. **Check for unfilled placeholders:**
   - Search the `.tex` file for `TODO`, `PLACEHOLDER`, `XXX`, `[...]`
   - Report any found as warnings

6. **Present summary:**
   - Compilation status (success/failure)
   - Page count
   - Warnings (if any)
   - Placeholder count (if any)
