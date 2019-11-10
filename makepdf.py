with open('SumyResult.txt', 'r', encoding = 'utf-8') as f:
    text = f.read()

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.add_font('DejaVu', '', 'fonts\\DejaVuSansCondensed.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)
pdf.cell(40, 10, 'Summary', align = 'C', ln = 2)
pdf.multi_cell(0, 10, text, align = 'L')
pdf.output('Summary.pdf', 'F')
