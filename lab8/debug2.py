# Calculating a shopping cart
prices = [5.95, 3.00, 12.50]
total_price = 0
tax_rate = 1.08    # 8% tax 
for price in prices:
    total_price += price * tax_rate # it is not calculating the total price, just overwriting the last iteration to the variable
    print(total_price)

print(f"Total price (with tax): ${total_price}")
