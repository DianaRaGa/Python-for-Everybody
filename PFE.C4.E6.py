#Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which
# takes two parameters (hours and rate).

def computepay (hours,rate):
    if hours <= 40 and hours > 0:
        pay = hours * rate
        print(pay)
        
    else:
        overtime_hours = hours - 40
        overtime_rate = rate * 1.5
        pay = 40 * rate + overtime_hours * overtime_rate
        print(f'Pay: ${pay}')
        
try:
    hours = float(input("Please enter the worked hours: "))
    rate = float(input("Please enter the rate: "))
    computepay(hours,rate)
    
except ValueError:
    print("Error in the computed parameters, please try again with number only")
