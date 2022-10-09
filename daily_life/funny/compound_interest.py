def compound_interest(principle, rate, time) :
    amount = principle * (pow((1 + rate / 100), time))
    CI = amount - principle
    print("Compound interest is",CI)

P = float(input("Enter principle value : "))
R = float(input("Enter rate value : "))
T = float(input("Enter time value : "))
compound_interest(P, R, T)