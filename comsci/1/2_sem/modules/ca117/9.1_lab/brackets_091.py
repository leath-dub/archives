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


match = {
    ")": "(",
    "]": "[",
    "}": "{"
}

def matcher(s) -> bool:
    global match
    stack = Stack()
    for ch in s:
        if ch in match:
            try:
                if stack.pop() != match[ch]:
                    return False
            except IndexError:
                return False
        elif ch in match.values():
            stack.push(ch)
    return not(stack.lst)
