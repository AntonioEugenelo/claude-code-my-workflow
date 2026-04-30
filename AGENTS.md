# AGENTS.md

This repository is configured for Codex-first use.

## Operating Principles

- Plan first for non-trivial tasks. If a task is likely to touch more than 3 files, take more than 30 minutes, or has multiple valid interpretations, write a plan to `quality_reports/plans/YYYY-MM-DD_short-description.md` before editing.
- Verify after edits. Do not report completion on LaTeX, Quarto, code, or data tasks until the relevant output has been compiled, rendered, executed, or otherwise checked.
- Treat source files as authoritative. For writing projects, `.tex`, `.qmd`, `.R`, `.py`, `.m`, and source figure scripts are the source of truth. PDFs, rendered HTML, and exported figures are derived artifacts.
- Keep context on disk. Plans belong in `quality_reports/plans/`, session notes in `quality_reports/session_logs/`, merge reports in `quality_reports/merges/`, and persistent lessons in `MEMORY.md`.
- Use explicit review passes instead of self-approval. After material fixes, re-run the relevant review checklist before claiming the issue is resolved.
- Respect active decision locks in `quality_reports/decisions/ACTIVE.md`. If a user request conflicts with an active lock, state the conflict and ask for an explicit override before proceeding.
- Use the rerun gate before expensive reruns. Do not rerun long MATLAB, Julia, Quarto, LaTeX, or data-generation jobs until `docs/codex-workflows/rerun-gate.md` has been applied.
- Keep `main` purpose-agnostic. It is an overset of reusable workflows and overlays, not a branch with one active project baked in.

## Startup Routine

1. Read this file.
2. Check `git status` before editing.
3. For non-trivial work, read the latest relevant plan in `quality_reports/plans/`.
4. Read `quality_reports/decisions/ACTIVE.md` before branch, sync, rerun, audit, or model-specification changes.
5. Read the workflow docs in `docs/codex-workflows/` that match the task.
6. If this is the first prompt on a newly repurposed project branch, apply `docs/codex-workflows/branch-tailoring.md`.
7. If the task activates a project-specific overlay, read the matching file in `docs/project-overlays/`.
8. If the task touches `master_supporting_docs/Tariffs_ECB/` and this is the first Codex call on the current branch/session, check Overleaf status first using the repo machinery in `scripts/sync-overleaf.sh` before editing. Prefer `status` first, then `pull` if remote changes are present or the user asks to sync.

## Core Workflows

- Planning and ambiguity handling: `docs/codex-workflows/plan-first.md`
- First-prompt project tailoring: `docs/codex-workflows/branch-tailoring.md`
- Implement-verify-review loop: `docs/codex-workflows/orchestrator.md`
- Explicit read-only review agents: `docs/codex-workflows/review-agents.md`
- Adversarial review loop: `docs/codex-workflows/adversarial-review.md`
- Review lens selection by document type: `docs/codex-workflows/review-routing.md`
- Working conventions and source fidelity: `docs/codex-workflows/working-conventions.md`
- Writing and analysis style guides: `docs/codex-workflows/style-guides.md`
- Quality gate details: `docs/codex-workflows/quality-gates.md`
- Session logging and merge reporting: `docs/codex-workflows/session-logging.md`
- Capability map for common requests: `docs/codex-workflows/capabilities.md`
- Rerun gate for expensive jobs: `docs/codex-workflows/rerun-gate.md`
- Claim ledger workflow: `docs/codex-workflows/claim-ledger.md`
- Long-run monitoring: `docs/codex-workflows/long-run-monitoring.md`
- Source authority checks: `docs/codex-workflows/source-authority.md`
- Migration notes from the previous Claude-first setup: `docs/codex-migration.md`

## Repository Notes

