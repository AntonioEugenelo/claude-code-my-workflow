# CLAUDE.MD -- Tariffs ECB Paper

**Project:** US-China Trade War Effects on the Euro Area
**Authors:** Aguilar, Chankova, Darracq, Dieppe, Dominguez-Diaz, Gallegos, Quintana (ECB) + Eugenelo (Oxford, RA)
**Institution:** ECB + University of Oxford
**Branch:** main (paper work on `Tariffs_ECB_paper` branch)

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- paper `.tex` in `master_supporting_docs/Tariffs_ECB/0_clean/` is authoritative (Overleaf-synced via GitHub submodule)
- **Quality gates** -- nothing ships below 90/100 (rigorous ECB audience)
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md
- **Mathematical rigour** -- every equation verified, notation consistent with model code

---

## Folder Structure

```
├── CLAUDE.MD                          # This file
├── .claude/                           # Rules, skills, agents, hooks
├── Bibliography_base.bib              # Centralized bibliography
├── Figures/                           # Generated figures (IRFs, heatmaps)
├── Preambles/                         # LaTeX headers, style files
├── Slides/                            # Paper .tex sections (working copies)
├── scripts/                           # Sync, quality, R/Python utilities
├── quality_reports/                   # Plans, session logs, merge reports
├── explorations/                      # Research sandbox
├── templates/                         # Session log, quality report templates
└── master_supporting_docs/
    ├── Tariffs_ECB/                   # ⭐ GIT SUBMODULE → Overleaf (main branch)
    │   └── 0_clean/                   # sections/, figures/, bibliography.bib
    └── MCMS/                          # ⭐ GIT SUBMODULE → model code (liberation-day-scenarios branch)
        ├── a0_launch.m                # Entry point
        ├── a1_calibration.m           # Calibration from OECD ICIO data
        ├── a2_preprocessing.m         # IRF extraction + Liberation Day scenarios
        ├── dynare_files/              # .mod files (model equations)
        │   ├── b0_main.mod            # Main Dynare file
        │   └── b4_declare_model.mod   # Core model equations
        ├── functions/                 # MATLAB helpers (fixed-point solver)
        ├── input_data/                # xlsx, mat calibration data
        └── new_process.py             # Python IRF post-processing + figure generation
```

---

## Commands

```bash
# Edit paper sections directly (auto-syncs to Overleaf via git push)
cd master_supporting_docs/Tariffs_ECB/0_clean/sections/
# After editing:
cd master_supporting_docs/Tariffs_ECB && git add -A && git commit -m "msg" && git push

# Run model postprocessing (generate scenario CSVs)
cd master_supporting_docs/MCMS && matlab -batch "a2_preprocessing"

# Generate figures from CSVs
cd master_supporting_docs/MCMS && python new_process.py

# Copy new figures to paper repo (for Overleaf)
cp master_supporting_docs/MCMS/output_python/extra_charts/Fig_*.png \
   master_supporting_docs/Tariffs_ECB/0_clean/figures/

# Quality score
python scripts/quality_score.py file.tex
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 90 | Commit | Minimum (ECB working paper standard) |
| 95 | PR | Ready for co-author review |
| 98 | Excellence | Publication-ready |

---

## MCMS Model Quick Reference

| Dimension | Value |
|-----------|-------|
| Countries | EA (k=1), CHN (k=2), ROW (k=3), USA (k=4=Knum) |
| Sectors | I=44 (3 energy + 41 non-energy, NACE 2-digit) |
| Shocks | Bilateral tariffs tau_{k,l,i}, AR(1) rho=0.96 (only US pairs active) |
| Invoicing | Het_DCP (data-based) or PCP (all producer currency) |
| Solver | Dynare, 1st-order log-linear approximation |
| IO matrix | Omega_X(buyer-country, seller-country, buyer-sector, seller-sector) |

**Key files for model modification:** `a1_calibration.m` (parameters), `b4_declare_model.mod` (equations), `b3_declare_par.mod` (parameter declarations), `b5_declare_variance.mod` (shock activation).

---

## Paper Status

| Section | File | Status |
|---------|------|--------|
| Introduction | `sections/11_introduction.tex` | Complete |
| Related Literature | `sections/12_related_literature.tex` | Needs update |
| Model (all) | `sections/21-26_*.tex` | Complete |
| Calibration | `sections/43_calibration.tex` | Complete |
| Determinants of Tariffs | `sections/44_results.tex` | Complete |
| Macro Effects | `sections/51_*.tex` | Commented out / planned |
| Sectoral Shocks | `sections/52_sectoral_shocks.tex` | Preliminary |
| Conclusions | `sections/60_Conclusions.tex` | Preliminary |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/compile-latex [file]` | 3-pass XeLaTeX + bibtex |
| `/proofread [file]` | Grammar/typo/overflow review |
| `/review-paper [file]` | 6-dimension manuscript review |
| `/validate-bib` | Cross-reference citations |
| `/commit [msg]` | Stage, commit, PR, merge |
| `/lit-review [topic]` | Literature search + synthesis |
| `/research-ideation [topic]` | Research questions + strategies |
| `/review-r [file]` | R code quality review |
| `/data-analysis [dataset]` | End-to-end R/Python analysis |

---

## Visual Identity (ECB Palette)

| Colour | Hex | Use |
|--------|-----|-----|
| ECB Blue | `#003299` | Primary, axes, labels |
| ECB Gold | `#FFD700` | Highlights, key results |
| ECB Orange | `#FF6600` | Secondary accent |
| ECB Green | `#009900` | Positive effects, third series |
