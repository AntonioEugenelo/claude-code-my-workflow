# Plan: DCP Bug Fix — Regenerate Simulations, Figures, Text, and Review

**Status:** APPROVED
**Date:** 2026-03-27
**Branch:** Tariffs_ECB_paper

---

## Context

A critical bug in `b4_declare_model.mod` applied dollar exchange rates to domestic DCP sales (commit `1e57e26`). The fix is committed. Now: re-run all DCP simulations, regenerate CSVs/figures, update every hardcoded number in the paper, and run the adversarial review loop until all agents score >= 90/100.

---

## Phase 1: Re-run Dynare Simulations (User — ~7.5 hours)

### Step 1.1: Claude creates `a0_rerun_DCP.m`
A dedicated script (not modifying `a0_launch.m`) that:
- Dynare is already on MATLAB path — no addpath needed
- Runs `invoicing_modes = [1]` (Het_DCP only) + one run for invoicing=4 (Full DCP)
- Sets `skip_existing = false` to force regeneration
- Includes pre-flight assertion: `assert(exist('a1_calibration.m','file')==2)`
- Backs up 3 stale .mat files as `*_PREFIX.mat` before overwriting

**10 runs required:**

| Run | File | Status |
|-----|------|--------|
| 1 | `irf_Het_DCP_Baseline` | Stale → re-run |
| 2 | `irf_Het_DCP_Direct1_NoDom` | Missing → generate |
| 3 | `irf_Het_DCP_Direct4_ZeroIO` | Missing → generate |
| 4 | `irf_Het_DCP_Direct5_Autarky` | Missing → generate |
| 5 | `irf_Het_DCP_CnPeg1` | Missing → generate |
| 6 | `irf_Het_DCP_CnPeg2` | Missing → generate |
| 7 | `irf_Het_DCP_CnPeg3` | Missing → generate |
| 8 | `irf_Het_DCP_Arm1` | Missing → generate |
| 9 | `irf_Het_DCP_NoMonPol` | Stale → re-run |
| 10 | `irf_DCP_Baseline` (invoicing=4) | Stale → re-run |

**Skip:** `irf_PCP_Baseline` (unaffected), `Direct2`, `Direct3` (not used by any figure).

### Step 1.2: Claude kicks off simulation via `matlab -batch`
Run `matlab -batch "a0_rerun_DCP"` from terminal (background, ~7.5 hours).
User can continue other work while this runs.

### Step 1.3: Claude verifies fix via h5py
Compare pre-fix vs post-fix `pi_C_2_varepsilon_tau_4_2_9` (CHN CPI, Textiles sector). Expected: post-fix values differ for non-US countries; US unchanged.

---

## Phase 2: Regenerate CSVs and Figures (~30 min)

### Step 2.1: User runs `a2_preprocessing` in MATLAB (~10 min)
Generates ~44 CSVs in `output_python/extra_charts/`.

### Step 2.2: Claude runs Python figure scripts
- `python new_process.py` — all main figures
- `python output_python/extra_charts/gen_section5_figs.py` — Section 5 figures

### Step 2.3: Claude copies updated PNGs to `Tariffs_ECB/0_clean/figures/`

### Step 2.4: Quick sanity check
Compare new China CPI quarterly figure against the old one. Verify the qualitative DCP-amplification story survives (DCP 3-year GDP > PCP 3-year GDP for China). If not, flag for narrative rewrite.

---

## Phase 3: Update Paper Text (~2-3 hours)

### Step 3.0: Build number reference table
Read all updated CSVs once. Extract every quantity cited in the paper into a structured table: (variable, country, period, transformation, new value).

### Step 3.1-3.6: Update sections in order of DCP sensitivity

| Order | File | Red-text instances | Key content |
|-------|------|-------------------|-------------|
| 1 | `55a_benchmark_and_robustness.tex` | ~33 | Benchmark + all robustness numbers |
| 2 | `a_appendix_liberation_day.tex` | ~13 | Scaled scenario numbers + EA table |
| 3 | `56_sectoral_channels.tex` | ~16 | Sectoral decomposition, R-squared |
| 4 | `44_results.tex` | ~20 | Benchmark narrative numbers |
| 5 | `60_conclusions.tex` | ~1 | Summary findings |
| 6 | `a_appendix_sectoral_targeting.tex` | ~2 | US-EA bilateral |

### Step 3.7: Cross-reference audit
Verify numbers referenced in multiple sections are consistent.

---

## Phase 4: Adversarial Review Loop (2-4 hours, max 5 rounds)

### Agent routing (Deep tier, research paper)

```
Parallel:  proofreader ∥ derivation-auditor ∥ figure-reviewer
Sequential: → theory-critic (after derivation-auditor passes)
Sequential: → narrative-reviewer (last)
```

### Early termination
- derivation-auditor >= 1 CRITICAL → skip theory-critic, fix first
- proofreader >= 5 CRITICAL/MAJOR → flag for rewrite
- Compilation failure → stop all, fix, recompile

### Loop
```
REVIEW → FIX (critical → major → minor) → RE-VERIFY (compile) → RE-SCORE (fresh agents)
Target: ALL agents >= 90/100. Max 5 rounds.
```

No self-scoring. Every fix round requires fresh agent review.

---

## Execution Model

MATLAB is available via `matlab -batch` from terminal. Dynare already on path.
Claude can launch simulations directly — no manual handoff needed.
Phases 1-4 run sequentially with MATLAB steps launched from terminal.

---

## Critical Files

- `MCMS/a0_launch.m` — template for rerun script
- `MCMS/a2_preprocessing.m` — CSV generation
- `MCMS/new_process.py` — figure generation
- `Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex` — highest number density
- `Tariffs_ECB/0_clean/sections/a_appendix_liberation_day.tex` — Liberation Day scenarios

---

## Verification

1. **Fix verification:** h5py comparison of pre/post .mat files (Step 1.3)
2. **CSV integrity:** spot-check 3 key values against .mat (Step 2.4)
3. **Text-figure consistency:** figure-reviewer agent (Phase 4)
4. **Compilation:** XeLaTeX 3-pass on `0_main.tex` (Phase 4, every round)
5. **Cross-section consistency:** audit in Step 3.7
