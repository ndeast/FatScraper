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
