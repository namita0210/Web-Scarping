from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/Tutorial2/index.html'
path = 'Tutorial2/copyIndex.html'

def saveFile(url , path): #Save url as file and then get its contents
    r = requests.get(url)
    with open (path , "w" , encoding='UTF-8') as f:
        f.write(r.text)

#saveFile(url , path)

with open('index.html') as f: #Get the contents from html file with lxml parser
    soup = BeautifulSoup(f, 'lxml')

#print(soup)

r = requests.get(url)  #Get the contents from url
#print(r.text)

