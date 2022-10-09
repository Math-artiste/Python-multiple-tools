from pdf2docx import Converter

pdf_file = input("Entrez le nom de votre fichier pdf : ")
docx_file = "transform_pdf.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()