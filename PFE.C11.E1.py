#Exercise 1: Write a simple program to simulate the operation of the grep command on Unix.
# Ask the user to enter a regular expression and count the number of lines that matched the regular expression:
#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author
#$ python grep.py
#Enter a regular expression: ^X
#mbox.txt had 14368 lines that matched ^X-
#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$

import re
from E_opentxt import open_texts  # Import the function to open a text file

#Initiatin a list for storing the matches found
match=[]

print("This program acts like a grep command on Unix, please follow the instructions bellow")

#Get user input for the regular expression to use as each in the file before opening the file
re_ex=input("Please enter the regular expression you wish to search for in the file: \n")

with open_texts() as file:  # Ensures the file is properly closed after reading
    for line in file:
        line=line.strip()
        if re.search(re_ex,line):
            match.append(line)#Store the full line to avoid overcounting

len_match=len(match)#Counts matching lines

#Outputs results
if len_match==0:
    print("There were NO matches in the search")
        
print(f"{file.name} had {len_match} lines that matched {re_ex}")