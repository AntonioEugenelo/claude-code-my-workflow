# Theory Review: Tariffs_ECB Section 5

**Date:** 2026-04-11  
**Scope:** Theory coherence only, current Section 5 rewrite  
**File reviewed:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`

## Overall Score

**97/100**

The Section 5 rewrite is materially tighter than the earlier version. The section now cleanly separates three distinct objects that were previously easy to conflate: sectoral contributions to aggregate GDP/CPI, own-sector value-added responses, and appendix-based cross-sectional ranking diagnostics. The new table-based treatment of the horse-race results is also theoretically much better than the old figure-heavy "structural determinants" discussion, because it is explicit that the appendix delivers reduced-form ranking diagnostics rather than a structural decomposition.

## Main Findings

### 1. Minor: The euro-area explanation still reads slightly more like a channel decomposition than the evidence identifies

- **Location:** `56_sectoral_channels.tex:95`, `56_sectoral_channels.tex:97`, `56_sectoral_channels.tex:101`, `56_sectoral_channels.tex:110`
- **Why it matters:** The section is now careful that the EA result is a net general-equilibrium outcome, but the phrasing still sometimes sounds as if "trade diversion" and "upstream cost propagation" have been separately measured and then netted out. The appendix and the benchmark simulations support this as a narrative interpretation of one GE response, not as a cleanly isolated two-channel decomposition.
- **Suggested fix:** Keep the mechanism story, but preserve the qualifier everywhere: these are organizing forces behind one equilibrium response, not separately identified counterfactual components.

### 2. Minor: The alpha-mu reversal is well documented, but one explanatory sentence is slightly stronger than the diagnostics shown

- **Location:** `56_sectoral_channels.tex:79`
- **Why it matters:** The appendix tables establish the directional reversal clearly: under the reverse China-to-US shock, `alpha` becomes more informative than `mu` for China as the imposing country and the US as the receiving country. What the current sentence adds is a stronger causal explanation, namely that Chinese imports from US sectors are "smaller and much flatter across sectors." That interpretation is plausible and likely correct, but Section 5 does not itself show the distributional evidence; the sentence therefore outruns the displayed diagnostics a bit.
- **Suggested fix:** Recast the claim as an interpretation rather than a demonstrated fact, for example by saying the reversal is "consistent with a weaker and flatter import-penetration margin under the reverse shock."

## What Works

- The opening distinction between aggregate contributions, own-sector responses, and appendix diagnostics is now explicit and theoretically clean.
- The section no longer oversells the appendix as structural identification; it repeatedly frames the horse-race exercise as descriptive.
- The new treatment of `alpha` and `mu` is substantially better than the earlier single trade-share narrative because it makes the benchmark result directional rather than universal.
- The new Section 5.4 is effective: it shows that the sectors most important for aggregate CPI, GDP, and consumption need not coincide exactly with those showing the largest own-sector value-added stress.

## Bottom Line

There is **no major theory-coherence problem** in the current Section 5. The remaining issues are both minor and both concern interpretive precision, not the underlying logic of the section.
