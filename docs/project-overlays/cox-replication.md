# Cox Replication Overlay

Use this overlay for Cox replication, model-result checks, and related government-spending paper reruns.

## Rules

- Apply the rerun gate before expensive MATLAB, Julia, LaTeX, or data-generation jobs.
- Treat model scripts, data construction scripts, and paper source as authoritative over copied result tables or PDFs.
- Use claim ledgers for broad numeric or figure audits.
- Do not overwrite benchmark outputs without a run card that states inputs, expected outputs, and rollback path.
- Keep local replication notes in `quality_reports/` rather than embedding project-specific assumptions into the generic workflow.

## Typical Capabilities

- reproduce model tables or figures;
- compare generated results with paper claims;
- audit source-to-output chains;
- document failed or partial reruns;
- prepare replication-fix branches.
