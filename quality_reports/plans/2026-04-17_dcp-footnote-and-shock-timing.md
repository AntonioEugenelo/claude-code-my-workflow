Status: In progress

Task: verify the DCP literature footnote references, remove the final sentence from that footnote, and update Section 4.1 to state the tariff-shock timing if supported by the model code.

Scope:
- Check the DCP literature footnote in `sections/12_related_literature.tex` against the bibliography entries and local manuscript references.
- Remove the sentence "We embed these insights into a production network framework by comparing DCP and PCP regimes across 44 sectors."
- Inspect the MCMS tariff-shock process to confirm whether the tariff shock is held constant for 12 quarters and then allowed to decline.
- Update the Section 4.1 text in `sections/55a_benchmark_and_robustness.tex` only if the model code supports that timing description.
- Recompile the manuscript and record the verification result.

Likely files:
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/12_related_literature.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib`
- `master_supporting_docs/MCMS/...` relevant tariff-shock declaration or calibration files
- `quality_reports/session_logs/2026-04-17_dcp-footnote-and-shock-timing.md`

Verification:
- Cross-check cited keys and bibliographic metadata locally.
- Inspect the model code path governing tariff persistence / timing.
- Rebuild `0_main.tex` in a fresh verification directory.

Assumptions:
- "Check that all the references are correct" means verify the citation keys and cited-paper identities in the DCP footnote, not run a broader external literature review.
- If the model does not support a literal "constant for the first 12 quarters" statement, revise the prose to match the actual shock law rather than forcing that wording.
