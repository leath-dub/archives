class MP3Track(object):

    def __init__(self, title, duration, by=None) -> None:
        self.title = title
        self.duration = duration
        if by is None:
            self.by = []
        else:
            self.by = by

    def add_artist(self, s) -> None:
        self.by.append(s)

    def __str__(self) -> str:
        return_str = ", ".join(self.by)
        return "Title: {}\nBy: {}\nDuration: {}".format(
            self.title, return_str, self.duration)
