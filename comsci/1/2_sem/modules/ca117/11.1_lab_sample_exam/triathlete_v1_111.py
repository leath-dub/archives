class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid

    def __str__(self) -> str:
        return "Name: {}\nID: {}".format(
            self.name, self.tid)
