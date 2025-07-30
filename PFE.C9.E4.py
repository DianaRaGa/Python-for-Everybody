#Exercise 4: Add code to the above program to figure out who has the most messages in the file. After all the data has
# been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5:
# Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: E_mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: E_mbox.txt
#zqian@umich.edu 195

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
        author = words[1].lower()  # Convert E-mail to lowercase for consistency
        mail_authors[author] = mail_authors.get(author, 0) + 1

#Getting the max autor sender and the count
biggest_sender = None
biggest_email_sender = None#I'm not convinced that this variable needs to be initialized but ChatGPT is adamant
for email,count in mail_authors.items():
    if biggest_sender is None or count > biggest_sender:
        biggest_sender = count
        biggest_email_sender = email

# Print the dictionary before sorting
print(f"\nThis is the dictionary created from the file '{file.name}':")
print(mail_authors)

#Prints the biggest sender with the max loop
print(f"\nThis is the address that sent the most emails and the count of how many they were:")
print(f"{biggest_email_sender}: {biggest_sender}")

#Prints the biggest sender with the lambda function
biggest=max (mail_authors.items(), key = lambda item: item[1]) #Gets the sorter version of the dictionary in descending order
print(f"\n{biggest[0]}: {biggest[1]}")


