class Node:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.pre = None


class queueUsingDll:
    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head == None:
            return "Queue is empty."
        elif self.tail == self.head:
            x = self.head.val
            self.head = None
            self.tail = None
            return x
        else:
            x = self.head.val
            self.head = self.head.next
            self.head.pre = None
            return x

    def rear(self):
        if self.head == None:
            return "Queue is empty."
        else:
            return self.tail.val

    def front(self):
        if self.head == None:
            return "Queue is empty."
        else:
            return self.head.val

    def show_queue(self):
        if self.head == None:
            return "Queue is empty."
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        current = self.head
        if current is None:
            return "Queue is empty."
        else:
            c = 0
            while current is not None:
                c += 1
                current = current.next
            return c


s1 = queueUsingDll()
print(s1.show_queue())
print(s1.is_empty())
print(s1.size())
print(s1.dequeue())
print(s1.front())
print(s1.rear())
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.enqueue(40)
s1.show_queue()
print(s1.size())
print(s1.front())
print(s1.rear())
print(s1.dequeue())
print(s1.size())
print(s1.front())
print(s1.rear())
print(s1.is_empty())
s1.show_queue()
