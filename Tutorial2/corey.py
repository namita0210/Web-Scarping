from bs4 import BeautifulSoup
import requests

url = 'https://www.patreon.com/coreyms'
path = 'Tutorial2/copyIndexSexy.html'

source = requests.get(url).text

soup = BeautifulSoup(source , 'lxml')

#print(soup.prettify())

container = soup.find('main') 
print(container.prettify())

