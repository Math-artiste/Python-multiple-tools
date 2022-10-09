from PIL import Image

def details() :
    print(img.format)
    print(img.mode)
    print(img.size)
    print(img.palette)

path = input("Enter the name of the photo you want to analyze : ")
img = Image.open(path)
details()