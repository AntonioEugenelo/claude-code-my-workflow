# Plan: Invoicing Wording And Red Cleanup

Date: 2026-04-20

Scope
- Replace references to `heterogeneous DCP` / `Het DCP` with `heterogeneous invoicing` in the active manuscript source.
- Remove red text formatting from the affected manuscript prose so accepted revisions are no longer displayed as markup.
- Rebuild the live paper and run targeted searches to confirm the cleanup.

Steps
1. Identify all live `.tex` occurrences of the old label and all red wrappers in the affected section files.
2. Patch the relevant manuscript files, keeping wording and economics unchanged except for the requested terminology cleanup.
3. Compile `0_clean/0_main.tex` and run targeted search checks for stale labels or residual red wrappers.
