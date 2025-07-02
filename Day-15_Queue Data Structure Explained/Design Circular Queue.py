class MyCircularQueue(object):

    def __init__(self, k):
        self.items = []
        self.k = k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.items.append(value)
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.items.pop(0)
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.items[0]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def isFull(self):
        return len(self.items) == self.k


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(4)
obj.enQueue(10)
obj.enQueue(20)
obj.enQueue(30)
obj.enQueue(40)
obj.enQueue(50)
print(obj.items)
obj.deQueue()
print(obj.items)
print(obj.Front())
print(obj.Rear())
print(obj.isEmpty())
print(obj.isFull())
