from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError, HTTPError
from datetime import datetime, date
import UpcomingRecord


def scrape():
    uprecList = []
    # Open and parse homepage
    fatwreck = "https://fatwreck.com"
    if url_is_good(fatwreck):
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
    if url_is_good(recLink):
        page = urlopen(recLink)
        soup = BeautifulSoup(page, "html.parser")

        imageLink = soup.find('meta', property='og:image')['content']
        image = saveAlbumArt(imageLink, recLink)
        artist = soup.find('h2', id='rectitle').a.string.strip()
        title = soup.find('h2', id='rectitle').span.contents[0].strip()
        releaseDate = soup.find(
            id='rright').b.string.replace('RELEASE DATE: ', "")
        releaseDate = datetime.strptime(releaseDate, '%B %d, %Y').date()

        upRec = UpcomingRecord.UpcomingRecord(artist, title, image, recLink)
        upRec.release_date = releaseDate
        return upRec


def saveAlbumArt(imageLink, link):
    if url_is_good(imageLink):
        urlretrieve(imageLink, "artwork/" + link.rsplit('/', 1)[-1] + ".jpg")
        return ("/artwork/" + link.rsplit('/', 1)[-1] + ".jpg")


# Better than just checking error codes which doesn't help
# when the server is down.
# taken from: https://stackoverflow.com/a/38145622
def url_is_good(url):
    try:
        response = urlopen(url)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        return True       