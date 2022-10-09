myfile = open("emoji-sequences.txt", "rt") # open lorem.txt for reading text
contents = myfile.read()         # read the entire file to string
myfile.close()                   # close the file
print(contents)        