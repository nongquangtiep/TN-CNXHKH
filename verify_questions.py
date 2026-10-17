import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f"Total questions loaded: {len(questions)}")

type_counts = {}
lesson_counts = {}
suspicious = []

for q in questions:
    t = q['type']
    type_counts[t] = type_counts.get(t, 0) + 1
    
    l = q['lesson']
    lesson_counts[l] = lesson_counts.get(l, 0) + 1
    
    # check structure
    if t in ['single_choice', 'multiple_choice']:
        if not q.get('options') or len(q['options']) < 2:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): options < 2: {q.get('options')}")
        if not q.get('correct_answers'):
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): no correct answers")
        if t == 'single_choice' and len(q['correct_answers']) != 1:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): single choice has {len(q['correct_answers'])} answers: {q['correct_answers']}")
        if t == 'multiple_choice' and len(q['correct_answers']) < 2:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): multiple choice has only {len(q['correct_answers'])} answer: {q['correct_answers']}")
            
    elif t == 'true_false':
        items = q.get('items', [])
        if not items or len(items) < 2:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): TF items count: {len(items)}")
        for it in items:
            if 'correct' not in it or not isinstance(it['correct'], bool):
                suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): TF item invalid correct: {it}")
                
    elif t == 'drag_drop_match':
        pairs = q.get('pairs', [])
        if not pairs or len(pairs) < 2:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): match pairs count: {len(pairs)}")
        for p in pairs:
            if not p.get('left') or not p.get('right'):
                suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): match pair empty left/right: {p}")
                
    elif t == 'drag_drop_categorize':
        cats = q.get('categories', [])
        if len(cats) != 2:
            suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): categorize categories count != 2: {len(cats)}")
        for c in cats:
            if not c.get('title') or not c.get('items'):
                suspicious.append(f"{q['id']} ({l} Q{q['q_num']}): empty category {c}")

print("\n--- TYPE COUNTS ---")
for t, c in type_counts.items():
    print(f"  {t}: {c}")

print("\n--- LESSON COUNTS ---")
for l, c in lesson_counts.items():
    print(f"  {l}: {c}")

print(f"\n--- SUSPICIOUS ISSUES ({len(suspicious)}) ---")
for s in suspicious:
    print(f"  {s}")
