import re
from group_questions import questions_raw

with open('tf_and_drag_analysis.txt', 'w', encoding='utf-8') as out:
    for q in questions_raw:
        title = q['title']
        has_table = any(e[0] == 'T' for e in q['elements'])
        is_drag = bool(re.search(r'kéo\s*thả|khớp\s*với|ghép|cột\s*tương\s*ứng', title, re.IGNORECASE))
        is_tf = bool(re.search(r'đúng\s*(hoặc|\/)\s*sai', title, re.IGNORECASE))
        
        if is_tf or has_table or is_drag:
            out.write(f"\n========================================\n")
            out.write(f"[{q['lesson']}] Câu {q['q_num']}: {title}\n")
            out.write(f"Type hints: is_tf={is_tf}, has_table={has_table}, is_drag={is_drag}\n")
            for etype, elem in q['elements']:
                if etype == 'P':
                    runs_desc = []
                    for r in elem.runs:
                        c = r.font.color.rgb if r.font.color else None
                        runs_desc.append(f"'{r.text}'(c={c},b={r.bold})")
                    out.write(f"   P: '{elem.text}' -> {' '.join(runs_desc)}\n")
                elif etype == 'T':
                    out.write(f"   TABLE {len(elem.rows)}x{len(elem.columns)}:\n")
                    for r in elem.rows:
                        out.write(f"     Row: {' | '.join(c.text.strip().replace(chr(10), ' ') for c in r.cells)}\n")

print("Saved tf and drag analysis.")
