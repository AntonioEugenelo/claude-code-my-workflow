# Plan: Overleaf Changes To Red

Date: 2026-04-20

Objective
- Inspect the changes currently present on `overleaf/master` but not in the local synced commit.
- Apply the Overleaf-side manuscript change into the live source without overwriting local edits.
- Mark the imported Overleaf change in red in the live manuscript source.

Steps
1. Diff the synced local Overleaf commit against `overleaf/master` to isolate the exact remote manuscript hunk.
2. Compare that hunk against the current working tree version of the same file and patch it into the live source with red markup.
3. Rebuild `0_clean/0_main.tex` and verify the Overleaf-derived red text is present only where intended.
