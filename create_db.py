from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date
from UpcomingRecord import UpcomingRecord, Base
from FatWreckScraper import saveAlbumArt

engine = create_engine('sqlite:///db/UpcomingRecords.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

image = saveAlbumArt(
    "https://fatwreck.com/release/record_cover/10/large/502.jpg?1370148051",
    "https://fatwreck.com/record/detail/502")

newRec = UpcomingRecord(
    "Lagwagon", "Duh", image,
    "https://fatwreck.com/record/detail/502")
newRec.release_date = date(1992, 10, 11)
newRec.is_released = True

session.add(newRec)
session.commit()

print(session.query(UpcomingRecord).first().artist)
