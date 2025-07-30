#Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the
# addresses from the line. Count the number of messages from each person using a dictionary. After all
# the data has been read, print the person with the most commits by creating a list of (count, email)
# tuples from the dictionary. Then sort the list in reverse order and print out the person who has the
# most commits.
#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Enter a file name: E_mbox-short.txt
#cwen@iupui.edu 5

authors = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    for line in file:
        words = line.split()
        
        # Skip lines that are too short or do not start with 'From'
        if len(words) <= 3 or words[0] != "From":
            continue
        
        # Process the second word (the email address of the sender) and update the count in the dictionary
        email = words[1].lower()  # Convert E-mail to lowercase for consistency
        authors[email] = authors.get(email,0)+1
        
    #First loop that converts the dictionary into a list of tuples for each key-value pair
    biggest_sender=list()
    for key,value in authors.items():
        authors_tuple = (value,key)
        biggest_sender.append(authors_tuple)
        
    #Second loop that sorts the list of tuples to get the first email and count of the person that sent te most emails
    biggest_sender = sorted(biggest_sender, reverse=True)
    for val,key in biggest_sender[:1]:
        print(key,val)