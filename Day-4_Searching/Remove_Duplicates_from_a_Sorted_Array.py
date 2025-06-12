# Method -> 1

nums = [3, 2, 2, 5, 7, 4, 45, 5, 2, 2, 2, 3, 3, 3, 3, 3, 3, 212, 0.98, 87]


def Remove_Duplicates(nums):

    n = len(nums)
    for i in range(0, n - 1):
        for j in range(i + 1, n - 1):
            if nums[i] == nums[j]:
                del nums[j]
                return Remove_Duplicates(nums)
    return nums


print(Remove_Duplicates(nums))

# Method -> 2

nums = [2, 3, 4, 5, 7, 87, 87, 87, 90, 90, 90]


def remove_duplicates(nums):
    i = 0
    j = i + 1
    n = len(nums)

    if n == 1:
        return 1

    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i + 1


print(remove_duplicates(nums))

# Method -> 3

nums = [2, 3, 4, 5, 7, 87, 87, 87, 90, 90, 90]

withdup = {}
n = len(nums)
for i in range(0, n):
    withdup[nums[i]] = 0
    list1 = list(withdup)
print(list1)
# print(withdup)
