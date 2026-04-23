# Plan: Weak-Type Audit Across Workspace Repos

Date: 2026-04-15

## Goal

Audit maintained source across the workspace root repository and nested repositories for weak typing patterns, excluding `.tex` and `.mod` files. Deliver a read-only critical assessment with file references, justified stronger replacements, and likely risks.

## Scope

- Root repository maintained source and automation
- Nested repositories under `master_supporting_docs/`
- Languages and source formats in scope where maintained: Python, MATLAB, shell, PowerShell, JavaScript/TypeScript, HTML/CSS, Markdown/Quarto frontmatter, JSON/YAML/TOML helpers
- Excluded: `.tex`, `.mod`, generated artifacts, compiled outputs, vendored code, and dead/generated documentation unless it acts as maintained source

## Assumptions

- “Weak types” includes `any`, `unknown`, untyped containers, loose dict/struct schemas, dynamically keyed payloads with undocumented shape, and equivalent patterns in non-TypeScript languages.
- The user wants an audit only; no code edits should be made.
- “Maintained source only” means active scripts and code paths that appear to be source-of-truth, not generated HTML/PDF outputs unless they are clearly maintained by hand.

## Steps

1. Inventory nested repositories and maintained source paths.
2. Scan for weak-type markers and structurally weak data-shape patterns.
3. Trace surrounding code, package contracts, JSON payloads, MATLAB struct fields, and function inputs/outputs to infer stronger shapes.
4. Separate actionable findings from lower-confidence observations.
5. Report the strongest replacements and the risks of each current weak pattern.

## Verification

- Confirm the audit covers both the root repo and nested repos.
- Confirm `.tex` and `.mod` files are excluded.
- Confirm findings reference maintained source files and explain the evidence for each proposed stronger type.
