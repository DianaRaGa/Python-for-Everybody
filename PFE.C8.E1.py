#Exercise 1: Write a function called chop that takes a list and modifies it, removing the first and last elements,
# and returns None. Then write a function called middle that takes a list and returns a new list that contains all
# but the first and last elements.

def middle(n):
    return n[1:-1]

def chop(n):
    n[:] = n[1:-1]

while True:
    data = input('''Hi! this program was created to practice modifying and creating new list from an existing one
to get started please enter more than 3 objects divided by a coma (,)
(If you wish to exit the program write 'exit'): \n''')
    t = data.split(",")

    if data == "exit":
        print(f"You selected to exit the program\nThank you!")
        sys.exit()
    elif len(t) >= 3:
        break
    else:
        print(f"You have enter less than 3 objects or are not separated by a coma\nPlease try again")
        continue
while True:
    question = input('''What do you want to do to this list?
Please chose from the options by writing the numbers for the desired option
1) Modify the list removing the first and last element, returning None
2) Return a new list that contains all but the first and last elements
(If you wish to exit the program write 'exit')\n''').strip().lower()
    if question=="exit":
            print(f"You selected to exit the program\nThank you!")
            break
            
    try:
        question=float(question)
    
        if question == 1:
            print(f"You selected option 1 Modify the list removing the first and last element, returning None to your list '{t}'")
            resultado = chop(t)
            print (f"Now your list is '{t}' that returns '{resultado}'")
            break
        elif question == 2:
            print(f"You selected option 2 Return a new list that contains all but the first and last elements to your list")
            resultado = middle(t)
            print(f"Your original list '{t}' stayed the same and know you have a second list '{resultado}' with the changes")
            break
    except ValueError:
        print("You did not selected a valid option, please try again")
        continue #Para seguir preguntando para que seleccione bien las opciones
        