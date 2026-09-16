# Define a list of survey response values (5, 7, 3, 8) and store them
# In a variable, define a tuple of response IDs (1012, 1015, 1021, and 1053)
# Add these to the list

"""
Name: Grace Lee
Date: 9/16/26
"""

response_values = [5, 7, 3, 8]
response_values.sort() # sorts the list in ascending order
response_ids = (1012, 1015, 1021, 1053)
response_values.append(response_ids)

print("Combined response values and IDs:", response_values)

response_values_new = [(1012,5), (1015,7), (1021,3), (1053,8)]
print("Combined response values and IDs as tuples:", response_values_new)