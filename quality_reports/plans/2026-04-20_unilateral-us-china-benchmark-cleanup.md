## Plan: Unilateral US-on-China Benchmark Cleanup

**Date:** 2026-04-20
**Status:** ACTIVE

### Objective

Align the compiled Tariffs_ECB manuscript with the MCMS benchmark experiment by removing reciprocal-tariff framing and presenting the benchmark consistently as a unilateral US tariff on Chinese imports.

### Scope

Primary manuscript files:

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/13_roadmap.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`

Supporting figure/code paths:

- `master_supporting_docs/MCMS/a2_preprocessing.m`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_Benchmark_Combined.png`

### Planned Changes

1. Verify from MCMS code that the benchmark shock path is `USA -> CHN` and that the reverse `CHN -> USA` path is only a separate auxiliary comparison.
2. Replace reciprocal/bilateral benchmark language in the compiled manuscript with unilateral US-on-China wording, keeping the new edits marked in red where appropriate.
3. Remove reverse-direction benchmark discussion from Section 4 so the narrative matches the actual benchmark experiment.
4. Update the benchmark figure generation so the paper figure shows only the unilateral US-on-China shock.
5. Adjust the horse-race appendix text so it no longer claims a two-shock stacked design if the compiled appendix is benchmark-only.
6. Recompile the paper and confirm that the redline PDF reflects the unilateral framing.

### Verification

- Inspect the cited MCMS source lines for benchmark and reverse shock definitions.
- Regenerate `Fig_Benchmark_Combined.png` without the reverse-direction series.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` successfully.
- Re-scan the compiled manuscript sources for reciprocal benchmark phrasing.

### Assumptions

- “Eliminate all reference to a reciprocal tariff” means removing reciprocal framing from the compiled benchmark paper, not rewriting excluded legacy draft sections that are not included in `0_main.tex`.
- The benchmark figure should display only the unilateral US tariff on Chinese imports because that is the benchmark shock used throughout the paper.
