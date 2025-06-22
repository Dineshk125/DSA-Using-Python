class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def traversal(self):
        if not self.head:
            print("SLL is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" ")
                current = current.next

    def insert_at(self, val, position):
        # current=self.head
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            pre_node = current
            current = self.head
            count = 0
            while current is not None and count < position:
                pre_node = current
                current = current.next
                count += 1
            pre_node.next = new_node
            new_node.next = current

    def delete(self, val):
        temp = self.head
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                # below is not necessary
                temp.next = None
                del temp
            else:
                pre_node = (
                    temp  # pre_node can be any value because it will change by loop.
                )
                found = False
                while temp is not None:
                    if temp.val == val:
                        found = True
                        break
                    pre_node = temp
                    temp = temp.next
                if found:
                    pre_node.next = temp.next
                    # not necessary
                    temp.next = None
                    del temp
                else:
                    print("Value not found in SLL.")
        else:
            print("SLL is empty.")


# n1 = Node(10)
# print(n1)
# print(n1.val)
# print(n1.next)
# n2 = Node(20)
# print(n2)
# print(n2.val)
# print(n2.next)


s1 = SinglyLinkedList()
s1.append(10)
s1.append(20)
s1.append(30)
s1.append(0)
s1.append(2)
s1.append(3)
s1.append(9)
s1.traversal()

print()
s1.delete(100)
s1.traversal()

print()
s1.delete(10)
s1.traversal()

print()
s1.delete(3)
s1.traversal()
