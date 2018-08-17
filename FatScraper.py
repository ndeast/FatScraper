from UpcomingRecord import Base, UpcomingRecord
import FatWreckScraper
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Connect to DB and create session
engine = create_engine('sqlite:///db/UpcomingRecords.db')
Base.metadata.bind = engine

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
###################################

upRecs = FatWreckScraper.scrape()

for rec in upRecs:
    session.add(rec)
session.commit()

recDB = session.query(UpcomingRecord).all()

for rec in recDB:
    print(rec.artist + " " + rec.title)

session.close()
engine.dispose()
