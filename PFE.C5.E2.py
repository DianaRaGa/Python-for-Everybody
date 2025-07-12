#Exercise 2: Write another program that prompts for a list of numbers as above and at the end
#prints out both the maximum and minimum of the numbers instead of the average.

numbers=[]
while True:
    number=input("Please enter a number: ").strip()
    
    if number.lower()=="done":
        if numbers:
            total=sum(numbers)
            count=len(numbers)
            maximum=max(numbers)
            minimum=min(numbers)
            print(f"Total: {total}, Count: {count}, Max: {maximum}, Min: {minimum}")
        else:
            print ("No numbers were entered.")
        break
        
    try:
        number=float(number)
        numbers.append(number)
    except ValueError:
        print("Error: Please enter a valid numeric value.\n")
        