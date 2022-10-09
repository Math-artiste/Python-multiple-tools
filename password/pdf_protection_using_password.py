from PyPDF2 import PdfFileWriter, PdfFileReader
import getpass
pdfwritter = PdfFileWriter()
pdf = PdfFileReader("C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\test.pdf")
for page_num in range(pdf.numPages) :
    pdfwritter.addPage(pdf.getPage(page_num))
password = getpass.getpass(prompt = 'Enter Password : ')
pdfwritter.encrypt(password)
with open("C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\test.pdf", 'wb') as f :
    pdfwritter.write(f)
print("Now file is password protected")