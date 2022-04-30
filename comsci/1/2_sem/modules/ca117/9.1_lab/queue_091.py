class Queue(object):

    def __init__(self):
        self.a = []

    def enqueue(self, item) -> None:
        self.a.append(item)

    def dequeue(self) -> "first":
        return self.a.pop(0)

    def first(self) -> "first":
        return self.a[0]

    def is_empty(self) -> bool:
        return not(self.a)

    def __len__(self) -> len:
        return len(self.a)
