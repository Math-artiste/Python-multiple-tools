def converts(s) :
    f = float(s)
    c = (f-32) * 5/9
    c = round(c, 2)
    return c 

def converts_2(r) :
    c = float(r)
    f = (c * 9/5) + 32
    f = round(f,2)
    return f


print("Chooose your measurement unit : ")
print("-1 for degreess Fahrenheit in Celsius")
print("-2 for degrees Celsius in Fahrenheit")
choice = input()

if choice == "1" :
    celsius = input("Enter a value in Fahrenheit : ")
    print(converts(celsius), "°C")
else :
    Fahrenheit = input("Enter a value in Celsius : ")
    print(converts_2(Fahrenheit), "°F")
print("Good Bye")