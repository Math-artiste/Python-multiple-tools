from PIL import Image

def Image_pdf(filename, output) :
    images = []

    for file in filename : 
        im = Image.open(file)
        im = im.convert("RGB")
        images.append(im)

        images[0].save(output, save_all = True, append_images = images[1:])
    

Image_pdf(["photo1.png", "photo2.png"], "output.pdf")