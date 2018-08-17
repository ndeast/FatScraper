from bs4 import BeautifulSoup
from urllib.request import urlopen
import UpcomingRecord


def scrape():
    uprecList = []
    # Open and parse homepage
    fatwreck = "https://fatwreck.com"
    page = urlopen(fatwreck)
    soup = BeautifulSoup(page, "html.parser")

    # store upcoming records
    uprecs = soup.find_all('p', class_='uprec')
    for rec in uprecs:
        recLink = fatwreck + rec.find('a', 'title').get('href')
        record = createUpRec(recLink)
        uprecList.append(record)
    return uprecList


def createUpRec(recLink):
    page = urlopen(recLink)
    soup = BeautifulSoup(page, "html.parser")

    image = soup.find('meta', property='og:image')['content']
    artist = soup.find('h2', id='rectitle').a.string.strip()
    title = soup.find('h2', id='rectitle').span.contents[0].strip()
    releaseDate = soup.find(id='rright').b.string.replace('RELEASE DATE: ', "")

    upRec = UpcomingRecord.UpcomingRecord(artist, title, image, recLink)
    upRec.release_date = releaseDate
    return upRec
