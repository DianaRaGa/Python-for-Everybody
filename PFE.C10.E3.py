#Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
# Your program should convert all the input to lower case and only count the letters a-z.
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z.
# Find text samples from several different languages and see how letter frequency varies between languages.
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string

letters = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    #First for loop is to get each line of the file and strip all the unwanted characters and make it a list
    for line in file:
        clean_line = list(line.translate(str.maketrans("","",string.punctuation + " \n\t0123456789")).lower())
        #Second for loop is to add each character from the line list to the dictionary
        for character in clean_line:
            letters[character] = letters.get(character,0) + 1
            
    #Third for loop is to print the sorted characters from the dictionary line by line and calculating the
    # percentage for each one to be able to compare them
    total_characters = sum(letters.values())
    for key,value in sorted(letters.items()):        
        percentage = (value * 100) / total_characters
        print(f"{key}, {value} - {round(percentage,2)} %")
    