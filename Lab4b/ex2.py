# Properly format an inputted name in title case

# Name: Grace Lee
# Date: 9/18/26

raw_name = input("Enter your name: ")

stripped_name = raw_name.strip() # removes whitespace by default
# Output: Formatted name in title case is: Ick, Kazman
# .strip() only removes leading and trailing characters, not those in the middle of the string
title_case_name = stripped_name.title()
print(f"Formatted name in title case is: {title_case_name}")