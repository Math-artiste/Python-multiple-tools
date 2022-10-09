import json
from re import L

names = []
phone_numbers = []
num = int(input("Enter number of contact you want to save : "))
for i in range(num) :
    name = input("Name : ")
    phone_number = input("Phone Number : ")
    names.append(name)
    phone_numbers.append(phone_number)


for i in range(num) :
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
    print("Voulez-vous rechercher un contact ? ")
    choice = input()


    if choice == "oui" or choice == "o" :
        search_term = input("\nEnter search term : ")
        print("Search result : ")
        if search_term in names :
            index = names.index(search_term)
            phone_number = phone_numbers[index]
            print("Name: {}, Phone Number: {}".format(search_term, phone_number))
        else : 
            print("Name Not Found")
else :
    print("Good Bye")

with open("Annuaire.json", "w", newline = "\r\n") as f :
    json.dump(names, f, indent = 4)
    json.dump(phone_numbers, f, indent = 4)
