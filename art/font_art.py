import pyfiglet


word  = input("Enter the word you want to draw : ")
font = pyfiglet.figlet_format(word)
print(font)
