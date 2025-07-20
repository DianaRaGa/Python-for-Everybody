#Exercise 2: Write a program that categorizes each mail message by which day of the week the commit was done.
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the
# days of the week. At the end of the program print out the contents of your dictionary (order does not matter).
#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Sample Execution:
#python dow.py
#Enter a file name: E_mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

week_days = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    for line in file:
        words = line.split()
        
        # Skip lines that are too short or do not start with 'From'
        if len(words) <= 3 or words[0] != "From":
            continue
        
        # Process the third word (day of the week) and update the count in the dictionary
        day_of_week = words[2].lower()  # Convert day to lowercase for consistency
        week_days[day_of_week] = week_days.get(day_of_week, 0) + 1 #This method works perfect for this type of work in a dict()

# Print the dictionary before sorting
print(f"\nThis is the dictionary created from the file '{file.name}':")
print(week_days)

# Sort the dictionary by day of the week and print the sorted result
print("\nThis is the dictionary in alphabetical order:")
for day, count in sorted(week_days.items()):
    print(f"{day}: {count}")