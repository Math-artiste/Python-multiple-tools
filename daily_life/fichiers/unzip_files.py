from zipfile import ZipFile

path = input("Entrez le nom de votre fichier : ")

with ZipFile(path, "r") as zip_object : 
    zip_object.extractall()


print(zip_object.namelist())