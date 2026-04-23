# Capability Map

This file replaces Claude slash commands with Codex-native task recipes. Users can ask for these in plain language.

## Common Requests

| User Intent | Codex Procedure |
| --- | --- |
| Compile LaTeX | Identify the target `.tex`, run the appropriate LaTeX command, inspect log/output, and report blocking warnings and generated artifacts. |
| Proofread a file | Run the read-only `proofreader` review agent from `review-agents.md`, save findings to `quality_reports/` when needed, and avoid editing unless the user asked for fixes. |
| Review a letter | Use the routed read-only review agents from `review-routing.md`, ending with `cover-letter-reviewer`. Verify recipient facts and one-page constraints. |
| Review a paper | Use the routed read-only review agents from `review-routing.md`. Prefer findings-first output and use `review_plan.py` for deep or adversarial runs. |
| Review code or analysis | Use `code-critic` and `code-structurer` as read-only review agents. Focus on bugs, regressions, reproducibility, and replication clarity. |
| Translate Beamer to Quarto | Preserve source-of-truth in Beamer, translate slide-by-slide, convert citations and environments, then render and proofread the Quarto output. |
| Validate bibliography or citations | Cross-check citation keys against the bibliography files and flag missing, stale, or incorrect references. |
| Draft or revise a cover letter | Gather target context, fit evidence, and constraints; draft in LaTeX; then verify tone, facts, and page length. |
| Create lecture material | Plan first, establish structure, draft source slides, compile, then run narrative/domain/layout review. |
| Run data analysis | Inspect inputs, confirm assumptions, follow `working-conventions.md` and `style-guides.md`, run the analysis code, regenerate outputs, and summarize reproducibility status. |
| Deploy docs or rendered outputs | Render first, verify artifacts, then run the repo-specific sync or publish script if applicable. |
| Challenge an argument | Use the adversarial review loop in `adversarial-review.md` and add the read-only `devils-advocate` review agent after the baseline route. |
| Brainstorm research ideas | Read relevant supporting material, synthesize literature constraints, and propose testable questions with empirical strategies. |
| Conduct an interview-style elicitation | Ask a short sequence of targeted questions, summarize the answers, and turn them into a concrete brief or research plan. |
| Commit work | Confirm the diff, summarize what changed, and use non-interactive git commands. Do not stage secrets or unrelated local state. |
| Explore an idea or prototype | Work in `explorations/` first, use the fast-track rules in `working-conventions.md`, and only graduate the result after it clears the production bar. |
| Use my writing style | Apply the prose guidance in `style-guides.md`; use the Eugenelo voice only when the user explicitly asks for it or when revising matching prose. |
| Check a local paper or PDF claim | Look in `master_supporting_docs/` first, use local PDF extraction before web search, and document what source was checked. |

## Output Expectations

- For reviews, default to findings-first.
- For review tasks, keep review agents read-only and reserve edits for the main agent.
- For implementation tasks, default to execute rather than merely propose.
- For verification-heavy tasks, include the command or method used and whether it passed.
- For exploratory tasks, distinguish provisional results from production-ready outputs.
