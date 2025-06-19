## Optimal Solution


class Solution(object):
    def lowerBound(self, nums, target):
        low, high = 0, len(nums) - 1
        lower_boundd = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lower_boundd = mid
                high = mid - 1
            else:
                low = mid + 1
        return lower_boundd

    def upperBound(self, nums, target):
        low, high = 0, len(nums) - 1
        upper_boundd = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                upper_boundd = mid
                high = mid - 1
            else:
                low = mid + 1
        return upper_boundd

    def searchRange(self, nums, target):
        lB = self.lowerBound(nums, target)
        if lB == -1 or nums[lB] != target:
            return [-1, -1]

        uB = self.upperBound(nums, target)
        if uB == -1:
            uB = len(nums)
        return [lB, uB - 1]


c1 = Solution()
print(c1.searchRange([5, 7, 7, 8, 8, 10], 8))


# Brutforce Solution


def firstLastOcc(nums, target):

    n = len(nums)
    low = 0
    high = n - 1
    first = -1
    last = -1

    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


print(firstLastOcc(nums=[1, 2, 3, 3, 3, 3, 3, 5, 6, 8, 9, 9, 10], target=3))

# Brut Solution

nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 10, 10, 10]
n = len(nums)
target = 1
lb = -1
low = 0
high = n - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] >= target:
        lb = mid
        high = mid - 1
    else:
        low = mid + 1

if lb == -1:
    print(f"[{-1},{-1}]")
else:
    ub = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1
    print(f"[{lb},{ub-1}]")
