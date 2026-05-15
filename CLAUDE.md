# CLAUDE.md -- Fiscal-LPT / MCMS Project Workflow

**Project:** Fiscal variables and fiscal-rule steps for the MCMS model  
**Paper repo:** `../Fiscal-LPT`  
**Model repo:** `../MCMS-private`  
**Workflow repo:** `.`  
**Institution:** University of Oxford, Department of Economics

## Core Principles

- Plan first for non-trivial work and save plans to `quality_reports/plans/`.
- Verify after edits. Compile paper changes, run model checks, or verify docs
  paths before reporting completion.
- Keep the three repositories separate:
  - `../Fiscal-LPT`: paper and Overleaf source only.
  - `../MCMS-private`: model code, calibration, runtime files, and outputs needed
    to support paper claims.
  - this repo: writing direction, review prompts, style sources, plans, and
    workflow machinery.
- Treat `docs/supporting_docs/` as writing-source material. It informs prose
  structure and style; it is not an Overleaf payload.
- Use `docs/codex-workflows/fiscal-lpt-writing-style.md` for all Fiscal-LPT
  paper prose.

## Active Project Overlays

- `docs/project-overlays/fiscal-lpt-mcms.md`
- `docs/project-overlays/mcms.md`
- `docs/codex-workflows/fiscal-lpt-writing-style.md`

## Writing Standard

Fiscal-LPT paper text should be mechanism-first economics prose:

1. puzzle or fact,
2. mechanism,
3. model object or result,
4. economic interpretation,
5. implication.

Use the Harvard writing guide for clarity, organization, evidence discipline,
and revision standards. Use the Cochrane papers only as evidence for
high-level rhythm and argument structure. Do not copy phrases from them.

## Review Standard

When Fiscal-LPT paper text changes, review with:

- `proofreader`
- `derivation-auditor` when equations or model logic changed
- `figure-reviewer` when figures, tables, outputs, or numeric claims changed
- `theory-critic`
- `cochrane-style-reviewer`
- `narrative-reviewer`

Use `scripts/review_plan.py ../Fiscal-LPT/main.tex` to confirm the expected
review waves.

## Commands

Paper compilation:

```powershell
cd ..\Fiscal-LPT
latexmk -pdf main.tex
```

Model environment:

```powershell
cd ..\MCMS-private
julia --project=. scripts/setup_dependencies.jl
```

Model runs should use the run card and rerun gate before any expensive or
output-overwriting command:

```powershell
cd ..\MCMS-private
julia --project=. scripts/run_model.jl --single
```

## Quality Gates

- `90/100`: commit-ready work.
- `95/100`: ready for supervisor or collaborator review.
- `98/100`: ready to send, publish, or submit.

Do not self-score after fixes. Re-run the relevant review checklist on the
current files.
