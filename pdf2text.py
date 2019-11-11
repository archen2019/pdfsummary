import subprocess
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
from pdfrw import PdfReader, PdfWriter


def PDF2Text(pdf):
    images = convert_from_path(pdf)
    txtlist = []
    writer = PdfWriter()

    for img in images:
        img = img.convert('LA')
        img.save('cur_img.png')
        subprocess.run(['tesseract', 'cur_img.png', 'cur_txt', '--dpi', '125'])
        with open('cur_txt.txt', 'r', encoding = 'utf-8') as curfile:
            txtlist.extend(curfile.readlines())
            del txtlist[-1]
            txtlist.append('\n')
        subprocess.run(['tesseract', 'cur_img.png', 'cur_pdf', '--dpi', '125', 'pdf'])
        writer.addpages(PdfReader('cur_pdf.pdf').pages)

    writer.write('searchable.pdf')

    return txtlist