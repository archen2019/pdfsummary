from pdf2text import PDF2Text
from cleantext import clean
from summarize import summarize
from keyphrase import get_key_phrases
from makepdf import make_pdf
from highlight import highlight

fileName = input('File Name: ')
numSentences = int(input('Number of sentences in summary: '))
numKey = int(input('Number of key phrases: '))
text = PDF2Text(fileName)
clean(text)
print('---cleaned---')
summarize('cleantext.txt', numSentences)
print('---summarized---')
keyphrases = get_key_phrases(numKey)
print('---key phrases found---')
make_pdf(keyphrases)
print('---pdf made---')
highlight(keyphrases)
print('---pdf highlighted---')
print('done')
