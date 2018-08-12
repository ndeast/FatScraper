from bs4 import BeautifulSoup
from urllib.request import urlopen
from marshmallow import pprint
from UpRec import UpRecSchema
import UpRec
import RecScrape

uprecList = []
schema = UpRecSchema()

# Open and parse page
fatwreck = "https://fatwreck.com"
page = urlopen(fatwreck)
soup = BeautifulSoup(page, "html.parser")

# store upcoming records
uprecs = soup.find_all('p', class_='uprec')
for rec in uprecs:
    recLink = fatwreck + rec.find('a', 'title').get('href')
    record = RecScrape.createUpRec(recLink)
    uprecList.append(record)

# Export upcoming records in json to file
try:
    outfile = open("UpcomingRecords.txt", "w")
    for uprec in uprecList:
        result = schema.dumps(uprec)
        pprint(result, outfile)
finally:
    outfile.close()

