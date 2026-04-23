from __future__ import annotations

import argparse
import pathlib
import re
import shutil
import subprocess
import sys
from datetime import datetime
from typing import Iterable


COLOR_NAMES = ("red", "blue")
DIFF_HUNK_RE = re.compile(
    r"^@@ -(?P<old_start>\d+)(?:,(?P<old_count>\d+))? \+(?P<new_start>\d+)(?:,(?P<new_count>\d+))? @@"
)


def run(cmd: list[str], cwd: pathlib.Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )


def ignore_copy(_src: str, names: list[str]) -> set[str]:
    ignored = {
        "__pycache__",
        "build",
        "build_redline_20260420",
        "build_redline_overleaf_head",
    }
    ignored.update({name for name in names if name.startswith("build_verify")})
    return ignored


def find_matching_brace(text: str, open_brace_idx: int) -> int:
    depth = 0
    for idx in range(open_brace_idx, len(text)):
        char = text[idx]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return idx
    raise ValueError("Unbalanced braces while unwrapping textcolor")


def unwrap_textcolor(text: str, color: str) -> str:
    pattern = re.compile(rf"\\textcolor\s*\{{\s*{color}\s*\}}\s*\{{")
    while True:
        match = pattern.search(text)
        if not match:
            return text
        open_brace_idx = match.end() - 1
        close_brace_idx = find_matching_brace(text, open_brace_idx)
        inner = text[open_brace_idx + 1 : close_brace_idx]
        text = text[: match.start()] + inner + text[close_brace_idx + 1 :]


def strip_manual_markup_preserve_lines(text: str) -> str:
    for color in COLOR_NAMES:
        text = unwrap_textcolor(text, color)

    for color in COLOR_NAMES:
        text = re.sub(rf"\\begingroup\s*\\color\s*\{{{color}\}}", "", text)
        text = re.sub(rf"\\color\s*\{{{color}\}}", "", text)

    text = text.replace("\\endgroup", "")
    return text


def parse_changed_ranges(diff_text: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for line in diff_text.splitlines():
        match = DIFF_HUNK_RE.match(line)
        if not match:
            continue
        new_start = int(match.group("new_start"))
        new_count = int(match.group("new_count") or "1")
        if new_count == 0:
            continue
        ranges.append((new_start, new_start + new_count - 1))

    if not ranges:
        return []

    merged: list[tuple[int, int]] = [ranges[0]]
    for start, end in ranges[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end + 1:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))
    return merged


def apply_red_groups_by_line(text: str, ranges: Iterable[tuple[int, int]]) -> str:
    lines = text.splitlines(keepends=True)
    normalized_ranges: list[tuple[int, int]] = []

    for start, end in ranges:
        start_idx = max(start - 1, 0)
        end_idx = max(end - 1, -1)

        block = "".join(lines[start_idx : end_idx + 1])
        if "\\caption" in block:
            for probe_idx in range(end_idx + 1, min(end_idx + 4, len(lines) - 1) + 1):
                if "\\label{" in lines[probe_idx]:
                    end_idx = probe_idx
                    break

        normalized_ranges.append((start_idx + 1, end_idx + 1))

    inserts_before: dict[int, list[str]] = {}
    inserts_after: dict[int, list[str]] = {}

    for start, end in normalized_ranges:
        start_idx = max(start - 1, 0)
        end_idx = max(end - 1, -1)
        inserts_before.setdefault(start_idx, []).append("\\begingroup\\color{red}\n")
        inserts_after.setdefault(end_idx, []).append("\\endgroup\n")

    out: list[str] = []
    for idx, line in enumerate(lines):
        if idx in inserts_before:
            out.extend(inserts_before[idx])
        out.append(line)
        if idx in inserts_after:
            out.extend(inserts_after[idx])

    if not lines and 0 in inserts_before:
        out.extend(inserts_before[0])
        out.extend(inserts_after.get(-1, []))

    return "".join(out)


def build_redline(repo_root: pathlib.Path) -> pathlib.Path:
    source_root = repo_root / "0_clean"
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    build_root = repo_root / f"build_redline_overleaf_head_{stamp}"
    temp_src = build_root / "src"
    output_dir = temp_src / "build"
    shutil.copytree(source_root, temp_src, ignore=ignore_copy)

    changed = run(
        ["git", "diff", "--name-only", "HEAD", "--", "0_clean/*.tex", "0_clean/sections/*.tex"],
        cwd=repo_root,
    )
    if changed.returncode != 0:
        raise RuntimeError(changed.stderr.strip() or "Failed to list changed TeX files")

    changed_files = [line.strip() for line in changed.stdout.splitlines() if line.strip()]

    for tex_path in temp_src.rglob("*.tex"):
        original = tex_path.read_text(encoding="utf-8")
        sanitized = strip_manual_markup_preserve_lines(original)

        repo_rel = "0_clean/" + tex_path.relative_to(temp_src).as_posix()
        if repo_rel in changed_files:
            diff = run(["git", "diff", "--unified=0", "HEAD", "--", repo_rel], cwd=repo_root)
            if diff.returncode != 0:
                raise RuntimeError(diff.stderr.strip() or f"Failed to diff {repo_rel}")
            ranges = parse_changed_ranges(diff.stdout)
            sanitized = apply_red_groups_by_line(sanitized, ranges)

        tex_path.write_text(sanitized, encoding="utf-8", newline="\n")

    compile_cmd = [
        "latexmk",
        "-pdf",
        "-interaction=nonstopmode",
        "-file-line-error",
        "-outdir=build",
        "0_main.tex",
    ]
    compiled = run(compile_cmd, cwd=temp_src)
    sys.stdout.write(compiled.stdout)
    sys.stderr.write(compiled.stderr)
    if compiled.returncode != 0:
        raise RuntimeError("latexmk failed for Overleaf-head redline build")

    pdf_path = output_dir / "0_main.pdf"
    if not pdf_path.exists():
        raise RuntimeError("Expected redline PDF was not produced")
    return pdf_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a temporary redline PDF against Tariffs_ECB HEAD.")
    parser.add_argument(
        "--repo-root",
        default="master_supporting_docs/Tariffs_ECB",
        help="Path to the Tariffs_ECB repo root relative to the current working directory.",
    )
    args = parser.parse_args()

    repo_root = pathlib.Path(args.repo_root).resolve()
    pdf_path = build_redline(repo_root)
    print(f"\nBuilt PDF: {pdf_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
