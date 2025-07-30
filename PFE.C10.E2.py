#Exercise 2: This program counts the distribution of the hour of the day for each of the messages.
# You can pull the hour from the “From” line by finding the time string and then splitting that string
# into parts using the colon character. Once you have accumulated the counts for each hour, print out the
# counts, one per line, sorted by hour as shown below.
#python timeofday.py
#Enter a file name: E_mbox-short.txt
#04 3
#06 1
#07 1
#09 2

hours = dict()  # Initialize the dictionary
from E_opentxt import open_texts  # Import the function to open a text file

# Open file using 'with' statement to ensure automatic closing
with open_texts() as file:
    for line in file:
        words = line.split()
        
        # Skip lines that are too short or do not start with 'From'
        if len(words) <= 3 or words[0] != "From":
            continue
        
        # Process the fifth word (the time stamp of the sender) and update the count in the dictionary
        time = words[5].split(":")  # Takes the whole time stamp and spit it from the colon
        hour = time[0]#Puts the first item of the time in a variable to append it to the dictionary
        hours[hour] = hours.get(hour,0) + 1
        
    #First loop that converts the dictionary into a list of tuples for each key-value pair
    hours_list = list()
    for key,value in hours.items():
        hours_tuple = (key,value)
        hours_list.append(hours_tuple)
        
    #Second loop that sorts the list of tuples to get the hours in order and print them
    hours_list = sorted(hours_list)
    for key,val in hours_list:
        print(key,val)
        
    #Instead  of the last two loops the list can be sorted using this instead for improved code
    for key,val in sorted(hours.items()):
        print(key,val)