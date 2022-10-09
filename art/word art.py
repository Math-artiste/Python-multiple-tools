import pywhatkit
path = input("Enter the name of the file you want to draw : ")
path = "C:\\Users\\montage du 60\\Documents\\Python\\art\\" + path
pywhatkit.image_to_ascii_art(path, "My art")
read_file = open("C:\\Users\\montage du 60\\Documents\\Python\\art\\My art.txt", "r")
print(read_file.read())
