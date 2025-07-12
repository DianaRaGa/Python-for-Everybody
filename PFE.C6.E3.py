#Exercise 3: Encapsulate this code in a function named count, and generalize it so that it accepts the
# string and the letter as arguments.
#word = 'banana'
#count = 0
#for letter in word:
#    if letter == 'a':
#        count = count + 1
#print(count)

def count(word, letter):
    i = 0
    for character in word:
        if character == letter:
            i+=1
    print (f"The times {letter} appears in '{word}' is {i}")

word =input("Please enter a word or sentence:\n").strip().lower()
letter = input("Please enter a letter you want to count in the sentence:\n").strip().lower()
count(word, letter)
