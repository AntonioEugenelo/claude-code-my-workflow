# Requirements Specification: Codex Adversarial Review Loop Parity

**Date:** 2026-04-13
**Status:** APPROVED

---

## Objective

Make the Codex branch's adversarial review loop behave as closely as possible to the old Claude review workflow while ensuring that all review agents are explicitly read-only.

---

## Requirements

### MUST Have (Non-Negotiable)

- [x] Restore an explicit review-agent layer, not just abstract review lenses.
- [x] Make the active review routing as close as possible to the old Claude routing and round structure.
- [x] Define a Codex-native adversarial review loop with baseline review, challenge pass, fix pass, and re-review.
- [x] State clearly that review agents are read-only and should be spawned as Codex `explorer` agents only.
- [x] Keep active review documentation, helper scripts, and public guide pages consistent.
- [x] Verify the new review workflow with at least one sample routing/planning run and one guide rebuild if guide source changes.

### SHOULD Have (Preferred)

- [x] Provide reusable prompt cards or agent definitions that mirror the old reviewer roles.
- [x] Preserve the old reviewer names where practical to minimize cognitive migration costs.
- [x] Keep review tracking on disk and compatible with the existing `review-mode.sh` helper.

### MAY Have (Optional, If Time)

- [x] Add a helper script that computes the required review agents and waves for a given file path and round.
- [x] Add an adversarial review report template or log guidance.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Meaning of "as close as absolutely possible" | CLEAR | Interpreted as matching old routing, agent names, execution waves, and loop discipline as far as Codex allows without Claude-only hooks. |
| Meaning of "review agents are read only" | CLEAR | Implement as explorer-only review agents with explicit report-only instructions and no write ownership. |
| Whether the old `.claude/agents/` files should become active again | ASSUMED | No; active equivalents should be Codex-native, while `.claude/agents/` remain archival reference. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- Active docs describe review agents, routing, and adversarial loops in Codex-native terms.
- Review agents are explicitly constrained to read-only explorer use.
- The repo contains reusable review-agent definitions or prompts for the common review roles.
- A helper command or documented procedure can reproduce the required review set for a target file and round.
- Verification demonstrates that the updated workflow artifacts and docs are internally consistent.

---

## Approval

[x] User approved: 2026-04-13
