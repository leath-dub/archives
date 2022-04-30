class Stack(object):

    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def top(self):
        return self.lst[-1]

    def is_empty(self):
        return not(self.lst)

    def __len__(self):
        return len(self.lst)
