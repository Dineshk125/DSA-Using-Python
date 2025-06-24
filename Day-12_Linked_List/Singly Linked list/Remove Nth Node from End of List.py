## Method -> 1 Brut Solution


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class KthNode:

    def __init__(self):
        self.head = None

    def traverse(self):
        self.head = n1
        if not self.head:
            print("empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def removeKthNode(self, n):
        self.head = n1
        lengthh = 0
        temp = self.head
        while temp is not None:
            lengthh += 1
            temp = temp.next

        if lengthh == n:
            self.head = n1
            self.head = self.head.next
            temp = self.head
            while temp is not None:
                print(temp.val, end=" ")
                temp = temp.next
            print()
        else:
            position_to_len = lengthh - n
            temp = self.head
            c = 1
            print((lengthh - n) + 1)
            while c < position_to_len:
                temp = temp.next
                c += 1
            temp.next = temp.next.next


s1 = KthNode()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(44)
n5 = Node(99)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = None
s1.traverse()
s1.removeKthNode(n=5)
# s1.traverse()


## Method -> 1 Optimal Solution


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class KthNode:

    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traverse(self):
        if not self.head:
            print("empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def removeKthNode(self, n):
        slow = self.head
        fast = self.head

        for _ in range(n):
            fast = fast.next

        if fast == None:
            self.head = self.head.next
        else:
            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next


s1 = KthNode()

s1.append(10)
s1.append(90)
s1.append(20)
s1.append(60)
s1.append(50)

s1.traverse()
s1.removeKthNode(n=5)
s1.traverse()
