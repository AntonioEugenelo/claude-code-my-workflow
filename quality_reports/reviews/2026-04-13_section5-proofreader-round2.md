# Proofreader Review: Section 5, Round 2

**Target:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
**Reviewer:** `proofreader`
**Round:** 2
**Score:** `92/100`

## Findings

1. `56_sectoral_channels.tex:77` mixes signed numbers with directional verbs, e.g. `fall -0.0187%` and `fall -0.0613%`. Use either signed values or prose direction, not both.
2. `56_sectoral_channels.tex:9` switches from `own-sector value added` to `the directly shocked sector's own output response`. Keep the object label consistent.
3. `56_sectoral_channels.tex:31,49,75` retains a few slightly informal phrases such as `The figure is useful because`, `The US case is the sharpest`, and `The euro area is the clean third-country example`.

## Residual Risks

- The numerical argument is internally coherent, but several claims still depend on figures and appendix objects outside this file.
- This pass checked prose and internal consistency, not the underlying data or rendered figures.
