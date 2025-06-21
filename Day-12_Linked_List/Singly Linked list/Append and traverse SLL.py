class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("List is Empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()


sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if self.head == None:
            print("List is Empty.")
        else:
            current = self.head
            while current != None:
                print(current.val, end=" ")
                current = current.next
            print()


sll = SinglyLinkedList()

sll.append(10)
sll.append(20)
sll.append(30)
sll.traverse()
