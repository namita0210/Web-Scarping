import requests
from bs4 import BeautifulSoup

with open("sample.html" , "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc , 'html.parser')    
#print(soup.prettify())


ulTag = soup.new_tag("ul")
liTag = soup.new_tag("li")
ulTag.append(liTag)

liTag = soup.new_tag("li")
liTag.string="About"
ulTag.append(liTag)

soup.html.body.insert(0, ulTag)
with open("modified.html", "w") as f:
    f.write(str(soup))