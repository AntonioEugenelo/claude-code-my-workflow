# Session Log: Invoicing Wording And Red Cleanup

Date: 2026-04-20

Request
- Replace mentions of `heterogeneous DCP` / `Het DCP` with `heterogeneous invoicing`.
- Remove red text formatting from accepted manuscript changes associated with the current paper revision.

Files Updated
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/11_introduction.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex`

Verification
- Rebuilt `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `pdflatex -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Searched the live `0_clean/**/*.tex` tree for stale `heterogeneous DCP` / `Het DCP` wording.
- Searched section files for residual `\textcolor{red}` / `\color{red}` markup.

Outcome
- Live manuscript now uses `heterogeneous invoicing` instead of the old label in the active prose.
- Red formatting was removed from accepted prose in the edited section files.
- The only remaining `\textcolor{red}` occurrence in `0_clean/sections` is the note macro definition in `01_preamble.tex`.
