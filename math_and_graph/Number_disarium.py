Number = int(input("Enter the number to check Disarium number = "))
length = len(str(Number))
temp = Number
Sum = 0
rem = 0
while temp > 0 :
    rem = temp % 10
    Sum = Sum + int(rem**length)
    temp = temp // 10
    length = length - 1

print("The sum of the digits = %d" % Sum)
if Sum == Number :
    print("\n%d is a Disarium Number." % Number)
else :
    print("%d is not a Disarium Number." % Number)
