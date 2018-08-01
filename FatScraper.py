from bs4 import BeautifulSoup
from urllib.request import urlopen

fatwreck = "https://fatwreck.com"

page = urlopen(fatwreck)

soup = BeautifulSoup(page, "html.parser")

soup.find_all('uprec_div')

uprecs = soup.find_all('p', class_='uprec')

first = uprecs[0]

firstTitle = first.find('a', 'title')
href = fatwreck + firstTitle.get('href')

print(href)

