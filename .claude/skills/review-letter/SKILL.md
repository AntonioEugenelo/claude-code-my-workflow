---
name: review-letter
description: Multi-agent review of a cover letter. Runs proofreader + cover-letter-reviewer, combines scores, and produces a unified report.
disable-model-invocation: true
argument-hint: "[filename or path to .tex file]"
allowed-tools: ["Read", "Glob", "Grep", "Agent", "Write"]
---

# Review Cover Letter

Multi-agent review combining proofreading and substantive assessment.

## Steps

1. **Identify file to review:**
   - If `$ARGUMENTS` is a full path: use it directly
   - If `$ARGUMENTS` is a filename: search in `Letters/` for it
   - If `$ARGUMENTS` is empty: review the most recently modified `.tex` file in `Letters/`

2. **Launch review agents in parallel:**

   **Agent 1: Proofreader**
   - Grammar, typos, consistency, formatting
   - Saves report to `quality_reports/`

   **Agent 2: Cover Letter Reviewer**
   - Narrative arc, personalisation, qualifications, tone, conciseness
   - Saves report to `quality_reports/`

3. **Combine results:**
   - Merge findings from both agents
   - Apply the scoring rubric from `.claude/rules/cover-letter-quality.md`
   - Calculate overall score

4. **Present unified report:**
   - Overall score (N/100)
   - Gate status: BLOCK (<90) / COMMIT (90--94) / REVIEW (95--97) / SEND (98+)
   - Critical issues first, then major, then minor
   - Specific recommendations in priority order

5. **Save combined report** to `quality_reports/[FILENAME]_combined_review.md`

## Important

- **Do NOT edit source files** -- report only
- Both agents run independently and may find overlapping issues
- Deduplicate overlapping findings in the combined report
- The combined score is the LOWER of the two individual scores
