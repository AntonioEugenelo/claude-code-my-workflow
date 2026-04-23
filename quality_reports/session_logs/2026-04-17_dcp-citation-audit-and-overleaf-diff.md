# 2026-04-17 DCP citation audit and Overleaf diff

## Scope

- Audited the DCP literature footnote citations against the cited papers online.
- Corrected bibliography metadata where the local entry was inaccurate.
- Recompiled the manuscript.
- Compared the current local manuscript against `overleaf/master` and isolated the non-color differences.

## Online citation audit

- `Gopinath2020` matches the AEA article "Dominant Currency Paradigm" in *American Economic Review* 110(3): 677--719, but the local author list was wrong.
  Source: https://www.aeaweb.org/articles?id=10.1257/aer.20171201
- `mukhin2023` matches the AEA article "Optimal Policy under Dollar Pricing" in *American Economic Review* 113(7): 1783--1824.
  Source: https://www.aeaweb.org/articles?id=10.1257/aer.20200636
- `devereux2003` matches the *Review of Economic Studies* article "Monetary Policy in the Open Economy Revisited: Price Setting and Exchange-Rate Flexibility" 70(4): 765--783.
  Source: https://academic.oup.com/restud/article/70/4/765/1521105

## File changes

- `master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib`
  - Normalized `mukhin2023` page range to `1783--1824`.
  - Corrected `Gopinath2020` authors to `Gopinath, Boz, Casas, Díez, Gourinchas, Plagborg-Moeller`.
  - Kept `Plagborg-Moeller` as ASCII because this LaTeX/BibTeX pipeline previously failed on `ø` in the bibliography output.
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/12_related_literature.tex`
  - Removed the final sentence from the DCP footnote.
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
  - Added the sentence stating that the benchmark tariff shock follows an AR(1) process with `rho_tau = 0.96` and decays over the 12-quarter horizon.

## Overleaf comparison

`./scripts/sync-overleaf.sh status` reported:

- Local: `1be6ee4d23ec0bddb40c32e49a2acd35cdbf761e`
- GitHub: `1be6ee4d23ec0bddb40c32e49a2acd35cdbf761e`
- Overleaf: `1be6ee4d23ec0bddb40c32e49a2acd35cdbf761e`
- Status: `ALL IN SYNC`

Non-color differences remaining versus `overleaf/master`:

- Title page title and author block edits in `02_title_page.tex`.
- DCP footnote final sentence removed in `12_related_literature.tex`.
- New AR(1) shock sentence in `55a_benchmark_and_robustness.tex`.
- Two bibliography metadata corrections in `bibliography.bib`.
- Local-only untracked artifacts under `0_clean/` such as verification PDFs, `build_verify*`, `__pycache__/`, and the `horse_race_*.py` files.

## Verification

Ran:

- `pdflatex -interaction=nonstopmode -halt-on-error -jobname=0_main_verify_20260417 -output-directory=build_verify_20260417 0_main.tex`
- `bibtex build_verify_20260417/0_main_verify_20260417`
- `pdflatex -interaction=nonstopmode -halt-on-error -jobname=0_main_verify_20260417 -output-directory=build_verify_20260417 0_main.tex`
- `pdflatex -interaction=nonstopmode -halt-on-error -jobname=0_main_verify_20260417 -output-directory=build_verify_20260417 0_main.tex`

Verified output:

- `master_supporting_docs/Tariffs_ECB/0_clean/build_verify_20260417/0_main_verify_20260417.pdf`

Remaining warnings were non-blocking:

- TinyTeX duplicate fontmap warnings
- `microtype` footnote patch warning
- two `Hfootnote` destination warnings
