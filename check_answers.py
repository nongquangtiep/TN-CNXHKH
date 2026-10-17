import json

with open('questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

single = [q for q in qs if q['type'] == 'single_choice']
multi = [q for q in qs if q['type'] == 'multiple_choice']
tf = [q for q in qs if q['type'] == 'true_false']
drag = [q for q in qs if q['type'].startswith('drag_drop')]

print(f"Total: {len(qs)}")
print(f"Single: {len(single)}")
print(f"Multi: {len(multi)}")
print(f"True/False: {len(tf)}")
print(f"Drag&Drop: {len(drag)}")

with open('answers_sample.txt', 'w', encoding='utf-8') as out:
    out.write("=== SINGLE CHOICE SAMPLE ===\n")
    for q in single[:15]:
        correct_opt = q['options'][q['correct_answers'][0]]
        out.write(f"[{q['lesson']} Q{q['q_num']}] {q['question']}\n")
        out.write(f"   -> ĐÁP ÁN BÔI ĐỎ: {correct_opt}\n\n")

    out.write("\n=== MULTI CHOICE SAMPLE ===\n")
    for q in multi[:10]:
        correct_opts = [q['options'][i] for i in q['correct_answers']]
        out.write(f"[{q['lesson']} Q{q['q_num']}] {q['question']}\n")
        out.write(f"   -> ĐÁP ÁN BÔI ĐỎ: {' | '.join(correct_opts)}\n\n")

print("Wrote sample to answers_sample.txt")
