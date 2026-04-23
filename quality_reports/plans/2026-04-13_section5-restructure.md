# Plan: Restructure Section 5 — aggregate → within-sector → across-sector → EA

**Status:** ACTIVE (clarifications resolved in working notes on 2026-04-13; implementation in progress)
**Branch (parent):** `claude-ecb-tariffs`
**Submodule:** `master_supporting_docs/Tariffs_ECB` on `main` (uncommitted working tree)
**Effort:** high / comprehensive

---

## Final structure target

| § | Title | Purpose | Key figures |
|---|---|---|---|
| 5.1 | Aggregate Sectoral Contributions to GDP and Inflation | Explain aggregate response to sector-specific tariffs; fold in current Section 4.2 | `Fig_Sectoral_Bars_GDP`, `Fig_Sectoral_Bars_CPI`, `Fig_CHN_Structural_Scatter_3x4`, `Fig_US_Structural_Scatter_3x4` |
| 5.2 | Within-sector transmission: own-sector value added and inflation | Decompose aggregate into own-sector response; value-added / inflation tradeoff | "Figure 12" and "Figure 13" (see Q1) |
| 5.3 | Cross-sector transmission within the US and China | Decompose aggregate into *other-sector* responses to a single-sector shock | **NEW** `Fig_SectoralSpillover_Matrix` (20×44 × 2 panels: VA + inflation, rows = shocked tradeable sector, cols = all 44 responding sectors, both sorted by upstreamness ↓) |
| 5.4 | Euro area sectoral exposure | EA third-country sectoral pattern | `Fig_EA_Sectoral_Heatmap_USCN`, `Fig_EA_Structural_Scatter_3x4` |

Rationale: superposition (Section 5 preamble, line 15) lets us decompose the aggregate tariff response as sum over shocked sectors; each per-sector shock in turn decomposes into (a) the shocked sector's own response and (b) spillovers to all other sectors. 5.1 = aggregate; 5.2 = own-sector slice; 5.3 = all-other-sector slice; 5.4 = the same logic applied to a third country.

---

## Files to modify

### Paper (Tariffs_ECB submodule)
1. `0_clean/sections/55a_benchmark_and_robustness.tex` — **remove** current 4.2 subsection (lines 100–131 `\subsection{Sectoral Heterogeneity in Aggregate Impact}` through the paragraph ending before `\FloatBarrier` at 130). Keep 4.1 (aggregate dynamics + EA transmission), 4.3 (invoicing), 4.4 (robustness). Renumber internal cross-references: 4.3 becomes 4.2, 4.4 becomes 4.3.
2. `0_clean/sections/56_sectoral_channels.tex` — rewrite into 5.1–5.4 structure. Move content surgically rather than regenerate: most prose already exists, it's being re-sequenced and re-headed. New prose only for (a) 5.1 framing paragraph that joins folded 4.2 material to horse-race discussion, (b) 5.3 introduction to the spillover matrix, (c) short transitions between subsections.
3. `0_clean/0_main.tex` — no changes (section inputs unchanged).
4. Any file referencing `\ref{sec:sectoral_results}` (that label was in 4.2): `grep -rn "sec:sectoral_results"` and update. On a quick scan, `11_introduction.tex`, `13_roadmap.tex`, `56_sectoral_channels.tex` itself use it. New label: `sec:aggregate_sectoral_contributions` (placed in 5.1).

### Figure generation (MCMS)
5. `master_supporting_docs/MCMS/new_process.py` — add function `create_sectoral_spillover_matrix(...)` that:
   - Reads per-sector IRFs from `output_matlab/irf_Het_DCP_Baseline.mat` (`pi_k_i_varepsilon_tau_1_4_j` and `va_k_i_varepsilon_tau_1_4_j` where k ∈ {1=US, 2=CN}, i ∈ 1..44 responding sector, j ∈ 1..20 shocked tradeable sector). Extract period-1 (on-impact) values for VA, 4Q cumulative sum for inflation (to match existing `Sec_Inf_*` convention).
   - Computes Antras–Chor upstreamness from the IO matrix stored in `calib.mat` (the global-sector intermediate-input allocation matrix). Upstreamness $U = (I - \tilde B)^{-1}\mathbf{1}$ where $\tilde B_{ij}$ is the share of sector $i$'s output absorbed by sector $j$ as intermediate input (domestic IO, per country).
   - Sorts the 20 tradeable shocked sectors (rows) and 44 responding sectors (columns) by upstreamness descending (two separate orderings — rows over tradeable-only, columns over all 44).
   - Renders a 2×2 figure: top row = US (VA heatmap | inflation heatmap), bottom row = China. Diverging colormap (`RdBu_r`) centered at zero. Sector labels on both axes.
   - Saves as `figures/Fig_SectoralSpillover_Matrix.png` inside Tariffs_ECB.
   - Register filename in the module-level list (`new_process.py:97`) and in the `active_figures` / output pipeline mirror to Tariffs_ECB.
6. Optional — a small CSV companion `output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv` with long-form columns (country, shocked_sector, responding_sector, upstream_row, upstream_col, va_response, inflation_response) for reproducibility.

---

## Data / computational checks before I start

