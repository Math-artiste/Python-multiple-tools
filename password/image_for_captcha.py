from captcha.image import ImageCaptcha
image = ImageCaptcha(width = 300, height = 100)

captcha_text = input("Enter captcha text : ")
data = image.generate(captcha_text)
image.write(captcha_text, "C:\\Users\\montage du 60\\Documents\\Python\\password\\captcha1.png")
from PIL import Image
Image.open("C:\\Users\\montage du 60\\Documents\\Python\\password\\captcha1.png")