import docx
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.text.paragraph import Paragraph
from docx.table import Table

doc = docx.Document('CHỦ NGHĨA XH-KH.docx')

elements = []
for child in doc.element.body:
    if isinstance(child, CT_P):
        p = Paragraph(child, doc)
        elements.append(('P', p))
    elif isinstance(child, CT_Tbl):
        t = Table(child, doc)
        elements.append(('T', t))

print(f"Total elements: {len(elements)}")

with open('elements_flow.txt', 'w', encoding='utf-8') as out:
    for idx, (etype, elem) in enumerate(elements):
        if etype == 'P':
            text = elem.text.strip()
            if text:
                out.write(f"[{idx:04d}] P: {text[:120]}\n")
        elif etype == 'T':
            out.write(f"[{idx:04d}] === TABLE ({len(elem.rows)}x{len(elem.columns)}) ===\n")
            for r_i, row in enumerate(elem.rows):
                row_txt = [c.text.strip().replace('\n', ' ') for c in row.cells]
                out.write(f"       R{r_i}: {' | '.join(row_txt)}\n")

print("Saved elements flow to elements_flow.txt")
