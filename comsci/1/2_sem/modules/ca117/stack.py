#!/usr/bin/env python3

class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, item):
        self.l.append(item)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return not(self.l)

    def __len__(self):
        return len(self.l)

def main() -> None:
    l = [1, 2, 3, 4, 5]
    stack = Stack()
    stack.l = l
    while not(stack.is_empty()):
        print(stack.pop())


if __name__ == "__main__":
    main()
