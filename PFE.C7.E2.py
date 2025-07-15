#Exercise 2: Write a program to prompt for a file name, and then read through the file and look for lines of the form:
#X-DSPAM-Confidence: 0.8475
#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point
# number on the line. Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.
#Enter the file name: PFE.C7.E1mbox.txt
#Average spam confidence: 0.894128046745
#Enter the file name: PFE.C7.E1mbox-short.txt
#Average spam confidence: 0.750718518519
#Test your file on the mbox.txt and mbox-short.txt files.

import numpy as np

spam_confidence=[]
while True:
    file = input("Please enter the name of a text file (or type 'exit' to quit):\n").strip()
    extension = file.find(".txt")
    
    if file.lower() == "exit":
        print("Exiting program.")
        break
    
    if extension == -1:
        file += ".txt"


    try:
        with open(file) as text:  # Ensures the file is properly closed after reading
            for line in text:
                if line.startswith("X-DSPAM-Confidence:"): # Strips newlines before converting to uppercase
                    colon = line.strip().find(":")
                    data = float(line[colon + 2:])
                    spam_confidence.append(data)
        x_dspam_confidence = np.mean(spam_confidence)
        print(f"Average spam confidence: {round(x_dspam_confidence,12)}")
        break  # Exit the loop when successful
    except FileNotFoundError:
        print("File not found. Please try again.")
