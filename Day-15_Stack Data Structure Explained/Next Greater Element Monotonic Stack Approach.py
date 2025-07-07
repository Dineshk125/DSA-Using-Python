"""
T.C. = O(2N) ~ O(N)
S.C. = O(N)

"""

nums = [19, 4, 2, 11, 4, 5, 6]
n = len(nums)
result = [-1] * n
stack = []
for i in range(n - 1, -1, -1):
    while len(stack) != 0 and stack[-1] <= nums[i]:
        stack.pop()

    if len(stack) != 0:
        result[i] = stack[-1]

    stack.append(nums[i])
print(result)


def greater(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while len(stack) != 0 and stack[-1] <= nums[i]:
            stack.pop()

        if len(stack) != 0:
            result[i] = stack[-1]

        stack.append(nums[i])
    return result


print(greater(nums=[19, 4, 3, 11, 5, 6, 9]))

"""
T.C. = O(N*(N+1))//2 ~O(N^2)

S.C. = O(1) + O(N) ~ O(N), where N = stack

"""


def grater(nums):
    n = len(nums)
    stack = [-1] * n

    for i in range(0, n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                stack[i] = nums[j]
                break
    return stack


print(grater(nums=[19, 4, 2, 11, 6, 5, 3, 10]))


print("Method 2")

nums = [19, 4, 2, 11, 4, 5, 6]

n = len(nums)
stack = [-1] * n

for i in range(0, n):
    for j in range(i + 1, n):
        if nums[j] > nums[i]:
            stack[i] = nums[j]
            break
print(stack)
