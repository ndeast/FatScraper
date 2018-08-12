from bs4 import BeautifulSoup
from urllib.request import urlopen
import UpRec

# Open and parse page
fatwreck = "https://fatwreck.com"
page = urlopen(fatwreck)
soup = BeautifulSoup(page, "html.parser")

# store upcoming records
uprecs = soup.find_all('p', class_='uprec')

for rec in uprecs:
    recLink = fatwreck + rec.find('a', 'title').get('href')
    



