# Plan: Codebase Quality Audit Across Repos

Date: 2026-04-15

## Goal

Produce a code-quality audit across the root repository and nested repositories, excluding `.tex` and `.mod` files, using eight specialized subagents. The deliverable is a critical assessment of the current code, concrete recommendations, and a prioritized cleanup sequence. This phase is research-only unless the user later asks for implementation.

## Scope

- Root repository source and automation files
- `master_supporting_docs/MCMS/` source files other than `.tex` and `.mod`
- `master_supporting_docs/Tariffs_ECB/` source files other than `.tex` and `.mod`
- Included languages and formats if used as source: Python, MATLAB, shell, PowerShell, Quarto, Markdown, HTML, CSS, JavaScript/TypeScript, JSON/YAML/TOML, and related helpers
- Excluded: `.tex`, `.mod`, compiled artifacts, and generated outputs unless needed to classify code as generated/legacy

## Assumptions

- “Across all repos” means the root repo plus nested git repositories present in this workspace.
- The user wants an assessment and recommendations first, not automatic code changes.
- File types such as `.html` or generated docs should be flagged when they appear derived, but still assessed if they act as maintained source.

## Agent Tasks

1. Deduplicate and consolidate code; identify DRY opportunities that reduce complexity.
2. Audit type definitions and identify types that should be shared or consolidated.
3. Find unused code and propose safe removals, with reference checks.
4. Detect and explain circular dependencies and propose untangling strategies.
5. Find weak typing (`any`, `unknown`, and equivalents) and recommend strong replacements with evidence.
6. Audit try/catch and equivalent defensive patterns; keep only justified error handling.
7. Find deprecated, legacy, fallback, or redundant code paths and propose removal.
8. Find AI slop, stubs, placeholder comments, migration chatter, and low-value comments for removal or rewrite.

## Steps

1. Inventory repositories, languages, and likely maintained source paths.
2. Spawn 8 specialist subagents with non-overlapping review charters.
3. In parallel, build a local map of source hotspots and generated artifacts.
4. Collect each agent’s assessment and recommendations.
5. Consolidate overlaps, conflicts, and dependencies into a cleanup roadmap.
6. Report findings and recommended sequence without editing code.

## Verification

- Confirm all requested audit areas are covered by separate subagents.
- Confirm the audit excludes `.tex` and `.mod` files.
- Confirm the final synthesis distinguishes findings from recommendations and notes uncertainty where tools could not be executed.
