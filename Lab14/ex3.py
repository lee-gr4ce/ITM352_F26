# Scrape names of ITM faculty and grad students
import ssl
from urllib import request as req
from bs4 import BeautifulSoup

itm_url = "https://shidler.hawaii.edu/itm/people"
html = req.urlopen(itm_url, context=ssl.create_default_context())
doc = BeautifulSoup(html, "html.parser")

itm_names = []
# print(doc.prettify())

# Find all the faculty names that are in h2 tags with class = "title"
faculty = doc.find_all("h2", class_ = "title")

for person in faculty:
    itm_names.append(person.text)
    print("Faculty:", person.text)

print("Total Faculty:", len(itm_names))