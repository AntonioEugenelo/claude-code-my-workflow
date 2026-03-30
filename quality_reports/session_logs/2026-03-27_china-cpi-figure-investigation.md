# Session Log: China CPI Figure Investigation

**Date:** 2026-03-27
**Branch:** Tariffs_ECB_paper
**Goal:** Investigate why China CPI inflation panel in Figure 3 (Section 4) shows inflation increasing on impact when US imposes tariffs

---

## Key Context

- **Figure:** `Fig_Benchmark_CPI.png` in `Tariffs_ECB/0_clean/figures/`, referenced in `55a_benchmark_and_robustness.tex`
- **CSV:** `Figure_1_Benchmark_IRFs_TimeSeries.csv`, column `piC_CHN_Benchmark`
- **Pipeline:** Dynare .mat → Matlab `a2_preprocessing.m` → CSV → Python `new_process.py:create_focused_benchmark_panels()` → PNG

## Findings

### Pipeline is clean — no extraction errors
- Raw .mat values match CSV exactly (verified via h5py)
- Matlab extraction logic (sectors 4-23, tau_shock=10) is correct
- Python 4Q rolling sum computation is mathematically correct

### Root cause: DCP exchange rate pass-through
- US tariff → dollar appreciates (REER_USA = −0.32) → yuan depreciates (REER_CHN = +0.22)
- Yuan depreciation raises all Chinese import prices → CPI spike of +0.12 pp at t=1
- From t=2 onward, quarterly CPI is **negative** (demand reduction dominates)
- The 4Q rolling sum stays positive for 4 periods because the t=1 spike remains in the window
- Sharp drop from +0.07 to −0.06 at t=5 when spike exits the rolling window (sawtooth artifact)

### Potential actions discussed
- Consider showing quarterly CPI instead of annualized for China panel
- Or note in text that initial positive response is a one-quarter DCP exchange rate effect
- The annualized measure creates a misleading visual for the China panel specifically

## Decisions

- (Pending user input)

## Open Questions

- Does the user want to modify the figure, the text, or both?
- Should the annualized vs quarterly distinction be handled differently across panels?
