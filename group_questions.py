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

# Group elements by question
questions_raw = []
current_lesson = "BÀI 1"
current_q = None

for idx, (etype, elem) in enumerate(elements):
    if etype == 'P':
        text = elem.text.strip()
        if not text:
            continue
        lesson_match = re.search(r'^(BÀI|Bài|Chương|CHƯƠNG)\s+(\d+)', text, re.IGNORECASE)
        if lesson_match:
            current_lesson = f"Bài {lesson_match.group(2)}"
            continue
        
        q_match = re.search(r'^(Câu|CÂU)\s+(\d+)\s*[:.]?\s*(.*)', text, re.IGNORECASE)
        if q_match:
            if current_q:
                questions_raw.append(current_q)
            current_q = {
                'lesson': current_lesson,
                'q_num': q_match.group(2),
                'title': text,
                'elements': [],
                'start_idx': idx
            }
        else:
            if current_q:
                current_q['elements'].append(('P', elem))
    elif etype == 'T':
        if current_q:
            current_q['elements'].append(('T', elem))
        else:
            print(f"Table at idx {idx} with no question!")

if current_q:
    questions_raw.append(current_q)

print(f"Total raw questions extracted: {len(questions_raw)}")

# Breakdown by lesson
by_lesson = {}
for q in questions_raw:
    by_lesson.setdefault(q['lesson'], []).append(q)

for lesson, qlist in by_lesson.items():
    print(f"  {lesson}: {len(qlist)} questions")

with open('all_questions_summary.txt', 'w', encoding='utf-8') as f:
    for q in questions_raw:
        f.write(f"\n========================================\n")
        f.write(f"[{q['lesson']}] Câu {q['q_num']}: {q['title']}\n")
        for etype, elem in q['elements']:
            if etype == 'P':
                # find red runs
                reds = []
                for r in elem.runs:
                    if r.font.color and r.font.color.rgb:
                        reds.append(f"{r.font.color.rgb}:{r.text}")
                f.write(f"   P: {elem.text.strip()}")
                if reds:
                    f.write(f"  [COLOR: {' | '.join(reds)}]")
                f.write("\n")
            elif etype == 'T':
                f.write(f"   TABLE {len(elem.rows)}x{len(elem.columns)}:\n")
                for r_idx, row in enumerate(elem.rows):
                    row_txt = []
                    for cell in row.cells:
                        c_reds = []
                        for p in cell.paragraphs:
                            for r in p.runs:
                                if r.font.color and r.font.color.rgb:
                                    c_reds.append(f"{r.font.color.rgb}:{r.text}")
                        c_str = cell.text.strip().replace('\n', ' ')
                        if c_reds:
                            c_str += f" [RED: {' | '.join(c_reds)}]"
                        row_txt.append(c_str)
                    f.write(f"     R{r_idx}: {' | '.join(row_txt)}\n")

print("Saved all questions summary to all_questions_summary.txt")
