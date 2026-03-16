# Infrastructure Manifest System

**Main branch = complete library. Feature branches = purpose-specific workspaces.**

Every branch inherits all infrastructure from main. On first use, a manifest file (`.claude/active-infrastructure.md`) declares what's active for that branch. Everything not listed is ignored — it stays on disk for clean merges from main, but Claude does not invoke it.

---

## How It Works

1. **Main branch has NO manifest.** Everything is active. Main is the canonical source.
2. **Feature branches have a manifest** at `.claude/active-infrastructure.md`.
3. **On first prompt of a new branch**, if no manifest exists, Claude asks the user what the branch is for and generates one from the template.
4. **The manifest controls:**
   - Which agents the orchestrator and agent-routing invoke
   - Which rules Claude follows (beyond core rules)
   - Which skills Claude suggests or runs

---

## Core Infrastructure (always active, every branch)

These are never listed in the manifest because they're always on:

### Core Rules
- `infrastructure-manifest.md` (this file)
- `orchestrator-protocol.md`
- `plan-first-workflow.md`
- `session-logging.md`
- `constitutional-governance.md`
- `agent-routing.md`
- `agent-learning.md`
- `troubleshooting-memory.md`
- `meta-governance.md`
- `pdf-processing.md`
- `exploration-fast-track.md`
- `exploration-folder-protocol.md`

### Core Agents
- `proofreader` (every document needs proofreading)

### Core Skills
- `commit`
- `proofread`
- `interview-me`
- `devils-advocate`
- `lit-review`
- `research-ideation`

---

## Manifest File Format

The manifest lives at `.claude/active-infrastructure.md` and uses this format:

```markdown
# Active Infrastructure

## Branch Purpose
[One sentence describing what this branch is for]

## Active Agents
[Only domain-specific agents — core agents are always active]
- agent-name-1
- agent-name-2

## Active Rules
[Only domain-specific rules — core rules are always active]
- rule-name-1
- rule-name-2

## Active Skills
[Only domain-specific skills — core skills are always active]
- skill-name-1
- skill-name-2
```

---

## Enforcement

### When invoking agents
Before running any agent (in orchestrator Step 3, in skills, or manually):
1. Check if `.claude/active-infrastructure.md` exists
2. If YES: only invoke agents listed in the manifest (plus core agents)
3. If NO (main branch or uninitialised): invoke any agent per agent-routing

### When following rules
Path-scoped rules auto-load by file pattern — the manifest cannot suppress them. But for always-on domain-specific rules (e.g., `beamer-quarto-sync.md`, `r-code-conventions.md`):
1. Check the manifest
2. If the rule is not listed and not in core: ignore it

### When suggesting skills
Only suggest or run skills that are in the manifest (plus core skills). Do not suggest `/compile-latex` on a cover-letter branch.

---

## Branch Initialisation

When Claude detects a new branch with no manifest (`.claude/active-infrastructure.md` does not exist and branch is not main):

1. Ask the user: "What is this branch for? (e.g., cover letter, lecture slides, research paper, journal review)"
2. Based on the answer, generate a manifest using the presets below
3. Save to `.claude/active-infrastructure.md`
4. Commit with message: "Initialise infrastructure manifest for [purpose]"

---

## Presets

### Cover Letter / Application
```
Agents: cover-letter-reviewer, domain-reviewer, narrative-reviewer
Rules: cover-letter-context, cover-letter-quality, cover-letter-verification, proofreading-protocol
Skills: compile-letter, draft-letter, review-letter
```

### Lecture Slides (Beamer)
```
Agents: slide-auditor, pedagogy-reviewer, narrative-reviewer, tikz-reviewer, beamer-translator, domain-reviewer
Rules: beamer-quarto-sync, no-pause-beamer, quality-gates, tikz-visual-quality, single-source-of-truth, verification-protocol
Skills: compile-latex, create-lecture, slide-excellence, extract-tikz, pedagogy-review, validate-bib
```

### Research Paper (Theory)
```
Agents: derivation-auditor, theory-critic, narrative-reviewer, domain-reviewer
Rules: quality-gates, single-source-of-truth, verification-protocol, replication-protocol
Skills: compile-latex, review-paper, validate-bib
```

### Research Paper (Empirical / R)
```
Agents: r-reviewer, narrative-reviewer, domain-reviewer
Rules: r-code-conventions, quality-gates, replication-protocol, single-source-of-truth
Skills: compile-latex, data-analysis, review-r, review-paper, validate-bib
```

### Quarto Site / Documentation
```
Agents: quarto-critic, quarto-fixer, narrative-reviewer
Rules: beamer-quarto-sync, quality-gates, knowledge-base-template
Skills: qa-quarto, translate-to-quarto, deploy
```

### Journal Peer Review
```
Agents: narrative-reviewer, domain-reviewer, derivation-auditor
Rules: quality-gates
Skills: review-paper
```

### Mixed / Custom
User specifies manually. Claude suggests based on file patterns found in the branch.

---

## Updating the Manifest

- **Adding infrastructure:** User says "I also need the R reviewer" → add `r-reviewer` to agents list
- **Removing infrastructure:** User says "drop the TikZ reviewer" → remove from list
- **Resetting:** Delete `.claude/active-infrastructure.md` → everything active (like main)

---

## Merging from Main

When main gets new agents/rules/skills:
1. Merge main into branch — new files arrive on disk
2. Manifest is unchanged — new infrastructure is inactive by default
3. User or Claude adds relevant new items to the manifest if needed

This is why we never delete files on branches — clean merges always work.
