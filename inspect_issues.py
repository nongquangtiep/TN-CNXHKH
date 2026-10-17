from group_questions import questions_raw

target_questions = [
    ('Bài 1', '34'),
    ('Bài 2', '15'),
    ('Bài 4', '1'),
    ('Bài 4', '21'),
    ('Bài 4', '22'),
    ('Bài 4', '23'),
    ('Bài 4', '24'),
    ('Bài 4', '25'),
    ('Bài 4', '34'),
    ('Bài 4', '35'),
    ('Bài 5', '17'),
]

with open('issue_questions_inspection.txt', 'w', encoding='utf-8') as out:
    for q in questions_raw:
        for l, qn in target_questions:
            if q['lesson'] == l and q['q_num'] == qn:
                out.write(f"\n============================================\n")
                out.write(f"[{q['lesson']}] Câu {q['q_num']}: {q['title']}\n")
                out.write(f"Start idx in doc: {q['start_idx']}\n")
                out.write(f"Elements count: {len(q['elements'])}\n")
                for etype, elem in q['elements']:
                    if etype == 'P':
                        mods = []
                        for r in elem.runs:
                            m = []
                            if r.bold: m.append('B')
                            if r.underline: m.append('U')
                            if r.font.color and r.font.color.rgb: m.append(f'C:{r.font.color.rgb}')
                            if r.font.highlight_color: m.append(f'H:{r.font.highlight_color}')
                            mods.append(f"[{','.join(m)}: '{r.text}']")
                        out.write(f"   P: '{elem.text}' -> {' '.join(mods)}\n")
                    elif etype == 'T':
                        out.write(f"   TABLE {len(elem.rows)}x{len(elem.columns)}\n")
                        for r in elem.rows:
                            out.write(f"     Row: {' | '.join(c.text.strip().replace(chr(10), ' ') for c in r.cells)}\n")

print("Saved to issue_questions_inspection.txt")
