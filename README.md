# pdfsummary

This is a python script that creates a text summary of a given pdf file. It also takes in inputs for the number of sentences in the summary and the number of key phrases desired.
This script works by first converting the pages in the pdf files into images. The images are then transcribed into text, which are cleaned up for the next few steps. The summary and the key phrases for the file are generated and are put into two separate text files as well as one pdf file. The key phrases are also highlighted in a new pdf file that contains the same content as the original. 