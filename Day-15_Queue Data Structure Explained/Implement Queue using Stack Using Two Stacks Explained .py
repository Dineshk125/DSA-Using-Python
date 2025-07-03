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
        return self.items.pop()

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


"""
Implementation Queue Usin two Stack.

T.C. = O(N^2)
S.C.  = O(N)

"""


class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, val):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(val)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        if self.empty():
            return False
        return self.st1.pop()

    def top(self):
        if self.empty():  # if len(self.items) == 0:
            return False
        return self.st1[-1]

    def empty(self):
        return len(self.st1) == 0

    def size(self):
        return len(self.st1)


obj = MyQueue()

print(obj.st1)
obj.push(1)
print(obj.st1)
obj.push(2)
print(obj.st1)

print(obj.top())
print(obj.pop())
