from better_profanity import profanity
import PyPDF2

pdf = open("test.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
text = page.extractText()
censored = profanity.censor(text)
print(censored)


