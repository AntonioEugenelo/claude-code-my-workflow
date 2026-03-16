# Agent Learning: Updating Review Agents from Missed Issues

**When the user catches an issue that a review agent missed, update that agent's file immediately.**

---

## When to Trigger

- The user points out a problem in a document that was recently reviewed by an agent
- The user corrects something that an agent should have flagged but didn't
- A factual error, tone issue, or formatting problem slips through review

## What to Do

1. **Identify which agent should have caught it** (proofreader, cover-letter-reviewer, domain-reviewer)
2. **Append the check to that agent's `## Learned Checks` section** at the bottom of its file
3. **Format:**
   ```markdown
   ### LC-N: <short description>
   - **Missed:** "<what the agent failed to flag>"
   - **Should check:** <what the agent should look for in future>
   - **Date:** YYYY-MM-DD
   ```
4. **If the `## Learned Checks` section doesn't exist yet**, create it at the bottom of the agent file

## Consolidation

When `## Learned Checks` reaches **5 or more items**, remind the user:

> "The [agent name] agent has accumulated N learned checks. Run `/simplify` on `.claude/agents/[agent].md` to consolidate them into the main sections and keep the file lean."

After `/simplify` runs, the learned checks should be **merged into the existing check categories** (not left as a separate section). The `## Learned Checks` section resets to empty or is removed.

## Rules

- Never silently drop a learned check — every item must either be merged into the main sections or explicitly discussed with the user before removal
- Keep learned checks specific and actionable, not vague
- If the same type of issue is missed twice, escalate it to a higher severity in the agent's main checklist
