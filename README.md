# pdfsummary

Python script that creates a text summary and finds key phrases of a PDF file.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Methodology](#methodology)
* [Citations](#citations)

## Installation

To install `pdfsummary` from GitHub:

```
git clone https://github.com/archen2019/pdfsummary
```

`pdfsummary` also needs the requirements listed in `requirements.txt`. To install, run the following:

```
pip install -r requirements.txt
```

## Usage

To run `pdfsummary`, simply enter the cloned folder and run the file `run.py`. Then, enter the file name of the PDF, the number of sentences in the summary, and the number of keywords. 

```
$ cd pdfsummary
$ python run.py
File Name: [FILE-NAME]
Number of sentences in summary: [NUM-SENTENCES]
Number of key phrases: [NUM-PHRASES]
```

This will create 4 files in the directory of the original PDF:
* `keyphrases.txt` A text file containing the key phrases.
* `summary.txt` A text file containing the summary.
* `Summary.pdf` A PDF file containing the key phrases and the summary.
* `highlighted.pdf` A PDF file containing the original pdf, with key phrases highlighted.

## Methodology

1. Use `pdf2image` to convert the PDF into PNG images.
2. Use `tesseract` to extract text from images and create a text-searchable copy of the original PDF.
3. Process text to remove extra newlines and reconnect hyphenated words.
4. Use `sumy` to generate a summary of the processed text.
5. Use `pke` to generate key phrases from the processed text.
6. Create pdf containing key phrases and summary.
7. Highlight key phrases in text-searchable PDF.

## Citations

Boudin, Florian. “Pke: An Open Source Python-Based Keyphrase Extraction Toolkit.” Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics: System Demonstrations, The COLING 2016 Organizing Committee, 2016, pp. 69–73. ACLWeb, https://www.aclweb.org/anthology/C16-2015.
