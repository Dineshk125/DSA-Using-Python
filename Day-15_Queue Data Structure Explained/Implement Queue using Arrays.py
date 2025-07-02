class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):  # S.C. -> O(1)
        return len(self.items) == 0

    def enqueue(self, val):  # S.C. -> O(1)
        self.items.append(val)

    def front(self):  # S.C. -> O(1)
        if len(self.items) == 0:
            return "Queue is Empty."

        return self.items[0]

    def rear(self):  # S.C. -> O(1)
        if len(self.items) == 0:
            return "Queue is Empty."
        return self.items[-1]

    def dequeue(self):  # S.C. -> O(N)
        if len(self.items) == 0:
            return "queue is Empty."

        return self.items.pop(0)

    def size(self):  # S.C. -> O(1)
        return len(self.items)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
print(queue.items)

print(queue.front())

print(queue.rear())

print(queue.size())

print(queue.isEmpty())

print(queue.dequeue())
print(queue.items)

queue.dequeue()
print(queue.items)

queue.enqueue(100)
print(queue.items)
