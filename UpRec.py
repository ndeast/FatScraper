from marshmallow import Schema, fields, post_load


class UpRec(object):
    artist = ""
    title = ""
    image = ""
    link = ""

    def __init__(self, artist, title, image, link):
        self.artist = artist
        self.title = title
        self.image = image
        self.link = link

    def printRecord(self):
        print("New Record: " + self.title + " by: " + self.artist)
        print(" buy here: \n" + self.link + " see? \n" + self.image)


class UpRecSchema(Schema):
    artist = fields.Str()
    title = fields.Str()
    image = fields.Str()
    link = fields.Str()

    @post_load
    def make_uprec(self, data):
        return UpRec(**data)
