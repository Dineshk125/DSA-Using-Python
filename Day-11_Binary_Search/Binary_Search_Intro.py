# # Method -> 1,  Iterative Solution

# nums = [1, 2, 3, 4, 5, 9, 10, 12, 34]

# nums.sort()
# n = len(nums)
# low = 0
# high = n - 1
# target = 10

# while low <= high:
#     mid = (low + high) // 2
#     if target == nums[mid]:
#         print(mid)
#         break

#     elif target > nums[mid]:
#         low = mid + 1
#     else:
#         high = mid - 1
# else:
#     print("-1")


# ## Method -> 2, Iterative Solution


# def binarySearch(nums, target):

#     n = len(nums)
#     nums.sort()
#     low = 0
#     high = n - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if target == nums[mid]:
#             return mid
#         elif target > nums[mid]:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# print(binarySearch(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=6))


## Method -> 3, Recursive Solution


def binary_Search(nums, low, high):
    nums.sort()
    n = len(nums)
    target = 6
    if low > high:
        return -1
    mid = (low + high) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_Search(nums, mid + 1, high)
    else:
        return binary_Search(nums, low, mid - 1)


print(binary_Search(nums=[1, 3, 3, 5, 6, 6, 7, 8, 9, 14], low=0, high=9))
