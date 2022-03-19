import docx

doc = docx.Document("Reqs.docx")

listMenu = [p.text for p in doc.paragraphs]