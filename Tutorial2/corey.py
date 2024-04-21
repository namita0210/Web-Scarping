from bs4 import BeautifulSoup
import requests

url = 'https://www.patreon.com/coreyms'
path = 'Tutorial2/corey.html'

def saveToFile(url, path):
    r = requests.get(url)
    with open (path , "w", encoding='UTF -8') as f:
        f.write(r.text)

#saveToFile(url,path)        

