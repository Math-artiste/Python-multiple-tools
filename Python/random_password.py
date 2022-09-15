import random
import json

passlen = int(input("Enter the lenght of password : "))

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?/\|"

p = " ".join(random.sample(s,passlen))

with open("Password.json", "r") as data_file :
    json.load(data_file)

with open("Password.json", "w") as f :
    json.dump(p, f, indent = 4)
print(p)