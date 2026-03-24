# CLAUDE.MD -- DSGE Model: Optimal Policy in Disaggregated Economies

**Project:** Replication & Extension of Cox et al. (2025) — Optimal Monetary and Fiscal Policies in Disaggregated Economies
**Institution:** University of Oxford, Department of Economics
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile and confirm output at the end of every task
- **Single source of truth** -- Cox et al. PDF is authoritative for baseline specification; Eugenelo `.tex` for extensions; Dynare `.mod` for implementation
- **Quality gates** -- see `quality-gates.md` for thresholds (default: 90/100 commit)
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
claude-code-my-workflow/
├── CLAUDE.MD                        # This file
├── .claude/                         # Rules, skills, agents, hooks
├── master_supporting_docs/
│   ├── supporting_papers/           # Cox et al. PDF + reference literature
│   ├── supporting_slides/           # Presentation materials
│   ├── Government-Spending-in-Disaggregated-Economies/  # Eugenelo extension (.tex)
│   └── MCMS/                        # Data reference (sector-level calibration data)
├── model/                           # Dynare/MATLAB model implementation
│   ├── launch.m                     # Master runner
│   ├── calibration.m                # Parameter calibration
│   ├── steady_state.m               # Steady-state computation
│   ├── dynare_files/                # .mod files
│   ├── scenarios/                   # Policy regime configurations
│   ├── functions/                   # Helper MATLAB functions
│   ├── output/                      # IRFs, welfare results (gitignored)
│   └── tests/                       # Verification against paper results
├── quality_reports/                 # Plans, session logs, reviews
├── explorations/                    # Research sandbox (see rules)
├── templates/                       # Session log, quality report templates
└── scripts/                         # Utility scripts
```

---

## Commands

```bash
# Dynare/MATLAB (full model)
cd model && matlab -batch "launch"

# Specific scenario
cd model && matlab -batch "run('scenarios/policy_baseline.m')"

# Paper compilation (reference only)
cd master_supporting_docs/Government-Spending-in-Disaggregated-Economies && latexmk -xelatex main.tex
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 90 | Commit | Minimum for this project |
| 95 | Submission review | Ready for supervisor/peer review |
| 98 | Send | Ready to submit |

See `quality-gates.md` for numerical tolerances: steady-state 1e-10, IRF 1e-6, welfare 1e-8, special-case nesting exact.

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/review-paper [file]` | Multi-agent theory paper review |
| `/compile-latex [file]` | Multi-pass XeLaTeX compilation |
| `/validate-bib [file]` | Bibliography verification |
| `/proofread [file]` | Grammar/typo/consistency review |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/devils-advocate` | Challenge model assumptions |
| `/interview-me [topic]` | Interactive research interview |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |

---

## Current Project State

| Component | Location | Status | Notes |
|-----------|----------|--------|-------|
| Cox et al. (2025) | `master_supporting_docs/supporting_papers/*.pdf` | Reference | Baseline model to replicate (NBER WP 32914) |
| Eugenelo extension | `master_supporting_docs/Government-Spending-.../*.tex` | Reference | Extensions: kappa, CRRA, constrained G-bar |
| MCMS | `master_supporting_docs/MCMS/` | Data reference | Sector-level data for calibration |
| Replication review | `quality_reports/2026-03-24_cox-et-al-replication-review.md` | Complete | Equation map + implementation roadmap |
| Model implementation | `model/` | Not started | Target: replicate Cox et al. first |
