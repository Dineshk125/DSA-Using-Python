nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

n = len(nums)
summ = 0
mx_sum = float("-inf")

for i in range(0, n - 1):
    summ = 0
    for j in range(i, n):
        summ = summ + nums[j]
        mx_sum = max(mx_sum, summ)
print(mx_sum)


# Optimal Solution


class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        mx_sum = float("-inf")
        summ = 0
        if n == 1:
            return nums[0]
        for i in range(0, n):
            summ = summ + nums[i]
            mx_sum = max(mx_sum, summ)
            if summ < 0:
                summ = 0
        return mx_sum


c1 = Solution()
c1.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
