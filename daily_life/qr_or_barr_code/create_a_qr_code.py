import pyqrcode
import png
link = "https://twitter.com/home?lang=fr"
qr_code = pyqrcode.create(link)
qr_code.png("test_twitter.png", scale = 5)