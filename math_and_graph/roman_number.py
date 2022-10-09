tallies = { "I" : 1, "V" : 5, "X" : 10,  "L" : 50, 
            "C" : 100, "D" : 500, "M" : 1000 }

def roman_numeral_to_decimal(roman_numeral) :
    sum = 0
    for i in range(len(roman_numeral) - 1 ) :
        left = roman_numeral[i] 
        right = roman_numeral[i + 1]
        if tallies[left] < tallies[right] :
            sum -= tallies[left]
        else :
            sum += tallies[left]
    sum += tallies[roman_numeral[-1]]
    return sum
roman = input("Enter roman number : ")
print(roman_numeral_to_decimal(roman))