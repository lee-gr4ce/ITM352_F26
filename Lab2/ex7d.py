# This program prompts the user to enter a temperature in Fahrenheit and then converts it to Celsius.
# Create the conversion as a function
# Name: Grace Lee
# Date: 9-4-2026

def F_to_C(farenheit):
    celsius_value = (farenheit - 32) * 5/9
    rounded_celsius = round(celsius_value, 2) # rounding is losing information
    return rounded_celsius

farenheit_input = input("Enter a temperature in Fahrenheit: ")
fareinheit_float = float(farenheit_input)

celsius_value = F_to_C(fareinheit_float)

print("You entered:", fareinheit_float)
print("The temperature in Celsius is:", celsius_value)