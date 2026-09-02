# Ask the user to enter their birth year. Calculate their age based on the current year and print it out.
# Name: Grace Lee
# Date: 9-2-2026

birth_year = input("Enter your birth year: ")
current_year = 2026
age = current_year - int(birth_year)
print(f"You entered: {birth_year}")
print(f"Your age is: {age} years old.")

print("Your age is: " + str(age) + " years old.") # Concatenation allows us to combine strings and variables into one string