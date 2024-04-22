from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3060-rtx-3060-ventus-2x-12g-oc/p/N82E16814137632"

r = requests.get(url)

soup = BeautifulSoup(r.text , 'html.parser')

prices = soup.find_all(["strong"], string ="289")
print(prices)
