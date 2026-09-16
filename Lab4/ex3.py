# Manipulate a list in various tricky ways
# Name: Grace Lee
# Date: 9/16/26

response_values = [5, 7, 3, 8]
response_values.append(0)

print("Response values after appending 0:", response_values)

# response_values.insert(2,6)
# print("Response values after inserting 6 at index 2:", response_values)

# list slicing
response_values = response_values[:2] + [6] + response_values[2:]
# split the list into two parts (before the 3rd list item and after the 3rd list item) and insert 6 in between
print("Response values after slicing and inserting 6 at index 2:", response_values)

