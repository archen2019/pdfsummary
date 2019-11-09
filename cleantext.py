newlines = []
with open('fulltext.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() or lines[i + 1].strip():
            newlines.append(lines[i])

with open('cleantext.txt', 'w') as f:
    f.write(''.join(newlines))

# replace hyphenated words with full words
lines = []
with open('cleantext.txt', 'r') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i][:-1].endswith('-') and lines[i + 1].strip():
            lines[i] = lines[i][:-2]
            split = lines[i + 1].split(' ', 1)
            lines[i] = lines[i] + split[0] + '\n'
            lines[i + 1] = split[1]

with open('cleantext.txt', 'w') as f:
    f.write(''.join(lines))
