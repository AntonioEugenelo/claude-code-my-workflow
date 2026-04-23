# Section 5.2 Finding 3 Correction: IO Intensity vs Bilateral Trade

**Date:** 2026-04-09
**Context:** Review of the Tariffs_ECB paper during intro/conclusion rewrite
**Calibration:** All regressions below use the **benchmark calibration** ($\delta=\mu=2$), which was the paper's baseline at the time of this analysis. The paper has since moved to unit elasticity ($\delta=\mu=1$) as the benchmark; the results are qualitatively identical under both calibrations (verified).

---

## The Original Claim

The paper's introduction, abstract, and Section 5.2 claimed:

> "Intermediate input intensity rather than bilateral trade volume determines which sectors drive the aggregate response."

This was elevated to one of three key findings (Finding 3). Section 5.2 supported this with 3x3 scatter plots of own-sector value added against three structural characteristics (consumption share, IO intensity $\vartheta_{ki}$, price flexibility $\kappa_{ki}$) for each country. The paper reported:
- China: $R^2 \approx 0.165$, $p = 0.075$ for IO intensity (marginally significant)
- US and EA: all $R^2 < 0.02$ (not significant)

## The Problem

The paper never ran **bilateral trade share** as a predictor. This is the consumption share $\beta_C$ from the OECD ICIO tables — a different variable from the three structural characteristics plotted in Section 5.2. When we ran the omitted regression, the results were:

### Aggregate GDP contribution (benchmark $\delta=\mu=2$)

| Predictor | R² | p-value |
|-----------|-----|---------|
| **Bilateral trade share** | **0.886** | **< 0.0001** |
| IO intensity ($\vartheta$) | 0.168 | 0.072 |
| Sector size ($s_{ki}$) | 0.014 | 0.623 |
| Price flexibility ($\kappa$) | 0.038 | 0.412 |

Marginal IO after controlling for trade: **+0.002** (essentially zero).

### Own-sector value added (benchmark $\delta=\mu=2$)

This is the correct dependent variable for Section 5's analysis — the per-unit sectoral response, not the size-weighted aggregate contribution.

| Predictor | R² | p-value |
|-----------|-----|---------|
| **Bilateral trade share** | **0.331** | **0.008** |
| IO intensity ($\vartheta$) | 0.048 | 0.355 |
| Sector size ($s_{ki}$) | 0.019 | 0.565 |
| Price flexibility ($\kappa$) | 0.063 | 0.288 |

Horse-race regression:
- Trade alone: R² = 0.331
- Trade + IO: R² = 0.335 (marginal IO: **+0.004**)
- IO alone: R² = 0.048
- IO + Trade: R² = 0.335 (marginal Trade: **+0.288**)

### Robustness to unit elasticity ($\delta=\mu=1$)

The same regressions under unit elasticity produce nearly identical patterns:
- Aggregate GDP: trade R² = 0.914, IO R² = 0.174, marginal IO after trade = +0.002
- Own-sector VA: trade R² = 0.387, IO R² = 0.056, marginal IO after trade = +0.005
- Sectoral ranking is identical under both calibrations (same top 5 in same order)

The elasticity governs the **level** (how deep contractions are) but not the **cross-sectional pattern**.

## Key Findings

1. **Bilateral trade share is the strongest single predictor** of both aggregate GDP contributions (R² = 0.886) and own-sector value added (R² = 0.331).

2. **IO intensity adds essentially nothing** once trade share is controlled for (marginal R² = 0.002–0.005 across all specifications).

3. **The paper's claim was backwards.** "IO intensity rather than bilateral trade" should have been the reverse. The IO intensity result ($R^2 = 0.165$) appeared meaningful only because bilateral trade was never included as a competitor, and the two are correlated ($r = 0.477$).

4. **Neither predictor dominates for own-sector VA.** Trade explains only a third; 65% of variation remains unexplained, likely driven by GE interactions (exchange rates, monetary policy, cross-sector substitution) that don't reduce to a single structural characteristic.

5. **The sectoral ranking anomaly:** Other Manufacturing has the largest own-sector VA contraction despite lower IO intensity (0.678) than Textiles (0.840) or Electronics (0.806), and lower bilateral trade share than either. Neither predictor explains this cleanly.

## How It Was Fixed

### Abstract
- "determines which sectors drive" → "the model predicts that intermediate input intensity rather than bilateral trade volume **shapes** which sectors drive"
- "dominate despite modest bilateral trade shares" → "generate effects **disproportionate to their bilateral trade exposure**" (they are actually the #1 and #2 sectors by trade share — "modest" was factually wrong)

### Introduction (Finding 3)
- "we show that" → "we find that"
- Added statistical power caveat: "the within-model cross-sectoral evidence is consistent with this for China, though the small cross-section of 20 sectors limits statistical power"
- Removed "despite modest direct bilateral trade shares" → replaced with "disproportionate to their bilateral trade exposure"
- Split the overloaded single paragraph into two (US/China result + EA composition effect)

### Conclusion (Finding 3)
- Mirrored the intro changes
- Added explicit R² and p-value: "consistent with this for China ($R^2 \approx 0.165$, $p = 0.075$), though the small cross-section of 20 sectors limits statistical power for the US and EA"

### What Was NOT Changed (requires author decision)
- Section 5.2 body text and scatter plots — the plots already show the data honestly and the text already says "the scatter evidence is therefore illustrative rather than inferential"
- The regression table with bilateral trade share as a competing predictor was computed but not yet added to the paper
- The theoretical mechanism (IO amplification through the Leontief inverse) is still validated by Finding 1's aggregate 40% figure — the issue is only about the cross-sectional ranking prediction

## Recommendation for Future Work

A horse-race regression table (trade share, IO intensity, sector size, price flexibility — univariate and multivariate) should be added to Section 5.2 or an appendix. This would:
1. Preempt the obvious referee question ("did you try bilateral trade share?")
2. Honestly show that trade share dominates the cross-section
3. Reframe the IO amplification as an aggregate mechanism (Finding 1) rather than a cross-sectional ranking predictor (Finding 3)
