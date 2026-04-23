## Requirements Note: EA Sectoral Overleaf Sync And Cleanup

### MUST

- Pull the full manuscript from Overleaf into the local `Tariffs_ECB` repo.
- Add an EA bilateral sectoral exports/imports figure grounded in the model output and code.
- Use the new figure to complete the EA subsection of the sectoral-dimension section in the active manuscript.
- Move unused sections and assets into an `old/` directory without breaking the active build.

### SHOULD

- Preserve prior local derived artifacts by backing them up if they block the pull.
- Keep the figure and text tightly aligned with the model’s trade-accounting notation.
- Leave the active manuscript structure cleaner and easier to navigate after the cleanup.

### MAY

- Add a scoped verification wrapper if the full manuscript compile remains blocked by unrelated missing assets.
- Preserve notes on which archived files were unused and why.

### CLEAR

- The user wants a full Overleaf pull first.
- The user wants a new EA trade-margin figure and matching subsection text.
- The user wants unused manuscript material archived into `old/`.

### ASSUMED

- "Unused" is determined by the active `0_main.tex` include graph and active figure references after the pull.
- The EA figure should emphasize bilateral sectoral exports and imports margins by partner because that is the missing accounting object discussed in the text.

### BLOCKED

- None at the outset; any blockers should be discovered from the pull, figure pipeline, or compile stage.
