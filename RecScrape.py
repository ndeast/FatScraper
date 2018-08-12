from bs4 import BeautifulSoup
from urllib.request import urlopen
import UpRec


def createUpRec(self, recLink):
    page = urlopen(recLink)
    soup = BeautifulSoup(page, "html.parser")

    image = soup.find('meta', property='og:image')['content']
    artist = soup.find('h2', id='rectitle').a.string
    title = soup.find('h2', id='rectitle').span.contents[0]

    return UpRec.UpRec(artist, title, image, recLink)

