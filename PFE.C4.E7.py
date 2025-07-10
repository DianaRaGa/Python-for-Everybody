#Exercise 7: Rewrite the grade program from the previous chapter using a function called computegrade that takes a score
# as its parameter and returns a grade as a string.

def computegrade(score):

    if score < 0 or score > 1.0:
        return "Error: Score out of range, it must be between 0.0 and 1.0"
    elif score  >= 0.9:
        return "A"
        
    elif score >= 0.8:
        return "B"
        
    elif score >= 0.7:
        return "C"
        
    elif score >= 0.6:
        return "D"
        
    elif score < 0.6:
        return "F"

while True:
    try:
        score=input("Please enter the score or out to end the program: ")

        if score.lower() == "out":
            break
        
        result = computegrade(float(score))
        
        if result == "Error: Score out of range, it must be between 0.0 and 1.0":
            print ("Please enter a number between 0.0 and 1.0\n")
            continue
        
        print (f"Grade: {result}")
        break
        
    except ValueError:
        print ("Error: Please enter a valid numeric value\n")
        