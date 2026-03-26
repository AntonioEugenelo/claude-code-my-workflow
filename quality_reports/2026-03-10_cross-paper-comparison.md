# Cross-Paper Comparison: ADDDGQ (2025) vs Jouvanceau et al. (2025) and Paries Discussant Slides

**Date:** 2026-03-10
**Purpose:** Systematic comparison of results, narrative, and claims between:
- **ADDDGQ (2025):** Aguilar, Darracq Paries, Dieppe, Dominguez-Diaz, Gallegos, Quintana -- "US-China decoupling and the euro area" (our paper, sections 55a/55b/55c)
- **JDDK (2025):** Jouvanceau, Darracq Paries, Dieppe, Kockerols -- "Trade wars and global spillovers: A quantitative assessment with ECB-Global" (ECB WP 3117)
- **Paries slides (Sep 2025):** Discussant slides at BoC-ECB conference, which present results from *both* models

---

## 1. Model Structure Comparison

| Feature | ADDDGQ (our paper) | JDDK / ECB-Global 3.0 |
|---------|--------------------|-----------------------|
| **Model type** | Micro-founded multi-sector NK DSGE | Semi-structural multi-region macro |
| **Countries/regions** | 4 (EA, CHN, USA, ROW) | 8 (US, EA, CN, Japan, UK, EME Asia, Oil Producers, ROW) |
| **Sectors** | 44 (3 energy, 21 services, 20 tradeable mfg) | 1 composite good per region |
| **Production networks** | Explicit IO matrix (OECD ICIO 2019), domestic + international | None (single composite good, no IO) |
| **Price setting** | Calvo, heterogeneous across sectors (PRISMA data) | Semi-structural Phillips curve |
| **Invoicing** | Heterogeneous DCP (7 PCP, 19 LCP, 18 DCP sectors) | Aggregate DCP share per region (Table 3: EA 32%, CN 86%) |
| **Exchange rate regime** | Baseline: all flexible; Robustness: China peg | China managed float in baseline |
| **Financial linkages** | Incomplete international markets only | Financial spillovers (all except China) |
| **Oil market** | No explicit oil block | Oil prices, oil consumption, oil revenues |
| **Trade diversion** | Endogenous via Armington substitution | Explicit trade diversion parameter |
| **Tariff persistence** | AR(1), rho=0.96 | AR(1), rho=0.975 (conditional forecast) |
| **Solution method** | 1st-order log-linear (hand-derived) | Linear semi-structural |
| **Calibration** | OECD ICIO 2019, PRISMA, COICOP | ECB-Global historical estimation |

**Key structural differences that explain result differences:**
1. ADDDGQ has IO networks (amplification mechanism absent from JDDK)
2. ADDDGQ has sectoral heterogeneity (allows sectoral reallocation costs)
3. JDDK has oil market, financial linkages, more regions (richer spillover channels)
4. JDDK models China's managed float in baseline; ADDDGQ has flexible rates
5. JDDK has 8 regions allowing richer third-country spillover analysis

---

## 2. Scenario Mapping

The two papers use different shock specifications. Approximate mappings:

| ADDDGQ scenario | Tariff specification | Closest JDDK scenario |
|------------------|---------------------|----------------------|
| Benchmark (55a) | 10pp bilateral US-CHN on 20 mfg sectors | Fig 1: 10% US unilateral on China |
| Liberation Day S1 | 54% on CHN only | No direct analog (scaled bilateral) |
| Liberation Day S2 | 20% EA, 145% CHN, 25% ROW | Severe scenario (~32pp weighted avg) |
| Liberation Day S3 | S2 + full symmetric retaliation | Severe scenario (includes retaliation) |
| Sectoral targeting (55c) | 10pp bilateral US-EA | Fig 1.C: 10% US on EA imports |

