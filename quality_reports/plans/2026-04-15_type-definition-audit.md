## Plan: Type Definition Audit Across Root And Nested Repos

Date: 2026-04-15
Status: In progress

### Goal

Audit maintained source across the root repo and nested repos, excluding `.tex` and `.mod` files, to find explicit and implicit type/data-shape definitions that should be shared or consolidated.

### Scope

- Root repository maintained source and automation files
- `master_supporting_docs/MCMS/` maintained source excluding `.tex` and `.mod`
- `master_supporting_docs/Tariffs_ECB/` maintained source excluding `.tex` and `.mod`
- Relevant type-like constructs:
  - Python annotations, aliases, dataclasses, TypedDict-like records, dict/list record shapes
  - MATLAB struct conventions and repeated field contracts
  - JSON or JSON-schema-like records used as contracts
  - Shell/PowerShell/QMD/HTML/JS maintained source only where they define or consume record-like shapes
- Excluded:
  - Generated artifacts
  - Compiled outputs
  - Pure prose/LaTeX source

### Assumptions

- The task is read-only for product code; only plan and session-log files may be added.
- “Should be shared” includes cross-file reuse inside a repo and cross-repo contracts where the same shape appears with drift risk.
- If explicit type systems are sparse, the audit should still identify where stronger shared interfaces would help.

### Steps

1. Inventory maintained source by language and path, filtering out generated artifacts.
2. Search for explicit type constructs and repeated record-shaped data flows.
3. Inspect the highest-value hotspots in root scripts and nested repos.
4. Identify duplicated or divergent shapes and where a shared contract would reduce ambiguity.
5. Deliver a critical assessment with file references and recommendations only.

### Verification

- Confirm the audit excludes `.tex` and `.mod` files.
- Confirm maintained source and generated artifacts are distinguished.
- Confirm findings include explicit and implicit contracts, not only formal type declarations.
