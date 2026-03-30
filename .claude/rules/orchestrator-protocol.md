# Orchestrator Protocol: Contractor Mode

**After a plan is approved, the orchestrator takes over autonomously.**

## The Loop

```
Plan approved → orchestrator activates
  │
  Step 1: IMPLEMENT — Execute plan steps
  │
  Step 2: VERIFY — Compile, render, check outputs
  │         If verification fails → fix → re-verify
  │
  Step 3: REVIEW
  │   3.0a Check .claude/active-infrastructure.md
  │         If manifest exists → only invoke listed agents + core (proofreader)
  │         If no manifest (main branch) → use full agent-routing table
  │   3.0b Activate review mode: run ./scripts/review-mode.sh start "<path-pattern>"
  │         This enables the completeness hook — without it, agents run ad-hoc
  │   3.1  Select agents per agent-routing.md (document type → agent set)
  │   3.2  Run agents (parallel where allowed, sequential where required)
  │   3.3  Agents produce the SCORE (Step 6 is agent-scored, never self-scored)
  │
  Step 4: FIX — Apply fixes (critical → major → minor)
  │
  Step 5: RE-VERIFY — Compile, render, check outputs after fixes
  │
  Step 6: RE-SCORE — Loop back to Step 3 for a FRESH agent review
  │         Agents re-score from scratch on the fixed files
  │         NEVER self-assess the score after fixing (see Article below)
  │
  └── Score >= threshold?
        YES → Present summary to user
        NO  → Loop back to Step 3 (max 5 rounds)
              After max rounds → present with remaining issues
```

## Article: No Self-Scoring After Fixes

**This is a non-negotiable rule. It may never be overridden.**

After applying fixes (Step 4), Claude MUST re-run the review agents (Step 3) to obtain a fresh score. Claude MUST NOT:

- Estimate the score by mentally adding back points for fixed issues
- Claim a score has been reached without agent verification
- Skip the re-review round because "the fixes were minor"
- Self-assess based on what it believes it changed

**Why:** Fixing bugs can introduce new bugs. Claude is not aware of whether its fixes are clean until independent review agents verify them. Self-scoring creates false confidence by relying on Claude's belief about what changed rather than independent verification. This is the same principle as software testing: a fix is not confirmed until the test suite passes.

**How to apply:** Every time fixes are applied in Step 4, the loop MUST return to Step 3 (REVIEW) for fresh agent scoring before any score is reported to the user. The only scores that count are those produced by review agents running on the current state of the files.

## Article: No Ad-Hoc Agent Subsetting in RE-SCORE Rounds

When the loop returns to Step 3 (RE-SCORE), Claude MUST NOT arbitrarily drop agents. Claude MUST NOT:

- Run only the agents that scored lowest in the previous round
- Skip agents that "passed" the previous round
- Reason that certain agents are unlikely to find new issues

**Exception — Round-1-only agents:** Agents marked with ¹ in the routing table (currently: `derivation-auditor`, `figure-reviewer`) run in Round 1 only and are skipped in RE-SCORE rounds (2+). These are expensive verification agents whose findings (derivation correctness, figure-data consistency) are unlikely to change from text-level fixes. The user can override this by requesting a "full review" for a subsequent round.

**RE-SCORE agent set for research papers (rounds 2+):** proofreader ∥ theory-critic → narrative-reviewer.

**Why:** The original no-subsetting rule existed to prevent Claude from self-assessing which agents to skip. The round-1-only exception is a deterministic rule (not a judgment call), so it does not reintroduce self-assessment. Fixes can still introduce new issues, which proofreader, theory-critic, and narrative-reviewer will catch.

**How to apply:** RE-SCORE rounds use the routing table minus ¹-marked agents. The parallel/sequential structure from agent-routing.md applies unchanged for the remaining agents. The only other valid reason to skip an agent is early termination (e.g., proofreader finds ≥5 CRITICAL errors → flag for rewrite).

**Incident:** 2026-03-28 — Round 2 ran only figure-reviewer and proofreader, dropping theory-critic and narrative-reviewer. This was ad-hoc subsetting (not the ¹ exception) and violated the rule.

## Limits

- **Main loop:** max 5 review-fix rounds
- **Critic-fixer sub-loop:** max 5 rounds
- **Verification retries:** max 2 attempts
- Never loop indefinitely

## "Just Do It" Mode

When user says "just do it" / "handle it":
- Skip final approval pause
- Auto-commit if score >= commit threshold (see quality-gates.md)
- Still run the full verify-review-fix loop
- Still present the summary
