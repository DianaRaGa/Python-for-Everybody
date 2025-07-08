#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay
hours=input('Please enter the Hours: ')
rate=input('Please enter the Rate: ')
try:
    hours=float(hours)
    rate=float(rate)
    pay = hours * rate
    print(f"Pay: {str(pay)}")
except (TypeError, ValueError) as e:
    print("Please enter numeric values to avoid errors")
