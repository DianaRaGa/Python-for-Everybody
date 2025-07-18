#This code is to automate and handle opening files with a .txt extension for reading files and expecting errors
# to make the code look cleaner

def open_texts():
    while True:
        filename = input("Please enter a file name you wish to open\nEnter 'exit' to quit the program:\n").rstrip()#Asking
        # for the file from the user or exiting the file
        if filename.lower() == "exit":#This is to break the code if the user wishes that
            print("Exiting the program")
            file.close() #This needs to go at the end
            break
        
        elif ".txt" not in filename: #I find putting .txt is something I forget often, this is to avoid an error
            filename += ".txt"
        
        try:#Handles cases where the file might not be found
            file= open(filename)
            return file
        
        except FileNotFoundError:#Makes the announcement of the error that the file they typed is
            # not found and makes the loop until they have a working file or they give up
            print(f"Error file '{filename}' not found, please try again\n")
            