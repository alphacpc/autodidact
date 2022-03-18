from connnectDB import conn, cursor
import docx
 
# open connection to Word Document
doc = docx.Document("Requetes.docx")
 
# read in each paragraph in file
result = [p.text for p in doc.paragraphs]

print(result)

print("hello")





