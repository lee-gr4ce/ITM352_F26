"""
Write Python code that creates a list with a variety of different values. 
Print different messages whether the list contains fewer than 5 elements, between 5 and 10 (inclusive), 
and more than 10 elements. 
Name: Grace Lee
"""

fruits = ["strawberry", "pineapple", "apple", "pear", "banana", "lychee", "grape", "watermelon", "mango", "coconut", "peach"]

def describe_list_size(items):
    if len(items) < 5:
        return "The list contains fewer than 5 elements."
    elif len(items) <= 10:
        return "The list contains between 5 and 10 elements."
    else:
        return "The list contains more than 10 elements."

print(len(fruits))
print(describe_list_size(fruits))

test_cases = [
    [[], "The list contains fewer than 5 elements."],
    [["apple"] * 4, "The list contains fewer than 5 elements."],
    [["apple"] * 5, "The list contains between 5 and 10 elements."],
    [["apple"] * 10, "The list contains between 5 and 10 elements."],
    [["apple"] * 11, "The list contains more than 10 elements."],
]

for test_list, expected_message in test_cases:
    actual_message = describe_list_size(test_list)
    print(f"{len(test_list)} items: {actual_message}")
    assert actual_message == expected_message



