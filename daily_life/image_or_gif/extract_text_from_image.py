from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Utilisateurs\\montage du 60\\Documents\\Python\\tesseract.exe'
path_to_tesseract = r"C:\\Utilisateurs\\montage du 60\\Documents\\Python\\tesseract.exe"

path_to_image = "photo1.png"
pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)

print(text)