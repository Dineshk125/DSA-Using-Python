# Method -> 1 , Optimal Solution


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Sll:

    def __init__(self):
        self.head = None


class Sll:
    def __init__(self):
        self.head = None

    def cycle(self):
        self.head = node1
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.val
        return None


s = Sll()


node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(50)
node5 = Node(52)
node6 = Node(67)
node7 = Node(57)
node8 = Node(23)
node9 = Node(11)
node10 = Node(45)
node11 = Node(90)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node4  # make cycle

print(s.cycle())


# Methodd -> 2 Brut  Solution


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Sll:

    def __init__(self):
        self.head = None

    def cycle(self):
        self.head = node1
        temp = self.head
        my_set = set()

        while temp is not None:
            if temp in my_set:
                return temp.val
            my_set.add(temp)
            temp = temp.next
        return None


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
node5.next = node2
print(s.cycle())
