# BrutForce Solution

nums = [1, 3, 0, 5, 6]

n = len(nums)

for i in range(0, n):
    if i not in nums:
        print(i)


# Better Solution
nums = [1, 3, 0, 5, 6]

n = len(nums)
freq = {}
for i in range(0, n + 1):
    freq[i] = 0
for num in nums:
    freq[num] = 1
for k, v in freq.items():
    if v == 0:
        print(k)


# T.C. = N+N+N = 3N ~ N
# S.C.  = O(1)


# Optimal Solution


nums = [1, 3, 0, 4, 5, 6]


def Missing_Number(nums):

    n = len(nums)
    result = n * (n + 1) // 2
    sum_result = sum(nums)
    return result - sum_result


print(Missing_Number(nums))


## Another Method

nums = [1, 3, 0, 2, 5, 6]

n = len(nums)
result = 0
for i in range(0, n + 1):
    result += i


print(result - sum(nums))


nums = [1, 3, 0, 4, 5, 6]

n = len(nums)
result = n * (n + 1) // 2
sum_result = sum(nums)
print(result - sum_result)
