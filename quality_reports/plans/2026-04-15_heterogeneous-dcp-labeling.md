# Plan: Heterogeneous DCP Labeling

Date: 2026-04-15

## Goal

Ensure that benchmark references to `DCP` in the active manuscript are explicitly labeled as `heterogeneous DCP`, while leaving generic conceptual uses of DCP unchanged.

## Scope

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_sectoral_targeting.tex`

## Steps

1. Identify benchmark-specific `DCP` references that should become `heterogeneous DCP`.
2. Patch only benchmark-context references; keep generic mechanism definitions unchanged.
3. Recompile `0_clean/0_main.pdf`.
4. Run a targeted text check to confirm that benchmark references are qualified consistently.
