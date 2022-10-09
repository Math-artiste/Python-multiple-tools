import barcode
from barcode.writer import ImageWriter

number = input("Enter the code to generate barcode : ")
barcode_format = barcode.get_barcode_class("upc")
my_barcode = barcode_format(number, writer = ImageWriter())

name = input("Entrez le nom du code barre : ")
my_barcode.save(name)