from PIL import Image
try:
    im=Image.open("img_arbre.png")
    print("iamge is ok")
    # do stuff
except IOError:
    print("filename not an image file")