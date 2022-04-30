class MP3Track(object):

    def __init__(self, title, duration, by):
        self.title = title
        self.duration = duration
        self.by = by

    def __str__(self):
        return_str = ", ".join(self.by)
        return "Title: {}\nBy: {}\nDuration: {}".format(
            self.title, return_str, self.duration)
