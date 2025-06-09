## Method -> 1

# n = 24

# num = n
# result = []

# for i in range(1, n + 1):
#     if num % i == 0:
#         result.append(i)
# print(result)


## Method -> 2

# n = 36

# num = n
# result = []

# for i in range(1, (n // 2) + 1):
#     if num % i == 0:
#         result.append(i)
# result.append(n)
# print(result)

## Method -> using sqrt -> it give optial solution

from math import *

n = 36

num = n
result = []

for i in range(1, int(sqrt(num))):
    if num % i == 0:
        result.append(i)
        result.append(int(num / i))
print(result)
