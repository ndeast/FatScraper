from UpcomingRecord import Base, UpcomingRecord, UpcomingRecordSchema
import FatWreckScraper
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker


newRelease = False
# Connect to DB and create session
engine = create_engine('sqlite:///db/UpcomingRecords.db')
Base.metadata.bind = engine

schema = UpcomingRecordSchema(many=True)

DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
###################################
#
# Pull existing titles and links
current_rec_titles = [rec.title for rec in session.query(UpcomingRecord.title)]
current_rec_links = [rec.link for rec in session.query(UpcomingRecord.link)]
upRecs = FatWreckScraper.scrape(current_rec_links)
###################################
# 
if upRecs is not None:
    for rec in upRecs:
        if rec.title not in current_rec_titles:
            session.add(rec)
            session.commit()
            newRelease = True
            print(rec)

# output new releases to json file
if newRelease:
    updated_recDB = session.query(UpcomingRecord).all()

    jsonOutput = schema.dumps(updated_recDB)
    with open("UpcomingRecords.json", 'w') as outFile:
        outFile.write(jsonOutput)


session.close()
engine.dispose()
