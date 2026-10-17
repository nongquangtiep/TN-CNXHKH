with open('elements_flow.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('tables_context.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if '=== TABLE' in line:
            start = max(0, i-4)
            end = min(len(lines), i+12)
            out.write('----------------------------------------\n')
            for j in range(start, end):
                out.write(lines[j])

print("Saved tables context.")
