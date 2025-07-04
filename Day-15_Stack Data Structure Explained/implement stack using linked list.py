class MyStack:
    def __init__(self):
        self.tail = None
        self.head = None


class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None

    # Function to push an integer into the stack.
    def push(self, val):
        if self.head is None:
            self.head = StackNode(val)
            self.tail = self.head
        else:
            self.tail.next = StackNode(val)
            self.tail = self.tail.next

    # Function to remove an item from top of the stack.
    def pop(self):
        if self.head == None:
            return -1
        prev = None
        curr = self.head
        while curr is not self.tail:
            prev = curr
            curr = curr.next
        if prev is not None:
            prev.next = None
            self.tail = prev
            return curr.data
        else:
            self.tail = None
            return curr.data


s1 = StackNode()

s1.push(100)
s1.push(200)
s1.push(300)

print(s1.data)
print(s1.pop(0))
