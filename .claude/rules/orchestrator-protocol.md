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
  │   3.0  Check .claude/active-infrastructure.md
  │         If manifest exists → only invoke listed agents + core (proofreader)
  │         If no manifest (main branch) → use full agent-routing table
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
