#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression and the findall() method.
# Compute the average of the numbers and print out the average as an integer.
#Enter file:mbox.txt
#38549
#Enter file:mbox-short.txt
#39756

import re
from E_opentxt import open_texts  # Import the function to open a text file

#Initiatin a list for storing the numbers that matched the found
num_match = []

with open_texts() as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            continue
        num = re.findall('^New Revision: ([0-9]+)',line)
        if len(num) == 0:
            continue
        num_int = int(num[0])
        num_match.append(num_int)
        
    ave = sum(num_match)//len(num_match)
    print(f"The sum of all the numbers in the file is: {ave}")