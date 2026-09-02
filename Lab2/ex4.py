# Ask the user to enter a decimal number. Calculate the square of that number, round it to 2 decimal places, and print it out.
# Name: Grace Lee
# Date: 9-2-2026

input_value = input("Enter a floating point number: ")
float_value = float(input_value) # float changes the string text to a floating point number so we can do math with it
squared_value = float_value ** 2 
round_value = round(squared_value, 2) # round changes the squared value to a floating point number rounded to 2 decimal places

print("You entered:", float_value)
print("The square of the number you entered is:", squared_value)
print("The rounded square of the number you entered is:", round_value)