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
        mins = self.duration // 60
        secs = self.duration % 60
        return_str = ", ".join(self.by)
        return "Title: {}\nBy: {}\nDuration: {}:{:0>2d}".format(
            self.title, return_str, mins, secs)
