from tkinter.ttk import Separator


def ip_address(address) :
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)
    return new_address
IPad = input("ENter your IP adress : ")
ipadress = ip_address(IPad)
print(ipadress)