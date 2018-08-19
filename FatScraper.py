from UpcomingRecord import Base, UpcomingRecord, UpcomingRecordSchema
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

schema = UpcomingRecordSchema(many=True)

upRecs = FatWreckScraper.scrape()

for rec in upRecs:
    session.add(rec)
session.commit()

recDB = session.query(UpcomingRecord).all()

jsonOutput = schema.dumps(recDB)
with open("UpcomingRecords.txt", 'w') as outFile:
    outFile.write(jsonOutput)

session.close()
engine.dispose()
