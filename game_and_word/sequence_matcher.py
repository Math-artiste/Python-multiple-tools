from difflib import SequenceMatcher
text1 = input("Enetr 1st sequence : ")
text2 = input("Enter 2nd sequence : ")
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")