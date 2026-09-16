first_name = input("Enter your first name: ")
middle_initial = input("Enter your middle initial: ")
last_name = input("Enter your last name: ")

# full_name = first_name + middle_initial + last_name
# output = Your full name is: GraceWLee

full_name = first_name + " " + middle_initial +". " + last_name
print("Your full name is:", full_name)

print(f"Your full name using f-strings is: {first_name} {middle_initial}. {last_name}")
# python is just replacing the variables with their values. Since the variables are strings, it is just concatenating them together.

print("Your full name using percent notation is %s %s. %s" % (first_name, middle_initial, last_name)) # % notation

print("Your full name using .format is {} {}. {}".format(first_name, middle_initial, last_name)) # .format() notation

print("Your full name using .join is " + " ".join([first_name, middle_initial + ".", last_name])) # .join() notation
# .join() concatenates the strings in the list with a space in between each string. "." is appended into the list to add a period after the middle initial.

