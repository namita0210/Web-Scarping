import requests

url = "https://timesofindia.indiatimes.com/city/delhi"

def saveToFile(url, path):    
    r = requests.get(url)
    with open (path , "w", encoding="UTF-8") as f:
        f.write(r.text)

saveToFile(url , "data/times.html")        
