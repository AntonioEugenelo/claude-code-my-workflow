# Plan: Adapt Workflow Configuration for Tariffs ECB Paper

**Status:** COMPLETED
**Date:** 2026-03-04

## Context

The user is starting a paper on the macroeconomic effects of a US-China trade war on the Euro Area. Infrastructure:
- **Model:** MCMS (4-country, 44-sector NK DSGE, MATLAB/Dynare) — `master_supporting_docs/MCMS/` branch `Paper`
- **Existing paper:** Tariffs_ECB — `master_supporting_docs/Tariffs_ECB/0_clean/`
- **Workflow:** Forked from `pedrohcgs/claude-code-my-workflow`, currently configured for Oxford workshop talk

### User Decisions
- **Replace** CLAUDE.md entirely (archive workshop talk config)
- **ECB colour palette** (#003299 blue, #FFD700 gold) for all figures/visuals
- **Separate Slides/ folder** — work in main repo, sync to Tariffs_ECB via `sync_to_overleaf.sh`

---

## Changes

### 1. Rewrite `CLAUDE.md` — Paper-centric configuration

Replace entirely. New content:
- Project: "Tariffs ECB Paper — US-China Trade War Effects on the Euro Area"
- Institution: ECB (multi-institutional collaboration)
- Folder structure: show Slides/, Figures/, MCMS and Tariffs_ECB clones
- Commands: LaTeX 3-pass for paper sections, sync-to-overleaf, MATLAB/Dynare references
- Current project state: paper sections table (complete vs preliminary vs planned)
- MCMS model structure quick reference (countries, sectors, key files)
- Remove workshop-specific Beamer environments, Quarto CSS classes (not relevant to paper)
- Keep quality thresholds, skills reference, core principles

### 2. Rewrite `knowledge-base-template.md` — Paper notation registry

Replace workshop notation with:
- **Countries:** EA (k=1), CHN (k=2), ROW (k=3), USA (k=4=Knum)
- **Sectors:** I=44 (3 energy: coal/oil, refined petrol, utilities; 41 non-energy)
- **Key notation:** tau_{k,l,i} (tariff), Omega_X (IO matrix), Beta_C (consumption shares), Alpha (labour share), Theta_p (Calvo), mc_{k,i} (marginal cost), q_{k,l} (RER), Lambda (Domar weights)
- **Key equations:** marginal cost decomposition, NKPC, Euler/UIP, tariff AR(1), market clearing
- **Invoicing regimes:** PCP, LCP, DCP — definitions and which sectors use which
- **Anti-patterns:** IO matrix ordering convention, Knum=USA hardcoding, tariff only on US pairs
- **References:** Aguilar et al. (2025), Baqaee-Farhi (2020), Atalay (2017), Gautier et al. (2024), Bohringer et al. (2021)

### 3. Update `r-code-conventions.md` — ECB palette

Change Section 4 (Visual Identity):
- primary_blue: `#003299` (ECB blue)
- primary_gold: `#FFD700` (ECB gold)
- accent colours: `#FF6600` (ECB orange), `#009900` (ECB green)
- Update theme_project() definition accordingly

### 4. Update `r-reviewer.md` — Domain correctness for DSGE/trade

Fill `<!-- Customize -->` placeholder:
- IRF sign conventions for tariff shocks
- Dynare naming ↔ paper notation mapping
- Calvo parameter interpretation (theta = probability of NOT resetting)
- Domar weight / IO share consistency checks
- Trade balance sign conventions

### 5. Update `domain-reviewer.md` — Add tariff-specific lenses

Augment existing macro lenses with:
- Tariff incidence verification (consumer vs producer burden)
- IO cascade consistency with b4_declare_model.mod equations
- Currency invoicing (PCP/LCP/DCP) correctly stated
- Calibration parameter consistency with a1_calibration.m

### 6. Update `beamer-translator.md` — Paper style files

Update environment mapping comment to reference `paper.sty` and `math.sty` from Tariffs_ECB.

### 7. Fix `templates/quality-report.md` — Threshold

Change `>= 80` → `>= 90`.

### 8. Update `MEMORY.md` — Store project knowledge

Add concise entries:
- MCMS model location, dimensions, key files
- Tariffs_ECB paper location and current state
- IO matrix convention: Omega_X(buyer-country, seller-country, buyer-sector, seller-sector)
- Only tariff shocks active; Knum=USA=4 is special
- sync_to_overleaf.sh workflow
- ECB colour palette decision

### 9. Update `sync_to_overleaf.sh` — Add directory existence checks

Add `mkdir -p` for target directories before copying (identified gap).

### 10. Update session log

Append configuration work to `quality_reports/session_logs/2026-03-04_project-setup-tariffs-paper.md`.

---

## Files Modified

| # | File | Change |
|---|------|--------|
| 1 | `CLAUDE.md` | Full rewrite for paper project |
| 2 | `.claude/rules/knowledge-base-template.md` | New notation registry |
| 3 | `.claude/rules/r-code-conventions.md` | ECB colour palette |
| 4 | `.claude/agents/r-reviewer.md` | Domain correctness for DSGE/trade |
| 5 | `.claude/agents/domain-reviewer.md` | Tariff-specific review lenses |
| 6 | `.claude/agents/beamer-translator.md` | Paper style file references |
| 7 | `templates/quality-report.md` | Fix threshold to 90 |
| 8 | `MEMORY.md` | Project knowledge entries |
| 9 | `scripts/sync_to_overleaf.sh` | mkdir -p safety |
| 10 | `quality_reports/session_logs/2026-03-04_*.md` | Session log update |

## NOT Touched

- Paper tex files (Tariffs_ECB)
- MCMS model code
- Hook scripts, settings.json

## Verification

1. CLAUDE.md under ~150 lines
2. MEMORY.md under 200 lines
3. Knowledge base notation matches model code (b3_declare_par.mod, b4_declare_model.mod)
4. All markdown files valid
5. Workshop talk config preserved in git history (no data loss)
