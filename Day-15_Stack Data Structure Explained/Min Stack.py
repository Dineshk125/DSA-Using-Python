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


# Your MinStack object will be instantiated and called as such:
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
