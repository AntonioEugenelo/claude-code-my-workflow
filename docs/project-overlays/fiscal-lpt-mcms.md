# Fiscal-LPT MCMS Overlay

Activate this overlay for the Fiscal-LPT project: adding fiscal variables and
fiscal-rule steps to the MCMS model and writing the associated paper.

## Repositories

- `../Fiscal-LPT`: paper and Overleaf source only.
- `../MCMS-private`: model code, calibration, runtime scripts, generated model
  outputs, and files needed to run or calibrate the MCMS fiscal extension.
- `.`: workflow machinery, writing direction, review prompts, supporting writing
  guides, and project-management material.

## Source Authority

- Model behavior is authoritative in `../MCMS-private/src`,
  `../MCMS-private/scripts`, `../MCMS-private/input_data`, and generated outputs.
- Paper source is authoritative in `../Fiscal-LPT`.
- Writing guidance is authoritative in `docs/supporting_docs`,
  `docs/fiscal_lpt_writing_materials`, and
  `docs/codex-workflows/fiscal-lpt-writing-style.md`.

## Model Boundary

MCMS should contain:

- Julia project files and runtime dependencies.
- Dynare or Julia model files required to run the fiscal-LPT extension.
- calibration files and input data.
- generated CSVs or model outputs when they are inputs to paper claims.
- README or run notes needed to reproduce scenarios.

MCMS should not contain:

- prose style guides,
- paper drafts not needed for execution,
- literature PDFs used only for writing style,
- narrative memos unless they document run/calibration requirements.

## Paper Boundary

Fiscal-LPT should contain only what Overleaf needs:

- `main.tex` and included `.tex` files,
- bibliography and style files,
- paper figures/tables actually included,
- minimal assets required to compile.

It should not contain model runners, calibration scratch files, supporting-paper
PDFs, style dossiers, or writing instructions.

## Writing Boundary

The workflow repo should contain:

- plans, review reports, and instruction files,
- writing guides and source-style material,
- Cochrane-informed prose rules,
- architecture notes that direct how agents write and review the paper.

## Paper Writing Rule

All Fiscal-LPT paper text should follow
`docs/codex-workflows/fiscal-lpt-writing-style.md` and be reviewed with the
`cochrane-style-reviewer` in addition to the standard research-paper agents.
