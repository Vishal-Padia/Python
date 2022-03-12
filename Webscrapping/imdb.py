import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.imdb.com/chart/top/')
soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select("Table tbody tr td.titleColumn a")
first50 = links[:50]
for anchor in first50:
    print(anchor.text)