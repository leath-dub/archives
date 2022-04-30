class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid
        self.times = {}

    def add_time(self, event, time) -> None:
        self.times[event] = time

    def get_time(self, event) -> int:
        return self.times[event]

    def __str__(self) -> str:
        return "Name: {}\nID: {}\nRace time: {}".format(
            self.name, self.tid, sum(self.times.values()))
