Height = float(input("Enter your height in centimeters : "))
Weight = float(input("Enter your weight in kg : "))
Height = Height/100
BMI = Weight / (Height * Height)
BMI = round(BMI, 2)
print("Your body mass  index  is : ", BMI)

if BMI > 0 :
    if (BMI <= 16) :
        print("You are severly underweight !")
    elif (BMI <= 18.5) :
        print("You are underweight !")
    elif (BMI <= 25) :
        print("You are healthy !")
    elif (BMI <= 30) :
        print("You are overweight !")
    else  :
        print("You are severly overweight !")
else : ("enter valid details")
    
    
