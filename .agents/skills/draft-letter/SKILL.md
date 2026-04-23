---
name: draft-letter
description: Guided cover letter drafting workflow. Gathers context, identifies gaps, asks clarifying questions, drafts the letter, compiles, and presents for review.
disable-model-invocation: true
argument-hint: "[application name, e.g. 'nuffield-yale-exchange']"
allowed-tools: ["Read", "Write", "Edit", "Bash", "Glob", "Grep", "Agent"]
---

# Draft Cover Letter

Guided workflow for drafting an academic cover letter from context.

## Steps

1. **Gather context:**
   - Read `.Codex/rules/cover-letter-context.md` for applicant profile
   - Read any existing letter template in `Letters/$ARGUMENTS/`
   - Read supporting documents in `master_supporting_docs/` (CVs, papers, slides)
   - Read any programme-specific documents

2. **Identify gaps:**
   - Check which PLACEHOLDER sections in `cover-letter-context.md` are unfilled
   - List what information is missing (faculty names, dates, specific achievements)

3. **Ask clarifying questions** (max 5):
   - Use AskUserQuestion for each gap
   - Focus on: recipient details, faculty matches, specific research plan, dates, achievements to highlight

4. **Draft the letter:**
   - Follow the structure in the template
   - Apply style guidelines from `cover-letter-context.md`
   - Ensure every paragraph earns its place
   - Target 350--450 words, strictly 1 page
   - Use British English throughout

5. **Compile:**
   - Run single-pass XeLaTeX
   - Verify 1 page, no errors

6. **Present to user:**
   - Show the compiled letter content
   - Highlight any areas that need user input
   - Note word count and page count
   - Ask for feedback before proceeding to review

## Important

- **Never send a letter without user approval** -- always present for review
- **Be specific** -- every claim should be backed by evidence from the supporting docs
- **Update `cover-letter-context.md`** with any new information gathered during drafting
