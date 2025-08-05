#Extracting Data from JSON
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
# The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the
# comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other
# is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_2010036.json (Sum ends with 28)

#Importing the corresponding libraries
import urllib.request
import json

while True:
    #Asking for the URL and adding the option to get out of the loop
    url = input("Please enter a URL to compute the sum or 'done' to exit the program:\n")
    if len(url) < 1 : 
        url = 'http://py4e-data.dr-chuck.net/comments_42.json'
    if url.strip().lower()=='done':
        break

    print('Retrieving', url)#Comment to let the user know the computation is being done
    
    #Doing the opening of the URL with urllib safely
    try:
        #Opening the URL safely
        with urllib.request.urlopen(url) as uh:#This is the part that can blow off
            data = uh.read()
            print('Retrieved',len(data),'characters')
            js = json.loads(data)#This part parse the data from the URL into a python data, in this case is a dictionary

            counts = js['comments']#Gets the list of the data from the dictionary
            nums = list()
            for result in counts:#Iterates inside the list from the URL obtain in line 26
                num = result['count']#The numbers are in the dictionary key 'count'
                nums.append(num)#Adds the numbers form the count into a list to compute later the calculations

            print('Count:', len(nums))
            print('Sum:', sum(nums))
    
    except urllib.error.URLError as e:
        print(f"Failed to retrieve the URL: {e}")
        exit()
        
    except json.JSONDecodeError:
        print("Failed to parse the JSON data")
        exit()
