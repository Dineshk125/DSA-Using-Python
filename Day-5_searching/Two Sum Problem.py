# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# n = len(nums)
# target = 11
# for i in range(0, n - 1):
#     for j in range(i + 1, n):
#         if nums[i] + nums[j] == target:
#             print(i, j)


# Optimal Solution

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

n = len(nums)
dictt = {}
target = 1
for i in range(0, n):
    remaning = target - nums[i]
    if remaning in dictt:
        print(dictt[remaning], i)
    dictt[nums[i]] = i

print(dictt)
