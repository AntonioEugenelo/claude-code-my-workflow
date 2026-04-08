# Capability Map

This file replaces Claude slash commands with Codex-native task recipes. Users can ask for these in plain language.

## Common Requests

| User Intent | Codex Procedure |
| --- | --- |
| Compile LaTeX | Identify the target `.tex`, run the appropriate LaTeX command, inspect log/output, and report blocking warnings and generated artifacts. |
| Proofread a file | Run the `proofreader` lens from `review-routing.md`, save findings to `quality_reports/`, and avoid editing unless the user asked for fixes. |
| Review a letter | Use proofreader, domain, narrative, and letter-quality lenses. Verify recipient facts and one-page constraints. |
| Review a paper | Use proofreader, derivation, figure-consistency, theory, and narrative lenses. Prefer findings-first output. |
| Review code or analysis | Use correctness, structure, and reproducibility lenses. Focus on bugs, regressions, and missing checks. |
| Translate Beamer to Quarto | Preserve source-of-truth in Beamer, translate slide-by-slide, convert citations and environments, then render and proofread the Quarto output. |
| Validate bibliography or citations | Cross-check citation keys against the bibliography files and flag missing, stale, or incorrect references. |
| Draft or revise a cover letter | Gather target context, fit evidence, and constraints; draft in LaTeX; then verify tone, facts, and page length. |
| Create lecture material | Plan first, establish structure, draft source slides, compile, then run narrative/domain/layout review. |
| Run data analysis | Inspect inputs, confirm assumptions, run the analysis code, regenerate outputs, and summarize reproducibility status. |
| Deploy docs or rendered outputs | Render first, verify artifacts, then run the repo-specific sync or publish script if applicable. |
| Challenge an argument | Use a devil's-advocate pass that looks for weak assumptions, omitted alternatives, and evidence gaps. |
| Brainstorm research ideas | Read relevant supporting material, synthesize literature constraints, and propose testable questions with empirical strategies. |
| Conduct an interview-style elicitation | Ask a short sequence of targeted questions, summarize the answers, and turn them into a concrete brief or research plan. |
| Commit work | Confirm the diff, summarize what changed, and use non-interactive git commands. Do not stage secrets or unrelated local state. |

## Output Expectations

- For reviews, default to findings-first.
- For implementation tasks, default to execute rather than merely propose.
- For verification-heavy tasks, include the command or method used and whether it passed.
- For exploratory tasks, distinguish provisional results from production-ready outputs.
