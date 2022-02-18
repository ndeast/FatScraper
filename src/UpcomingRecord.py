from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, Integer, String, Boolean, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UpcomingRecord(Base):
    __tablename__ = 'upcomingrecords'
    id = Column(Integer, primary_key=True)
    artist = Column(String(40))
    title = Column(String(80))
    image = Column(String(100), nullable=True, default="img")
    link = Column(String(40))
    release_date = Column(Date)
    is_released = Column(Boolean, unique=False, default=False, nullable=True)

    def __init__(self, artist, title, image, link, date):
        self.artist = artist
        self.title = title
        self.image = image
        self.link = link
        self.release_date = date
        self.is_released = False

    def __str__(self):
        return "Title: {}\nArtist: {}\nRelease Date: {}\n{}\n".format(
            self.title, self.artist, self.release_date, self.link)

engine = create_engine('sqlite:////FatScraper/output/db/UpcomingRecords.db')
Base.metadata.create_all(engine)


class UpcomingRecordSchema(Schema):
    class Meta:
        ordered = True
    id = fields.Integer()
    artist = fields.Str()
    title = fields.Str()
    release_date = fields.Date()
    link = fields.Str()
    image = fields.Str()
    is_released = fields.Boolean()

    @post_load
    def make_uprec(self, data):
        return UpcomingRecord(**data)
