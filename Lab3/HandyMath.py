""""
Add three more handy math functions: 
a.	exponent, which takes two numbers, a base and an exponent, and returns the value when you raise the base to the power of the exponent. 
b.	max, which takes two numbers as input and returns the value of the larger one. Use the two comparison expressions or a conditional expression (do not use an if-statement)
c.	min, which takes two numbers as input and returns the value of the smaller one. Use the two comparison expressions or a conditional expression (do not use an if-statement). 
"""
# midpoint
def midpoint(num1, num2):

    return (num1 + num2) / 2

# square root
def square_root(num):
    return num ** 0.5

# exponent
def exponent(base, exp):
    return base ** exp

#max
def max(num1, num2):
    return num1 if num1 >= num2 else num2

#min
def min(num1, num2):
    return num1 if num1 <= num2 else num2

