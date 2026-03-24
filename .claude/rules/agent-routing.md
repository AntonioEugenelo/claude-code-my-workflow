# Agent Routing: Which Agents Run on Which Documents

**When the orchestrator reaches Step 3 (REVIEW), use this table to determine which agents to run.**

This replaces ad-hoc agent selection. Every document type has a defined agent set, execution order, and early termination rules.

**Manifest check:** Before invoking any agent, check `.claude/active-infrastructure.md`. If a manifest exists, only invoke agents listed there (plus core agents like proofreader). If no manifest exists (main branch), use the full routing table. See `infrastructure-manifest.md` for details.

---

## Routing Table

| Document Type | Path Pattern | Agents (in order) | Review Tier |
|---|---|---|---|
| **Cover letter / proposal** | `Letters/**/*.tex` | proofreader ∥ domain-reviewer ∥ narrative-reviewer → cover-letter-reviewer | Standard |
| **Beamer slides** | `Slides/**/*.tex` | proofreader ∥ narrative-reviewer → domain-reviewer | Standard |
| **Research paper (theory)** | `master_supporting_docs/**/*.tex` (any paper in supporting docs, including submodules like `Tariffs_ECB/`, `MCMS/`) | proofreader ∥ derivation-auditor → theory-critic → narrative-reviewer | Deep |
| **Journal peer review** | `**/*review*.xml`, `**/*review*.md` | proofreader → narrative-reviewer | Light |
| **Exams / problem sets** | `**/*exam*.*`, `**/*PSet*.*`, `**/*tutorial*.*` | proofreader → domain-reviewer | Light |
| **Documentation** | `quality_reports/**/*.md`, `*.md` | proofreader | Quick |

### Reading the table

- **∥** means run in parallel (no dependency between agents)
- **→** means run sequentially (right agent depends on left agent's output or assumes it passed)
- Agents listed left-to-right reflect execution order

---

## Execution Order Logic

### Why order matters

Some agents assume the output of others:
- **derivation-auditor → theory-critic:** No point critiquing the theory if the maths is wrong. The theory-critic assumes derivations are correct.
- **proofreader ∥ everything:** Proofreading is independent of all other agents. Always run in parallel with the first batch.
- **domain-reviewer before cover-letter-reviewer (for letters):** Factual accuracy should be confirmed before assessing narrative quality, since a factual error changes the narrative assessment.
- **narrative-reviewer last (for papers):** Narrative flow review assumes the content is mathematically and theoretically sound.

---

## Review Tiers

Not every edit needs every agent. Three tiers:

| Tier | When to use | What runs |
|---|---|---|
| **Quick** | Typo fix, single-sentence edit, formatting change | proofreader only |
| **Standard** | After drafting, significant rewriting, or section restructuring | Full agent set from routing table |
| **Deep** | Before submission, after major revision, or on user request | Full agent set + cross-check against source documents in `master_supporting_docs/` |

### Tier selection

- Default: **Standard** (the orchestrator uses this unless told otherwise)
- Use **Quick** when the change is < 5 lines and purely cosmetic
- Use **Deep** when the user says "review thoroughly", "before sending", "final check", or when score needs to reach ≥ 95

---

## Early Termination

To save compute, stop the review pipeline early when critical errors are found:

| Condition | Action |
|---|---|
| derivation-auditor finds ≥ 1 CRITICAL error | Skip theory-critic. Report: "Fix derivation errors before theoretical review." |
| domain-reviewer finds ≥ 1 CRITICAL error (wrong name, wrong institution) | Skip cover-letter-reviewer. Report: "Fix factual errors before narrative review." |
| proofreader finds ≥ 5 CRITICAL/MAJOR errors | Flag for rewrite rather than continuing the pipeline. |
| Any agent finds compilation-blocking issue | Stop all agents. Fix and recompile first. |

---

## Adding New Document Types

When a new branch introduces a document type not listed above:

1. Identify the path pattern
2. Determine which agents are relevant (ask: what can go wrong with this document?)
3. Add a row to the routing table
4. Commit to all branches

---

## Relationship to Skills

| Skill | Uses routing? | Notes |
|---|---|---|
| `/review-letter` | Yes — routes to cover letter agent set | Should be generalised to `/review` |
| `/proofread` | No — always runs proofreader only | Equivalent to Quick tier |
| `/compile-letter` | No — compilation only, no agents | Pre-review step |
| Orchestrator Step 3 | Yes — this is the primary consumer | Reads document type from file path |
