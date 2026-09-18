# Parse through the portions of an email address and print out the username and domain name.
# Name: Grace Lee
# Date: 9/18/26

# Method 1: Using split() method
email_address = input("Enter an email address: ")
username = email_address.split("@")[0] # splits the string into a list of parts based on the "@" character and takes the first part
domain_name = email_address.split("@")[1]

# parts = email_address.split("@")
# username = parts[0]
# domain_name = parts[1]

print("Username:", username)
print("Domain name:", domain_name)

# Method 2: Using index and slicing
at_sign_index = email_address.index("@") # finds the index of the "@" character in the string
username2 = email_address[:at_sign_index]
domain2 = email_address[at_sign_index + 1:]
# slicing does not include the character at the end index
print("Username (method2):", username2)
print("Domain name (method2):", domain2)