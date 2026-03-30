# Narrative Changes Due to Heterogeneous DCP Bug Fix

**Date:** 2026-03-28
**Bug:** `b4_declare_model.mod` applied dollar exchange rates to domestic DCP sales. Fix: commit `1e57e26`.
**Scope:** All quantitative results for non-US economies; US results changed <5%.

---

## Root Cause

The bug applied the bilateral dollar exchange rate to *domestic* sales in DCP sectors. Domestic prices should not involve exchange rates — only export prices are invoiced in foreign currency. The effect was to inflate non-US CPI responses by transmitting dollar exchange rate movements into domestic consumer prices, creating a spurious DCP amplification channel for China and the EA.

---

## 1. EA Third-Country Spillover: From "Mildly Contractionary" to "Essentially Zero"

| | OLD | NEW |
|---|---|---|
| EA GDP Q1 | −0.025% | **+0.001%** |
| EA GDP 3yr avg | +0.013% | +0.009% |
| EA CPI Q1 | +0.035 pp | **+0.007 pp** |
| EA interest rate Q1 | 0.015 pp | **0.003 pp** |

**Narrative shift:** The EA was previously characterized as experiencing a "mild contractionary spillover" from the US–China tariff. Now the EA is "essentially unaffected on impact" — trade diversion toward EA producers *nearly exactly offsets* the upstream cost propagation through IO linkages. The two channels generate competing forces that cancel to within numerical precision.

**Affected text:** Section 5.1 (GDP, CPI, TB paragraphs), Section 5.1.3 (EA transmission), Section 5.6 (EA sectoral exposure), Conclusions.

---

## 2. China CPI: From "Substantial" to "Negligible"

| | OLD | NEW |
|---|---|---|
| CHN CPI Q1 | 0.120 pp | **0.015 pp** (−88%) |
| CHN CPI / US CPI ratio | ~94% | **~12%** |

**Narrative shift:** Previously, the Chinese CPI response was nearly as large as the US response, suggesting the tariff raised prices globally. Now Chinese CPI is one-eighth of the US response. The new narrative: "the tariff is levied at the US border and does not directly raise Chinese consumer prices; the modest positive response reflects second-round effects through renminbi depreciation on non-dollar-invoiced imports."

**Affected text:** Section 5.1 (CPI paragraph), Section 5.6 (Chinese sectoral inflation discussion).

---

## 3. Full DCP: From "Amplifies" to "Dampens" (Ordering Reversal)

| | OLD | NEW |
|---|---|---|
| CHN GDP 3yr (Het DCP) | −0.151% | −0.147% |
| CHN GDP 3yr (Full DCP) | **−0.283%** | **−0.135%** |
| Full DCP vs Het DCP | Full DCP **more severe** | Full DCP **less severe** |
| EA GDP 3yr (Full DCP) | −0.019% | **+0.009%** (sign flip) |

**Narrative shift:** The old narrative was straightforward: "full dollar invoicing amplifies tariff transmission by shutting down the expenditure-switching channel." The new narrative is counterintuitive and requires careful explanation: full DCP produces a *smaller* Chinese contraction than heterogeneous DCP. The text explains this as "the interaction of two offsetting forces: while full dollar invoicing shuts down the expenditure-switching channel (amplifying the trade disruption), it also eliminates exchange rate pass-through to domestic intermediate input prices, reducing the cost-push amplification through production networks. The net effect depends on the relative strength of these two channels and is not analytically signed."

**Mechanism (corrected after theory-critic review):** The Het→Full DCP switch replaces 20 LCP and 7 PCP sectors with DCP. The key is how LCP→DCP changes *import* demand equations:

- **PCP→DCP (7 sectors):** Removes expenditure-switching for exporters → harms targeted country (standard story).
- **LCP→DCP (20 sectors):** Under LCP, the demand-relevant import price has **no exchange rate term** — prices are sticky in the buyer's currency, so exchange rates are irrelevant for demand on impact. Under DCP, the buyer's USD rate enters demand ($\hat{q}_{k,\text{US}}$). For China, this means CNY depreciation vs USD now raises the cost of ALL imports in those 20 sectors. Two simultaneous effects:
  - **Import compression:** Higher import prices reduce import quantities → improves China's trade balance (−0.88% vs −1.02%)
  - **Higher import costs:** Raises CES consumption price index → worsens China's consumption (−0.08% vs −0.06%)
  - The trade balance improvement dominates in GDP accounting.

