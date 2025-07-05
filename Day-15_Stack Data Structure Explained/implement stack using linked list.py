class Node:

    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None


class StackUsingDLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

    def pop(self):
        if self.tail == None:
            return "Linked List Is Empty."
        elif self.tail == self.head:
            x = self.tail.val
            self.head = None
            self.tail = None
            return x

        else:
            x = self.tail.val
            self.tail = self.tail.prev
            self.tail.next = None
            return x

    def top(self):
        if self.head == None:
            return "Linked List is empty."
        else:
            return self.head.val

    def show_ele(self):
        if self.head == None:
            return "LL Is Empty."
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


s1 = StackUsingDLL()

s1.show_ele()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
print(s1.top())
print(s1.head.val)
print(s1.tail.val)
s1.show_ele()
print(f"pop value is : {s1.pop()}")
print(s1.head.val)
print(s1.tail.val)
s1.show_ele()
print(s1.top())
print(s1.tail.val)
