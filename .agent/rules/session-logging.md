# Session Logging

**Location:** `quality_reports/session_logs/YYYY-MM-DD_description.md`
**Template:** `templates/session-log.md`

## Three Triggers (all proactive)

### 1. Post-Plan Log

After plan approval, immediately capture: goal, approach, rationale, key context.

### 2. Incremental Logging

Append 1-3 lines whenever: a design decision is made, a problem is solved, the user corrects something, or the approach changes. Do not batch.

### 3. End-of-Session Log

When wrapping up: high-level summary, quality scores, open questions, blockers.

**After the log, always present the following reflection prompt to the user:**

---

#### Session Reflection

Take a moment to reflect on learnings from this session.

**Where should learnings go?**

- 📚 **MEMORY.md** (committed, synced across machines)
  - Generic patterns applicable to ALL academic workflows
  - Examples: workflow improvements, design principles, documentation patterns
  - Format: `[LEARN:category] pattern → benefit`

- 🔒 **.agent/state/personal-memory.md** (gitignored, local only)
  - Machine-specific learnings (file paths, tool versions, edge cases)
  - Examples: "XeLaTeX on macOS requires TEXINPUTS=../Preambles"
  - Stays on this machine, doesn't clutter template for other users

**Consider adding `[LEARN]` entries if:**
- [ ] You corrected a mistake that might recur
- [ ] You discovered a pattern applicable to similar projects
- [ ] You solved a problem through trial and error
- [ ] You received user feedback on approach or quality

Not every session needs entries — only capture reusable insights.

---

## Local-First Document Lookup

**ALWAYS check `master_supporting_docs/supporting_papers/` and `master_supporting_docs/supporting_slides/` BEFORE searching the web** for any paper, reference, or slide deck. Only go online if the document is not available locally.

## Quality Reports

Generated **only at merge time** -- not at every commit or PR.
Save to `quality_reports/merges/YYYY-MM-DD_[branch-name].md` using `templates/quality-report.md`.
