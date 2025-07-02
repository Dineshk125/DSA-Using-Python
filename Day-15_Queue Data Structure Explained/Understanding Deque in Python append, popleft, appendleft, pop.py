from collections import deque

lst = deque()

lst.append(100)
lst.append(200)
lst.append(400)
lst.append(500)

print(lst)

lst.pop()
print(lst)
lst.appendleft(9)
print(lst)
print(lst.popleft())
