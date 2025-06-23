# Method -> 1 Optimal Solution , using two pointer


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Sll:

    def __init__(self):
        self.head = None

    def hasCycle(self):
        self.head = node1
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


s1 = Sll()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(50)
node5 = Node(55)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

print(s1.hasCycle())

# method -> 2 Brut solution


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Sll:

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
        if self.head == None:
            print("LL is Enpty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def cycle(self):
        self.head = node1
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return True
            my_set.add(temp)
            temp = temp.next
        return False


s = Sll()


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(50)
node5 = Node(55)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node1

s.append(10)
s.append(20)
s.append(30)
s.append(10)
# s.traverse()
print(s.cycle())


# Method -> 3 Using Make Cycle


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Sll:

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
        if self.head == None:
            print("Linked list is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def reversee(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev

    def make_cycle(self):
        a = self.head
        current = self.head
        while current is not None:
            current = current.next
            if current.next is None:
                current.next = a
                return

    def hasCycle(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False


s1 = Sll()

s1.append(10)
s1.append(20)
s1.append(30)
s1.append(10)
s1.append(2)

# s1.traverse()
s1.make_cycle()
print(s1.hasCycle())
