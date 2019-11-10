import fitz

def highlight(keyphrases, directory):
    doc = fitz.open('searchable.pdf')

    for key in keyphrases:
        for page in doc:
            instances = page.searchFor(key)
            for i in instances:
                page.addHighlightAnnot(i)

    doc.save(directory + 'highlighted.pdf', garbage=4, deflate=True, clean=True)
