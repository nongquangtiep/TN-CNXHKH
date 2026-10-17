import docx
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table
import re

doc = docx.Document('CHỦ NGHĨA XH-KH.docx')

elements = []
for child in doc.element.body:
    if isinstance(child, CT_P):
        p = Paragraph(child, doc)
        elements.append(('P', p))
    elif isinstance(child, CT_Tbl):
        t = Table(child, doc)
        elements.append(('T', t))

with open('elements_detailed.txt', 'w', encoding='utf-8') as f:
    current_lesson = "Unknown"
    for idx, (etype, elem) in enumerate(elements):
        if etype == 'P':
            text = elem.text.strip()
            if not text:
                continue
            if re.search(r'^(BÀI|Bài|Chương|CHƯƠNG)\s+\d+', text, re.IGNORECASE):
                current_lesson = text
                f.write(f"\n=================== {text} ===================\n")
            elif re.search(r'^(Câu|CÂU)\s+\d+', text, re.IGNORECASE):
                f.write(f"\n--- [{idx:04d}] ({current_lesson}) {text}\n")
            else:
                # check runs for red color or formatting
                runs_info = []
                for r in elem.runs:
                    mods = []
                    if r.bold: mods.append('B')
                    if r.underline: mods.append('U')
                    if r.font.color and r.font.color.rgb:
                        mods.append(f'C:{r.font.color.rgb}')
                    if r.font.highlight_color:
                        mods.append(f'H:{r.font.highlight_color}')
                    if mods:
                        runs_info.append(f"[{','.join(mods)}: {r.text}]")
                f.write(f"    P: {text}")
                if runs_info:
                    f.write(f"  --> {' '.join(runs_info)}")
                f.write("\n")
        elif etype == 'T':
            f.write(f"\n    [TABLE {idx:04d}] {len(elem.rows)}x{len(elem.columns)}\n")
            for r_i, row in enumerate(elem.rows):
                row_str = []
                for c_i, cell in enumerate(row.cells):
                    c_runs = []
                    for p in cell.paragraphs:
                        for r in p.runs:
                            if r.font.color and r.font.color.rgb:
                                c_runs.append(f"C:{r.font.color.rgb}")
                    c_txt = cell.text.strip().replace('\n', ' ')
                    if c_runs:
                        c_txt += f" ({','.join(c_runs)})"
                    row_str.append(c_txt)
                f.write(f"      Row {r_i}: {' | '.join(row_str)}\n")

print("Saved detailed elements to elements_detailed.txt")
