from bs4 import BeautifulSoup
import requests

url = 'http://127.0.0.1:5500/Tutorial2/index.html'
path = 'Tutorial2/copyIndex.html'

def saveFile(url , path): #Save url as file and then get its contents
    r = requests.get(url)
    with open (path , "w" , encoding='UTF-8') as f:
        f.write(r.text)

#saveFile(url , path)

r = requests.get(url)  #Get the contents from url
#print(r.text)

with open('index.html') as f: #Get the contents from html file with lxml parser
    soup = BeautifulSoup(f, 'lxml')

#print(soup.prettify())

#get the title
match = soup.title
# print(match.text)

#get all the divs
divs = soup.div
#print(divs)

article = soup.find_all('div' , class_='article')

for i,a in enumerate(article):
    print(i ,' ',a,'\n\n')

    headline = a.h2.a.text
    print('\n',headline)

    summary = a.p.text
    print('\n',summary,'\n---------------------------------------')