**Important caveats on comparison:**
- ADDDGQ Liberation Day scenarios use *linear scaling* of the 10pp benchmark (model is log-linearized). For tariffs as high as 145%, this extrapolation is acknowledged as extending beyond the local domain of approximation.
- JDDK scenarios use *conditional forecasts* with actual 2025 tariff schedules (Table 4) applied to goods & services.
- ADDDGQ tariffs apply only to 20 tradeable manufacturing sectors; JDDK tariffs apply to all goods and services.
- Reporting conventions differ: ADDDGQ reports on-impact deviations and quarterly IRFs; JDDK reports peak deviations; Paries slides report 3-year cumulative deviations.

---

## 3. Quantitative Comparison: 10pp Bilateral US-China Tariff

This is the most directly comparable experiment across the papers.

### 3.1 GDP Responses

| Variable | ADDDGQ (on impact) | ADDDGQ (3-yr avg) | JDDK (on impact) | JDDK (peak) |
|----------|--------------------|--------------------|-------------------|-------------|
| US GDP | -0.04% | ~+0.01% (recovers) | -0.1% (Fig 1.A) | -0.1% |
| China GDP | -0.36% | -0.15% | -0.3% (Fig 1.B) | -0.3% |
| EA GDP | -0.025% | ~+0.01% | "limited spillover" | ~-0.02% |

**Assessment:** On-impact US effects are smaller in ADDDGQ (-0.04% vs -0.1%), likely because:
- ADDDGQ tariffs apply only to 20 manufacturing sectors (not services), so the effective tariff is smaller in coverage
- ADDDGQ includes tariff revenue rebate to households, which provides an offsetting positive transfer
- The ADDDGQ US GDP recovers quickly (positive by Q4), whereas JDDK shows a more persistent contraction

China impacts are broadly comparable (-0.36% ADDDGQ vs -0.3% JDDK on impact). The slightly larger ADDDGQ effect may reflect IO network amplification.

EA spillovers are minimal in both models -- consistent.

### 3.2 Inflation Responses

| Variable | ADDDGQ (on impact) | JDDK (on impact, yoy) |
|----------|--------------------|-----------------------|
| US CPI | +0.13 pp | +0.1 pp |
| China CPI | +0.12 pp | ~-0.02 pp (muted) |
| EA CPI | +0.03 pp | +0.1 pp |

**Assessment:**
- US inflation broadly similar (+0.13 vs +0.1 pp)
- **China inflation: significant divergence.** ADDDGQ shows +0.12pp initial spike (driven by renminbi depreciation and demand reallocation), whereas JDDK shows muted or negative CPI. **Explanation: structural.** JDDK models China's managed float in baseline, which prevents large renminbi depreciation and thus limits import price pass-through. ADDDGQ's baseline has flexible rates for China, allowing the renminbi to depreciate and pass through to CPI. When ADDDGQ runs the peg robustness check, the China exchange rate channel is suppressed, but CPI results under the peg are not separately reported.
- **EA inflation: divergence.** ADDDGQ shows +0.03pp while JDDK shows +0.1pp. JDDK's larger EA inflation likely reflects: (a) euro depreciation against USD in JDDK is larger because financial linkages amplify the effect; (b) JDDK includes oil price channel (global oil price rises from tariff shock); (c) JDDK's DCP parametrization for EA (32% of exports in USD) generates more import price pass-through at the aggregate level.

### 3.3 Trade Balance

| Variable | ADDDGQ (on impact) | JDDK |
|----------|--------------------|----|
| US TB | +1.6% improvement | US imports -1.3% (large) |
| China TB | -1.0% deterioration | CN exports -2.2% |
| EA TB | +0.03% slight improvement | EA trade balance improves (small) |

Both models agree on the direction of trade balance effects. JDDK reports larger trade volume changes, partly because tariffs apply to all goods and services (broader base).

### 3.4 DCP vs PCP

| Metric | ADDDGQ | JDDK |
|--------|--------|------|
| China GDP under DCP vs PCP | -0.15% vs -0.11% (3-yr avg) | China GDP falls 0.1pp less without DCP |
| Direction | DCP deepens China contraction | DCP deepens China contraction |
| Mechanism | Exchange rate decoupling, amplified cost propagation | USD pricing prevents FX buffering |
| Relative importance | "Critical" but IO networks are "primary amplification" | "DCP dominates trade diversion in driving global spillovers" |

