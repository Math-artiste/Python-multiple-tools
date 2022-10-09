from textblob import TextBlob
def Convert(string) : 
    li = list(string.split())
    return li
str1 = input("Enter your word : ")
words = Convert(str1)
corrected_word = []
for i in words : 
    corrected_word.append(TextBlob(i))
print("Wrong words :", words)
print("Corrected words are :")
for i in corrected_word :
    print(i.correct(), end = " ")