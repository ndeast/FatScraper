from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import URLError, HTTPError
from datetime import datetime, date
import datefinder
import UpcomingRecord


def scrape(current_rec_links):
    uprecList = []
    # Open and parse homepage
    fatwreck = "https://fatwreck.com"
    newreleases = "https://fatwreck.com/collections/all-releases?sort_by=created-descending"
    if url_is_good(newreleases):
        page = urlopen(newreleases)
        soup = BeautifulSoup(page, "html.parser")

        # store new releases not in database
        uprecs = soup.find_all('div', class_='fat-list-product')
        for rec in uprecs:
            recLink = fatwreck + rec.find(
                'a', 'fat-list-product--image').get('href')
            if recLink not in current_rec_links:
                record = createUpRec(recLink)
                uprecList.append(record)
        return uprecList


def createUpRec(recLink):
    if url_is_good(recLink):
        page = urlopen(recLink)
        soup = BeautifulSoup(page, "html.parser")

        imageLink = "https:" + soup.find(
            'meta', itemprop='image')['content']
        image = saveAlbumArt(imageLink, recLink)
        artist = soup.find('meta', itemprop='brand')['content']
        title = soup.find('meta', itemprop='name')['content']
        description = soup.find(
            'meta', itemprop='description')['content'].split(' ', 1)[-1]
        dates = datefinder.find_dates(description)
        releaseDate = next(dates).date()

        upRec = UpcomingRecord.UpcomingRecord(
            artist, title, image, recLink)
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
    except HTTPError:
        return False
    except URLError:
        return False
    except:
        return False
    return True
