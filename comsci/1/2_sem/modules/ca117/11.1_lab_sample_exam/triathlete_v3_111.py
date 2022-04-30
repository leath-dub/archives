class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid
        self.times = {}
        self.race_time = 0

    def add_time(self, event, time) -> None:
        self.race_time += time
        self.times[event] = time

    def get_time(self, event) -> int:
        return self.times[event]

    def __str__(self) -> str:
        return "Name: {}\nID: {}\nRace time: {}".format(
            self.name, self.tid, self.race_time)

    def __eq__(self, other) -> bool:
        return self.race_time == other.race_time

    def __lt__(self, other) -> bool:
        return self.race_time < other.race_time

    def __gt__(self, other) -> bool:
        return self.race_time > other.race_time
