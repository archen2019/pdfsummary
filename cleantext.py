newlines = []
with open('fulltext.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() or lines[i + 1].strip():
            newlines.append(lines[i])

with open('cleantext.txt', 'w') as f:
    f.write(''.join(newlines))
