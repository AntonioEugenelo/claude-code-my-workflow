# MCMS Overlay

Activate this overlay for MCMS model work, calibration, simulation, and output
audits.

## Scope

The active MCMS model repository is `../MCMS-private`.

Use this overlay when the task touches:

- model equations,
- calibration values,
- Julia or Dynare runtime files,
- scenario runners,
- generated model outputs,
- paper claims that depend on MCMS outputs.

## Verification

- Check the current branch and dirty worktree before editing.
- Do not overwrite generated outputs without applying
  `docs/codex-workflows/rerun-gate.md`.
- Tie every paper-facing numeric claim to the script, input, and output file that
  generated it.
- Prefer explicit run notes and reproducible commands over manual output edits.

## Repository Boundary

Keep runnable model material in `../MCMS-private`. Keep paper source in
`../Fiscal-LPT`. Keep writing direction and style material in this workflow repo.
