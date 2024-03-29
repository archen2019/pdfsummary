from fpdf import FPDF

def make_pdf(keyphrases, directory):
    with open(directory + 'summary.txt', 'r', encoding = 'utf-8') as f:
        text = f.read()

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    pdf.cell(40, 10, 'Key Phrases', align = 'C', ln = 2)
    for key in keyphrases:
        pdf.cell(0, 10, key, align = 'L', ln = 2)

    pdf.add_page()
    pdf.cell(40, 10, 'Summary', align = 'C', ln = 2)
    pdf.multi_cell(0, 10, text, align = 'L')
    pdf.output(directory + 'Summary.pdf', 'F')
