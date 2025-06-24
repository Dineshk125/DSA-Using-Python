## Method -> 1 Optimal Solution, T.C = O(n) ,S.C =O(1)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Sll:

    def __init__(self):
        self.head = None

    def findLength(self):
        self.head = node1
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = self.head
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0


sll = Sll()

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

print(sll.findLength())


# Method -> 2 Brut solution ,  T.C = O(n) ,S.C =O(n)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Sll:

    def __init__(self):
        self.head = None

    def findLength(self):
        self.head = node1
        temp = self.head
        my_dict = {}
        travel = 0

        while temp is not None:
            if temp in my_dict:
                return travel - my_dict[temp]
            my_dict[temp] = travel
            travel += 1
            temp = temp.next
        return 0


sll = Sll()

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

print(sll.findLength())
