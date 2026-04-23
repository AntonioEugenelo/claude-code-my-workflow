import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PAPER_ROOT = ROOT / "master_supporting_docs" / "Tariffs_ECB" / "0_clean"
MAIN_TEX = PAPER_ROOT / "0_main.tex"
OUTPUT_DIR = ROOT / "explorations" / "full_paper_mcms_audit" / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
NUMBER_RE = re.compile(r"(?<![A-Za-z])[-+]?\d+(?:\.\d+)?(?:\\%)?|\\d+(?:\.\d+)?")


def resolve_input(current_file: Path, target: str) -> Path:
    candidate = (current_file.parent / target).with_suffix(".tex")
    if candidate.exists():
        return candidate
    candidate = PAPER_ROOT / f"{target}.tex"
    if candidate.exists():
        return candidate
    raise FileNotFoundError(f"Could not resolve input {target!r} from {current_file}")


def expand_inputs(tex_path: Path, seen=None):
    if seen is None:
        seen = []
    if tex_path in seen:
        return []
    seen.append(tex_path)
    files = [tex_path]
    text = tex_path.read_text(encoding="utf-8", errors="replace")
    uncommented = "\n".join(line.split("%", 1)[0] for line in text.splitlines())
    for match in INPUT_RE.finditer(uncommented):
        target = match.group(1)
        child = resolve_input(tex_path, target)
        files.extend(expand_inputs(child, seen))
    return files


def is_candidate_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped or stripped.startswith("%"):
        return False
    if "\\cite" in stripped or "\\bibliograph" in stripped:
        return False
    if stripped.startswith("\\label") or stripped.startswith("\\ref") or stripped.startswith("\\input"):
        return False
    if stripped.startswith("\\begin{align}") or stripped.startswith("\\end{align}"):
        return False
    return bool(NUMBER_RE.search(stripped))


def extract_figures(text: str, path: Path):
    figures = []
    current = None
    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("\\begin{figure}"):
            current = {
                "file": str(path.relative_to(ROOT)).replace("\\", "/"),
                "begin_line": lineno,
                "image": None,
                "caption": None,
                "label": None,
            }
        elif current is not None and "\\includegraphics" in stripped:
            current["image"] = stripped
        elif current is not None and stripped.startswith("\\caption"):
            current["caption"] = stripped
        elif current is not None and stripped.startswith("\\label"):
            current["label"] = stripped
        elif current is not None and stripped.startswith("\\end{figure}"):
            current["end_line"] = lineno
            figures.append(current)
            current = None
    return figures


def main():
    active_files = expand_inputs(MAIN_TEX)
    active_files = [p for p in active_files if p.suffix == ".tex"]

    claims = []
    figures = []
    for path in active_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        for lineno, line in enumerate(text.splitlines(), start=1):
            if is_candidate_line(line):
                claims.append(
                    {
                        "file": str(path.relative_to(ROOT)).replace("\\", "/"),
                        "line": lineno,
                        "text": line.strip(),
                    }
                )
        figures.extend(extract_figures(text, path))

    out = {
        "main_tex": str(MAIN_TEX.relative_to(ROOT)).replace("\\", "/"),
        "active_files": [str(p.relative_to(ROOT)).replace("\\", "/") for p in active_files],
        "claim_count": len(claims),
        "figure_count": len(figures),
        "claims": claims,
        "figures": figures,
    }

    json_path = OUTPUT_DIR / "active_claim_inventory.json"
    json_path.write_text(json.dumps(out, indent=2), encoding="utf-8")

    md_lines = [
        "# Active Claim Inventory",
        "",
        f"- Main file: `{out['main_tex']}`",
        f"- Active files: `{len(active_files)}`",
        f"- Candidate numeric-claim lines: `{len(claims)}`",
        f"- Figure environments: `{len(figures)}`",
        "",
        "## Active Files",
        "",
    ]
    for rel in out["active_files"]:
        md_lines.append(f"- `{rel}`")
    md_lines.extend(["", "## Figures", ""])
    for fig in figures:
        md_lines.append(
            f"- `{fig['file']}:{fig['begin_line']}` | image: `{fig['image']}` | "
            f"caption: `{fig['caption']}` | label: `{fig['label']}`"
        )
    md_lines.extend(["", "## Candidate Numeric-Claim Lines", ""])
    for claim in claims:
        md_lines.append(f"- `{claim['file']}:{claim['line']}` {claim['text']}")

    (OUTPUT_DIR / "active_claim_inventory.md").write_text("\n".join(md_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
