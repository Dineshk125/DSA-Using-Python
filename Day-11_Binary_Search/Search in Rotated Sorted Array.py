# Optimal Solution


def rotateArray(nums, target):
    n = len(nums)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] <= nums[high]:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


print(rotateArray(nums=[11, 12, 13, 10, 2, 4, 5, 6, 7, 8], target=10))

# brut Solution


def rotateArray(nums, target):
    n = len(nums)
    for i in range(0, n):
        if nums[i] == target:
            return i
    return -1


print(rotateArray(nums=[1, 2, 4, 5, 6, 7, 8], target=4))
