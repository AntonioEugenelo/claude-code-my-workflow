Status: COMPLETED

Goal
- Complete the repository's migration from a Claude-first workflow layer to a fully Codex-native active workflow.

Scope
- Update active instructions, workflow docs, helper scripts, templates, and generated guide artifacts.
- Promote high-value project guidance from `.claude/` into active Codex-readable docs where needed.
- Leave unrelated project work and nested-repo content untouched.

Assumptions
- `.claude/` may remain as archived reference material, but no active script or current documentation should require it.
- Existing user edits in nested repos and untracked report files are out of scope and must be preserved.

Likely Files
- `AGENTS.md`
- `README.md`
- `docs/codex-migration.md`
- `docs/codex-workflows/*.md`
- `docs/index.html`
- `guide/workflow-guide.qmd`
- `guide/workflow-guide.html`
- `scripts/review-mode.sh`
- `scripts/sync-overleaf.sh`
- `scripts/quality_score.py`
- `explorations/README.md`
- `templates/skill-template.md`
- `quality_reports/specs/2026-04-13_complete-codex-port.md`
- `quality_reports/session_logs/2026-04-13_complete-codex-port.md`

Execution Steps
1. Create the migration spec and working log.
2. Audit active scripts/docs for remaining Claude-era dependencies and choose Codex-native replacements.
3. Port live state paths, threshold definitions, review helper behavior, and active reference docs.
4. Promote project-specific rules that still matter into active docs/reference material.
5. Sweep templates/helper docs for stale `.claude` and Claude-only instructions.
6. Regenerate workflow-guide outputs if source files change.
7. Verify by reading updated files, running the relevant render/generation/check commands, and scanning for stale active references.

Verification
- Read back the updated docs and scripts.
- Re-render the workflow guide if `guide/workflow-guide.qmd` changes.
- Search the active repo surface for stale `.claude` / Claude-only references and confirm they are confined to archived/reference material.

Known Risks
- Existing generated HTML may drift from source docs if the guide is not regenerated.
- Some project-specific guidance in `.claude/rules/` may need selective promotion rather than wholesale copying to avoid carrying over runtime assumptions.

Outcome
- Active repo instructions, helper scripts, templates, and public guide artifacts now use the Codex-native workflow surface.
- Repo-local helper state was migrated to `.codex/state/` for the Overleaf sync path.
- Legacy Claude references remain only as archived migration context or explicit ignore/mapping entries.
