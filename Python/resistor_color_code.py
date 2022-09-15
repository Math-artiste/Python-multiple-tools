color = ["black", "brown", "red", "orange", "yellow", 
        "green", "blue", "violet", "grey", "white"]


n=color.index((input("Enter the 1st color : ")))
m=color.index((input("Enter the 2nd color : ")))
p=color.index((input("Enter the 3rd color : ")))

q=int(((n*10)+(m))*(10**(p)))
z=q/1000

print("\nThe resister value is : ")
print(f"{q}Ώ and in Kiloohm : {z}kΏ")