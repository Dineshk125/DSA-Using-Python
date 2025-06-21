def findMinimum(nums):
    n = len(nums)
    low = 0
    high = n - 1
    mini = float("inf")

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[mid])
            low = mid + 1
    return mini


print(findMinimum(nums=[11, 12, 2, 3, 4]))

# T.C. = O(logN)
# S.C. = O(1)


## Brut Solution


def findMinimum(nums):
    n = len(nums)
    mini = float("inf")

    for i in range(0, n):
        mini = min(mini, nums[i])
    return mini


print(findMinimum(nums=[4, 5, 6, 2, 3, 0]))

# T.C. = O(N)
# S.C. = O(1)
