"""
Add a function to your HandyMath module that takes two numbers x,y and a function name as arguments then returns a string “The function <function name> x,y = <function applied to x,y>”. 
You can use .__name__ to get the identifier of a variable. 
Try this out for min, max, and exponent. 
"""

from HandyMath import max, min, exponent

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
func = input("Enter the function name (max, min, exponent): ")

functions = {
    "max": max,
    "min": min,
    "exponent": exponent
}

selected_function = functions[func]

def describe_function(x, y, function):
    return f"The function {function.__name__}({x}, {y}) = {function(x, y)}"

print(describe_function(x, y, selected_function))
