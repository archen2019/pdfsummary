from pdf2text import PDF2Text
from cleantext import clean
from summarize import summarize
from keyphrase import get_key_phrases
from makepdf import make_pdf
from highlight import highlight
import subprocess
import re
import platform

fileName = input('File Name: ')
directory = ''
if re.match(r':?/?([.a-zA-Z0-9_-]+/)+', fileName):
    directory = fileName[:fileName.rfind('/')+1]

numSentences = int(input('Number of sentences in summary: '))
numKey = int(input('Number of key phrases: '))
text = PDF2Text(fileName)
print('---text loaded---')
clean(text)
print('---cleaned---')
summarize('cleantext.txt', numSentences, directory)
print('---summarized---')
keyphrases = get_key_phrases(numKey, directory)
print('---key phrases found---')
make_pdf(keyphrases, directory)
print('---pdf made---')
highlight(keyphrases, directory)
print('---pdf highlighted---')
if platform.system() == 'Windows':
    subprocess.run(['del', 'cur_img.png'], shell = True)
    subprocess.run(['del', 'cur_txt.txt'], shell = True)
    subprocess.run(['del', 'cur_pdf.pdf'], shell = True)
    subprocess.run(['del', 'cleantext.txt'], shell = True)
    subprocess.run(['del', 'searchable.pdf'], shell = True)
else:
    subprocess.run(['rm', 'cur_img.png'])
    subprocess.run(['rm', 'cur_txt.txt'])
    subprocess.run(['rm', 'cur_pdf.pdf'])
    subprocess.run(['rm', 'cleantext.txt'])
    subprocess.run(['rm', 'searchable.pdf'])
print('done')
