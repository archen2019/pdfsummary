from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"

def summarize(fileName, sentence_count, directory):
    parser = PlaintextParser.from_file((fileName), Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)

    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)

    with open(directory + 'summary.txt', 'w', encoding = 'utf-8') as f:
        for sentence in summarizer(parser.document, sentence_count):
            f.write(str(sentence))
            f.write('\n')
