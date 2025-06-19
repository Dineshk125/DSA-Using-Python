## ceil the Floor

nums = [3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15]


def floorCeil(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    smalest = -1
    largest = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return [nums[mid], nums[mid]]

        elif nums[mid] > target:
            largest = nums[mid]
            high = mid - 1
        else:
            smalest = nums[mid]
            low = mid + 1
    return [smalest, largest]


print(floorCeil(nums=[3, 4, 4, 4, 8, 9, 9, 10, 12, 12, 14, 15], target=20))

# T.C. -> O(log2^N)
# S.C. -> O(1)