**Assessment:** Both agree DCP deepens Chinese contraction and amplifies global spillovers. The magnitude of the DCP effect is remarkably similar (~0.04pp in ADDDGQ vs 0.1pp in JDDK for China GDP). The key narrative difference is:
- **JDDK:** "DCP dominates trade diversion" as the leading channel
- **ADDDGQ:** IO networks are the "primary amplification mechanism"; DCP is important but secondary to production networks

This difference is **structural**: JDDK has no IO networks, so DCP must be the dominant channel. ADDDGQ, by including IO networks, finds they matter more than DCP alone. **This is a complementary finding, not a contradiction.**

---

## 4. Quantitative Comparison: Broad/Liberation Day Scenarios

### 4.1 JDDK Baseline (10.7pp weighted avg US tariffs, May 2025 actuals)

| Variable | JDDK baseline | ADDDGQ closest: Liberation S2 (20% EA, 145% CN, 25% ROW) |
|----------|--------------|-----------------------------------------------------------|
| US GDP | -0.45% (peak) | -0.05% on impact |
| China GDP | -0.75% | -0.59% on impact |
| EA GDP | -0.10% | -0.14% on impact |
| US CPI | +0.7 pp | Not separately reported for S2 |
| EA CPI | +0.2 pp | +0.10 pp on impact |
| US policy rate | +130 bp | Not separately reported |

**Assessment:** Direct comparison is difficult because:
1. JDDK's baseline includes *actual* tariff schedules (5.4pp on EA, 25.9pp on China, etc.) while ADDDGQ S2 uses stylized rates (20% EA, 145% CN, 25% ROW)
2. JDDK tariffs apply to goods & services; ADDDGQ to manufacturing only
3. JDDK includes oil, financial channels, and 8 regions
4. JDDK reports peak effects; ADDDGQ reports on-impact effects

The US GDP difference is striking (-0.45% JDDK vs -0.05% ADDDGQ). While some of this is explained by structural differences, the magnitude gap deserves scrutiny (see Flag 1 below).

### 4.2 JDDK Severe (32.4pp weighted avg, April 2 levels)

| Variable | JDDK severe | ADDDGQ Liberation S3 (+ retaliation) |
|----------|-------------|---------------------------------------|
| US GDP | -1.8% | -0.39% on impact |
| China GDP | -2.8% | -0.39% on impact |
| EA GDP | -0.85% | -0.08% on impact |
| US CPI | +2.0 pp | Not separately reported |
| EA CPI | +0.6 pp | +0.06 pp spike |

**Assessment:** JDDK severe scenario produces dramatically larger effects than ADDDGQ S3. Multiple structural factors contribute:
1. JDDK severe includes 50% on EU, 120% on China -- substantially different from ADDDGQ S3 rates
2. JDDK's monetary policy tightening (380bp US, 115bp EA) amplifies the contraction
3. JDDK's financial linkages and equity price channels add demand contraction
4. JDDK's oil channel adds inflationary pressure
5. But: ADDDGQ's linear scaling may *understate* effects at these tariff magnitudes (acknowledged in paper's footnote 1 of S55b)

### 4.3 10pp US Tariff on EA

| Variable | ADDDGQ (55c) | JDDK (Fig 1.C) | Paries slide 17 |
|----------|--------------|-----------------|-----------------|
| EA GDP | -0.344 pp (sum across sectors) | -0.25% on impact | -0.12% (baseline) |
| US GDP | ~0 (near zero) | ~-0.05% | ~0 |

This comparison reveals an important discrepancy -- see Flag 2 below.

---

## 5. Narrative Differences

### 5.1 Primary transmission mechanism

| Aspect | ADDDGQ | JDDK |
|--------|--------|------|
| Lead mechanism | IO networks are "primary amplification" | DCP "dominates trade diversion" |
| Secondary | DCP invoicing | Trade diversion |
| Tertiary | Trade elasticity | Financial spillovers, oil |