**Critical note:** For US-China bilateral trade, LCP and DCP are mechanically identical (US is the dollar country, so $q_{\text{US},\text{US}} = 0$). The entire Full DCP vs Het DCP gap is driven by third-country indirect effects, not the primary tariff channel.

**Earlier incorrect explanation:** A previous version attributed PCP's exchange-rate-in-demand property to LCP (claiming LCP "enables bilateral exchange rate trade diversion"). This was wrong — under LCP, no exchange rate enters demand. The correct mechanism is import compression from the introduction of the USD exchange rate into demand equations that previously had none.

**Implication:** This result depends on the trade elasticity and the share of LCP sectors. The paper characterizes it as "not analytically signed." Running intermediate counterfactuals (switching only LCP or only PCP sectors) would provide the acid test.

**Affected text:** Section 5.2 (DCP vs PCP comparison — rewritten with import compression mechanism), Conclusions.

---

## 4. Monetary Policy: From "Matters" to "Irrelevant"

| | OLD | NEW |
|---|---|---|
| CHN GDP 3yr (Benchmark) | −0.151% | −0.147% |
| CHN GDP 3yr (NoMonPol) | −0.158% | −0.140% |
| US CPI 3yr (NoMonPol) | 0.035 pp | **0.063 pp** |
| US REER Q1 (NoMonPol) | −0.215% | **−0.366%** |

**Narrative shift:** Previously, there were meaningful differences between the benchmark and no-monetary-policy counterfactuals, supporting a narrative about "the role of monetary policy in shaping tariff transmission." Now the results are nearly identical: China GDP −0.147% vs −0.140%, US +0.019% vs +0.021%, EA +0.009% vs +0.008%. The new narrative: "the insensitivity of the results to monetary policy reflects the structure of the tariff shock and the invoicing regime. Because the tariff shock is persistent ($\rho^\tau = 0.96$) and operates primarily through trade quantities and IO cost propagation, the monetary policy channel — which operates through the exchange rate via UIP — has limited scope to alter the transmission."

**Note:** The theory-critic flagged this as potentially an artifact of (a) growth targeting in the Taylor rule and (b) near-permanent shock persistence, not purely a DCP property. This should be acknowledged.

**Affected text:** Section 5.3 (new monetary policy paragraph), Conclusions.

---

## 5. Liberation Day S1: EA and ROW Flip to Positive

| | OLD | NEW |
|---|---|---|
| S1 EA GDP Q1 | **−0.13%** | **+0.01%** |
| S1 ROW GDP Q1 | **−0.16%** | **+0.06%** |
| S1 CHN GDP Q1 | −1.98% | −1.31% |
| S2 EA GDP Q1 | −1.38% | **−0.62%** (−55%) |
| S2 EA CPI Q1 | 0.96 pp | **0.18 pp** (−81%) |

**Narrative shift:** Under Scenario 1 (54% US tariff on China only), the EA and ROW previously contracted — suggesting negative spillovers even when not directly targeted. Now both are mildly positive, with trade diversion dominating: "the EA and ROW are essentially unaffected (+0.01% and +0.06% respectively), as trade diversion offsets the indirect contractionary impulse." This is a qualitative change in the policy message: bilateral US–China tariffs do not hurt uninvolved third countries at Liberation Day magnitudes.

Scenario 2 effects are halved in magnitude for EA CPI (0.96 → 0.18 pp) and substantially reduced for EA GDP (−1.38% → −0.62%).

**Affected text:** Appendix B (Liberation Day), Conclusions ("up to 0.62%" replaces larger figure).

---

## 6. Chinese Consumption: From "Large" to "Small" Relative to US

| | OLD | NEW |
|---|---|---|
| CHN consumption Q1 | −0.173% | **−0.055%** (−68%) |
| US consumption Q1 | −0.257% | −0.257% (unchanged) |
| CHN/US ratio | 67% | **21%** |

**Narrative shift:** Previously, Chinese consumers bore a substantial share of the welfare cost relative to US consumers. Now the Chinese consumption decline is less than one-quarter of the US decline. The new narrative emphasizes the asymmetry: "Chinese consumption contracts by 0.06% on impact — substantially less than the US decline — because the tariff is collected at the US border, so US consumers pay tariff-inclusive prices directly."

**Affected text:** Section 5.1 (consumption paragraph).

---

