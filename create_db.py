from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from UpcomingRecord import UpcomingRecord, Base

engine = create_engine('sqlite:///db/UpcomingRecords.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

newRec = UpcomingRecord(
    "Lagwagon", "Duh",
    "https://fatwreck.com/release/record_cover/10/large/502.jpg?1370148051",
    "https://fatwreck.com/record/detail/502")
newRec.release_date = 'OCTOBER 01, 1992'
newRec.is_released = True

session.add(newRec)
session.commit()

print(session.query(UpcomingRecord).first().artist)
