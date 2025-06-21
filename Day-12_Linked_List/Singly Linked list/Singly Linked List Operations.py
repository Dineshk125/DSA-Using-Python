class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


node1 = Node(5)
node2 = Node(10)
node3 = Node(14)
node4 = Node(9)


node1.next = node2
node2.next = node3
node3.next = node4

print(
    f" node1: {node1} \n node2: {node2} = {node1.next} \n node3: {node3} = {node2.next} \n node: {node4} = {node3.next}"
)

print()

print(node1.next)
print(node2.next)
print(node3.next)
print(node4.next)

print()

print(node1.val)
print(node2.val)
print(node3.val)
print(node4.val)

print()

print(node1.next.val)
print(node2.next.val)
print(node3.next.val)
# print(node4.next.val)
