def letter_range(start, stop="{", step=1):
    """Yield a range of lowercase letters.""" 
    for ord_ in range(ord(start.upper()), ord(stop.upper()), step):
        yield chr(ord_)

print(list(letter_range("A", "D")))
# ['a', 'b', 'c', 'd', 'e']

print(list(letter_range("A", "F", step=2)))
# ['a', 'c', 'e']

tuple = ()

tuple = list(letter_range("A", "F", step=3))
print(tuple)

