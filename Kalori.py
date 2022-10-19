import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests import get

url = 'https://www.kaloricetveli.org/yiyecek/'
url_extended = url + 'Meyveler'
response = get(url_extended)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')


table1 = soup.tbody
count = len(table1)

Data=[]
Data1=[]
Data2=[]
Data3=[]
Data4=[]
Data5=[]
Data6=[]
Data=pd.DataFrame(None)

for i in range(count):
    list_2 = table1.find_all('td', class_ = 'food')
    list_3 = table1.find_all('td', class_ = 'kcal')
    list_4 = table1.find_all('td', class_='serving 100g')
    list_5 = table1.find_all('td', class_='kj')
    list_6 = table1.find_all('td', class_='serving portion')
    Data1.append(list_2[i].text)
    Data2.append(list_3[i].data.text)
    Data3.append(list_4[i].data.text)
    Data4.append(list_5[i].data.text)
    Data5.append(list_6[i].text)
    Data6.append(list_6[i].data.text)

Data['Meyve']=Data1
Data['Kcal']=Data2
Data['Kj']=Data4
Data['Serving']=Data3
Data['Portion']=Data5
Data['Portion (g)']=Data6
print(Data)