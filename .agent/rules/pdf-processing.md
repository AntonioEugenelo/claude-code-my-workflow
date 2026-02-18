---
description: Always check master_supporting_docs/ for papers and slides before searching online. Use PyMuPDF for PDF extraction.
---

# Robust PDF Processing

## Local-First Principle

**ALWAYS check `master_supporting_docs/supporting_papers/` and `master_supporting_docs/supporting_slides/` BEFORE searching the web.** These folders contain the authoritative copies of papers and slides. Only go online if the file is not available locally or if you need supplementary information not in the local copy.

## Preferred PDF Text Extraction: PyMuPDF (fitz)

This machine has **PyMuPDF** (`import fitz`) and **pypdf** installed. Use PyMuPDF for text extraction — it handles academic PDFs well and preserves structure.

```python
import fitz, sys, io, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
doc = fitz.open(r'path/to/paper.pdf')
for i in range(min(25, len(doc))):
    text = doc[i].get_text()
    print(f'=== PAGE {i+1} ===')
    print(text[:3000])
doc.close()
```

**Important notes:**
- Always set `encoding='utf-8', errors='replace'` on stdout (Windows cp1252 fails on academic Unicode)
- Use `glob.glob()` for filenames with special characters (e.g., umlauts: Müller)
- Process 20-30 pages at a time to stay within output limits
- The `Read` tool's built-in PDF reader requires `pdftoppm` which is NOT installed on this machine

## The Safe Processing Workflow

**Step 1: Check Local Files First**
- Look in `master_supporting_docs/supporting_papers/` and `supporting_slides/`
- Use `Glob` tool to find papers by partial name match

**Step 2: Extract Text with PyMuPDF**
- Use the Python snippet above via Bash tool
- Adjust page range as needed for the specific verification task

**Step 3: Process Selectively**
- Extract key information from relevant sections
- For claim verification: target abstract, results sections, and tables
- Don't try to hold all pages in working memory

**Step 4: Only Go Online If Needed**
- If the paper is not in supporting docs, THEN use WebSearch/WebFetch
- If you need supplementary materials or appendices not in the local PDF

## Error Handling Protocol

**If PyMuPDF fails:**
1. Check the file path (use `glob.glob()` for special characters)
2. Try `pypdf` as fallback: `from pypdf import PdfReader`
3. If encoding issues persist, ensure `errors='replace'` is set

**If the PDF is not in supporting docs:**
1. Ask the user if they have the paper
2. Search online as last resort
3. Document what you found and where

