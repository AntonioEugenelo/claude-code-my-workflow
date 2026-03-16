# CLAUDE.MD -- Academic Applications with Claude Code

**Project:** Academic Applications -- Nuffield College Yale Exchange
**Institution:** University of Oxford, Department of Economics
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile and confirm output at the end of every task
- **Single source of truth** -- LaTeX `.tex` is authoritative; PDF is derived
- **Quality gates** -- see `quality-gates.md` for thresholds (default: 90/100 commit)
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
claude-code-my-workflow/
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── Letters/                     # Cover letters (LaTeX)
│   └── nuffield-yale-exchange/  # Yale exchange application
│       └── cover-letter.tex     # Main cover letter
├── master_supporting_docs/      # Papers, CVs, and existing slides
│   ├── supporting_papers/       # Research papers, CVs
│   └── supporting_slides/       # Presentation materials
├── quality_reports/             # Plans, session logs, reviews
├── explorations/                # Research sandbox (see rules)
├── templates/                   # Session log, quality report templates
└── scripts/                     # Utility scripts
```

---

## Commands

```bash
# LaTeX (single-pass XeLaTeX for letters)
cd Letters/nuffield-yale-exchange && xelatex -interaction=nonstopmode cover-letter.tex
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 90 | Commit | Minimum for this project (high-stakes application) |
| 95 | Submission review | Ready for supervisor/peer review |
| 98 | Send | Ready to submit to recipient |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-letter [file]` | Single-pass XeLaTeX, verify 1 page |
| `/draft-letter [application]` | Guided drafting: context → gaps → questions → draft |
| `/review-letter [file]` | Multi-agent review: proofreader + cover-letter-reviewer |
| `/proofread [file]` | Grammar/typo/consistency review |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/devils-advocate` | Challenge letter content and strategy |
| `/interview-me [topic]` | Interactive research interview |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/review-paper [file]` | Manuscript review |

---

## Current Project State

| Application | File | Status | Key Content |
|-------------|------|--------|-------------|
| Yale Exchange | `Letters/nuffield-yale-exchange/cover-letter.tex` | Template with TODOs | Cover letter for Nuffield → Yale exchange selection |
