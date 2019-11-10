import fitz

def highlight(keyphrases):
    doc = fitz.open('searchable.pdf')

    for key in keyphrases:
        for page in doc:
            instances = page.searchFor(key)
            for i in instances:
                page.addHighlightAnnot(i)

    doc.save('highlighted.pdf', garbage=4, deflate=True, clean=True)
