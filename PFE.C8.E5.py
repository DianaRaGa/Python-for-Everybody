#Exercise 5: Minimalist Email Client.
#Write a program to read through the mailbox data, and when you find line that starts with “From”,
# you will split the line into words using the split function. We are interested in who sent the message, which is
# the second word on the Form line. You will parse the Form line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and print out a count at the end.

from E_opentxt import open_texts #Imports the function defined to prompt the user for a file name and returns
# an openable .txt file
file = open_texts()
count = 0
unique_senders = set()#Starts a set for adding the email senders to have a list of non-repetitive senders
for line in file:
    words = line.split()
    if len(words) <= 3 or words[0] != "From": #Goes line by line avoiding lines with no words or that do not have the email address
        continue
    unique_senders.add(words[1])
    print(f"{words[1]}") #Prints all the emails, even if they are repeated
    count += 1
    
sorted_emails = sorted(unique_senders) #Sorts the set into a list to print and in alphabetical order
    
if count == 0: #To ensure there are lines in count to avoid having an error
    print("There were no lines fulfilling the requisites")
else:
    print(f"There were {count} lines in the file with 'From' as the first word") #This prints the number of lines that
    # start with 'From' that are the persons sending Emails
    print(f"List of non-repetitive senders:\n{sorted_emails}'") 
    print(f"Total number of non-repetitive senders:\n{len(sorted_emails)}")
        
file.close() #This needs to go at the end
        