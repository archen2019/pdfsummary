import fitz

doc = fitz.open('searchable.pdf')

keywords = ['baby']
for keyword in keywords:
    for page in doc:
        instances = page.searchFor(keyword)
        for i in instances:
            page.addHighlightAnnot(i)

doc.save('highlighted.pdf', garbage=4, deflate=True, clean=True)
