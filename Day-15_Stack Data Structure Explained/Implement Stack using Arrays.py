class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):  # T.C. -> O(1)
        return len(self.items) == 0

    def push(self, item):  # T.C. -> O(1)
        self.items.append(item)

    def pop(self):  # T.C. -> O(1)
        if len(self.items) == 0:
            return "Can't pop, Stack Is Empty."
        x = self.items.pop()
        return x

    def top(self):  # T.C. -> O(1)
        if len(self.items) == 0:
            return "Can't Top, Stack is Empty."
        return self.items[-1]

    def size(self):  # T.C. -> O(1)
        return len(self.items)


stack = Stack()

stack.push(90)
stack.push(100)
stack.push(89)
print(stack.items)

stack.pop()
print(stack.items)

print(stack.top())

print(stack.size())

print(f"Stack Content: {stack}")
print(f"Stack Poped Item: {stack.pop()}")
print(f"Stack Content: {stack}")
print(f"Top Item After Pop: {stack.top()}")
print(f"Stack is Empty: {stack.isEmpty()}")
print(f"Stack Content Size: {stack.size()}")
