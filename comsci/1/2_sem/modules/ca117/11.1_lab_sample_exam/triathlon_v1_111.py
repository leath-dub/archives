class Triathlete(object):

    def __init__(self, name, tid) -> None:
        self.name = name
        self.tid = tid

    def __str__(self) -> str:
        return "Name: {}\nID: {}".format(
            self.name, self.tid)

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
