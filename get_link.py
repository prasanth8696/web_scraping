import sys

import requests

from bs4 import BeautifulSoup

url = input('enter ')
try :
 response = requests.get(url)
except :
 sys.exit('request timed out')


soup = BeautifulSoup(response.text,'lxml')

links = soup.find_all('a',href=True)
k=0
for link in links :
  print(link.text)
  print()
  print(link['href'])
  print()
  k += 1
  if k == 35 :
    break



