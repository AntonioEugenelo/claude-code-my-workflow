Status: in progress

Task:
- Check whether figures shown in the local `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf` are outdated relative to the current local source tree, and reconcile any mismatch without touching Overleaf.

Scope:
- `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- figure-bearing section files under `master_supporting_docs/Tariffs_ECB/0_clean/sections/`
- local figure assets under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
- any local generation scripts or generated artifacts that prove necessary to refresh stale figures

Core requirements:
- Treat the local workspace as authoritative for this task.
- Do not sync, pull, or otherwise modify Overleaf state.
- Preserve unrelated dirty changes already present in the nested `Tariffs_ECB` repo.
- Determine whether the issue is a stale compiled PDF, stale figure assets, or stale manuscript references.
- Rebuild and verify the local `0_main.pdf` before reporting completion.

Likely implementation approach:
- Compare current source timestamps and current dirty files against the last local `0_main.pdf` build.
- Enumerate the figures currently referenced by the active section files.
- Inspect diffs in the figure-bearing sections to see whether the manuscript now expects different figures than the compiled PDF shows.
- If needed, regenerate missing or outdated local figures from source, then rebuild `0_main.tex`.
- Review the rebuilt output with a figure-consistency lens and note any residual issues.

Verification:
- compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- inspect the compilation log for blocking errors or figure-related warnings
- compare the rebuilt PDF timestamp and, if useful, checksum against the previous local build
- inspect the resulting PDF pages that contain the suspected figures

Known assumptions and risks:
- The user's concern is about the local PDF only, not Overleaf divergence.
- Existing uncommitted edits in `Tariffs_ECB` are user-owned unless I make them during this task.
- Some figure inconsistencies may stem from changed section text or table inputs rather than changed image files.
