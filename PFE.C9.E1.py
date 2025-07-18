#Exercise 1: Download a copy of the file
#www.py4e.com/code3/words.txt
#Write a program that reads the words in words.txt and stores them as keys in a dictionary.
# It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is
# in the dictionary.

words_in_file = dict()#Inicialices the directory

from E_opentxt import open_texts #imports the defined function to open a text file

file = open_texts()
for line in file:#Goes through each line in the file to save memory for larger files
    words = line.split()
    for word in words:#Goes to each word in the generated list for each line
        word = word.lower()
        words_in_file[word] = words_in_file.get(word,0)+1
        #if word not in words_in_file:#Adss the word that is not in the dictionary and sets the value as 1, because is the first time it appears
        #    words_in_file[word]=1
        #else:#This else handles words that have been added and are repeated to update the counter in the value of the key
        #    words_in_file[word]+=1

file.close()#Best place to put the closing file after the file processing and it stills works the file.name for printing            
word_check = input("Please enter a word to check if it's in the selected file:\n").rstrip()#Ask the user to inicialice the word check
if word_check.lower() in words_in_file:#Ensures that the words are homogeneous and checks if the searched word is in the dictionary from the file
    print(f"Your word: '{word_check}' is in the file: '{file.name}'")#it has a weir output for the file name
    # "<_io.TextIOWrapper name='words.txt' mode='r encoding='cp1252'>" C2= the code was modified by adding file.name to only show the file name
    print(f"The searched word appears '{words_in_file[word_check]}' times in the file")#it correctly prints the times the word repeats
else:
    print(f"Your word: '{word_check}' is NOT in the file: '{file}'")#Handles cases where the word is not found
    
#I have no idea where to place the file.close()