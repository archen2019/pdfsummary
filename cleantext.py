import re

newlines = []
with open('fulltext.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() or lines[i + 1].strip():
            newlines.append(lines[i])

# replace hyphenated words with full words
# for i in range(len(newlines) - 1):
#     if newlines[i][:-1].endswith('-') and newlines[i + 1].strip():
#         newlines[i] = newlines[i][:-2]
#         split = newlines[i + 1].split(' ', 1)
#         newlines[i] = newlines[i] + split[0] + '\n'
#         newlines[i + 1] = split[1]

def replace(match):
    replacement = re.sub(r'-\s*', '', match.group(0))
    return replacement

def hyphenRegex(text):
    return re.sub(r'[a-zA-Z]+-\s*\n[a-zA-Z]+', replace, text, flags=re.IGNORECASE)

cleantext = hyphenRegex(''.join(newlines))

with open('cleantext.txt', 'w', encoding = 'utf-8') as f:
    f.write(cleantext)
