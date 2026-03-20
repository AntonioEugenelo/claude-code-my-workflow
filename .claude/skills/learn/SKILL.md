---
name: learn
description: Update a review agent when it missed an issue the user caught. Identifies the responsible agent, reads its file, and appends a learned check.
disable-model-invocation: true
argument-hint: "[description of what was missed, or leave blank for guided mode]"
allowed-tools: ["Read", "Grep", "Glob", "Edit"]
---

# Agent Learning: Update Review Agents

When the user catches an issue that a review agent should have flagged, use this skill to update the agent's file with a new learned check so the error is never repeated.

**Input:** `$ARGUMENTS` — optional description of the missed issue.

---

## Steps

1. **Identify the missed issue.** If `$ARGUMENTS` is empty, ask the user:
   - What issue did you find?
   - Which document was it in?
   - Was this document recently reviewed by agents?

2. **Identify the responsible agent(s).** Determine which agent's lens covers this type of issue:

   | Issue type | Primary agent | Backup agent |
   |---|---|---|
   | Factual errors, wrong names/institutions | domain-reviewer | — |
   | Grammar, typos, formatting | proofreader | — |
   | Narrative overclaiming, logical flow gaps | narrative-reviewer | theory-critic |
   | Figure-claim misalignment, evidence overclaiming | theory-critic | narrative-reviewer |
   | Mathematical errors, derivation gaps | derivation-auditor | — |
   | Variable naming vs measurement mismatch | domain-reviewer | theory-critic |
   | Letter tone, structure, fit | cover-letter-reviewer | narrative-reviewer |
   | Visual/layout issues | slide-auditor | — |
   | R code quality | r-reviewer | — |
   | Citation inaccuracy | domain-reviewer | — |

   If the issue spans categories, update ALL relevant agents.

3. **Read the agent file(s).** Check for an existing `## Learned Checks` section.

4. **Determine the next LC number.** Count existing learned checks. If none, start at LC-1 and create the `## Learned Checks` section at the bottom of the file (before any final blank lines).

5. **Append the learned check** using this exact format:
   ```markdown
   ### LC-N: <short description>
   - **Missed:** "<exact quote or description of what the agent failed to flag>"
   - **Should check:** <specific, actionable instruction for future reviews>
   - **Date:** YYYY-MM-DD
   ```

6. **Check consolidation threshold.** If the agent now has **5 or more** learned checks, tell the user:
   > "The [agent] agent has N learned checks. Run `/simplify` on `.claude/agents/[agent].md` to consolidate them into the main review lenses."

7. **Confirm the update** to the user: which agent(s) were updated, the LC number, and a one-line summary.

---

## Principles

- Every learned check must be **specific and actionable**, not vague
- Include enough context in "Missed" that the check makes sense months later
- If the same type of issue was missed before (check existing LCs), escalate severity
- If multiple agents should have caught it, update ALL of them
- Never remove or overwrite existing learned checks — only append
