#Exercise 4: There is a string method called count that is similar to the function in the previous exercise.
# Write an invocation that counts the number of times the letter "a" occurs in “banana”
#word="banana"
#number=word.count("a")
#print (number)

def count_letter(word,letter):
    return word.count(letter)

#Applied the while loop to repeat the proces in case the user enter more than one letter
while True:
    word = input("Please enter a word or sentence:\n").strip().lower()
    letter = input("Please enter a single letter to count on the sentence:\n").strip().lower()

    #ensure the valid input of only one letter to count
    if len(letter) != 1:
        print("Please enter only one single letter to count\n")
        continue #To ask for the entry again
        
    else:
        break #To get out of the buckle once the input is correct
    
result = count_letter(word,letter)
print(f"The letter '{letter}' appears '{result}' times in '{word}'")
