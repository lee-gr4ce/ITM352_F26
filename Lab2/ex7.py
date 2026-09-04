# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Name: Grace Lee
# Date: 9-4-2026

farenheit_input = input("Enter a temperature in Fahrenheit: ")
fareinheit_float = float(farenheit_input)

celsius_value = (fareinheit_float - 32) * 5/9

celsius_value = round(celsius_value, 2) # rounding is losing information

print("You entered:", fareinheit_float)
print("The temperature in Celsius is:", celsius_value)