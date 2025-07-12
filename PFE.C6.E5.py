#Exercise 5: Slicing strings
#Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence: 0.8475'
#Use find and string slicing to extract the portion of the string after the colon
#character and then use the float function to convert the extracted string into a
#floating point number.

str = 'X-DSPAM-Confidence: 0.8475'
double_point = str.find(":")
numero = float(str[double_point + 1:])
print(f"The extracted number '{numero}' from '{str}' is a '{type(numero)}'")
