#Exercise 2: Figure out which line of the above program is still not properly guarded.
# See if you can construct a text file which causes the program to fail and then modify the program so that the
# line is properly guarded and test it to make sure it handles your new text file.

while True:
    text = input('''Please enter a file name to search trough emails and extract the day it was sent
or type ('exit') to quit:\n''').rstrip()
    if text.lower() == "exit":
        print("Exiting program")
        break
    
    if ".txt" not in text:
        text += ".txt"
    
    try:
        with open(text) as file:
            count = 0
            for line in file:
                words = line.split()
                if len(words) < 3: continue
                if words[0] != "From": continue
                print(words[2])
                count += 1
                
            if count == 0:
                print("No valid 'From' lines found in the file")
                
            else:
                print(f'''There where '{count}' lines that contain the day of the week the email was sent to
From the total days of the week sent and email''')
                
    except FileNotFoundError:
        print("File not foud. Please try again")
