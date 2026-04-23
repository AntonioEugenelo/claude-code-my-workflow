## Action-Point Response Memo

Date: 2026-04-18
Update: 2026-04-20 after syncing `master_supporting_docs/Tariffs_ECB` through Overleaf commits `64f1707` (Alistair Dieppe) and `adcd671`.
Update: 2026-04-20 after the live Section 4 reciprocal-benchmark restore and the current-tree status refresh below.

Scope: This memo explains how I would address the current Tariffs ECB action points without editing the manuscript itself. Every substantive claim below is tied either to a source-file reference, to an editorial restriction stated in this memo, or to a numerical computation from the generated CSV outputs.

### Executive Summary

Three items now require explicit decisions before the cleanup can be closed:

1. The MCMS code and saved run config resolve the provenance of the current export: it is `\delta=\mu=1`, not `\delta=1, \mu=2`. The manuscript text and caption in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:142,153` are therefore stale unless either the manuscript is updated to `\delta=\mu=1` or the figure is regenerated under `armington=1`.
2. The point-9 status in the original memo is now stale. The live manuscript is no longer the same tree as the inspected `2026-04-17` Overleaf snapshot. Alistair's `64f1707` touched only `0_clean/sections/02_title_page.tex` and `0_clean/sections/11_introduction.tex`, so the theory-cleanup bundle was not addressed there; the current tree still contains visible slips in `22_households.tex:47`, `23_firms.tex:34,47,74,84`, and `a_appendix.tex:18,675,822`.
3. Point 10 is now partly addressed, not fully open. Alistair has already revised the active abstract and introduction framing in `02_title_page.tex:95` and `11_introduction.tex:3,13,15,17`, but the title page still contains two incompatible author lists in source form, the abstract now duplicates `net object: a net object:` at `02_title_page.tex:95`, and the calibration file still carries the commented-out heatmap block at `43_calibration.tex:71-105`.

Three items are ready to draft immediately:

1. Section 4.1.2 can be rewritten now by moving the euro-area trade-balance and REER material out of Section 4.1.1.
2. The household-dynamics discussion in Section 4 can be strengthened now, but only with aggregate reciprocal-benchmark evidence. The current household-vs-intermediate decomposition should not be used in manuscript prose in its present state.
3. The IO-robustness placeholders can be filled now with exact averaged values.

### Current Status Snapshot (2026-04-20, Live Tree)

This snapshot supersedes the older open/closed labels below when they disagree with the current manuscript state.

1. Improve Figure 1 visually. `Status now: complete in the live tree.` The combined benchmark figure now uses the darker retaliation line, without the old internal title/legend stack, and the caption is aligned with the plotted color.
2. Move euro-area trade-balance and REER dynamics out of Section 4.1.1 and into Section 4.1.2. `Status now: complete in the live tree.` Section 4.1.2 now carries the EA trade-balance, REER, and consumption-response discussion, adapted to the two-sided benchmark.
3. Improve the household-dynamics discussion in Section 4, without using the current household-vs-intermediate output decomposition. `Status now: complete in the live tree.` The current Section 4 discussion uses aggregate benchmark evidence rather than the excluded decomposition.
4. Improve the euro-area dynamics discussion in Section 5. `Status now: complete in the live tree.` The EA subsection in Section 5 is materially expanded relative to the earlier compressed version.
5. Fill the three IO-robustness placeholders. `Status now: complete in the live tree.`
6. Reconcile the elasticity robustness definition, then fill the four trade-elasticity placeholders. `Status now: complete in the live tree.` The current text is aligned with the code-backed `\delta=\mu=1` export.
7. Blue-markup cleanup in `55a_benchmark_and_robustness.tex`. `Status now: complete in the live tree.` No blue markup remains in the active Section 4 source.
8. Harmonize the invoicing-regime counts everywhere in the manuscript. `Status now: complete in the active manuscript tree.` The legacy source carrying the old `7/19/18` counts is no longer in the live include graph, and no remaining hits were found in the current `0_clean/sections/*.tex` tree.
9. Fix the concrete theory-notation slips that remain in Jose Elias's rewrite bundle. `Status now: still open.` The live tree still contains the line-level issues in `22_households.tex`, `23_firms.tex`, and `a_appendix.tex`.
10. Review the title page, abstract framing, commented calibration heatmaps, and appendix table status. `Status now: partly open.` The duplicated abstract wording has been cleaned, but the title page still carries the legacy `\iffalse` author block, the commented calibration heatmap block remains, and the broader benchmark framing is now inconsistent across the paper: Section 4 is two-sided while the title page, introduction, roadmap, and conclusions still describe the benchmark as unilateral.

### Evidence Standard

1. File references use repo-relative `path:line` notation on first mention in each section; later repeated references may use the basename when the file is already unambiguous in that section.
2. Robustness averages use the logic in `master_supporting_docs/MCMS/new_process.py:4635-4681`, specifically:
   - IO un-cumulation: `4635-4641`
   - trade-balance averages: `4661-4666`
   - CPI averages: `4670-4674`
   - GDP averages: `4678-4681`
3. For the IO robustness figure, the cumulative CSV must be un-cumulated before averaging because the code explicitly applies `diff()` when `cumulative=True` at `new_process.py:4635-4641`.
4. When manuscript prose, plot labels, and saved outputs disagree, the model code and the saved `config_used` block inside the generated `.mat` file are the source of truth.

### Action Point Register

I keep the original numbering so earlier references remain stable. Point 7 is deferred in this memo.

1. Improve Figure 1 visually. `Status: open.`
2. Move euro-area trade-balance and REER dynamics out of Section 4.1.1 and into Section 4.1.2. `Status: open.`
3. Improve the household-dynamics discussion in Section 4, without using the current household-vs-intermediate output decomposition. `Status: open.`
4. Improve the euro-area dynamics discussion in Section 5. `Status: open.`
5. Fill the three IO-robustness placeholders. `Status: open.`
6. Reconcile the elasticity robustness definition, then fill the four trade-elasticity placeholders. `Status: open.`
7. Blue-markup cleanup in `55a_benchmark_and_robustness.tex` (deferred in this memo). `Status: deferred/open.`
8. Harmonize the invoicing-regime counts everywhere in the manuscript. `Status: open.`
9. Fix the concrete theory-notation slips that remain in Jose Elias's rewrite bundle. `Status: open; refresh against the synced live tree, not the old 2026-04-17 snapshot.`
10. Review the title page, abstract framing, commented calibration heatmaps, and appendix table status. `Status: partly addressed by Alistair's 2026-04-19 Overleaf commit.`

### Status Update After Alistair's 2026-04-19 Overleaf Commit

- Commit `64f1707` changes only `0_clean/sections/02_title_page.tex` and `0_clean/sections/11_introduction.tex`.
- No action-point progress is visible in the robustness placeholders, the blue DCP markup, the invoicing-count mismatch, or the theory-cleanup bundle; those remain open in the live tree.
- The later synced commit `adcd671` does not close those open items either: the IO and elasticity placeholders are still visible in `55a_benchmark_and_robustness.tex:131-152`, and the legacy invoicing counts remain in `55_model_dynamics_and_scenarios.tex:57`.

## 1. Figure 1 Visual Revision

Current evidence:

- The combined benchmark figure is produced by `master_supporting_docs/MCMS/new_process.py:1888-2097`.
- The figure currently carries an internal suptitle at `new_process.py:2081-2084`, a top legend at `new_process.py:2086-2089`, and a separate internal note at `new_process.py:2091-2094`.
- The manuscript caption already explains the line styles in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:28`.
- The reverse-shock series currently uses `ECB_ORANGE = '#FFD700'` at `master_supporting_docs/MCMS/new_process.py:1312`, and the dashed reverse-shock line is drawn with that color at `new_process.py:2028-2029`.
- Current font sizes are small for a 3x5 grid: column titles `12` at `new_process.py:2068`, row labels `11` at `new_process.py:2070`, tick labels `8` at `new_process.py:2077`, suptitle `15` at `new_process.py:2081-2083`, and legend/note text `10` at `new_process.py:2088-2094`.
- The layout reserves top space via `plt.tight_layout(rect=[0, 0, 1, 0.94])` at `new_process.py:2096`, so the figure is explicitly sacrificing vertical space to the title/legend/note stack.

Recommended change:

- Remove the internal suptitle in `new_process.py:2081-2084`.
- Remove `fig.legend(...)` in `new_process.py:2086-2089` and keep the line-style explanation only in the caption/note.
- Replace `#FFD700` with a dark red such as `#8B0000` or `#B22222`, then update the caption text from `dashed gold` to `dashed dark red`.
- Increase the figure typography by about 2 points in each layer: titles `12 -> 14`, row labels `11 -> 13`, ticks `8 -> 10`, note text `10 -> 11 or 12`.
- Reclaim some of the top margin after removing the title/legend stack.

Why this is the right fix:

- The user request is fully code-addressable: title, legend, color, and font size each map directly to identified lines.
- The figure currently duplicates information across internal title/legend and external LaTeX caption.

## 2. Rebalance Section 4.1.1 and Section 4.1.2

Current evidence:

- Section 4.1.1 contains 5 `\paragraph{}` blocks at `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:15,19,33,38,42`.
- Section 4.1.2 contains only 2 `\paragraph{}` blocks at `55a_benchmark_and_robustness.tex:50,53`.
- The euro-area trade-balance mechanics are currently embedded in Section 4.1.1 at `55a_benchmark_and_robustness.tex:33`:
  - EA aggregate trade balance `+0.017%` on impact
  - EA-US net margin `+0.0785%`
  - EA-China margin `-0.0604%`
  - ROW margin `-0.0010%`
  - reverse-shock margins `-0.0268%`, `+0.0368%`, and `+0.0029%`
- The euro-area REER discussion is also in Section 4.1.1 at `55a_benchmark_and_robustness.tex:38`, including the on-impact EA REER depreciation of `+0.08%`.

Recommended change:

- Move the EA-specific trade-balance material from `55a_benchmark_and_robustness.tex:33` into Section 4.1.2.
- Move the EA-specific REER sentences from `55a_benchmark_and_robustness.tex:38` into Section 4.1.2.
- Rewrite Section 4.1.2 as 3 compact prose paragraphs without `\paragraph{}` headings:
  - paragraph 1: CPI headline
  - paragraph 2: GDP plus a short bilateral trade-balance summary
  - paragraph 3: REER interpretation and reverse-shock sign reversal
- Keep Section 4.1.1 focused on direct US-China incidence only.

Why this is the right fix:

- The current subsection balance is visibly lopsided.
- The EA evidence is already in the manuscript; it is just located in the wrong subsection.

## 3. Strengthen the Household-Dynamics Discussion in Section 4

Current evidence:

- The current household discussion is concentrated in a single consumption paragraph at `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:42-46`.
- That paragraph gives the main aggregate facts:
  - US consumption falls `-0.26%` on impact while GDP falls only `-0.04%` and the trade balance improves `+1.55%` at `55a_benchmark_and_robustness.tex:42-44`
  - China consumption falls `-0.06%` on impact while GDP contracts `-0.24%` at `55a_benchmark_and_robustness.tex:19,42-46`
  - EA consumption is slightly negative `-0.003%` on impact while GDP is near zero `+0.001%` at `55a_benchmark_and_robustness.tex:53`
- This memo excludes the current household-vs-intermediate output decomposition from manuscript use because it is not precise enough for the intended claim and because it does not match the reciprocal benchmark discussed in Section 4.
- There is also a scope mismatch: the transmission overview is explicitly labeled as a single-leg US-tariff shock, `Shock: aggregate 10 pp US tariff on Chinese imports`, at `master_supporting_docs/MCMS/new_process.py:2943`, whereas Section 4 is the reciprocal benchmark section.

Recommended change:

- Do not use the current household-vs-intermediate output decomposition in Section 4.
- Strengthen the household discussion using only aggregate reciprocal-benchmark evidence that already belongs to Section 4:
  - US: large consumption loss, small GDP loss, large trade-balance gain
  - China: modest immediate household contraction, much larger GDP contraction
  - EA: no household boom on impact
- Add one short aggregate paragraph immediately after the current real-consumption paragraph.

Why this is the right fix:

- It keeps the evidence on the same reciprocal experiment already discussed in Section 4.
- It avoids relying on a decomposition object that this memo is intentionally excluding.

## 4. Strengthen the Euro-Area Dynamics Discussion in Section 5

Current evidence:

- The dedicated EA subsection in Section 5 runs only from `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:87-101`.
- The section already contains the key numerical ingredients:
  - largest EA aggregate GDP contributions: Electronics `-0.0013%`, Pharmaceuticals `+0.0012%`, Other Manufacturing `+0.0006%` at `56_sectoral_channels.tex:92`
  - own-sector gains: Electronics `+0.139%`, Textiles `+0.109%`, Other Manufacturing `+0.10%` at `56_sectoral_channels.tex:92`
  - `12 of the 20` tariffed sectors have positive own-sector value added but negative aggregate GDP contribution at `56_sectoral_channels.tex:92`
  - bilateral margin accounting: EA-US `+0.0785%`, EA-China `-0.0604%`, ROW `-0.0010%`, total trade balance `+0.0171%`, GDP `+0.0011%`, consumption `-0.0031%` at `56_sectoral_channels.tex:101`

Recommended change:

- Expand the subsection from 3 short paragraphs to 4 focused paragraphs:
  - paragraph 1: headline net-object result
  - paragraph 2: own-sector versus aggregate contributions
  - paragraph 3: bilateral trade-margin accounting
  - paragraph 4: link the tiny GDP gain to the negative consumption response
- Preserve the current sectoral numbers; the gap is explanatory room, not missing evidence.

Why this is the right fix:

- The Section 5 evidence is already numerically strong.
- The current presentation is compressed relative to the importance of the EA narrative.

## 5. Fill the Three IO-Robustness Placeholders

Current evidence:

- The IO paragraph still contains 3 explicit placeholders at `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:127,129,131`.
- The active averaging logic first un-cumulates the CSV with `diff()` when `cumulative=True` at `master_supporting_docs/MCMS/new_process.py:4635-4641`.
- Using that exact logic on `master_supporting_docs/MCMS/output_python/extra_charts/Figure_2_Cumul_IO_Decomposition_TimeSeries.csv`, the three-year average GDP responses are:

| Region | Benchmark | Zero Intl IO | Zero All IO |
| --- | ---: | ---: | ---: |
| USA | `+0.0191%` | `+0.0320%` | `+0.0205%` |
| CHN | `-0.1469%` | `-0.0975%` | `-0.0883%` |
| EA | `+0.0085%` | `+0.0037%` | `+0.0032%` |

- Relative to benchmark, removing international IO reduces the absolute Chinese contraction by `33.7%`, and removing all IO reduces it by `39.9%`.

Recommended change:

- Replace the US placeholder with a sentence noting that average US GDP rises from `+0.0191%` to `+0.0320%` when international IO is removed, then returns near benchmark at `+0.0205%` when all IO is removed. That pattern should be presented as suggestive, not identified.
- Replace the China placeholder with the computed sequence `-0.1469% -> -0.0975% -> -0.0883%`.
- Replace the EA placeholder with the computed sequence `+0.0085% -> +0.0037% -> +0.0032%`.

Why this is the right fix:

- The placeholders can now be filled with exact numbers.
- The memo now keeps the interpretation no broader than the evidence warrants.

## 6. Fix the Elasticity Robustness Definition Using the Model Code as Source of Truth

Current evidence:

- The trade-elasticity paragraph still contains 4 placeholders at `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:140,144,146,148`.
- The manuscript text and caption define the active counterfactual as low household elasticity only: `\delta=1, \mu=2 unchanged` at `55a_benchmark_and_robustness.tex:142-143`, and `low household elasticity (\delta=1, \mu=2)` at `55a_benchmark_and_robustness.tex:153`.
- The MCMS export path uses the file `master_supporting_docs/MCMS/output_python/extra_charts/Figure_4_UnitElast_vs_HighElast_TimeSeries.csv`, and the plotting pipeline labels the comparison as `Unit baseline (\delta=\mu=1)` versus the benchmark at `master_supporting_docs/MCMS/new_process.py:5267-5271`.
- The model code resolves the disagreement:
  - `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline_UnitElast.mat` stores `config_used.armington = 2`.
  - `master_supporting_docs/MCMS/a1_calibration.m:37-42` maps `armington = 2` to `Delta_C = 1`.
  - `master_supporting_docs/MCMS/a1_calibration.m:196-201` maps `armington = 2` to `Delta_X = 1`.
  - Therefore the current Figure 4 export is a true `\delta=\mu=1` run.
- The current CSV-backed averages are therefore real, and the model code confirms that they belong to the `\delta=\mu=1` experiment:

| Region | Current MCMS Export: `\delta=\mu=1` | Benchmark: `\delta=\mu=2` |
| --- | ---: | ---: |
| USA | `-0.0079%` | `+0.0191%` |
| CHN | `-0.1054%` | `-0.1469%` |
| EA | `+0.0012%` | `+0.0085%` |

- Under that current export, the China gap is `0.0415` percentage points, or `28.3%` smaller in absolute value than the benchmark contraction.

Recommended change:

- Treat the current model code as the source of truth: the existing Figure 4 export corresponds to `\delta=\mu=1`.
- If the authors want to keep the existing Figure 4 export, update the manuscript text and caption in `55a_benchmark_and_robustness.tex:140-153` to say `\delta=\mu=1` rather than `\delta=1, \mu=2`.
- If the intended economic experiment is instead low household elasticity only (`\delta=1, \mu=2`), rerun MCMS with `armington=1` and regenerate the Figure 4 export before inserting any exact numbers.
- Use the current `\delta=\mu=1` numbers only for a manuscript that explicitly describes that same specification.

Why this is the right fix:

- The model code now resolves the provenance question for the current export.
- The remaining issue is editorial alignment: either update the manuscript to match the code-backed current experiment, or rerun the model for the intended alternative.

## 8. Harmonize the Invoicing-Regime Counts

Current evidence:

- The stale sentence in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55_model_dynamics_and_scenarios.tex:57` says the baseline has `7` PCP, `19` LCP, and `18` DCP sectors.
- The active calibration code defines `Inum = 44` at `master_supporting_docs/MCMS/a1_calibration.m:5`.
- PCP sectors are assigned at `a1_calibration.m:742`, LCP sectors at `a1_calibration.m:759`, and DCP is the complement at `a1_calibration.m:780`.
- The code therefore implies:
  - PCP = `7`
  - LCP = `20`
  - DCP = `17`
- The same counts are corroborated in `master_supporting_docs/MCMS/BUG_REPORT_DCP_domestic_pricing.txt:116-118`.
- The newer Section 4 text is already aligned with the code at `55a_benchmark_and_robustness.tex:74,98`.

Recommended change:

- Update `55_model_dynamics_and_scenarios.tex:57` from `7/19/18` to `7/20/17`.
- Run a manuscript-wide search for any other legacy references to `18 DCP` or `19 LCP`.

Why this is the right fix:

- The model code is authoritative.
- The manuscript is currently internally inconsistent on a basic calibration fact.

## 9. Fix the Concrete Theory-Notation Slips That Remain in Jose Elias's Rewrite Bundle

Current evidence:

- The broader rewrite bundle flagged for review is listed in `quality_reports/session_logs/2026-04-18_overleaf-jose-elias-action-points.md`.
- The point-9 status in the original memo compared the live tree against `quality_reports/tmp/overleaf_inspect_20260418/`, but that current-tree comparison is now stale because `master_supporting_docs/Tariffs_ECB` is synced through `64f1707` and `adcd671`.
- Alistair's `64f1707` touched only `0_clean/sections/02_title_page.tex` and `0_clean/sections/11_introduction.tex`, so it did not address the theory bundle.
- Visible current slips in the synced live tree include:

| File | Current Tree | Issue |
| --- | --- | --- |
| `22_households.tex` | `master_supporting_docs/Tariffs_ECB/0_clean/sections/22_households.tex:47` | malformed empty bracket `\left[]` and mismatched object description |
| `23_firms.tex` | `master_supporting_docs/Tariffs_ECB/0_clean/sections/23_firms.tex:34,47,74,84` | wrong summation upper bound `\sum_{l=1}^I`, tautological price ratio `(P^k_{l,j,t}/P^k_{l,j,t})`, and duplicated equation label `eq:general_model_price_setting_foreign` |
| `a_appendix.tex` | `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix.tex:18,675,822` | duplicated wording, sector-indexed wage-shock term `u_{ki,t}^w`, and `que the expressions` |

Recommended change:

- Treat this as a live-tree cleanup list, not as a stale current-vs-snapshot comparison.
- Do not mark point 9 as addressed by Alistair. His `64f1707` commit bypassed the theory files entirely.
- Fix the visible line-level slips first, then run a full manuscript build and a focused equation-reference pass.

Why this is the right fix:

- The synced manuscript has moved since 2026-04-18, but the visible errors still justify a targeted theory cleanup rather than a new theory rewrite.
- The correct next step is targeted cleanup plus build verification.

## 10. Review the Title Page, Abstract Framing, Commented Calibration Heatmaps, and Appendix Table Status

Current evidence:

- Since the original memo, Alistair's `64f1707` has already revised the active abstract in `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex:95` and the introduction framing in `11_introduction.tex:3,13,15,17`.
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex:1` still contains a commented legacy title-page block.
- The commented legacy block contains 8 authors, including `Rosi D. Chankova` at `02_title_page.tex:11`.
- The active title page begins at `02_title_page.tex:54` and lists 7 authors at `02_title_page.tex:61,65,69,74,78,82,86`.
- The active abstract states:
  - shutting down all IO reduces the Chinese GDP decline by `about 40%` at `02_title_page.tex:95`
  - China's three-year average contraction is `over 30% larger` under heterogeneous DCP than under PCP at `02_title_page.tex:95`
  - the EA on-impact GDP response ranges from `-0.017%` under full DCP to `+0.017%` under PCP at `02_title_page.tex:95`
- The first abstract claim is numerically consistent with the verified IO attenuation `39.9%`.
- The second abstract claim is also consistent with current exports: in `master_supporting_docs/MCMS/output_python/extra_charts/Figure_17_DCP_PCP_FullDCP_TimeSeries.csv`, the absolute Chinese average GDP contraction is `0.1469 / 0.1123 - 1 = 30.8%` larger under heterogeneous invoicing than under PCP.
- The third abstract claim is consistent with the Section 4 text at `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:109`, which reports EA on-impact GDP of `-0.017%` under DCP, `+0.001%` under heterogeneous invoicing, and `+0.017%` under PCP.
- The same abstract line now also contains duplicated wording `net object: a net object:` at `02_title_page.tex:95`.
- The appendix table is already tied into the calibration section:
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/43_calibration.tex:4` already cites `Table \ref{tab:nace_sectors}`
  - the table itself appears in `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex:129-195` with `44` counted rows
- The calibration file still contains a large commented-out heatmap block at `43_calibration.tex:71-105`.

Recommended change:

- Mark point 10 as partly completed, not fully open. The active title/abstract framing has already been revised by Alistair.
- Confirm whether the active 7-author title page is intentional. If yes, remove the commented 8-author legacy block.
- Keep the abstract's three headline quantitative claims; on current evidence, all three are numerically consistent, but delete the duplicated phrase `net object: a net object:` from `02_title_page.tex:95`.
- Keep the NACE appendix table and note that the main calibration section already cross-references it.
- Make an explicit editorial decision on the commented heatmap block in `43_calibration.tex:71-105`: either restore it as live material or delete it from source if it is permanently retired.

Why this is the right fix:

- The framing work has already started, so the remaining task is cleanup and finalization rather than first-pass review.
- The appendix table is not orphaned; the real open issue there is source hygiene and intentionality, not missing linkage.

## Draft Wording for the Ready Text Changes

### Point 2: Section 4.1.2 Rewrite

Proposed paragraph 1:

Following the US tariff on China, the euro-area inflation response is negligible, with CPI rising by only $+0.007$~pp on impact and turning mildly negative from the fifth quarter onward. The euro area is not directly targeted by the tariff, so its price dynamics reflect second-round spillovers rather than a direct border-price shock.

Proposed paragraph 2:

The same logic governs euro-area activity. On impact, EA GDP is essentially flat at $+0.001$\%, before rising to about $+0.012$\% by the fifth quarter. This near-zero aggregate is a net object, not a small-effect object. The key trade accounting is simple: under the US tariff on China, the EA--US net margin improves by $+0.0785$\%, the EA--China margin falls by $-0.0604$\%, and a near-zero negative ROW term leaves the total EA trade-balance response at only $+0.017$\% on impact. EA consumption is slightly negative at $-0.003$\%, which confirms that the short-run response is not a demand boom but a small trade-diversion gain offset by weaker household absorption.

Proposed paragraph 3:

The exchange rate moves consistently with that accounting. Under the US tariff on China, the euro-area REER depreciates only modestly, by about $+0.08$\% on impact, as the euro weakens slightly against the appreciating dollar, and then returns close to zero over the horizon. Under the Chinese tariff on US imports, the bilateral margins reverse sign, but the total EA trade-balance response remains only marginally positive at $+0.0128$\%. The euro-area result is therefore best read as a finely balanced third-country net effect rather than as an independent demand expansion.

### Point 3: Aggregate Household-Dynamics Paragraph

Proposed paragraph:

Household dynamics differ sharply across the three blocs. In the United States, the tariff hits households much more strongly than it hits output: real consumption falls by about $0.26$\% on impact, while GDP declines by only $0.04$\%, because the loss in purchasing power is partly offset in GDP accounting by a sharp improvement in the trade balance ($+1.55$\%) and by the rebate of tariff revenue. In China, the pattern is different: real consumption falls only $0.06$\% on impact, but GDP contracts $0.24$\%, which indicates that the main short-run adjustment is not a collapse in household spending. In the euro area, household dynamics are subdued rather than expansionary: consumption is slightly negative on impact ($-0.003$\%) even though GDP is near zero ($+0.001$\%), which confirms that the EA response reflects limited trade diversion rather than a broad-based demand boom.

### Point 5: IO-Robustness Paragraph

Proposed paragraph:

Production networks materially amplify the tariff shock, especially in China. In the benchmark, China's three-year average GDP contraction is $-0.1469$\%. Shutting down international IO linkages attenuates it to $-0.0975$\%, and shutting down all IO linkages attenuates it further to $-0.0883$\%, a total reduction of $39.9$\% relative to the benchmark. The euro area's indirect gain also shrinks, from $+0.0085$\% in the benchmark to $+0.0037$\% with zero international IO and $+0.0032$\% with zero all IO. The US and EA comparisons therefore suggest additional IO transmission, but they do not isolate its exact source cleanly: in the United States, the average GDP response rises from $+0.0191$\% to $+0.0320$\% when international IO linkages are removed, before returning near benchmark at $+0.0205$\% when all IO linkages are shut down.

### Point 6: Elasticity-Robustness Wording

Code-backed answer:

The current Figure 4 export corresponds to `\delta=\mu=1`. The decisive evidence is in the saved model output itself: `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline_UnitElast.mat` stores `config_used.armington = 2`, and `master_supporting_docs/MCMS/a1_calibration.m:37-42,196-201` maps `armington = 2` to `Delta_C = 1` and `Delta_X = 1`. The manuscript text and caption are therefore stale if they describe the current export as `\delta=1, \mu=2`.

Paragraph to use if the manuscript is updated to match the current MCMS export:

Trade elasticities materially shape the size of the tariff shock. Under the benchmark with $\delta=\mu=2$, the US three-year average GDP response is $+0.0191$\%, whereas under unit elasticity it falls to $-0.0079$\%, so the average US gain disappears once expenditure switching is muted. China also becomes less exposed: its average contraction moderates from $-0.1469$\% to $-0.1054$\%, a reduction of $0.0415$ percentage points, or $28.3$\% in absolute value. The euro area is affected in the same direction, with its average GDP gain shrinking from $+0.0085$\% to $+0.0012$\%. Lower trade elasticities therefore attenuate the cross-border reallocation induced by the tariff shock.

If the intended experiment is instead low household elasticity only (`\delta=1, \mu=2`), rerun MCMS with `armington = 1`, regenerate `Figure_4_UnitElast_vs_HighElast_TimeSeries.csv`, and replace the paragraph above with the rerun numbers.

## Recommended Implementation Order

1. Resolve point 6 first by auditing the generating elasticity specification and aligning text, caption, and export.
2. Close the remaining point-10 cleanup items: confirm the title-page author list, remove the duplicated abstract wording, and decide the status of the commented calibration heatmaps.
3. Implement the Figure 1 cleanup in point 1.
4. Implement the ready text rewrites for points 2, 3, and 5.
5. Expand Section 5 using point 4's structure.
6. Harmonize the invoicing counts in point 8.
7. Fix the targeted theory slips in point 9 and run a full manuscript build.

## Verification Notes

- All numerical robustness values in this memo were computed from the generated CSV outputs in `master_supporting_docs/MCMS/output_python/extra_charts/` using the averaging rules cited above.
- The point-9 status check in this updated memo was verified against the synced live manuscript tree and the scope of Alistair's `64f1707` commit, rather than against the stale 2026-04-17 snapshot alone.
