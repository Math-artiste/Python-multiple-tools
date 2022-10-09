import imageio

photo_1 = input("Entrez le nom de la première photo : ")
photo_2 = input("Entrez le nom de la deuxième photo : ")

filenames = [photo_1, photo_2]
images = []

for filename in filenames :
    images.append(imageio.v2.imread(filename))
imageio.mimsave("C:\\Users\\montage du 60\\Documents\\Python\\daily_life\\gif\\movie.gif", images, 'GIF', duration = 1)