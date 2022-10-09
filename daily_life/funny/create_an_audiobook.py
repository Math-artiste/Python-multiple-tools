import PyPDF2
import pyttsx3

pdfReader = PyPDF2.PdfFileReader(open("C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\Gargantua.pdf", "rb"))

speaker = pyttsx3.init()

for page_num in range(pdfReader.numPages) :
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()

speaker.stop()
speaker.save_to_file(text, "C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\dl_vid_yout")
speaker.runAndWait