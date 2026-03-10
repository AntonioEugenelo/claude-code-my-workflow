---
paths:
  - "Slides/**/*.tex"
  - "scripts/**/*.R"
  - "scripts/**/*.py"
  - "master_supporting_docs/MCMS/**/*.mod"
  - "master_supporting_docs/MCMS/**/*.m"
---

# Knowledge Base: Tariffs ECB Paper — US-China Trade War Effects on the Euro Area

## Model Dimensions

| Dimension | Convention | Values |
|-----------|-----------|--------|
| Countries | Index $k$, $l$ for trade partner | EA ($k=1$), CHN ($k=2$), ROW ($k=3$), USA ($k=4=K_{\text{num}}$) |
| Sectors | Index $i$, $j$ for input sector | $I=44$: energy (1-3), non-energy (4-44) |
| Energy sectors | First 3 after reordering | Coal/oil (05-06), Refined petrol (19), Utilities (35) |
| Dollar country | $K_{\text{num}}=4$ (USA) | Anchor for DCP, UIP bonds, cross-rates |

## Notation Registry

| Symbol | Meaning | Key File |
|--------|---------|----------|
| $\tau_{k,l,i,t}$ | Tariff: country $k$ on imports of sector $i$ from $l$ | b4 eq.48 |
| $\Omega_X(k,l,i,j)$ | IO matrix: expenditure by sector $i$ of country $k$ on good $j$ from $l$ | a1_calibration |
| $\beta_C(k,l,i)$ | Consumption share: country $k$'s spending on good $i$ from $l$ | a1_calibration |
| $\alpha_{k,i}$ | Labour share of sector $i$ in country $k$ | a1_calibration |
| $\theta^p_{k,i}$ | Calvo price rigidity (prob. of NOT resetting) | Gautier et al. |
| $\theta^w_k$ | Calvo wage rigidity ($= 0.75$) | Common |
| $\text{mc}_{k,i,t}$ | Log-deviation marginal cost | b4 eq.A.39 |
| $\kappa^p_{k,i}$ | Slope of sectoral NKPC | Derived from $\theta^p$ |
| $q_{k,l,t}$ | Real exchange rate between $k$ and $l$ | b4 RER block |
| $\Lambda_{k,i}$ | Domar weight (sales/GDP ratio) | Fixed-point solver |
| $\mathcal{M}_{k,i}$ | Steady-state markup | $= \Psi_{rs} / (\alpha + \vartheta)$ |
| $\vartheta_{k,i}$ | Intermediate input share of sector $i$ | Sum of $\Omega_X$ |
| $\Upsilon_k$ | Export share of GDP for country $k$ | Fixed-point solver |
| $Y_{k,l}$ | Ratio of nominal GDP between countries | Fixed-point solver |

## Key Equations

| Equation | Description | Reference |
|----------|-------------|-----------|
| $\text{mc}_{k,i} = -a_{ki} + \mathcal{M}\alpha w_k + \sum_{l,j}\mathcal{M}\omega_{klij} p_{klij}$ | Marginal cost decomposition | b4 eq.A.39-40 |
| $\pi_{l,k,i} = \kappa^p_{ki}(\text{mc}_{ki} - p_{lki}) + \beta\pi_{l,k,i}(+1)$ | Sectoral NKPC (PCP case) | b4 NKPC block |
| $c_k = c_k(+1) - \frac{1}{\sigma}(i_k - \pi_{C,k}(+1))$ | Euler equation | b4 eq.A.13 |
| $i_k - i_{K_\text{num}} = \Delta e_{k,K_\text{num}}(+1) - \gamma^* \text{nfa}_k$ | UIP with risk premium | b4 eq.A.14 |
| $\tau_{k,l,i} = \rho^\tau \tau_{k,l,i}(-1) + \sigma^\tau \varepsilon^\tau_{k,l,i}$ | Tariff AR(1) process ($\rho=0.96$) | b4 eq.48 |
| $y_{k,i} = \mathcal{M}\alpha n_{ki} + \mathcal{M}\vartheta x_{ki}$ | Production function | b4 eq.A.51 |

## Invoicing Regimes

| Regime | Price in destination $k$ | NKPC deflator | Sectors |
|--------|--------------------------|---------------|---------|
| PCP | $p_{k,l,i,k} = p_{k,l,i} + q_{k,l}$ | $\pi_{C,k}$ | Services, utilities |
| LCP | $p_{k,l,i,k} = p_{k,l,i}$ | $\pi_{C,l}$ | Machinery, pharma, food |
| DCP | $p_{k,l,i,k} = p_{k,l,i} + q_{k,K_\text{num}}$ | $\pi_{C,K_\text{num}}$ | Commodities, electronics |

## Key Calibration Parameters

| Parameter | Value | Source |
|-----------|-------|-------|
| $\beta$ (discount) | 0.99 | Standard |
| $\sigma$ (inv. IES) | 1 | Log utility |
| $\varphi$ (inv. Frisch) | 1 | Chetty (2011) |
| $\gamma_C$ (energy/non-energy, consumption) | 0.4 | Bohringer et al. (2021) |
| $\delta_C$ (Armington, consumption) | 1 | Boehm et al. (2023) |
| $\psi$ (labour/intermediates) | 0.5 | Atalay (2017) |
| $\rho_r$ (Taylor smoothing) | 0.7 | Standard |
| $\phi_\pi$ / $\phi_{\Delta y}$ | 1.5 / 0.125 | Gali (2015) |

## Key References

| Paper | Role |
|-------|------|
| Aguilar et al. (2025) | Base model (MCMS without tariffs) |
| Baqaee & Farhi (2020, 2024) | IO networks, misallocation, trade |
| Atalay (2017) | Input substitution elasticities |
| Gautier et al. (2024) | ECB PRISMA: sectoral Calvo parameters |
| Bohringer et al. (2021) | Energy/non-energy substitution |
| Boehm, Levchenko & Pandalai-Nayar (2023) | Short/long-run trade elasticities |
| Egorov & Mukhin (2023) | Optimal policy under DCP |

## Anti-Patterns

| Anti-Pattern | Correction |
|-------------|-----------|
| IO matrix ordering: (seller, buyer, ...) | Correct: $\Omega_X$(buyer-country, seller-country, buyer-sector, seller-sector) |
| $K_\text{num}$ is generic | $K_\text{num}=4=\text{USA}$ is hardcoded as dollar anchor everywhere |
| Tariffs on all country pairs | Only pairs involving USA have active shock innovations |
| $\theta^p$ = prob of resetting | $\theta^p$ = prob of NOT resetting (higher = stickier) |
| Mixing country reordering | Data: EA=1, USA=2, CHI=3, ROW=4. Model: EA=1, CHN=2, ROW=3, USA=4 |
| Energy sectors are flexible | Energy $\theta^p = 0.01$ (nearly flexible); don't treat like other sectors |
