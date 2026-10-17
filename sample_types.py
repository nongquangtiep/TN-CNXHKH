import json

with open('questions.json', 'r', encoding='utf-8') as f:
    qs = json.load(f)

seen = set()
with open('sample_types.txt', 'w', encoding='utf-8') as out:
    for q in qs:
        if q['type'] not in seen:
            seen.add(q['type'])
            out.write(f"\n================ TYPE: {q['type']} ================\n")
            out.write(json.dumps(q, ensure_ascii=False, indent=2))
            out.write("\n")

print("Saved samples.")
