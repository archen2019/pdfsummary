# pdfsummary

This is a Python script that creates a text summary of a given pdf file.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Methodology](#methodology)

## Installation

To install `pdfsummary` from github:

```
git clone https://github.com/archen2019/pdfsummary
```

`pdfsummary` also needs the requirements listed in `requirements.txt`. To install, run the following:

```
pip install -r requirements.txt
```

## Usage

To run `pdfsummary`, simply run the file `run.py`. Then, enter the file name of the pdf, the number of sentences in the summary, and the number of keywords. 

```
$ python run.py
File Name: [FILE-NAME]
Number of Sentences in summary: [NUM-SENTENCES]
Number of key phrases: [NUM-PHRASES]
```

This will create 4 files in the directory of the original pdf:
* `keyphrases.txt`: A text file containing the key phrases.
* `summary.txt`: A text file containing the summary.
* `Summary.pdf`: A pdf file containing the key phrases and the summary.
* `highlighted.pdf`: A pdf file containing the original pdf, with key phrases highlighted.

## Methodology

1. Use `pdf2image` to convert pdf into png files.
2. Use `tesseract` to extract text from images and create a text-searchable copy of the original pdf.
3. Process text to remove extra newlines and reconnect hyphenated words.
4. Use `sumy` to generate a summary of the processed text.
5. Use `pke` to generate key phrases from the processed text.
6. Create pdf containing key phrases and summary.
7. Highlight key phrases in text-searchable pdf.
