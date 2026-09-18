# Get a URL from the user, clean it, and extract the domain name and TLD (top-level domain)
# Name: Grace Lee
# Date: 9/18/26

url = input("Enter a URL: ")

cleaned_url = url.replace("https://", "") # 2 conditions; what you want to replace and what you want to replace it with
# replacing "https://" with an empty string removes it from the URL
cleaned_url = cleaned_url.replace("/", "")
print("Cleaned URL:", cleaned_url)

parts = cleaned_url.split(".") # splits the string into a list of parts based on the "." character
print("The parts are:", parts)

domain_name = parts[1]
tld = parts[2]
print("Domain name:", domain_name)
print("TLD:", tld)

full_domain = domain_name + "." + tld
print("Full domain:", full_domain)