# Session Logging

**Location:** `quality_reports/session_logs/YYYY-MM-DD_description.md`
**Template:** `templates/session-log.md`

## Three Triggers (all proactive)

### 1. Post-Plan Log

After plan approval, immediately capture: goal, approach, rationale, key context.

### 2. Incremental Logging

Append 1-3 lines whenever: a design decision is made, a problem is solved, the user corrects something, or the approach changes. Do not batch.

### 3. End-of-Session Log

When wrapping up: high-level summary, quality scores, open questions, blockers.

### 4. Repo Map Maintenance

When files are added, moved, or deleted — especially in `master_supporting_docs/MCMS/` or `Tariffs_ECB/` — update `reference_repo_map.md` in the memory directory. The repo map tracks directory structure, data pipeline paths, and CSV-to-figure mappings. Check it at session start; update it at session end if the structure changed.

## Quality Reports

Generated **only at merge time** -- not at every commit or PR.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md` using `templates/quality-report.md`.
