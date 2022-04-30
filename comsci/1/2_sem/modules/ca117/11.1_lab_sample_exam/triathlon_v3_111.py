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

class Triathlon(object):

    def __init__(self) -> None:
        self.table = {}

    def add(self, obj) -> None:
        self.table[obj.tid] = obj

    def remove(self, tid) -> None:
        del self.table[tid]

    def lookup(self, tid) -> object or None:
        if tid in self.table:
            return self.table[tid]

    def __str__(self) -> str:
        store = []
        for v in self.table.values():
            store.append("{}".format(v))
        return "\n".join(sorted(store))

    def best(self) -> str:
        i = 0
        for v in self.table.values():
            if i == 0:
                maxi = v
            elif v.race_time < maxi.race_time:
                maxi = v
            i += 1
        return "{}".format(maxi)

    def worst(self) -> str:
        i = 0
        for v in self.table.values():
            if i == 0:
                mini = v
            elif v.race_time > mini.race_time:
                mini = v
            i += 1
        return "{}".format(mini)
