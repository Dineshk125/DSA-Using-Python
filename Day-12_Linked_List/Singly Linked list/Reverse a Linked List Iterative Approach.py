# Method -> 1 optimal Solution


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class SinglyLl:

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

    def travrse(self):
        if self.head == None:
            print("Linked List is Empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def revers(self):
        temp = self.head
        prev = None
        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        self.head = prev


sll = SinglyLl()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)

sll.travrse()
print(sll.head.val)
sll.revers()
print()
sll.travrse()
print(sll.head.val)


# Method -> 2

# Definition for singly-linked list.


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
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
            print("Linked List is Empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next
            print()

    def reverseList(self):
        temp = self.head
        stack = []
        while temp != None:
            stack.append(temp.val)
            temp = temp.next

        temp = self.head
        while temp != None:
            e = stack.pop()
            temp.val = e
            temp = temp.next


sll = Solution()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()

sll.reverseList()

sll.traverse()

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None


# class SinglySLL:

#     def __init__(self):
#         self.head = None

#     def append(self, val):
#         new_node = Node(val)
#         if self.head == None:
#             self.head = new_node

#         else:
#             current = self.head
#             while current.next != None:
#                 current = current.next
#             current.next = new_node

#     def traverse(self):
#         if self.head == None:
#             print("List is Empty.")
#         else:
#             current = self.head
#             while current is not None:
#                 print(current.val, end=" ")
#                 current = current.next

#             print()


# sll = SinglySLL()

# sll.append(10)
# sll.append(100)
# sll.append(1000)
# sll.append(10000)

# sll.traverse()
