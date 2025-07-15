#Exercise 6:
#Rewrite the program that prompts the user for a list of numbers and prints out the maximum and minimum of the numbers
# at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and use
# the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
#I already did this program from the book PFE chapter 5 exercise 2 and did this calculation with the max and min
# function of list instead of a loop, so the code is the same

numbers = []
while True: #Did everything on a loop to get a valid list with numbers from the user
    number=input("Please enter a number:\nor 'done' to end the calculations\n").strip() #ask for done to stop the list
 
    #This section handles all the calculations when the list of data is set
    if number.lower() == "done":
        if numbers: #This condition checks if there are numbers in the list to make the calculations,
            # if not gets out of the code, I wish to have this return to the beginning, but the user should know if
            # they press done
            total=sum(numbers)
            count=len(numbers)
            maximum=max(numbers)
            minimum=min(numbers)
            print(f"Total: {total}\nCount: {count}\nMax: {maximum}\nMin: {minimum}") #Change the presentation with the \n
            # character so it looks better
        else:
            print ("No numbers were entered.")
        break
        
    try:
        number=float(number)
        numbers.append(number)
    except ValueError:
        print("Error: Please enter a valid numeric value.\n")
        