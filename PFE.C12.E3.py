#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving the document from a URL,
# (2) displaying up to 3000 characters, and (3) counting the overall number of characters in the document.
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error

while True:
    # Prompt for URL
    user_URL = input("Enter a URL or write 'done' to exit:\n").strip()
    
    if user_URL.lower() == 'done':
        break

    try:
        total_char=0
        printed_char=0
        printing=True # Control flag to stop printing after 3000 characters
        
        file = urllib.request.urlopen(user_URL)# Open the URL as a file
        for line in file:
            line = line.decode().rstrip()# Decode and remove trailing spaces
            len_line = len(line)
            
            total_char += len_line# Update total character count
            
            if printing:
                # Check if the line can be printed without exceeding 3000 characters
                if len_line + printed_char <= 3000:
                    print(line)# Print the whole line if under limit
                    printed_char += len_line
                else:
                    # Print only part of the line to hit exactly 3000 characters
                    to_print = 3000 - printed_char
                    print(line[:to_print])# Print the cut-off part
                    printed_char += len(line[:to_print])# After printing part, stop printing
                    printing = False# No more printing required
                    
                            
        print(f"The total of characters in the URL was: {total_char}")
    
    except urllib.error.URLError:
        print("There was a problem accessing the given URL")
        
    except urllib.error.HTTPError:
        print("There was an error in the server")
        
    except ValueError:
        print("The given URL has an incorrect format")