## 7. Reverse Direction: China CPI and Consumption Sign Flips

| | OLD | NEW |
|---|---|---|
| CHN CPI Q1 (reverse) | −0.023 pp | **+0.030 pp** (sign flip) |
| CHN consumption Q1 (reverse) | +0.009% | **−0.052%** (sign flip) |

**Narrative shift:** Under the Chinese tariff on US imports, Chinese CPI previously fell (deflationary) but now rises (+0.030 pp). Chinese consumption previously rose (tariff revenue benefit) but now falls (−0.052%). The new narrative: "Chinese CPI rises on impact (+0.030 pp) as the tariff directly raises import prices for Chinese consumers, before dissipating as the demand contraction dominates."

**Affected text:** Section 5.1 (CPI and consumption paragraphs, reverse direction).

---

## 8. Sectoral Targeting (US–EA Bilateral): Magnitudes Collapse

| | OLD | NEW |
|---|---|---|
| Pharma own-sector VA | −14.61% | **−4.53%** |
| Food & Bev own-sector VA | −7.03% | **−0.27%** |
| Total EA GDP (20 sectors) | −0.344 pp | **−0.285 pp** |
| Full retaliation EA GDP | +0.063 pp | **+0.031 pp** |
| Full retaliation EA CPI | +0.038 pp | **+0.054 pp** |
| Retaliation efficiency range | 1.8–23.9 | **1.4–5.5** |

**Narrative shift:** The sectoral targeting results are quantitatively different but qualitatively preserved. Pharma still dominates. The main change is that own-sector contractions are far less extreme (Pharma −14.61% → −4.53%), and the retaliation efficiency range is much narrower (max 5.5 vs 23.9), making the differentiation across sectors less dramatic. Food & Bev goes from "a large own-sector contraction" to "a modest own-sector contraction" — its 4th-place ranking is now driven primarily by its high consumption share rather than its within-sector response.

The retaliation cost changed character: EA GDP gains from retaliation halved (+0.063 → +0.031), but EA CPI cost increased (+0.038 → +0.054), making retaliation less attractive.

**Affected text:** Appendix C (sectoral targeting).

---

## 9. Cost-Push vs Trade Diversion Balance

**OLD narrative:** Cost-push channel from upstream IO propagation "dominates on impact, generating a contractionary impulse for the EA."

**NEW narrative:** "The two channels nearly exactly offset, with a marginally contractionary net impulse (+0.001% GDP) that is not economically distinguishable from zero."

**Affected text:** Section 5.1.3 (EA transmission paragraph, footnote).

---

## 10. Peg Amplification: Modest Increase

| | OLD | NEW |
|---|---|---|
| Peg amplification | 55.4% | **60.9%** |

**Narrative shift:** Minor quantitative change. The peg is slightly more costly post-fix (amplifies CHN GDP contraction by 61% vs 55%). Narrative unchanged: "the peg eliminates the expenditure-switching channel that a renminbi depreciation would provide."

**Affected text:** Section 5.3 (peg paragraph).

---

## Summary Table: Which Narratives Changed Qualitatively?

| Narrative | Change Type |
|-----------|-------------|
| EA impact response | **Qualitative flip** (contractionary → zero) |
| China CPI magnitude | **Order-of-magnitude reduction** |
| Full DCP vs Het DCP ordering | **Qualitative reversal** |
| Monetary policy relevance | **Qualitative collapse** (matters → irrelevant) |
| Liberation Day S1 third-country effects | **Qualitative flip** (negative → positive) |
| Chinese consumption relative to US | **Scale change** (67% → 21%) |
| Reverse-direction China CPI/consumption | **Sign flips** |
| Cost-push vs trade diversion | **Qualitative shift** (dominates → cancels) |
| Sectoral targeting magnitudes | Scale change (own-sector VA 3× smaller) |
| Peg amplification | Minor quantitative change |

---

## Footnote Added

A TODO footnote has been added to Section 5.2 (`55a_benchmark_and_robustness.tex`, line 104) flagging the need to add the DCP export Phillips curve to the theoretical appendix:

> *TODO: The DCP export Phillips curve — the equation in which the real exchange rate $\hat{q}_{kl,t}$ is replaced by the dollar exchange rate for non-US exporters — should be written down explicitly in the Appendix alongside the LCP condition (eq. A.5) and the PCP Phillips curve. This is the key equation differentiating the invoicing regimes and is currently absent from the derivation.*
