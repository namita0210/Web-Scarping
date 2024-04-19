import requests
from bs4 import BeautifulSoup

url = "https://www.meesho.com/search?q=iphone&searchType=manual&searchIdentifier=text_search"

# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

spans = soup.select("p.sc-eDvSVe gQDOBc NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU NewProductCardstyled__StyledDesktopProductTitle-sc-6y2tys-5 ejhQZU")
print(spans)