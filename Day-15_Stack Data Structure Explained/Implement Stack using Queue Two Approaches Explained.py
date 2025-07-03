from collections import deque


class MyStack(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        if len(self.queue) == 0:
            return False
        return self.queue.popleft()

    def top(self):
        if len(self.queue) == 0:
            return False
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


obj = MyStack()

print(obj.queue)
obj.push(100)
obj.push(200)
# obj.push(300)
# obj.push(400)
print(obj.queue)
param_3 = obj.top()
print(param_3)

param_2 = obj.pop()
print(param_2)
print(obj.queue)
param_4 = obj.empty()
print(param_4)
