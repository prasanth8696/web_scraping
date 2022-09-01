import sys
import requests
from bs4 import BeautifulSoup 
url_list = input('enter 1tamilmv url or tamilblasters url : ')
try :
  url_list = url_list.split('www.')
  url = ''.join(url_list)
except :
  url = url_list
try :
  response = requests.get(url,timeout=10).text
except :
  sys.exit('request timed out...')
soup = BeautifulSoup(response,'lxml')

#print(soup.prettify())

article = soup.find('div',class_='cPost_contentWrap')

#scrape torrent file links
for anker in  article.find_all('a',href=True) :
 try :
  print(anker.text)
  print()
  print(anker['href'])
  print()
 except :
   pass


