class MP3Track(object):

    def __init__(self, title, duration, by):
        self.title = title
        self.duration = duration
        self.by = by

    def __str__(self):
        return_str = ", ".join(self.by)
        return "Title: {}\nBy: {}\nDuration: {}".format(
            self.title, return_str, self.duration)

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

    def get_mp3s_by_artist(self, artist) -> list:
        new_collection = []
        for track in self.tracks.values():
            if artist in track.by:
                new_collection.append(track)
        return new_collection

    def __len__(self) -> int:
        return len(self.tracks)

    def __add__(self, other) -> object:
        new_collection = MP3Collection()
        for track in self.tracks.values():
            new_collection.add(track)
        for track in other.tracks.values():
            new_collection.add(track)
        return new_collection
