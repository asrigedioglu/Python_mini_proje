#HABER ÇEKME

import requests
from bs4 import BeautifulSoup

url = "https://www.sondakika.com/magazin/"

response = requests.get(url)
response

haberler=response.content
soup = BeautifulSoup(haberler,"html.parser")

haberler= soup.find_all("span",{"class":"title"})

haber_liste= []
for h in haberler:
   print(h.text)
   haber_liste.append(h.text)
    
haber_liste



    