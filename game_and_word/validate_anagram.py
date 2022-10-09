def anagram(word_1, word_2) :
    word_1 = word_1.lower()
    word_2 = word_2.lower()
    return sorted(word_1) == sorted(word_2)

choice_1 = input("Réflechissez à un anagrame puis écrivez le premier mot : ")
choice_2 = input("Ecrivez le deuxième mot : ")
print(anagram(choice_1, choice_2))