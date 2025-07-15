#Exercise 3:
#Sometimes when programmers get bored or want to have a bit of fun, they add a
#harmless Easter Egg to their program. Modify the program that prompts the user
#for the file name so that it prints a funny message when the user types in the exact
#file name “na na boo boo”. The program should behave normally for all other files
#which exist and don’t exist. Here is a sample execution of the program:

while True:
    file = input("Please enter the name of a text file (or type 'exit' to quit):\n").strip()
    
    if file.lower() == "exit":
        print("Exiting program.")
        break
    
    if ".txt" not in file:
        file += ".txt"

    easter = file.find("na na boo boo")
    if easter != -1:
        print ("NA NA BOO BOO TO YOU - You have been punk'd!\n")
        continue
        
    try:
        count = 0
        with open(file) as text:  # Ensures the file is properly closed after reading
            for line in text:
                count += 1  # Counts the total of lines in the text
        print(f"There were {count} subject lines in {file}")
        break  # Exit the loop when successful
    except FileNotFoundError:
        print("File not found. Please try again.\n")
