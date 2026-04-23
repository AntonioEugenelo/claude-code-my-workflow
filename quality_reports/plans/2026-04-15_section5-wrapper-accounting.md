# Plan: Section 5 Wrapper and Accounting Clarification

**Status:** COMPLETED
**Date:** 2026-04-15

## Objective

Create a Section 5-only LaTeX wrapper that can be compiled independently for editing, revise the Section 5 opening paragraph to remove the current framing the user dislikes, and document precisely how the household-versus-intermediate benchmark transmission split is constructed in the code.

## Scope

- New wrapper target: `master_supporting_docs/Tariffs_ECB/0_clean/0_section_5_only.tex`
- Section source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Verification target: `master_supporting_docs/Tariffs_ECB/0_clean/0_section_5_only.tex`
- Tracking files:
  - `quality_reports/plans/2026-04-15_section5-wrapper-accounting.md`
  - `quality_reports/session_logs/2026-04-15_section5-wrapper-accounting.md`

## Assumptions

1. The wrapper should preserve Section 5 numbering and figure numbering as in the main paper.
2. Cross-references back to the full paper should resolve from the main manuscript `.aux` file instead of by re-including Section 4.
3. Wrapper compilation is the relevant verification target for this pass; a full-manuscript rebuild is not required unless the wrapper reveals a shared-source problem.

## Planned Steps

1. Create a standalone Section 5 wrapper that imports labels from the main manuscript.
2. Revise the opening paragraph in `56_sectoral_channels.tex` to remove the "modest aggregate numbers" framing and the justification for focusing on the US-on-China tariff leg.
3. Compile the Section 5-only wrapper and confirm the PDF is generated successfully.
4. Explain the household-demand versus intermediate-demand distinction directly from the benchmark transmission code path.

## Verification

- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_section_5_only.tex`

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/0_section_5_only.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/plans/2026-04-15_section5-wrapper-accounting.md`
- `quality_reports/session_logs/2026-04-15_section5-wrapper-accounting.md`
