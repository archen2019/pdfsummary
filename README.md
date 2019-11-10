# pdfsummary

This is a python script that creates a text summary of a given pdf file.

## Table of Contents

* [Installation](#installation)
* [How to use pdfsummary](#how-to)

## Installation

To install `pdfsummary` from github:

```
git clone https://github.com/archen2019/pdfsummary
```

`pdfsummary` also needs the requirements listed in `requirements.txt`. To install, run the following:

```
pip install -r requirements.txt
```

## How to use pdfsummary

To run `pdfsummary`, simply run the file `run.py`. Then, enter the file name of the pdf, the number of sentences in the summary, and the number of keywords. 

```
$ python run.py
File Name: [FILE-NAME]
Number of Sentences in summary: [NUM-SENTENCES]
Number of key phrases: [NUM-PHRASES]
```

This script works by first converting the pages in the pdf files into images. The images are then transcribed into text, which are cleaned up for the next few steps. The summary and the key phrases for the file are generated and are put into two separate text files as well as one pdf file. The key phrases are also highlighted in a new pdf file that contains the same content as the original. 