**Structural explanation:** JDDK has no IO channel, so it cannot identify network amplification. ADDDGQ has no oil or financial channels. Each paper identifies as "primary" the mechanism that is *present and active* in their model. **Not contradictory -- complementary.**

### 5.2 China's exchange rate response

| Aspect | ADDDGQ | JDDK |
|--------|--------|------|
| Baseline regime | Flexible | Managed float |
| Key implication | Renminbi depreciates, buffering exports but raising CPI | Managed float limits FX adjustment, mutes inflation |
| Robustness | Peg amplifies contraction by 55% | Not a robustness check (in baseline) |

**Structural explanation:** Different baseline assumptions. ADDDGQ's robustness peg result (55% amplification) is qualitatively consistent with JDDK's finding that China's managed float constrains the exchange rate channel.

### 5.3 EA monetary policy implications

| Aspect | ADDDGQ | JDDK |
|--------|--------|------|
| Key finding | DCP constrains ECB exchange rate channel | CPI-targeting requires tightening, amplifies contraction |
| Alternative rules | "Beyond scope" | PPI targeting "slightly better"; annual CPI also helps |
| Recommendation | None (mechanical Taylor rule) | PPI or annual CPI targeting reduces GDP cost |

**Assessment:** JDDK provides more actionable policy analysis because it explores alternative Taylor rules. ADDDGQ's contribution is identifying that DCP *constrains* the exchange rate channel but does not explore the implication for optimal rules. **There is no contradiction, but ADDDGQ could reference JDDK's finding that PPI targeting helps.**

### 5.4 Sectoral heterogeneity

| Aspect | ADDDGQ | JDDK |
|--------|--------|------|
| Sectoral analysis | Extensive (44 sectors, heatmaps, rankings) | None (single composite good) |
| Key finding | Pharma, Chemicals, Motor Vehicles dominate EA effects | N/A |
| IO intensity vs trade exposure | IO intensity, not bilateral trade exposure, drives aggregate impact | N/A |
| Retaliatory design | Sector-by-sector cost-benefit analysis | No sectoral retaliation analysis |

**Structural explanation:** Entirely attributable to model structure. JDDK cannot do sectoral analysis; this is ADDDGQ's unique contribution. The Paries discussant slides explicitly identify this as a limitation of two-region aggregate models (slide 8: "two-region aggregate masks sectoral reallocation costs").

### 5.5 Trade diversion

| Aspect | ADDDGQ | JDDK |
|--------|--------|------|
| Mechanism | Endogenous via Armington elasticity | Explicit trade diversion parameter |
| EA benefit | Small positive (+0.03% TB from US-CN tariff) | "EA trade balance improves" |
| Direction | Both agree EA can benefit from trade diversion | Both agree |
| Quantitative role | Secondary to IO amplification | One of two key channels (alongside DCP) |

**Assessment:** Consistent findings -- both papers agree that trade diversion creates small EA benefits from US-CN bilateral tariffs. JDDK finds trade diversion matters more because its model has no IO to compete as an alternative channel.

---

## 6. FLAGS: Discrepancies Not Fully Explained by Model Structure

### FLAG 1: US GDP impact under broad tariffs -- large magnitude gap

**JDDK baseline:** US GDP -0.45% (peak) under ~10.7pp weighted avg US tariffs
**ADDDGQ Liberation S2:** US GDP -0.05% on impact under 20% EA + 145% CN + 25% ROW

Even accounting for reporting differences (peak vs on-impact) and the fact that ADDDGQ tariffs apply only to manufacturing (not services), the gap is difficult to reconcile. ADDDGQ's tariff *rates* in S2 are far higher than JDDK's baseline, yet produce a much smaller US GDP contraction.

