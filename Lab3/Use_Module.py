"""
Create a new file, call it Use_Module.py, that imports HandyMath.py, asks for two numbers from a user, and prints out the midpoint of those numbers, the square root of the square of one number, the result when raising one number to the exponent of the other, and finally the max and min of the numbers. 
Use the Python f-string capability to format these strings. 
"""

import HandyMath as hm

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"The midpoint of {num1} and {num2} is: {hm.midpoint(num1, num2)}") # midpoint
print(f"The square root of the square of {num1} is: {hm.square_root(num1 ** 2)}") # square root
print(f"{num1} raised to the power of {num2} is: {hm.exponent(num1, num2)}") # exponent
print(f"The maximum of {num1} and {num2} is: {hm.max(num1, num2)}") # maximum
print(f"The minimum of {num1} and {num2} is: {hm.min(num1, num2)}") # minimum