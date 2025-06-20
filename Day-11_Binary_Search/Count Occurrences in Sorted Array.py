# Optimal Solution


class Solution(object):
    def lowerBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        lo_bo = -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                lo_bo = mid
                high = mid - 1
            else:
                low = mid + 1
        return lo_bo

    def upperBound(self, nums, target):
        n = len(nums)
        up_bo = -1
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                up_bo = mid
                high = mid - 1
            else:
                low = mid + 1
        return up_bo

    def countOcc(self, nums, target):
        lb = self.lowerBound(nums, target)
        if lb == -1 or nums[lb] != target:
            return 0

        ub = self.upperBound(nums, target)
        if ub == -1:
            ub = len(nums)
        return [ub - lb]


c1 = Solution()
print(c1.countOcc(nums=[1, 2, 3, 3, 3, 4, 5, 8, 8, 9, 9, 10], target=8))


# brut force solution


def countOcc(nums, target):
    n = len(nums)
    first = -1
    last = -1
    for i in range(0, n):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    if first == -1:
        return 0
    return last - first + 1


print(countOcc(nums=[1, 2, 3, 3, 3, 4, 5, 8, 8, 9, 9, 10], target=9))
