#Exercise 1: Write a program to read through a file and print the contents of the file (line by line)
# all in upper case.

while True:
    file = input(f"Please enter the name of a text file: ").rstrip()
    dot = file.find(".txt")
    print(dot)
    if dot == -1:
        file +=".txt"
    try:
        text = open(file)
        for line in text:
            print(line.upper())
        break
    except FileNotFoundError:
        print("File not found. Please try again.")
