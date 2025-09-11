from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from zipfile import ZipFile
import xml.etree.ElementTree as ET


def load_shared_strings(zf: ZipFile) -> List[str]:
    try:
        with zf.open("xl/sharedStrings.xml") as f:
            tree = ET.parse(f)
        return ["".join(si.itertext()) for si in tree.getroot().iterfind(".//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si")]
    except KeyError:
        return []


def cell_ref_to_col_idx(ref: str) -> int:
    col_letters = ''.join([c for c in ref if c.isalpha()])
    col_idx = 0
    for ch in col_letters:
        col_idx = col_idx * 26 + (ord(ch) - ord('A') + 1)
    return col_idx - 1


def read_sheet_matrix(xlsx_path: Path, max_rows: int = 1000, max_cols: int = 30) -> List[List[str]]:
    with ZipFile(xlsx_path) as zf:
        shared = load_shared_strings(zf)
        with zf.open("xl/worksheets/sheet1.xml") as f:
            tree = ET.parse(f)
        ns = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        rows = tree.getroot().findall(".//s:sheetData/s:row", ns)
        matrix: List[List[str]] = []
        for r in rows[:max_rows]:
            row_vec = [""] * max_cols
            for c in r.findall("s:c", ns):
                ref = c.attrib.get("r", "A1")
                t = c.attrib.get("t")
                v = c.find("s:v", ns)
                text = ""
                if v is not None and v.text is not None:
                    if t == "s":
                        try:
                            idx = int(v.text)
                            text = shared[idx] if 0 <= idx < len(shared) else ""
                        except ValueError:
                            text = v.text
                    else:
                        text = v.text
                col = cell_ref_to_col_idx(ref)
                if 0 <= col < max_cols:
                    row_vec[col] = text
            matrix.append(row_vec)
        return matrix


@dataclass
class DataRow:
    group: str
    library: str
    url: str
    platform: str


@dataclass
class VersionData:
    label: str
    browse_url: Optional[str] = None
    raw_rows: List[DataRow] = field(default_factory=list)
    bam_rows: List[DataRow] = field(default_factory=list)
    genome_links: List[tuple[str, str]] = field(default_factory=list)  # (type, url)


def normalize_label(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def parse_matrix(matrix: List[List[str]]) -> Dict[str, VersionData]:
    versions: Dict[str, VersionData] = {}
    current_version: Optional[str] = None
    current_group: str = ""
    in_bam_section = False
    in_genome_section = False

    for row in matrix:
        a, b, c, d = (row + ["", "", "", ""])[:4]
        a = normalize_label(a)
        b = normalize_label(b)
        c = normalize_label(c)
        d = normalize_label(d)

        if a in {"v1.1", "v2.0"}:
            current_version = a
            versions.setdefault(current_version, VersionData(label=current_version))
            current_group = ""
            in_bam_section = False
            in_genome_section = False
            continue

        if not current_version:
            continue

        if a.startswith("raw sequencing data for T2T-YAO"):
            versions[current_version].browse_url = c or None
            current_group = "YAO"
            in_bam_section = False
            in_genome_section = False
            continue

        if a.startswith("BAM alignment files for T2T-YAO"):
            in_bam_section = True
            in_genome_section = False
            # Treat header row as the first BAM entry if it contains data
            if b or c:
                versions[current_version].bam_rows.append(
                    DataRow(group=b or current_group, library=b or "", url=c, platform="")
                )
                current_group = b or current_group
            else:
                current_group = b or current_group
            continue

        if a.startswith("T2T-YAO") and a.endswith("genome"):
            in_bam_section = False
            in_genome_section = True
            if b or c:
                versions[current_version].genome_links.append((b or "", c))
            continue

        # Continuation lines of the genome section usually have empty column A
        if in_genome_section and not a and (b or c):
            versions[current_version].genome_links.append((b or "", c))
            continue

        if a:
            current_group = a
            # leaving genome section if a new header/group appears
            in_genome_section = False

        if b and c:
            data_row = DataRow(group=current_group or "", library=b, url=c, platform=d)
            if in_bam_section:
                versions[current_version].bam_rows.append(data_row)
            else:
                versions[current_version].raw_rows.append(data_row)

    return versions


def md_link(url: str, label: Optional[str] = None) -> str:
    if not url:
        return ""
    text = label if label else url
    return f"[{text}]({url})"


def render_markdown(versions: Dict[str, VersionData]) -> str:
    lines: List[str] = []
    lines.append("## T2T-YAO resources")
    lines.append("")
    lines.append("This README is auto-generated from `data-NGDC.xlsx`. Modeled after the structure of the public project `T2T-MMU8`.")
    lines.append("")
    lines.append("Reference: see the style of `T2T-MMU8` README at "
                 "[`http://43.128.62.24:91/zhang-shilong/T2T-MMU8?tab=readme-ov-file`](http://43.128.62.24:91/zhang-shilong/T2T-MMU8?tab=readme-ov-file).")
    lines.append("")

    for version_label in ["v1.1", "v2.0"]:
        if version_label not in versions:
            continue
        v = versions[version_label]
        lines.append(f"### {v.label}")
        lines.append("")
        # 1) Genome first
        if v.genome_links:
            lines.append("- **Genome assemblies**:")
            for t, url in v.genome_links:
                label = t if t else "assembly"
                lines.append(f"  - {label}: {md_link(url, 'FASTA')} ")
            lines.append("")

        # 2) Raw data second
        if v.browse_url:
            lines.append(f"- **Raw sequencing data portal**: {md_link(v.browse_url)}")
            lines.append("")

        if v.raw_rows:
            lines.append("- **Raw sequencing data details**:")
            lines.append("")
            lines.append("  | Group | Library | Platform | URL |")
            lines.append("  | --- | --- | --- | --- |")
            for r in v.raw_rows:
                lines.append(f"  | {r.group} | {r.library} | {r.platform} | {md_link(r.url, 'download')} |")
            lines.append("")

        # 3) v2.0 only: BAMs (three entries)
        if version_label == "v2.0" and v.bam_rows:
            lines.append("- **BAM alignment files**:")
            lines.append("")
            lines.append("  | Group | Library | URL |")
            lines.append("  | --- | --- | --- |")
            for r in v.bam_rows:
                lines.append(f"  | {r.group} | {r.library} | {md_link(r.url, 'download')} |")
            lines.append("")

    # Footer sections
    lines.append("### Issues")
    lines.append("")
    lines.append("Please report problems or requests via GitHub Issues.")
    lines.append("")
    lines.append("### License")
    lines.append("")
    lines.append("Unless noted otherwise, data links are from public archives. If you need a specific license statement, add it here (e.g., CC0-1.0).")
    lines.append("")
    lines.append("### Citation")
    lines.append("")
    lines.append("If you use T2T-YAO resources, please acknowledge this repository and the original data providers.")
    lines.append("")
    lines.append("### Changelog")
    lines.append("")
    lines.append("- 2025-08: T2T-YAO v2.0 release")
    lines.append("- 2023-08: T2T-YAO v1.1 release")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("Auto-generated from `data-NGDC.xlsx`. Regenerate by running `scripts/generate_readme_from_ngdc_xlsx.py`.")
    return "\n".join(lines)


def main() -> None:
    excel_path = Path(__file__).resolve().parents[1] / "data-NGDC.xlsx"
    matrix = read_sheet_matrix(excel_path)
    versions = parse_matrix(matrix)
    md = render_markdown(versions)
    out_path = Path(__file__).resolve().parents[1] / "README.md"
    out_path.write_text(md, encoding="utf-8")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()


