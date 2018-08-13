from bs4 import BeautifulSoup
from urllib.request import urlopen
from marshmallow import pprint
from UpRec import UpRecSchema
import UpRec
import RecScrape

uprecList = []
schema = UpRecSchema(many=True)
newRelease = False

# TODO: replace saving to file with SQLite DB
#       add deleted flag and release date to UpRec

# # open and read json outfile
# with open("UpcomingRecords.txt", 'r') as inFile:
#     text = inFile.read()
#     if (text):
#         currentUpRecs = schema.loads(text)

# Open and parse page
fatwreck = "https://fatwreck.com"
page = urlopen(fatwreck)
soup = BeautifulSoup(page, "html.parser")

# store upcoming records if not already obtained
uprecs = soup.find_all('p', class_='uprec')
for rec in uprecs:
    recLink = fatwreck + rec.find('a', 'title').get('href')
    record = RecScrape.createUpRec(recLink)
    uprecList.append(record)
    newRelease = True

if newRelease:
    jsonOutput = schema.dumps(uprecList)
    with open("UpcomingRecords.txt", 'w') as outFile:
        outFile.write(jsonOutput)
