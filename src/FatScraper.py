from os import mkdir
from UpcomingRecord import Base, UpcomingRecord, UpcomingRecordSchema
import FatWreckScraper
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker
from datetime import datetime, date

def main():
    newRelease = False
    newReleases = 0
    # Connect to DB and create session
    engine = create_engine('sqlite:////FatScraper/output/db/UpcomingRecords.db')
    Base.metadata.bind = engine

    schema = UpcomingRecordSchema(many=True)

    DBSession = sessionmaker()
    DBSession.bind = engine
    session = DBSession()

    ###################################
    # Pull existing titles and links
    current_rec_titles = [rec.title for rec in session.query(UpcomingRecord.title)]
    current_rec_links = [rec.link for rec in session.query(UpcomingRecord.link)]
    ###################################
    
    #  Scrape releases and add new releases to session
    upRecs = FatWreckScraper.scrape(current_rec_links)
    if upRecs:
        for rec in upRecs:
            if rec.title not in current_rec_titles:
                session.add(rec)
                newRelease = True
                newReleases += 1
                print(rec)

    #  update released flag on database entries
    current_unreleased = session.query(UpcomingRecord).filter(UpcomingRecord.is_released == False)
    for rec in current_unreleased:
        if rec.release_date <= date.today():
            rec.is_released = True
            newRelease = True

    # output new releases to json file
    if newRelease:
        session.commit()
        updated_recDB = session.query(UpcomingRecord).all()
        jsonOutput = schema.dumps(updated_recDB)
        with open("/FatScraper/output/UpcomingRecords.json", 'w') as outFile, open("new_releases", 'w') as new:
            outFile.write(jsonOutput)
            new.write(str(newReleases))

    session.close()
    engine.dispose()


main()