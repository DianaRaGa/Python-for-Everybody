#Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

try:
    hours = float(input('Please enter the Hours: '))
    rate = float(input('Please enter the Rate: '))
    if hours>40:
        pay=(40*rate)+((hours-40)*(rate*1.5))
    else:
        pay=hours*rate
    print(f"Pay : {pay:.2f}")

except ValueError:
    print("Please enter numeric values")