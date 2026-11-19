# Scrape data from the City of Chicago's data  portal
# Print any line with a <title> tag in it

import urllib.request

url = "https://data.cityofchicago.org/Historic-Preservation/Landmark-Districts/zidz-sdfj/about_data"\

print("Retrieving", url)
response = urllib.request.urlopen(url)

for line in response:
    line = line.decode("utf-8").strip()
    if "<title>" in line:
        print(line)