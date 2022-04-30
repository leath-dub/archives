class MP3Track(object):

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return "Title: {}\nDuration: {}".format(
            self.title, self.duration)

class MP3Collection(object):

    def __init__(self) -> None:
        self.tracks = {}

    def add(self, obj) -> None:
        self.tracks[obj.title] = obj

    def remove(self, title) -> None:
        if title in self.tracks:
            del self.tracks[title]

    def lookup(self, title) -> object or None:
        if title in self.tracks:
            return self.tracks[title]
