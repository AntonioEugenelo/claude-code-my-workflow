# Plan: Independent Data Verification & Deep Code Audit

**Status:** APPROVED
**Date:** 2026-03-26
**Approach:** Maximally skeptical — assume everything is wrong until proven otherwise

## Context

The MCMS pipeline (Matlab → Dynare → Python) generates all quantitative results for the Tariffs_ECB paper. The pipeline has never been independently verified end-to-end. The user is particularly concerned about:
1. CN inflation response under the reverse tariff (Chinese tariff on US)
2. The effect of near-fixed monetary policy ($\rho_r = 0.999$)
3. Any silent bugs in sector/country reordering, scaling, or sign conventions

## Phase 1: Independent Data Extraction (Python-only, from .mat files)

**Goal:** Build a completely independent script that extracts IRF data directly from the HDF5 .mat files, with NO dependency on new_process.py or a2_preprocessing.m logic.

**Method:**
- Use h5py to open `output_matlab/irf_*.mat` files directly
- Construct IRF key names from first principles (variable_country_shock pattern)
- Extract, scale, and aggregate independently
- Export to a separate CSV directory for comparison

**Files to read:**
- `output_matlab/irf_Het_DCP_Baseline.mat` (benchmark)
- `output_matlab/irf_PCP_Baseline.mat` (PCP)
- `output_matlab/irf_DCP_Baseline.mat` (full DCP)
- `output_matlab/irf_Het_DCP_NoMonPol.mat` (near-fixed rates)
- `output_matlab/calib.mat` (calibration parameters)

**Key variables to extract independently:**
- y (GDP), c (consumption), piC (CPI), reer_dw (REER), exp, imp, i (interest rate), pi_w (wage inflation)
- For each: 4 countries × 20 sectors × 12 quarters
- Both directions: US→CN (shock_from=4, shock_to=2) and CN→US (shock_from=2, shock_to=4)

**Output:** `output_python/verification/` directory with independent CSVs

## Phase 2: Cross-Validation

**Goal:** Compare every number in the independent extraction against the existing CSVs in `output_python/extra_charts/`.

**Checks:**
1. Value-by-value comparison (tolerance: 1e-10)
2. Sign consistency
3. Sector ordering match
4. Country ordering match
5. Scaling factor consistency (tau_shock = 10)
6. CPI rolling sum computation
7. Trade balance computation (exp - imp)

**Any discrepancy stops execution and gets reported.**

## Phase 3: Deep Code Review

**Goal:** Line-by-line audit of the pipeline code, assuming every line is wrong.

**Files:**
1. `a0_launch.m` (211 lines) — scenario configuration
2. `a1_calibration.m` (801 lines) — parameter construction
3. `a2_preprocessing.m` (843 lines) — IRF extraction & aggregation
4. `new_process.py` (1838 lines) — figure generation

**Specific concerns to investigate:**
- Sector reordering: [3,10,23] → positions 1-3. Is Theta_pki double-reordered?
- Country reassignment: USA=2→4, CHI=3→2. Are direct-mode filters correct?
- CN inflation under reverse tariff: sign, magnitude, mechanism
- Near-fixed monetary policy: Phi_Delta_y=0 vs Phi_Delta_y=0.125, effect on CPI
- DCP sector count: 7 PCP + 20 LCP + 17 DCP vs 7 + 19 + 18 (old file)

## Phase 4: Cleanup

If Phase 2 finds no discrepancies: delete the verification script and directory.
If discrepancies found: report, diagnose, and fix before any deletion.

## Verification

- Independent extraction matches existing CSVs to 1e-10
- All figure-referenced numbers verified
- Code review flags documented with severity ratings