**Possible explanations:**
1. ADDDGQ tariff revenue is rebated lump-sum, which directly offsets household income loss -- the paper explicitly notes this as a recovery mechanism. JDDK may recycle revenue differently.
2. ADDDGQ has no financial spillovers (no equity channel, no real interbank rate amplification). JDDK's monetary tightening and equity price declines substantially amplify the contraction.
3. ADDDGQ tariffs apply to 20/44 sectors only. Many service sectors (21/44) are unaffected.
4. ADDDGQ's linear approximation may understate effects at Liberation Day magnitudes.
5. **ADDDGQ lacks an oil channel** -- global oil price increases would add inflationary and contractionary pressure.

**Recommended action:** Verify whether the revenue recycling assumption and the limited sectoral coverage account for the bulk of the gap. Consider a back-of-envelope calculation comparing effective tariff *rates* weighted by trade shares.

### FLAG 2: Paries slides vs current paper on EA GDP from 10pp US-EA tariff

**Paries slide 17 (Sep 2025):** EA GDP -0.12% (baseline) from 10pp US tariff on EA goods
**ADDDGQ paper (current, 55c):** Total EA GDP effect -0.344pp from 10pp US-EA bilateral tariff

This is the **same model, same experiment**, presented at two points in time. The current paper shows an EA GDP effect nearly 3x larger than what was presented at the BoC-ECB conference.

**Possible explanations:**
1. **Calibration change:** The model may have been recalibrated between Sep 2025 and the current version (Mar 2026). Different ICIO vintage, different Calvo parameters, or different trade elasticities could change magnitudes.
2. **Metric difference:** The Paries slide may report on-impact or peak GDP deviation, while the paper's -0.344pp may be a cumulative or sectoral-sum measure. However, the paper describes this as "aggregate GDP response" which typically means the single-period aggregate effect.
3. **Shock specification:** The slide says "US 10% tariff on EA goods (no retaliation)" -- the paper applies "10pp bilateral US tariff on EA exports" which should be equivalent.
4. **IO structure change:** The Paries slide also shows "No IO" at -0.10%, very close to the baseline -0.12%. If IO amplification went from negligible to substantial between versions, this suggests a change in IO calibration.

**Recommended action:** This discrepancy should be resolved before the paper is circulated. If the calibration changed, document the change. If the metrics differ, clarify both the slide and paper numbers.

### FLAG 3: Paries slides US GDP (-2.0%) vs current paper scaling

**Paries slide 14:** "US and China GDP drop by 2.0% and 2.5%" for 50% US-CN tariff (3-year cumulative)
**ADDDGQ current paper (55a):** 10pp benchmark gives US GDP -0.04% on impact, recovering to +0.035% by Q8

Under linearity, a 50% tariff = 5x the benchmark. The US cumulative 3-year GDP deviation from the 10pp benchmark would need to be ~-0.4% for the 50% scaling to produce -2.0%. Given the rapid recovery pattern in the current paper (positive by Q4), the cumulative 3-year US GDP effect from the 10pp benchmark appears close to zero or slightly positive.

5 x (~0) != -2.0%.

**This arithmetic does not add up under the current calibration.** Either:
1. The model calibration changed substantially (e.g., the trade elasticity was higher in the Sep 2025 version, producing larger and more persistent US contractions)
2. The Paries slides used a different calibration variant (e.g., the "higher trade elasticity" sensitivity shown in slide 15)
3. The 3-year cumulative convention in the slides includes a different set of quarters or uses a different deviation measure

**Recommended action:** This is the most important flag. The Paries slides are the paper's only public-facing presentation to date, and the numbers shown there should be reconcilable with the published paper. If the calibration has changed, the slides should be updated or the paper should note the change.

### FLAG 4: China inflation narrative

**JDDK:** China CPI "muted" or negative under tariff shock -- consistent with managed float limiting FX pass-through
**ADDDGQ:** China CPI +0.12pp on impact, comparable to US (+0.13pp)

Under ADDDGQ's flexible-rate baseline, China experiences substantial CPI inflation from the tariff shock. This is driven by renminbi depreciation and demand reallocation effects. **However, the paper's robustness check with a China peg (phi_{k,e}=15) should substantially alter this result.** The paper reports the peg amplifies *GDP contraction* by 55% but does not separately report the *inflation* effect under the peg.

