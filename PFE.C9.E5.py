#Exercise 5: This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.
#python schoolcount.py
#Enter a file name: E_mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

domain_authors = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    for line in file:
        words = line.split()
        
        # Skip lines that are too short or do not start with 'From'
        if len(words) <= 3 or words[0] != "From":
            continue
        
        # Process the second word (the email address of the sender) and update the count in the dictionary
        author = words[1].lower()  # Convert E-mail to lowercase for consistency
        arroba = author.find("@")
        domain = author[arroba + 1:]
        domain_authors[domain] = domain_authors.get(domain, 0) + 1

# Print the dictionary before sorting
print(f"\nDomain counts from file '{file.name}':")
print(domain_authors)

# Sort the dictionary by alphabetical order and print the sorted result
print("\nDomain counts in alphabetical order:")
for domain, count in sorted(domain_authors.items()):
    print(f"{domain}: {count}")

#Sorts the dictionary in descending order
print("\nDomain counts in descending order:")
for domain,count in sorted(domain_authors.items(), key=lambda item:item[1], reverse=True):
    print(f"{domain}: {count}")