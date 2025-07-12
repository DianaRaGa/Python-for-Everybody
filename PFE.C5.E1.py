#Exercise 1: Write a program which repeatedly reads integers until the user enters “done”.
# Once “done” is entered, print out the total, count, and average of the integers.
# If the user enters anything other than a integers, detect their mistake using try and except
# and print an error message and skip to the next integers.

import statistics
numbers=[]

while True:
    number=input("Please enter a number or done to finish: ")
    if number=="Done":
        print(f"Total: {total} Count: {count}  Average: {average}")
        break
        
    try:
        number=float(number)
        numbers.append(number)
        total=sum(numbers)
        count=len(numbers)
        average=statistics.mean(numbers)
        
    except ValueError:
        print ("Error: Please enter a valid numeric number\n")
        