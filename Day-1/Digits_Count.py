# ## Method -1

# n = 6556566556565

# count_digit = len(str(n))

# print(count_digit)


# # Method -> 2

# n = 6497916

# num = n

# count = 0

# while num > 0:
#     digit = num % 10
#     count += 1
#     num = num // 10

# print(count)


# Method -> 3

from math import *

n = 49796139

num = n

count = int((log10)(num) + 1)

print(count)
