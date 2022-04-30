from math import sqrt

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


binops = {'+': float.__add__,
          '-': float.__sub__,
          '*': float.__mul__,
          '/': float.__truediv__}

uniops = {'n': float.__neg__,
          'r': sqrt}

def calculator(line) -> float:
    stack = Stack()
    for ch in line.split():
        if ch in binops:
            second = stack.pop()
            first = stack.pop()
            stack.push(float(binops[ch](first, second)))
        elif ch in uniops:
            stack.push(float(uniops[ch](
                stack.pop())))
        else:
            stack.push(float(ch))
    return stack.lst[0]
