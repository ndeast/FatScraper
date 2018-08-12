from bs4 import BeautifulSoup
from urllib.request import urlopen
import UpRec


def createUpRec(recLink):
    page = urlopen(recLink)
    soup = BeautifulSoup(page, "html.parser")

    image = soup.find('meta', property='og:image')['content']
    artist = soup.find('h2', id='rectitle').a.string.strip()
    title = soup.find('h2', id='rectitle').span.contents[0].strip()

    return UpRec.UpRec(artist, title, image, recLink)
