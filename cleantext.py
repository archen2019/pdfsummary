import re

def replace(match):
    replacement = re.sub(r'-\s*', '', match.group(0))
    return replacement

def hyphenRegex(text):
    return re.sub(r'[a-zA-Z]+-\s*\n[a-zA-Z]+', replace, text, flags=re.IGNORECASE)

def clean(text):
    newlines = text

    for i in range(len(lines) - 1):
        if lines[i].strip() or lines[i + 1].strip():
            newlines.append(lines[i])

    cleantext = hyphenRegex(''.join(newlines))

    with open('cleantext.txt', 'w', encoding = 'utf-8') as f:
        f.write(cleantext)
