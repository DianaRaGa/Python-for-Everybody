#Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. 
#If the score is between 0.0 and 1.0,print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
try:
    score=float(input("Please enter a score between 0.0 and 1.0: "))
    if score>=0.9:
        score="A"
    elif score>=0.8:
        score="B"
    elif score>=0.7:
        score="C"
    elif score>=0.6:
        score="D"
    else:
        score="F"
    print (f'{score}')
except ValueError:
    print ("Bad score")
