def ageCalculator(y, m, d) : 
    import datetime
    today = datetime.datetime.now().date()
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
response = int(input("Enter the year of your birthday : "))
response_2 = int(input("Enter the month of your birthday : "))
response_3 = int(input("Enter the day of your birthday : "))
ageCalculator(response, response_2, response_3)
