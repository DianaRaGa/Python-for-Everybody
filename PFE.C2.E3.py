#Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay
hours=input('Please enter the Hours: ')
rate=input('Please enter the Rate: ')
hours=float(hours)
rate=float(rate)
pay=hours*rate
print('Pay: '+ str(pay))
