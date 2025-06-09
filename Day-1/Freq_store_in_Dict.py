# num = [2, 3, 4, 5, 6, 3, 2, 1, 6, 7, 7, 7, 8, 8, 4, 6, 3, 7]

# n = num

# freq = {}

# for i in n:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)


num = [2, 3, 4, 2, 2, 2, 3, 4]

n = len(num)

freq = {}

for i in range(0, n):
    freq[num[i]] = freq.get(num[i], 0) + 1
print(freq)
