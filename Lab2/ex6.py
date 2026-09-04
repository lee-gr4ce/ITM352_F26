# This program prompts the user to enter their weight in pounds and then converts it to kilograms.
# Name: Grace Lee
# Date: 9-4-2026

# print("Your weight in kilograms is:", float(input("Enter weight in pounds: "))* 0.453592)

LBS_TO_KG = 0.453592 # constant for converting pounds to kilograms; never changes, so it is written in all caps
weight_in_lbs = input("Enter weight in pounds: ")
weight_in_lbs_float = float(weight_in_lbs)
weight_in_kg = weight_in_lbs_float * LBS_TO_KG # multiply the weight in pounds by the constant to get the weight in kilograms

print("You entered:", weight_in_lbs_float)
print("Your weight in kilograms is:", weight_in_kg)