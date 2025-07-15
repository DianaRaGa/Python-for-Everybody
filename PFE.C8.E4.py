#Exercise 4: Find all unique words in a file
#Create a list of unique words, which will contain the final result.
# For each line, split the line into a list of words using the split function. For each word,
# check to see if the word is already in the list of unique words. If the word is not in the list of unique words,
# add it to the list. When the program completes, sort and print the list of unique words in alphabetical order.

while True:
    filename=input("Please enter a file name to check for unique words\nEnter 'exit' to quit the program:\n").rstrip()
    if filename.lower() == "exit":
        print("Exiting the program")
        break
        
    elif ".txt" not in filename:
        filename += ".txt"
        
    try:
        with open(filename) as text:
            unique_words = []
            for lines in text:
                words = lines.split()
                if len(words) <= 0: continue
                for word in words:
                    if word not in unique_words:
                        unique_words.append(word)
                    else:continue
            unique_words.sort()
            print(f"This is the list of sorted unique words {"\n".join(unique_words)}")
            
            
    except FileNotFoundError:
        print("File not found. Please try again.\n")
        