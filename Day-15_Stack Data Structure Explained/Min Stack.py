class MinStack(object):

    def __init__(self):
        self.items = []
        self.minstack = []

    def push(self, val):
        self.items.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self):
        if len(self.items) == 0:
            return []
        self.items.pop()
        self.minstack.pop()

    def top(self):
        if len(self.items) == 0:
            return []
        return self.items[-1]

    def getMin(self):
        return self.minstack[-1]


obj = MinStack()
obj.push(10)
obj.push(20)
obj.push(30)
obj.push(40)
print(obj.items)
obj.pop()
print(obj.items)
param_3 = obj.top()
print(param_3)
param_4 = obj.getMin()
print(param_4)


## Method -> 2


class minStack:

    def __init__(self):
        self.item = []

    def push(self, val):
        if len(self.item) == 0:
            self.item.append([val, val])
        else:
            mini = min(self.item[-1][1], val)
            self.item.append([val, mini])

    def pop(self):
        if len(self.item) == 0:
            return 0
        return self.item.pop()

    def top(self):
        if len(self.item) == 0:
            return 0
        return self.item[-1][0]

    def getMin(self):
        if len(self.item) == 0:
            return 0
        return self.item[-1][1]


s1 = minStack()

s1.push(100)
s1.push(200)
s1.push(300)

print(s1.item)
s1.pop()
print(s1.item)
print(s1.top())
print(s1.getMin())
