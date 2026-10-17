import json
import re

from group_questions import questions_raw

stats = {
    'single_choice': 0,
    'multiple_choice': 0,
    'true_false': 0,
    'drag_drop': 0,
    'unknown': 0
}

issues = []
details = []

for q in questions_raw:
    title = q['title']
    elements = q['elements']
    lesson = q['lesson']
    q_num = q['q_num']
    
    # Check if table present
    has_table = any(e[0] == 'T' for e in elements)
    is_drag_drop_title = bool(re.search(r'kéo\s*thả|khớp\s*với|ghép|cột\s*tương\s*ứng', title, re.IGNORECASE))
    is_tf_title = bool(re.search(r'đúng\s*(hoặc|\/)\s*sai', title, re.IGNORECASE))
    is_multi_title = bool(re.search(r'chọn\s*[2345]\s*(đáp\s*án|phương\s*án)', title, re.IGNORECASE))
    
    # Check options A, B, C, D
    option_paras = []
    
    for etype, elem in elements:
        if etype == 'P':
            ptxt = elem.text.strip()
            if re.match(r'^[A-D]\s*[\.\:]', ptxt):
                is_correct = False
                for r in elem.runs:
                    if r.font.color and r.font.color.rgb:
                        rgb_hex = f"{r.font.color.rgb}".upper()
                        # Red colors
                        if any(rgb_hex.startswith(c) for c in ['EE', 'FF', 'C0', 'ED', 'E5', 'CC']):
                            is_correct = True
                    # Also check underline if used for answer
                    if r.underline:
                        # only if not entire question
                        pass
                option_paras.append((ptxt, is_correct))
    
    if has_table:
        stats['drag_drop'] += 1
        details.append(f"[{lesson} Q{q_num}] TYPE: drag_drop (table)")
    elif is_drag_drop_title:
        stats['drag_drop'] += 1
        details.append(f"[{lesson} Q{q_num}] TYPE: drag_drop (no table)")
        issues.append(f"{lesson} Q{q_num} (DragDrop without table): Title: {title}")
    elif is_tf_title:
        stats['true_false'] += 1
        details.append(f"[{lesson} Q{q_num}] TYPE: true_false")
    elif is_multi_title:
        stats['multiple_choice'] += 1
        correct_opts = [opt for opt, corr in option_paras if corr]
        details.append(f"[{lesson} Q{q_num}] TYPE: multiple_choice (correct: {len(correct_opts)})")
        if len(correct_opts) < 2:
            issues.append(f"{lesson} Q{q_num} (Multi): found {len(correct_opts)} correct answers in {len(option_paras)} options. Title: {title}")
    elif option_paras:
        correct_opts = [opt for opt, corr in option_paras if corr]
        if len(correct_opts) == 1:
            stats['single_choice'] += 1
            details.append(f"[{lesson} Q{q_num}] TYPE: single_choice")
        elif len(correct_opts) > 1:
            stats['multiple_choice'] += 1
            details.append(f"[{lesson} Q{q_num}] TYPE: multiple_choice (unflagged title, correct: {len(correct_opts)})")
        else:
            issues.append(f"{lesson} Q{q_num} (Single): NO correct answer found! Options count: {len(option_paras)}. Title: {title}")
            stats['unknown'] += 1
    else:
        issues.append(f"{lesson} Q{q_num}: No options and no table! Title: {title}")
        stats['unknown'] += 1

with open('classification_report.txt', 'w', encoding='utf-8') as f:
    f.write("=== CLASSIFICATION STATS ===\n")
    for k, v in stats.items():
        f.write(f"  {k}: {v}\n")
    f.write(f"\n=== ISSUES / SUSPICIOUS ({len(issues)}) ===\n")
    for issue in issues:
        f.write(f"  - {issue}\n")
    f.write(f"\n=== DETAILS ===\n")
    for d in details:
        f.write(f"  {d}\n")

print("Report written to classification_report.txt")
