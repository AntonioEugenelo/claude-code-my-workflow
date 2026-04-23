# Requirements Specification: Complete Codex Port

**Date:** 2026-04-13
**Status:** APPROVED

---

## Objective

Finish the repository migration so that Codex-native instructions, scripts, and documentation are the active control plane and no live workflow depends on Claude-specific runtime concepts.

---

## Requirements

### MUST Have (Non-Negotiable)

- [x] Align the active repository instructions, scripts, and thresholds so they agree on the same Codex workflow.
- [x] Remove live dependencies on `.claude/settings.json`, hook enforcement, Claude-only agent semantics, and Claude-only state paths from active scripts and docs.
- [x] Promote high-value project-specific guidance that is still only in `.claude/` into active Codex-readable documentation.
- [x] Keep the repository usable for current work without deleting unrelated user/project content in nested repos.
- [x] Verify the migrated state by checking the updated docs, scripts, and generated workflow guide artifacts.

### SHOULD Have (Preferred)

- [x] Preserve legacy Claude material only as explicitly archived reference, not as an implied active workflow path.
- [x] Replace stale references in templates and helper docs so new work products are generated in Codex-native form.
- [x] Keep the migration legible by documenting the new active locations for style, review, exploration, and reproducibility guidance.

### MAY Have (Optional, If Time)

- [x] Add lightweight bridging notes where legacy assets are retained for comparison.
- [x] Consolidate duplicated migration guidance if that can be done without losing clarity.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Scope of "complete the port in full" | CLEAR | Interpreted as completing the active workflow migration for this repo, not deleting all legacy reference material outright. |
| Treatment of `.claude/` | ASSUMED | Legacy assets may remain on disk for comparison, but active docs/scripts should no longer depend on them. |
| Nested project repos | CLEAR | Out of scope except where active workflow docs/scripts reference them. Existing project edits must be preserved. |
| Generated docs | CLEAR | Regenerate the workflow guide/html if source docs or guide source changes materially. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- Active instructions and helper scripts point to Codex-native docs/state/thresholds rather than Claude-specific runtime machinery.
- New users can follow `AGENTS.md`, `docs/codex-workflows/`, and supporting templates without being routed back into `.claude/`.
- Repo searches for active documentation and script entrypoints show legacy Claude references only in archived/reference material.
- The updated guide/source files are verified and the repository state is documented on disk.

---

## Approval

[x] User approved: 2026-04-13
