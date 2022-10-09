from PIL import Image

Image.open('photo2.png')

img = Image.open("photo2.png")
Mirror_image = img.transpose(Image.Transpose.TRANSPOSE.FLIP_LEFT_RIGHT)
Mirror_image.save(r'mirror_image.png')
Image.open("mirror_image.png")