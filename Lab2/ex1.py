value_entered = input("Enter a value between 1 and 100: ")
value_as_integer = int(value_entered) # integer changes the string text to an integer so we can do math with it

value_squared = value_as_integer ** 2 # ** is the exponent operator, so this is value_as_integer to the power of 2

print("You entered:", value_as_integer)
print("The value squared is:", value_squared)

print(f"You entered: {value_as_integer} and the square of that value is: {value_squared}") # f-string allows us to put variables inside a string