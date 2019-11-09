from summa import summarizer
from summa import keywords

fileName = 'fulltext.txt'

with open(fileName, 'r', encoding = 'utf-8') as f:
    text = f.read()

with open('SummaResult.txt', 'w', encoding = 'utf-8') as f:
    f.write(summarizer.summarize(text, ratio = 0.1))