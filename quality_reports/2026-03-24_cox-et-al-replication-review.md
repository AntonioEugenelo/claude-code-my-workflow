# Cox et al. (2025) Replication Review & Implementation Roadmap

**Date:** 2026-03-24
**Paper:** "Optimal Monetary and Fiscal Policies in Disaggregated Economies" — Cox, Feng, Muller, Pasten, Schoenle, Weber (NBER WP 32914)
**Purpose:** Map every equation and parameter to its source, identify data requirements, and lay out a phased implementation roadmap for Dynare/MATLAB replication.

---

## Part A: Equation Inventory

### A.1 Setup (Section 2, pp. 6-9)

| Eq | Description | Paper Ref | Source | Dynare Target |
|----|------------|-----------|--------|---------------|
| 2.1 | Household utility: log prefs over C, G; disutility from N_k | p.6 | Standard (Gali-Monacelli 2008) | Welfare objective |
| 2.2 | Cobb-Douglas aggregators: C_t = prod(omega_ck^{-1} C_kt)^{omega_ck}, same for G_t | p.6 | Standard | Aggregation identities |
| 2.3 | CES within-sector bundles: C_kt, G_kt with elasticity theta | p.7 | Standard (Dixit-Stiglitz) | Demand functions |
| 2.4 | Budget constraint: sum P_k C_k + sum P_k^G G_k + Q B = sum W_k N_k + B + Pi | p.7 | Standard | Redundant (Walras' law) |
| 2.5 | Consumption FOCs: C_kt = omega_ck (P_kt/P_ct)^{-1} C_t; variety demand | p.7 | Derived from 2.1-2.4 | model_equations.mod |
| 2.6 | Price indices: P_ct = prod(P_kt^{omega_ck}); P_kt = CES aggregator | p.7 | Standard from CES | model_equations.mod |
| 2.7 | Labour supply: nu_k C_t N_kt^phi = (1-chi) W_kt/P_ct | p.8 | Derived from 2.1 | model_equations.mod |
| 2.8 | Euler equation: 1 = beta E_t[I_t (C_{t+1}/C_t)^{-1} P_ct/P_{ct+1}] | p.8 | Standard | model_equations.mod |
| 2.9 | Production: Y_kt(j) = A_kt N_kt(j) | p.8 | Standard (linear) | model_equations.mod |
| 2.10 | Marginal cost: MC_kt = (1-tau_k) W_kt / A_kt | p.8 | Standard | model_equations.mod |
| 2.11 | Calvo pricing FOC: Y_d = C only (kappa=0 implicitly) | p.8 | Standard Calvo, with key restriction | Phillips curve derivation |
| 2.12 | Variety market clearing: Y_kt(j) = C_kt(j) + G_kt(j) | p.9 | Standard | model_equations.mod |
| 2.13 | Sectoral market clearing: Y_kt = C_kt + G_kt | p.9 | Standard | model_equations.mod |
| 2.14 | Labour aggregation: N_kt = integral N_kt(j) dj | p.9 | Standard | model_equations.mod |

### A.2 Efficient Allocation (Section 2.2, pp. 9-10)

| Eq | Description | Paper Ref | Source | Dynare Target |
|----|------------|-----------|--------|---------------|
| 2.15 | Planner FOC: nu_k N_kt^phi / A_kt = (1-chi) omega_ck / C_kt = chi omega_gk / G_kt | p.9 | Derived (Samuelson rule) | steady_state.m |
| 2.16 | SS employment: N_k = mu_k | p.10 | Derived from normalisation | steady_state.m |
| 2.17 | SS output: Y_kt = mu_k A_kt | p.10 | Derived | steady_state.m |
| 2.18 | SS private consumption: C_kt = (1-chi_k) Y_kt | p.10 | Derived | steady_state.m |
| 2.19 | SS government consumption: G_kt = chi_k Y_kt | p.10 | Derived | steady_state.m |

**Derived quantities:**
- mu_k = (1-chi) omega_ck + chi omega_gk (sector measure)
- nu_k = mu_k^{-phi} (normalisation)
- chi_k = chi omega_gk / mu_k (G/Y share in sector k)
- tau_k = 1/theta (optimal subsidy)

### A.3 Log-Linearised System (Section 2.3, pp. 10-12)

| Eq | Description | Paper Ref | Source | Dynare Target |
|----|------------|-----------|--------|---------------|
| 2.20 | Market clearing: y_kt = (1-chi_k) c_kt + chi_k g_kt; y_t = (1-chi) c_t + chi g_t | p.10 | Log-linear of 2.13 | model_equations.mod |
| 2.21 | Sectoral IS (levels): y_hat_kt = E y_hat_{kt+1} - (1-chi_k)(i_t - E pi_{kt+1} - rho) - chi_k E Delta g_hat_{kt+1} | p.11 | Derived from 2.5, 2.8, 2.20 | Intermediate |
| **2.22** | **Sectoral IS (gaps)**: y_tilde_kt = E y_tilde_{kt+1} - (i_t - E pi_{kt+1} - r_bar_kt) - chi*_k E Delta f_tilde_{kt+1} | p.11 | **Core equation** | **model_equations.mod** |
| **2.23** | **Sectoral Phillips curve**: pi_kt = beta E pi_{kt+1} + lambda_k (1+phi) y_tilde_kt - lambda_k chi*_k f_tilde_kt | p.11 | **Core equation** | **model_equations.mod** |
| 2.24 | Demand relation: y_tilde_kt - y_tilde_t = chi*_k f_tilde_kt - chi* f_tilde_t - (p_kt - p_ct) - (a_kt - a_t) + chi* sum(mu_k - omega_gk) a_kt | p.11 | Derived from 2.5, 2.20 | model_equations.mod |
| 2.25 | Price-inflation identity: p_kt = pi_kt + p_{kt-1} | p.12 | Definition | model_equations.mod |
| 2.26 | Aggregate price: p_ct = sum omega_ck p_kt | p.12 | From 2.6 | model_equations.mod |
| 2.27 | Aggregate inflation: pi_t = sum omega_ck pi_kt | p.12 | From 2.26 | model_equations.mod |
| 2.28 | Aggregate fiscal gap: f_tilde_t = sum omega_gk (f_tilde_kt + y_tilde_kt) - y_tilde_t | p.12 | Definition | model_equations.mod |
| 2.29 | Aggregate output gap: y_tilde_t = sum mu_k y_tilde_kt | p.12 | From 2.24, 2.28 | model_equations.mod |

**Key definitions:**
- chi*_k = chi_k / (1 - chi_k)
- chi* = chi / (1 - chi)
- lambda_k = (1 - alpha_k)(1 - beta alpha_k) / alpha_k
- f_tilde_kt = g_kt - y_kt (fiscal gap = gov spending minus output, both in deviations)
- r_bar_kt = E Delta a_{kt+1} (natural rate)

### A.4 Optimal Policy (Section 3, pp. 13-17)

| Eq | Description | Paper Ref | Source | Dynare Target |
|----|------------|-----------|--------|---------------|
| 3.30 | Divine coincidence index: pi_DC = sum (lambda_k^{-1} mu_k / sum lambda_k^{-1} mu_k) pi_kt | p.13 | Derived from aggregation of 2.23 | Validation |
| **3.31** | **Welfare**: W = -1/2 sum beta^t sum_k mu_k [theta(1-chi_k)/lambda_k pi_kt^2 + (1+phi) y_tilde_kt^2 + chi*_k f_tilde_kt^2] | p.14 | **2nd-order approx (App B)** | **Objective** |
| **3.32** | **Optimal fiscal rule**: f_tilde*_kt = -[(1+phi)(1+lambda_k)/(1+(1+phi)lambda_k)] y_tilde*_kt - [theta(1-chi_k)phi/(1+(1+phi)lambda_k)] pi*_kt | p.15 | **Derived (App C)** | **model_equations.mod** |
| **3.33** | **Optimal monetary policy**: theta sum_k [(1-chi_k)mu_k / (1+lambda_k(1+phi))] pi_kt = -sum_k [mu_k / (1+lambda_k(1+phi))] y_tilde_kt | p.16 | **Derived (App C)** | **model_equations.mod** |
| 3.34 | Aggregate fiscal neutrality: sum mu_k (g_kt - g_bar_kt) = 0 | p.16 | Derived from 3.32 + 3.33 | Validation |

### A.5 Appendix Derivations (Online Appendix, pp. 38-42)

| Section | Content | Pages | Needed for Implementation |
|---------|---------|-------|--------------------------|
| App A | Steady-state solution | p.38 | Yes — verify steady_state.m |
| App B | Welfare 2nd-order approximation (eqs B.35-B.37) | pp.38-40 | Yes — verify welfare objective matches 3.31 |
| App C | Time-consistent policy FOCs (eqs C.38-C.48) | pp.40-42 | **Critical** — these ARE the model equations for Ramsey solution |
| App D | Fiscal divine coincidence (frictionless case) | p.42 | Validation only |

**App C equations needed for Dynare (the Ramsey FOC system):**

| Eq | Description |
|----|------------|
| C.38 | theta(1-chi_k)/lambda_k pi_kt + phi^pi_kt + phi^p_kt = 0 |
| C.39 | (1+phi) y_tilde_kt - (1+phi)lambda_k phi^pi_kt + phi^y_kt - nu_yt - (omega_gk/mu_k) nu_ft = 0 |
| C.40 | f_tilde_kt + lambda_k phi^pi_kt - phi^y_kt - (chi*)^{-1} (omega_gk/mu_k) nu_ft = 0 |
| C.41 | phi^p_kt = phi^y_kt + (omega_ck/mu_k) nu_pt |
| C.42 | nu_pt = sum mu_k phi^y_kt |
| C.43 | nu_yt + nu_ft = sum mu_k phi^y_kt |
| C.44 | (chi*)^{-1} nu_ft = -sum mu_k phi^y_kt |
| C.45-48 | Simplified system after combining C.42-C.44 |

---

## Part B: Calibration Parameters

### B.1 Directly Set Parameters

| Parameter | Symbol | Value | Source | Frequency |
|-----------|--------|-------|--------|-----------|
| Discount factor | beta | 0.997 | Monthly | Cox et al. |
| Inverse-Frisch | phi | 4 | Chetty et al. (2011) | — |
| Gov't demand share | chi | 0.185 | Cox et al. (2024, "Big G") | — |
| Shock persistence | rho_a | 0.85 | Cox et al. calibration | — |

### B.2 Parameters Requiring Data

| Parameter | Symbol | Dimension | Source | Access |
|-----------|--------|-----------|--------|--------|
| Private consumption shares | omega_ck | 121 sectors | BEA Use Table, NAICS 4-digit, 2007-2012 avg | Public (BEA website) |
| Government demand shares | omega_gk | 121 sectors | USASpending.gov, federal procurement, 2007-2012 avg | Public |
| Calvo probabilities | alpha_k | 121 sectors | BLS PPI micro data, freq. of price changes (Pasten et al. 2020/2024) | **Restricted** (BLS confidential) |

### B.3 Derived Parameters

| Parameter | Formula | Notes |
|-----------|---------|-------|
| mu_k | (1-chi) omega_ck + chi omega_gk | Sector measure (= Y_k/Y in SS) |
| nu_k | mu_k^{-phi} | Labour disutility normalisation |
| chi_k | chi omega_gk / mu_k | Gov't share of sector k output |
| chi*_k | chi_k / (1 - chi_k) | Fiscal gap coefficient |
| lambda_k | (1-alpha_k)(1-beta alpha_k)/alpha_k | Phillips curve slope |
| tau_k | 1/theta | Optimal subsidy (offsets markup) |

### B.4 Parameters Not Specified

| Parameter | Symbol | Notes |
|-----------|--------|-------|
| Within-sector elasticity | theta | Not stated in calibration section. Standard: 6 (Gali 2008) or 11 (Woodford 2003). The Eugenelo paper uses theta=6 in examples. |
| Shock variance | sigma^2_a | Table 3 reports "variance multipliers" normalised by shock variance, so exact value may not be needed for replication of ratios. |

---

## Part C: Implementation Roadmap

### Phase 1: Baseline 2-Sector Analytical Model

**Objective:** Verify the algebra before going to Dynare.

**Steps:**
1. Set K=2, symmetric sectors (omega_ck = omega_gk = mu_k = 0.5, alpha_1 = alpha_2)
2. Write the system: 2 Phillips curves (2.23), 2 IS curves (2.22), 2 demand relations (2.24), identities (2.25-2.29)
3. Code optimal fiscal rule (3.32) and verify it analytically
4. Verify K=1 special case: divine coincidence holds (pi=0, y_tilde=0, f_tilde=0)
5. Verify aggregate fiscal neutrality (3.34)

**Tool:** MATLAB script (no Dynare needed)

### Phase 2: Full K-Sector Dynare Model

**Objective:** Implement the log-linearised system in Dynare with optimal policy.

**Approach:** Code the Ramsey FOCs (App C, eqs C.45-C.48) directly as model equations alongside the structural equations (2.22-2.29). This is more transparent than using Dynare's `ramsey_model` command and makes verification easier.

**Dynare file structure:**
```
model/dynare_files/
  main.mod              # @#include directives
  declare_var.mod        # y_tilde_k, pi_k, f_tilde_k, p_k, phi_pi_k, phi_y_k, ...
  declare_varexo.mod     # eps_k (sector productivity shocks)
  declare_par.mod        # beta, phi, chi, theta, rho_a, omega_ck, omega_gk, alpha_k, ...
  model_equations.mod    # Structural eqs 2.22-2.29 + Ramsey FOCs C.45-C.48
  shocks.mod             # var(eps_k) = sigma^2_a
```

**Key Dynare features:**
- Use `@#for k in 1:K` macro loops for sector-indexed equations
- AR(1) shock process: `a_k = rho_a * a_k(-1) + eps_k` (must be added — not in paper)
- Steady state: all gaps = 0 (by construction around efficient allocation)

### Phase 3: Reproduce U.S. Calibration (Table 3)

**Objective:** Match Cox et al. variance multipliers and cyclicality results.

**Data needed:**
1. omega_ck: Download BEA Use Tables (NAICS 4-digit, 2007-2012) — **public**
2. omega_gk: Download USASpending.gov procurement data (2007-2012) — **public**
3. alpha_k: Frequency of price changes from Pasten et al. (2020/2024) — **restricted BLS data**
   - Alternative: use publicly available estimates or the data published with Pasten et al.

**Simulations to reproduce:**
- 4 policy schemes: (1) optimal i + optimal f, (2) optimal i + passive f, (3) pi=0 + optimal f, (4) pi=0 + passive f
- 4 parameterisations: (a) full heterogeneity, (b) omega_gk=omega_ck, (c) alpha_k=alpha_bar, (d) both
- Target: var(pi_t)=0.14%, var(y_tilde_t)=0.35% under scheme (1a)

### Phase 4: Extensions (Eugenelo Paper)

**Objective:** Add novel features after baseline verification.

| Sub-phase | Extension | Key Equation Change | Verification |
|-----------|-----------|-------------------|--------------|
| 4a | kappa pass-through | Phillips curve slope: lambda'_k = lambda_k / (1 - kappa/(theta-1) chi*_k); G enters PC directly | kappa=0 reproduces Phase 2 |
| 4b | CRRA (sigma > 1) | Aggregate terms enter sectoral PC; welfare gets (sigma-1) terms | sigma=1 reproduces Phase 2 |
| 4c | Constrained G-bar | CES aggregator constraint; relative fiscal rules | rho=0 gives exogenous G level |

---

## Part D: MCMS as Data Reference

The MCMS model (Dominguez-Diaz et al.) is a 4-country 44-sector open-economy trade model — structurally different from Cox et al.

**Useful for:**
- Sector-level calibrated parameters (weight matrices, price rigidity) that may overlap with U.S. NAICS sectors
- Dynare macro patterns: `@#for k in 1:Knum` loop syntax for sector indexing
- MATLAB orchestration patterns: launch scripts, calibration scripts, scenario structs

**NOT useful for:**
- Model structure (open economy, trade, exchange rates, IO networks — none of this is in Cox et al.)
- Optimal policy specification (MCMS uses Taylor rules, Cox et al. uses Ramsey)

---

## Part E: Gaps and Open Questions

### E.1 Critical Gaps

1. **theta value:** Cox et al. do not state theta in the calibration section (Section 5.1). The Eugenelo paper uses theta=6 in examples (consistent with Gali 2008). Need to confirm or check if Cox et al. state it elsewhere.

2. **alpha_k data:** The Calvo probabilities come from BLS PPI confidential micro data (Pasten et al. 2020/2024). Check if:
   - Pasten et al. publish sector-level estimates in their paper/appendix
   - MCMS has overlapping price rigidity data for U.S. sectors
   - Alternative publicly available estimates exist

3. **Shock process:** The paper assumes AR(1) productivity shocks with persistence rho=0.85 but does not specify variance. Table 3 reports "variance multipliers" (var(X)/var(epsilon)), so absolute variance cancels. For IRFs, need to pick a normalisation.

### E.2 Implementation Decisions

4. **Ramsey approach:** Code FOCs directly (App C eqs C.45-C.48) vs. use Dynare `ramsey_model`. Recommend direct FOCs for transparency and easier verification.

5. **Number of sectors:** Start with K=2 (analytical), then scale to K=121 for U.S. calibration. May need intermediate K=5 or K=10 for testing.

6. **Monthly frequency:** Cox et al. use monthly (beta=0.997). Eugenelo paper does not explicitly state frequency. Maintain monthly for baseline replication; convert if needed for extensions.

### E.3 Validation Targets

7. **Special cases to verify:**
   - K=1: divine coincidence holds (pi=0, y_tilde=0 under optimal policy)
   - Symmetric sectors (omega_ck=omega_gk for all k): aggregate fiscal neutrality exact
   - Flexible prices (alpha_k -> 0): lambda_k -> infinity, fiscal rule approaches f_tilde=0

8. **Quantitative targets from Table 3:**
   - Scheme (1a): var(pi)=0.14%, var(y_tilde)=0.35%
   - Scheme (2a): var(pi)=0.35%, var(y_tilde)=0%
   - Scheme (3a): var(pi)=0%, var(y_tilde)=1.7%
   - Scheme (4a): var(pi)=0%, var(y_tilde)=7.8%
   - Cyclicality: corr(Y, G) = 0.62 under (1a), 0.43 under (3a)
