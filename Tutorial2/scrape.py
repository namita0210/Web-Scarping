from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/Tutorial2/index.html'
path = 'Tutorial2/copyIndex.html'

def saveFile(url , path):
    r = requests.get(url)
    with open (path , "w" , encoding='UTF-8') as f:
        f.write(r.text)

saveFile(url , path)