shopping_list =  []
shopping_list.append("Apples") # add items to the list
shopping_list.append("Bananas")
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs ")
shopping_list.append(42)

print("Shopping List:", shopping_list)

shopping_list.remove("Milk") # remove AN item from the list
print("Updated Shopping List:", shopping_list)

shopping_list.pop() # remove the LAST thing on the list
print("Final Shopping List:", shopping_list)
