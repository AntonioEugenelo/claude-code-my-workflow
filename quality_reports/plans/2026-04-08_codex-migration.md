Status: COMPLETED

Goal
- Convert the repository's primary workflow instructions from Claude-specific runtime semantics to Codex-first guidance.

Approach
- Add a root `AGENTS.md` as the new authoritative instruction file.
- Reframe planning, orchestration, review routing, session logging, and capability mapping as explicit Codex workflow documents under `docs/codex-workflows/`.
- Rewrite the top-level README for Codex-first onboarding.
- Downgrade `CLAUDE.md` to a legacy pointer instead of a live control file.

Files Changed
- `AGENTS.md`
- `README.md`
- `CLAUDE.md`
- `docs/codex-migration.md`
- `docs/codex-workflows/plan-first.md`
- `docs/codex-workflows/orchestrator.md`
- `docs/codex-workflows/review-routing.md`
- `docs/codex-workflows/session-logging.md`
- `docs/codex-workflows/capabilities.md`

Verification
- Confirmed the new files exist and are readable.
- Confirmed the repository now exposes Codex-first entrypoints at the root and under `docs/codex-workflows/`.

Notes
- Existing `.claude/` assets were intentionally preserved as legacy reference material.
- Unrelated pre-existing workspace changes were left untouched.
