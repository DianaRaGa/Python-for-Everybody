#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
try:
    hours=float(input('Please enter the Hours: '))
    rate=float(input('Please enter the Rate: '))
    if hours>40:
        pay=(40*rate)+((hours-40)*(rate*1.5))
    
    else:
        pay=hours*rate
    
    print(f"Pay : {pay:.2f}")
except ValueError:
    print("Error, please enter numeric input")