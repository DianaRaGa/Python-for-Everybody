#Exercise 3: Rewrite the guardian code in the above example without two if statements.
# Instead, use a compound logical expression using the or logical operator with a single if statement.

while True:
    text=input('''Please enter a file name to search trough emails and extract the day it was sent
or type 'exit' to quit:\n''').rstrip()
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
                if len(words) < 3 or words[0] != "From": continue #line change to make it more concise
                print(words[2])
                count += 1
                
            if count == 0:
                print("No valid 'From' lines found in the file")
                
            else:
                print(f'''There were '{count}' lines that contain the day of the week the email was sent to
From the total days of the week sent and email\n''')
                
    except FileNotFoundError:
        print("File not found. Please try again")