**Why this matters:** If the paper is to be compared with ECB-Global or cited alongside it, the reader may be confused by opposite China inflation results. The paper should clarify that the baseline assumes flexible Chinese rates (unlike reality and unlike JDDK's baseline).

**Recommended action:** Consider adding a sentence noting that under a managed float (or peg), Chinese CPI inflation would be substantially lower, consistent with JDDK's findings.

### FLAG 5: EA spillovers -- qualitative consistency but quantitative ambiguity

Both papers agree that EA spillovers from US-CN bilateral tariffs are small. But the *sign* of the cumulative EA GDP effect differs:
- **ADDDGQ S1 (54% on CN only):** Cumulative EA GDP +0.083pp (positive, trade diversion)
- **JDDK baseline (includes small EA tariffs too):** EA GDP -0.1% (negative)

This is partly explained by JDDK's baseline including some tariffs on the EA (5.4pp), while ADDDGQ S1 has zero EA tariffs. But the Paries slides (slide 16) show EA GDP is near zero or slightly positive in the ADDDGQ baseline -- consistent with the paper.

**No action needed** -- the difference is explained by shock specification (EA is tariffed in JDDK baseline, untariffed in ADDDGQ S1).

---

## 7. Complementary Findings (No Conflict)

The following results are consistent across both papers and reinforce each other:

1. **Tariffs are contractionary for all parties** -- both models find negative global GDP effects
2. **DCP amplifies tariff transmission** -- agreed on direction and qualitative importance
3. **Retaliation worsens outcomes for all** -- ADDDGQ S3 and JDDK severe both show escalation costs
4. **EA spillovers from US-CN bilateral tariffs are small** -- both agree
5. **Trade diversion creates some third-country benefits** -- both agree
6. **Exchange rate regime matters for China** -- JDDK (managed float in baseline) and ADDDGQ (peg robustness) both show FX regime shapes outcomes
7. **Monetary policy rule choice affects outcomes** -- JDDK explores alternatives, ADDDGQ's Taylor rule discussion is qualitatively consistent

---

## 8. Summary Table of Flags

| Flag | Issue | Severity | Explainable by structure? | Recommended action |
|------|-------|----------|--------------------------|-------------------|
| **1** | US GDP much smaller in ADDDGQ under broad tariffs | Medium | Partially (revenue recycling, no financial channel, manufacturing only) | Verify arithmetic; add discussion |
| **2** | Paries slide EA GDP (-0.12%) vs paper (-0.344pp) for same experiment | **High** | No -- same model | Reconcile; document calibration change |
| **3** | Paries slide US GDP (-2.0%) inconsistent with current 10pp benchmark scaling | **High** | No -- same model | Reconcile; update slides or document change |
| **4** | China inflation direction opposite (muted in JDDK, +0.12pp in ADDDGQ) | Medium | Yes (exchange rate regime) | Add clarifying sentence |
| **5** | EA spillover sign (positive in ADDDGQ S1, negative in JDDK baseline) | Low | Yes (different shock specs) | No action needed |

---

## 9. Recommendations for the Paper

1. **Acknowledge JDDK explicitly** in the related literature or results discussion, as it uses the same co-authors and institution but a different model. A sentence like: "Using the semi-structural ECB-Global model, Jouvanceau et al. (2025) find broadly similar qualitative patterns for a comparable tariff shock, with the key distinction that our multi-sector framework identifies IO networks as the primary amplification mechanism absent from aggregate models."

2. **Reconcile the Paries slide numbers** with the current paper before public release. The -2.0% US GDP and -0.12% EA GDP on the slides do not match the current calibration.

3. **Clarify China's exchange rate assumption** in the benchmark discussion. The paper's baseline flexible-rate assumption for China differs from JDDK (and from reality), and this explains the opposite China inflation results.

4. **Consider adding a short comparative paragraph** in section 55a noting that ADDDGQ's smaller US GDP effects relative to ECB-Global partly reflect the absence of financial spillovers, oil channels, and the limited sectoral coverage of tariffs (manufacturing only).
