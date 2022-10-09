import os

path = input("Veuillez entrer le chemin du dossier que voulez regarder : (utiliser \\) ") 

PATH = path

file_count = 0
directory_Count = 0

for root, dirs, files in os.walk(PATH) :
    print("Looking in :", root)
    for directories in dirs :
        directory_Count += 1
    for Files in files :
        file_count += 1

print("Number of file(s)", file_count)
print("Number of directorie(s)", directory_Count)
print("Total : ",(directory_Count + file_count))