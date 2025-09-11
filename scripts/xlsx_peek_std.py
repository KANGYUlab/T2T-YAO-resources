import sys
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as ET


def load_shared_strings(zf: ZipFile):
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


def read_sheet_matrix(xlsx_path: Path, max_rows: int = 500, max_cols: int = 30):
    with ZipFile(xlsx_path) as zf:
        shared = load_shared_strings(zf)
        with zf.open("xl/worksheets/sheet1.xml") as f:
            tree = ET.parse(f)
        ns = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
        rows = tree.getroot().findall(".//s:sheetData/s:row", ns)
        matrix = []
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


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python xlsx_peek_std.py <excel_path>")
        sys.exit(1)
    excel_path = Path(sys.argv[1]).expanduser().resolve()
    matrix = read_sheet_matrix(excel_path)
    for i, row in enumerate(matrix[:200], start=1):
        print(f"{i}\t" + " | ".join(row[:12]))


if __name__ == "__main__":
    main()


