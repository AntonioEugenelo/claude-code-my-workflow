---
paths:
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
  - "scripts/**/*.R"
---

# Course Knowledge Base: Macro Workshop — Fiscal Policy in Multisectoral Economies

## Notation Registry

| Rule | Convention | Example | Anti-Pattern |
|------|-----------|---------|-------------|
| Sector index | $k$ for sector, $i$ for residual sector | $g_{k,t}$, $\pi_{i,t}$ | Using $i$ and $j$ interchangeably |
| Country-sector | Country $k$, sector $i$ (Aguilar et al.) | $\mathrm{mc}_{ki,t}$ | Swapping country/sector order |
| Hat notation | Log-deviation from steady state | $\hat{w}_{k,t}$ | Missing hat on deviations |
| Calvo parameter | $\alpha_k$ (simple model), $\theta^p_{ki}$ (Aguilar) | $\alpha_k$ in slides 2-3 | Mixing $\alpha$ and $\theta$ conventions |
| Accent red | `\red{}` for emphasis in equations | `\red{\hat{\tau}^w_{k,t}}` | Using raw colour commands |

## Symbol Reference

| Symbol | Meaning | Introduced |
|--------|---------|------------|
| $y_{k,t}$ | Output gap, sector $k$ | Slide 2 (welfare loss) |
| $\pi_{k,t}$ | Inflation, sector $k$ | Slide 2 (welfare loss) |
| $g_{k,t}$ | Gov spending gap, sector $k$ | Slide 2 (welfare loss) |
| $\bar{G}_t$ | Exogenous aggregate public-good bundle | Slide 2 (key constraint) |
| $\sigma$ | CRRA coefficient | Slide 2 (utility) |
| $\varphi$ | Inverse Frisch elasticity | Slide 2 (utility) |
| $\chi_k$ | Public-good share, sector $k$ | Slide 2 (welfare) |
| $\lambda_k$ | Phillips curve slope, sector $k$ | Slide 2 (welfare) |
| $\mu_k$ | Sectoral weight in welfare | Slide 2 (welfare) |
| $\Phi_{ki}$ | Structural coefficient in relative rule | Slide 3 |
| $\mathrm{mc}_{ki,t}$ | Marginal cost, country $k$ sector $i$ | Slide 4 (Aguilar) |
| $\omega_{klij}$ | IO expenditure share | Slide 4 (Aguilar) |
| $\mathcal{M}_{ki}$ | Steady-state markup | Slide 4 (Aguilar) |
| $\kappa_{ki}$ | Phillips curve slope (Aguilar) | Slide 4 |
| $\hat{\tau}^w_{k,t}$ | Labour income tax deviation | Slide 5 (extension) |
| $\hat{\tau}^s_{ki,t}$ | Production subsidy deviation | Slide 5 (extension) |
| $G_{ki,t}$ | Sector-specific gov purchases | Slide 6 (research agenda) |

## Lecture Progression

| # | Title | Core Question | Key Notation | Key Method |
|---|-------|--------------|-------------|------------|
| S1 | Motivation & Plan | What is the welfare cost of constrained fiscal policy? | -- | -- |
| S2 | Simple Multi-Sector Model | How does the welfare loss decompose? | $y_{k,t}$, $\pi_{k,t}$, $g_{k,t}$ | 2nd-order welfare approximation |
| S3 | Relative Allocation Rule | What is the optimal spending rule under budget constraint? | $\Phi_{ki}$, $g_{k,t}$ | FOC of constrained planner |
| S4 | Aguilar et al. (2025) | How do production networks transmit shocks? | $\mathrm{mc}_{ki,t}$, $\omega_{klij}$ | Log-linearised DSGE |
| S5 | Fiscal Extensions | How do taxes/subsidies enter Phillips curves? | $\hat{\tau}^w$, $\hat{\tau}^s$ | Calvo pricing with wedges |
| S6 | Research Agenda | How large is the welfare gap: fixed vs endogenous budget? | $G_{ki,t}$ | Ramsey optimal policy |
| S7 | Summary | -- | -- | -- |

## Key References

| Paper | Role in Talk | Slide(s) |
|-------|-------------|----------|
| Cox et al. (2024) | Foundation: simple multisectoral fiscal model | S1, S2, S3 |
| Aguilar, Ghironi & Piersanti (2025) | Rich model with production networks + tariffs | S1, S4, S5, S6 |
| Acemoglu et al. (2012) | Network origins of fluctuations | S1 |
| Baqaee & Farhi (2020, 2024) | Networks, misallocation, trade | S1 |
| Rubbo (2023) | Networks and Phillips curves | S1 |

## Design Principles

| Principle | Evidence | Lectures Applied |
|-----------|----------|-----------------|
| Build up step by step | Simple → rich model flow | All slides |
| Equations must be self-contained | Each slide's math is derivable from stated assumptions | S2, S3, S5 |
| Use colour annotation sparingly | `\red{}` only for novel contributions | S3, S5, S6 |
| Two-column for dense model features | Keeps slide within 15-min constraint | S4, S6 |

## Anti-Patterns (Don't Do This)

| Anti-Pattern | What Happened | Correction |
|-------------|---------------|-----------|
| Mixing $\alpha_k$ and $\theta^p_{ki}$ | Calvo parameter notation differs between simple and Aguilar models | Always specify which model context |
| Omitting steady-state bars | Readers confuse levels with deviations | Always use $\bar{G}$ vs $g_{k,t}$ |
| Overloading subscript $k$ | Country vs sector ambiguity in Aguilar model | Use $k$ for country, $i$ for sector in Aguilar context |
