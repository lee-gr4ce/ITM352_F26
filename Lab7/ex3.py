
data = ("hello", "10", "goodbye", 3, "goodnight", 5)
user_input = input("Enter a value to add to the tuple: ")

try:
    data.append(user_input)
except AttributeError:
    data = list(data)
    data.append(user_input)
    data = tuple(data)

print(data)

string_count = 0

for item in data:
    if type(item) == str:
        string_count += 1

print(f"There are {string_count} strings in the tuple.")