- This branch is purpose-agnostic by default. Specialized academic capabilities are present, but they are opt-in overlays rather than global assumptions.
- When creating a project branch from this branch, use `templates/branch-tailoring-prompt.md` as the first prompt and activate only the necessary overlays.
- `master_supporting_docs/` may contain optional project material, supporting papers, and submodules. Treat nested git repos and submodules carefully.
- `model/` may contain optional MATLAB/Dynare/research-analysis assets for overlays that need them.
- `scripts/` contains reusable automation. Prefer using or extending these scripts over reimplementing workflow logic in prose.
- `templates/` contains plan, quality-report, and session-log templates.
- `quality_reports/decisions/ACTIVE.md` contains active locks that prevent repeated branch/source/model confusion.
- `quality_reports/claim_ledgers/` contains source-to-claim verification ledgers for result audits.
- `quality_reports/run_cards/` contains contracts for expensive or output-overwriting runs.
- `quality_reports/run_state/` is ignored runtime state for current long-running jobs.
- `.claude/` is retained as compatibility/reference material. Do not rely on Claude-specific runtime semantics for Codex behavior unless the user is explicitly running Claude Code.
- `.codex/` mirrors agents, skills, rules, hooks, and workflow metadata for Codex-first use. Treat `.claude/` as the source for Claude parity and `.codex/` as the Codex-facing reference.
- `.codex/review_agents/` contains read-only review prompt cards used by `docs/codex-workflows/review-agents.md`.
- `.codex/config.toml` actively registers supported Codex hooks for command guards, `PostToolUse`, `SessionStart[resume]`, and `Stop`. Claude `Notification` and `PreCompact` have no exact Codex event in the installed runtime, so checkpointing and session-log capture remain explicit workflow obligations.

## Project Overlays

- Generic base: no project overlay required.
- Branch-to-purpose map: `docs/project-overlays/branch-purpose-map.md`.
- Academic research workflows: `docs/project-overlays/academic-research.md`.
- Antonio/Oxford local circumstances: `docs/project-overlays/antonio-eugenelo.md`.
- Tariffs/Overleaf workflow: `docs/project-overlays/tariffs-overleaf.md`.
- MCMS model workflow: `docs/project-overlays/mcms.md`.
- Government Spending project: `docs/project-overlays/government-spending.md`.
- Cox replication workflow: `docs/project-overlays/cox-replication.md`.
- Cover letters and applications: `docs/project-overlays/cover-letters.md`.
- CV editing and application-packet checks: `docs/project-overlays/cv-editing.md`.
- Referee and conference reviews: `docs/project-overlays/referee-review.md`.
- Teaching, lectures, and slides: `docs/project-overlays/teaching-slides.md`.
- Slide/application prototypes: `docs/project-overlays/slide-prototype.md`.
- Workflow infrastructure maintenance: `docs/project-overlays/workflow-infrastructure.md`.

## Review and Quality

- Use the quality thresholds in `docs/codex-workflows/orchestrator.md`. The inherited default gates are 90 for commit-ready work, 95 for external review, 98 for send/deploy, and 60 for exploratory work.
- When a task materially changes prose, analysis, or outputs, perform a review pass using the correct lenses from `docs/codex-workflows/review-routing.md`.
- Do not estimate post-fix scores from memory. Re-check the current files.

## Capability Triggers

If the user asks to proofread, review, compile, translate to Quarto, validate citations, draft a letter, analyze data, or prepare a deployment, follow the matching procedure in `docs/codex-workflows/capabilities.md`.

If the user asks to rerun, recompute, regenerate figures, recompile a large artifact, or check whether outputs changed, apply `docs/codex-workflows/rerun-gate.md` first.

If the user asks to audit all results, all figures, all numeric claims, or whether text still matches generated outputs, create or update a claim ledger under `quality_reports/claim_ledgers/` before broad edits.

If the user asks to push, pull, sync Overleaf, merge branches, or copy outputs between repos, apply `docs/codex-workflows/source-authority.md` first.

If the user asks for harsh review, adversarial review, review agents, or external-style critique, use `docs/codex-workflows/review-agents.md` and `docs/codex-workflows/adversarial-review.md`.
