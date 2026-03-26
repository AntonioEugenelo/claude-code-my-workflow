# Session Log: Paper Restructure — 2026-03-17

## Goal
Restructure Tariffs_ECB paper: move Sections 5-6 (Liberation Day, Sectoral Targeting) to appendix, augment Section 4 with EA trade diversion, create new Section 5 on sectoral channels of US-CN transmission, drop policy implications and retaliation from main text.

## Completed

### Phase 1: Structure (DONE)
- Created `a_appendix_liberation_day.tex` and `a_appendix_sectoral_targeting.tex`
- Updated `0_main.tex` to include new appendix sections
- Removed duplicate Liberation Day figures from `a_appendix.tex`

### Phase 2: Section 4 Augmentation (DONE)
- Added "EA Transmission: Trade Diversion and Upstream Cost Propagation" subsubsection
- Removed monetary policy implications subsection
- Fixed DCP mechanism: "raises initial import price shock" not "amplifies cascade"
- Added DCP cross-reference to Appendix export Phillips curve
- Clarified Calvo × invoicing interaction
- Fixed peg amplification 55% → 60%
- Fixed citations: Armington for expenditure switching

### Phase 3: New Section 5 (DONE)
- Created `56_sectoral_channels.tex` with three subsections:
  1. Sectoral Heterogeneity in Bilateral Transmission
  2. Structural Determinants (IO intensity, GDP share, price rigidity)
  3. EA Sectoral Exposure Through Production Networks
- All figures reference back to Section 4 (no new figures yet)

### Phase 4: Supporting Files (DONE)
- Updated `11_introduction.tex`, `13_roadmap.tex`, `60_conclusions.tex`
- Anchored all findings on benchmark, Liberation Day → appendix references

### Phase 5: Adversarial Loop (4 ROUNDS COMPLETE)
All scores ≥ 90:
- Narrative: 95/92 (Sec4/Sec5)
- Domain Sec 4: 90
- Domain Sec 5: 94
- Theory-critic: 91
- Proofreader: 90

### Phase 6: New Figures for Section 5 (IN PROGRESS)
Need to generate 4 figures from corrected .mat IRFs:
1. Chinese Sectoral Heatmap (VA + inflation)
2. Chinese Structural Scatter (3×3)
3. EA Sectoral Ranking (indirect exposure under US-CN)
4. EA + CN Sectoral Phillips trade-off

**Data source:** `C:/CustomTools/MCMS/output_matlab/irf_Het_DCP_Baseline.mat` (Mar 10 18:56, post-bugfix)
**IRF structure:** HDF5 format, keys: `irfs_saved` (group with individual IRFs), `config_used`, `#refs#`
**Need to:** Copy .mat to repo, explore IRF naming convention, extract sectoral VA/inflation/GDP contributions, generate figures

### Key IRF naming pattern (from exploration):
- `c_1_varepsilon_tau_1_4_1` = variable `c` (consumption), country 1, shock `varepsilon_tau_1_4_1` (tariff shock on country-sector pair)
- Need to understand: variable names (y, va, pi, etc.), country indices (1=EA?, 2=USA?, 3=CHN?, 4=ROW?), sector indices

## Phase 6 Progress (IN PROGRESS)
- [x] Copied corrected `irf_Het_DCP_Baseline.mat` (Mar 10 18:56) from CustomTools/MCMS to repo
- [x] Explored IRF structure: HDF5 format, 108768 keys, variables=[c,y,exp,imp,i,pi_w,reer_import], countries 1-4, shocks=tau_K_L_S
- [x] Verified CSV cross-section data matches paper numbers (Textiles -0.027% etc)
- [x] Found `new_process.py` in CustomTools/MCMS — this is the master post-processing script
- [ ] User wants figures generated from .mat IRFs (not CSVs) to ensure post-bugfix data
- [ ] User wants .mat pushed to repo
- [ ] Need: extract sectoral VA and inflation from .mat, or use existing CSV (verified matching)
- [ ] Generate 4 figures: CN heatmap, CN structural scatter, EA ranking, EA+CN Phillips
- [ ] Integrate into Section 5 text
- [ ] Recompile and run final adversarial loop

## Key Findings (Phase 6)

### VA Bugfix Verified Quantitatively
- Corrected .mat: China Textiles Sec_VA = **-0.75%**
- Old CSV (pre-bugfix): China Textiles Sec_VA = **-31.16%** (42x larger!)
- GDP contributions UNAFFECTED: both give -0.086% for China Textiles
- Confirms the `ind_e`/`delta_X` bugs dramatically inflated sectoral VA but left aggregate GDP unchanged

### Country Ordering in .mat (from a2_preprocessing.m)
- Country 1 = EA, 2 = CHN, 3 = ROW, 4 = USA
- US-CN tariff shock: `varepsilon_tau_4_2_{sector}` (USA→CHN)
- IRF scaling: `tau_shock = 10` (multiply raw IRF by 10 for 10pp shock)

### Data Extraction from .mat
- Aggregate: `y_{K}_varepsilon_...`, `c_{K}_varepsilon_...`, `pi_C_{K}_varepsilon_...`
- Sectoral VA: `va_{K}_{I}_varepsilon_...` (own-sector value added)
- Sectoral Inflation: `pi_{K}_{I}_varepsilon_...` (own-sector inflation)
- Script: `gen_section5_figs.py` reads .mat directly via h5py

### Figures Generated (from corrected .mat)
1. `Fig_CN_Sectoral_Heatmap.png` — Chinese sectors VA + inflation
2. `Fig_CN_Structural_Scatter.png` — 3x3 structural determinants for China
3. `Fig_EA_Sectoral_Ranking_USCN.png` — EA indirect sectoral exposure
4. `Fig_EACN_Sectoral_Phillips.png` — CN + EA Phillips trade-off

### Integration
- All 4 figures added to Section 5 (56_sectoral_channels.tex)
- Paper compiles to 64 pages (up from 61)
- R5 adversarial loop launched (all 5 agents)

## R5 Results (partial)
- Domain Sec 4: 90 ✓
- Domain Sec 5: 85 → fixed (text numbers wrong, inflation claim false, missing Other Mfg)
- Theory-critic: 62 → fixed (figure-text mismatches, scatter middle row, axis labels, title)
- Narrative: pending
- Proofreader: pending

### Critical fixes applied after R5:
- Text VA numbers corrected: Other Mfg -1.80%, Electronics -1.22%, Textiles -0.75%
- "Uniformly positive" inflation → "generally small, most positive, but some negative"
- Other Mfg now mentioned as largest VA contraction
- Scatter middle row: GDP_impact (broken) → Cons_CHN (working)
- Figure title: "Contributions" → "Own-Sector Responses"
- EA ranking caption: "on-impact" consistent with data
- Phillips axis: "on impact" consistent with data
- All 4 figures regenerated

## Open Items
- [ ] Wait for remaining R5 results
- [ ] Launch R6 with all fixes applied
- [ ] Final compile

## Pre-existing Issues (not addressed)
- 3 red TODO notes in 55a (lines 67, 75, 118) — co-author annotations
- "Analyze" vs "analyse" spelling — project-wide choice
- Sector naming inconsistency ("Furniture & Other Manufacturing" vs "Other Manufacturing")
