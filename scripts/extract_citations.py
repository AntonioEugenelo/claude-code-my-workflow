import fitz  # PyMuPDF
import fitz
import os

files_to_check = [
    r"c:\Users\raffa\OneDrive - Nexus365\Desktop\Teaching\Presentation\workshop-presentation\master_supporting_docs\supporting_papers\2025_Antonova_Müller_NK-Network-Targeted-Taxes.pdf",
    r"c:\Users\raffa\OneDrive - Nexus365\Desktop\Teaching\Presentation\workshop-presentation\master_supporting_docs\supporting_papers\Missing_Tax_Instruments_LaO_Tahbaz-Salehi_2024_WP.pdf"
]

def extract_text(pdf_path, pages=5):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for i in range(min(len(doc), pages)):
            text += doc[i].get_text()
        return text
    except Exception as e:
        return str(e)

with open("paper_content.txt", "w", encoding="utf-8") as outfile:
    for f in files_to_check:
        outfile.write(f"--- FILE: {os.path.basename(f)} ---\n")
        outfile.write(extract_text(f, 6)) # Read first 6 pages (abstract + intro)
        outfile.write("\n" + "="*50 + "\n")
