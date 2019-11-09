import re

newlines = []
with open('fulltext.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()
    for i in range(len(lines) - 1):
        if lines[i].strip() or lines[i + 1].strip():
            newlines.append(lines[i])

# replace hyphenated words with full words
text = ''.join(newlines)
def replaceHyphen(match):
    return re.sub(r'-\s*', '', match.string)
cleantext = re.sub(r'[a-zA-Z]+-\s*[a-zA-Z]+', replaceHyphen, text, flags=re.IGNORECASE)

with open('cleantext.txt', 'w', encoding = 'utf-8') as f:
    f.write(cleantext)
