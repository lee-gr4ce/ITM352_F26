amount = 87

penny = 1
nickel = 5
dime = 10
quarter = 25

num_quarter = round(amount/quarter)
remainder = amount - (num_quarter * quarter)

num_dime = round(remainder/dime)
remainder = remainder - (num_dime * dime)

num_nickel = round(remainder/nickel)
remainder = remainder - (num_nickel * nickel)

num_penny = round(remainder/penny)
remainder = remainder - (num_penny * penny)

print(remainder)
print(f"{num_quarter} quarters, {num_dime} dimes, {num_nickel} nickels, {num_penny} pennies")
