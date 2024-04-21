from bs4 import BeautifulSoup
import requests

url = 'https://www.patreon.com/coreyms'
path = 'Tutorial2/copyIndexSexy.html'

r = requests.get(url)
print(r.text)

with open (r.text) as f:
    soup = BeautifulSoup(f, 'lxml')
    print(soup.prettify())
 


