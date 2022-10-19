import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.kaloricetveli.org/'
response = get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

divTag = soup.find_all("ul", {"class": "menu"})
# print((divTag))

for tag in divTag:
    tdTags = tag.find_all("a", {"href": True})
    for tag in tdTags:
        print(tag.text)
        # print(tag['href'])
        # print(tag.text, '  ||  ',tag['href'])

