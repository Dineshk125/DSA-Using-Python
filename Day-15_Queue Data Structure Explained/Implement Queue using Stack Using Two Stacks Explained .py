"""
T.C. = O(N^2)
S.C.  = O(N)

"""


class MyQueue(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)
        if self.empty():
            return False
        for _ in range(len(self.items) - 1):
            self.items.append(self.items.pop(0))

    def pop(self):
        if self.empty():
            return False
        return self.items.pop(-1)

    def top(self):
        if self.empty():  # if len(self.items) == 0:
            return False
        return self.items[-1]

    def empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


obj = MyQueue()

print(obj.items)
obj.push(1)
print(obj.items)
obj.push(2)
print(obj.items)

print(obj.top())
print(obj.pop())
