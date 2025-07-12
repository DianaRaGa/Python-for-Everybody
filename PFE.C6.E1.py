#Exercise 1: Write a while loop that starts at the last character in the string and works its way backwards
# to the first character in the string, printing each letter on a separate line, except backwards

word = str(input("Please enter a word or phrase: ")).strip()
last_character = len(word) - 1 #contrarrest the offset

while last_character >= 0:
    print (word[last_character])
    last_character -= 1
    