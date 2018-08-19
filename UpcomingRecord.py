from marshmallow import Schema, fields, post_load
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UpcomingRecord(Base):
    __tablename__ = 'upcomingrecords'
    id = Column(Integer, primary_key=True)
    artist = Column(String(40))
    title = Column(String(80))
    image = Column(String(100))
    link = Column(String(40))
    release_date = Column(String(250), nullable=True)
    is_released = Column(Boolean, unique=False, default=False, nullable=True)

    def __init__(self, artist, title, image, link):
        self.artist = artist
        self.title = title
        self.image = image
        self.link = link
        self.release_date = None
        self.is_released = False

engine = create_engine('sqlite:///db/UpcomingRecords.db')
Base.metadata.create_all(engine)


class UpcomingRecordSchema(Schema):
    id = fields.Integer()
    artist = fields.Str()
    title = fields.Str()
    image = fields.Str()
    link = fields.Str()
    release_date = fields.Date()
    is_released = fields.Boolean()
  
    @post_load
    def make_uprec(self, data):
        return UpcomingRecord(**data)
