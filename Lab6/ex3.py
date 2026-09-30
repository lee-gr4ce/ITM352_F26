"""Write the Python conditional logic to determine a movie price for a theater chain. The applicable business rules are:
- The normal price is $14
- If someone is 65 or older, they pay $8.
- If it is Tuesday, the price is $10.
- If it is a matinee, the price is $5 for seniors and $8 otherwise
# Name = Grace Lee
# Date = 9/25/26
"""
# should always set a default value of a variable; good practice
age = 22
day = "Tuesday"
matinee = True

price = 14

if day == "Tuesday":
    price = 10

if age >= 65:
    price = 8

if matinee:
    if age >= 65:
        price = 5
    else:
        price = 8
# if statements are mutually exclusive; so 3 if-statements are necessary bc elifs can only be used if the first condition is false

print(f"Day: {day}, Matinee: {matinee}")
if (age >= 65):
    print("Welcome, senior")
else:
    print("Welcome, non-senior")
print("Ticket price is $", price)