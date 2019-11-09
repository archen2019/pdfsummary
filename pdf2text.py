import subprocess
from pdf2image import convert_from_path
from PIL import Image
import pandas as pd
import numpy as np

pdf = input('File name: ')

images = convert_from_path(pdf)
txtlist = []

for img in images:
    img = img.convert('LA')
    img.save('cur_img.png')
    subprocess.run(['tesseract', 'cur_img.png', 'cur_txt', '--dpi', '125'])
    with open('cur_txt.txt', 'r') as curfile:
        txtlist.extend(curfile.readlines())
        del txtlist[-1]
        txtlist.append('\n')

with open('fulltext.txt', 'w') as f:
    f.write(''.join(txtlist))

subprocess.run(['rm', 'cur_img.png'])
subprocess.run(['rm', 'cur_txt.txt'])
