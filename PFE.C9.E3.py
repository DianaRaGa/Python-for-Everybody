#Exercise 3: Write a program to read through a mail log, build a histogram using
#a dictionary to count how many messages have come from each email address, and
#print the dictionary.
#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

mail_authors = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    for line in file:
        words = line.split()
        
        # Skip lines that are too short or do not start with 'From'
        if len(words) <= 3 or words[0] != "From":
            continue
        
        # Process the second word (the email address of the sender) and update the count in the dictionary
        autor = words[1].lower()  # Convert E-mail to lowercase for consistency
        mail_authors[autor] = mail_authors.get(autor, 0) + 1

# Print the dictionary before sorting
print(f"\nThis is the dictionary created from the file '{file.name}':")
print(mail_authors)

# Sort the dictionary by alphabetical order and print the sorted result. I like it better in alphabetical order
print("\nThis is the dictionary in alphabetical order:")
for autor, count in sorted(mail_authors.items()):
    print(f"{autor}: {count}")