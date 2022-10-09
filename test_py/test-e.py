# -*- coding: utf -*-
#ouverture en lecture
f = open("number.txt","r")

while True :
    s = f.readline()
    if (s != "") :
        print(s)
        print()
    else :
        break;
f.close()