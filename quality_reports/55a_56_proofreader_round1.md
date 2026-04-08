# Proofreader Review Report: Tariffs_ECB Sections 4 and 5

- **Scope:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`, `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- **Round:** 1
- **Reviewer focus:** proofreader pass only; no source edits made.

## Summary

The two sections are structurally sound and compile cleanly after the earlier syntax fix, but they are not yet final-copy clean. The main problem is pervasive unreconciled revision markup (`\textcolor{red}{...}`) that still appears throughout both files. There are also a couple of clarity issues that are worth tightening before the sections are treated as polished paper prose.

## Findings

### Issue 1: Residual revision markup remains throughout both sections
- **File:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`; `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- **Location:** Multiple lines throughout both files, e.g. `55a...`: 15, 17, 19, 23, 78, 82, 84, 86, 88, 90, 94, 96, 102, 111, 122, 128, 148, 152, 154, 156, 158, 160, 162, 167, 174, 184, 186, 191, 200, 204, 213, 215, 217, 219, 221, 226, 233; `56...`: 3, 9, 11, 13, 15, 19, 24, 45, 49, 54, 58, 63, 70, 80, 82, 84, 86, 91, 97
- **Current:** Examples include `\textcolor{red}{Chinese inflation rises by only $+0.015$~pp on impact...}` and `\textcolor{red}{A striking finding emerges for the euro area...}`; dozens of similar red wrappers remain in both files.
- **Proposed:** Remove all final revision wrappers and leave only the reconciled prose/captions. If any tracked-change color is still needed for internal drafting, it should not appear in the final paper sections.
- **Category:** Typo
- **Severity:** High

### Issue 2: Monetary-policy paragraph is overloaded and hard to parse
- **File:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- **Location:** Line 215, `\paragraph{Monetary policy (Figure~\ref{fig:robust_monpol})}`
- **Current:** The paragraph beginning `We compare the benchmark with a counterfactual in which the smoothing parameter is set to $\rho_{k,r} = 0.999$...` runs through setup, mechanism, comparative interpretation, and quantitative results in one dense block.
- **Proposed:** Split the paragraph into shorter units: one sentence for the counterfactual setup, one for the mechanism/channel distinction, and one for the quantitative comparison. That will make the section easier to scan without changing the content.
- **Category:** Academic Quality
- **Severity:** Medium

### Issue 3: Tariff magnitude notation is not fully standardized
- **File:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`; `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- **Location:** Section 4 prose and captions, especially lines 3, 11, 52, 75, 107, 116; Section 5 prose and captions, especially lines 13, 24, 45, 54, 63, 70, 91
- **Current:** The same shock is described as `10\% tariff increase`, `10~pp reciprocal US--China tariff shock`, and `10~pp bilateral tariff across all 20 tradeable sectors`.
- **Proposed:** Standardize on one expression throughout the two sections, ideally something like `10 percentage-point tariff increase` or a single definition introduced once and reused consistently in prose and captions.
- **Category:** Consistency
- **Severity:** Low

## Score Deduction Suggestion

Using the Research Papers rubric in `.claude/rules/quality-gates.md`, I would suggest a conservative deduction of **-18 points** overall for this round:

- Residual revision markup: **-12** minimum as a bundled typo/production issue; a strict per-occurrence count would be larger because the markup is widespread.
- Overloaded monetary-policy paragraph: **-2** as an academic-quality/clarity issue.
- Tariff notation inconsistency: **-3** for inconsistent notation.

That puts the sections below a clean final-copy standard until the red markup is removed and the prose is tightened.
