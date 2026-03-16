---
paths:
  - "Letters/**/*.tex"
---

# Cover Letter Verification Protocol

## Compilation

Single-pass XeLaTeX (no bibliography needed for letters):

```bash
cd Letters/<application-folder> && xelatex -interaction=nonstopmode cover-letter.tex
```

### Verification Checklist

1. **Compiles without errors** -- warnings acceptable only if documented
2. **Target page count** -- 1 page for letters; 3 pages (2 body + 1 references) for proposals
3. **No overfull hbox** -- text fits within margins
4. **Fonts render correctly** -- XeLaTeX + fontspec working

## Content Verification

Before any commit, verify:

- [ ] **Recipient correct:** Name, title, institution, address
- [ ] **Programme correct:** Full name, dates, term
- [ ] **Applicant details correct:** Name, college, department, email
- [ ] **Faculty names correct:** Spelled correctly, at correct institution, research area accurate
- [ ] **No unfilled TODOs:** Search for `TODO`, `PLACEHOLDER`, `XXX`, `[...]`
- [ ] **Dates consistent:** Application deadline, exchange dates, current date
- [ ] **Supervisor name correct:** If mentioned

## Pre-Send Checklist

Before the letter is sent (score >= 98):

- [ ] Proofread by proofreader agent
- [ ] Reviewed by cover-letter-reviewer agent
- [ ] All factual claims verified against source documents
- [ ] PDF opened and visually inspected
- [ ] Supervisor has reviewed (if applicable)