- IRFs exist: verified `pi_k_i_varepsilon_tau_1_4_j` and per-sector VA keys are present in `irf_Het_DCP_Baseline.mat` (HDF5 v7.3). Each is shape (20 periods, 1).
- IO matrix location: need to confirm in `calib.mat` (structure unknown to me; I'll inspect in implementation).
- **Sign / units sanity check before plotting:** (a) shocked sector should appear on the diagonal with largest magnitude (own-sector effect); (b) VA of the shocked sector in the US should be positive (US benefits from tariff per current 5.1 text); (c) VA of the shocked sector in China should be negative. If any of these fail, something is wrong in the mapping — surface before proceeding.
- Upstreamness validation: hand-check the top-3 most upstream sectors against the Antras–Chor 2012 U.S. ranking (Mining, Petroleum, Utilities typically near the top). If it's clearly off, stop and fix before plotting.

---

## Execution order

1. **[Impl]** Extract 20×44 IRF matrices + compute upstreamness → save CSV, print sanity diagnostics (diagonals, sign pattern, upstreamness top-5).
2. **[Impl]** Add `create_sectoral_spillover_matrix` to `new_process.py`, wire into pipeline list.
3. **[Impl]** Run `new_process.py` (subset invocation if possible) to generate the new figure.
4. **[Impl]** Edit `55a_benchmark_and_robustness.tex`: remove 4.2 block, delete now-orphaned figure references inside that block (`Fig_Sectoral_Bars_GDP`, `Fig_Sectoral_Bars_CPI` — they move, not delete).
5. **[Impl]** Rewrite `56_sectoral_channels.tex` into 5.1–5.4 structure, preserving prose where possible.
6. **[Impl]** `grep -rn "sec:sectoral_results"` → update all callers to new label.
7. **[Verify]** Compile `0_main.tex` (3-pass pdfLaTeX + bibtex). Must build clean.
8. **[Review]** Run `theory-critic` on the rewritten Section 5 (per user directive).
9. **[Fix]** Apply theory-critic findings per orchestrator-protocol (critical → major → minor).
10. **[Re-verify / re-score]** Re-compile; re-run theory-critic on fixed text until score passes gate or loop cap is hit.

Scope-creep guard: **no** figure redesigns beyond the new spillover matrix; prose edits are strictly re-sequencing + bridging text; no new empirical claims introduced without code-verified numbers.

---

## Locked decisions

- Q1. Figure 12 = `Fig_CN_Sectoral_Heatmap`; Figure 13 = `Fig_CN_Structural_Scatter`.
- Q2. The 3×4 structural scatters move to the appendix.
- Q3. Section 4.2 is fully removed from Section 4; no teaser duplication remains there.
- Q4. Upstreamness ordering is country-specific, not pooled.

These are locked by the working note `quality_reports/session_logs/2026-04-13_section5-restructure-working-notes.md` and should be treated as authoritative for implementation.

---

## Scope revision (2026-04-13, later user instruction)

The task expanded after the first Section 5 rewrite. The operative requirements are now:

1. Move Figure 12 (`Fig_CN_Sectoral_Heatmap`) out of the main text and into the appendix because it is redundant with Figure 13.
2. Redesign the spillover matrix output:
   - restore the diagonal,
   - split the current combined US/China matrix into two separate figures,
   - for each country, stack GDP and inflation panels vertically,
   - use sector names on the x-axis rather than sector codes.
3. Strengthen Section 5.3 so that it states the relative importance of own-sector versus cross-sector spillovers precisely and numerically.
4. Remove mentions in the main text of the appendix R-squared / horse-race analysis, while **keeping the appendix regression material itself in place**.
5. Consolidate Figure 2 benchmark IRFs so the benchmark macro-dynamics figure fits on a single page.

This revision supersedes the earlier assumption that the appendix horse-race material would be removed or repurposed.

## Scope revision (2026-04-13, latest follow-up)

The user then added a final polish pass focused on the active Section 5.2/5.3 objects:

1. Improve the Section 5.3 matrix figures so they fit cleanly on the page; in particular, reduce the oversized lower margin that is currently pushing the caption off the page.
2. Change the spillover colormap to a blue--yellow scheme, with blue for negative responses and yellow for positive responses.
3. Mark the diagonal own-sector cells with a black square outline so they remain visually distinct after restoring the diagonal.
4. Rewrite Section 5.3 so it explains where the negative spillovers come from, and back that mechanism with numbers from the generated spillover CSV.
5. Rewrite Section 5.2 into publication-ready prose in the author's `writing-style-eugenelo.md` style.

This polish pass does not change the underlying decomposition or the appendix-placement decision. It is a figure-design and prose-quality pass on the already-verified Section 5 structure.

## Scope revision (2026-04-13, current rewrite pass)

The user then asked for a more substantive reframing rather than another local polish pass. The operative target is now:

1. Rebuild Section 5 around the claim that aggregate tariff effects are net objects that hide larger gross reallocations, but only where that claim is numerically defensible.
2. Substantiate every empirical claim with code-backed numbers rather than qualitative wording.
3. Reconsider whether the Section 5.3 matrices should remain in weighted aggregate-GDP-contribution space (exact decomposition) or move to sectoral value-added space (clearer gross-incidence object); either choice is allowed, but the final text must explain the choice explicitly.
4. Restructure Section 5 to fit the new argument rather than preserve the existing 5.1--5.4 split mechanically.
5. Rewrite the euro-area discussion in both Section 4 and Section 5 so it separately identifies:
   - the increase in EA exports to the US,
   - the increase in EA imports from China,
   - the increase in EA consumption of Chinese goods if it is numerically material,
   - and the DCP / ROW channel operating through the dollar and third-country trade prices.

This scope revision supersedes the narrower "polish only" objective. The next implementation pass should therefore start from diagnostics and only then rewrite the prose.
