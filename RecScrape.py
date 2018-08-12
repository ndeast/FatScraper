from bs4 import BeautifulSoup
from urllib.request import urlopen
import UpRec

# def createUpRec(self, recLink):
#     page = urlopen(recLink)
#     soup = BeautifulSoup(page, "html.parser")
recLink = "https://fatwreck.com/record/detail/106"
page = urlopen(recLink)
soup = BeautifulSoup(page, "html.parser")

print(soup.find('meta', property='og:image'))

print(soup.find('h2', id='rectitle'))
    
