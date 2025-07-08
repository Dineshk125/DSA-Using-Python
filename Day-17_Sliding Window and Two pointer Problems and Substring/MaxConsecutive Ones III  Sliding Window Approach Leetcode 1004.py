"""
Optimal Solution

T.C. = O(N)
S.C. = O(1)

"""


class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        right = 0
        maxi = 0
        zero = 0

        while right < len(nums):
            if nums[right] == 0:
                zero += 1
            if zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
            if zero <= k:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi


s1 = Solution()

print(s1.longestOnes(nums=[1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0], k=2))


"""
Better Solution

T.C. = O(n)+O(n) = O(2n) ~ O(N)
S.C. = (1)
"""

nums = [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1]

left = 0
right = 0
k = 2  # Maximum number of zeros that can be flipped to ones
maxi = 0
zero = 0

while right < len(nums):
    if nums[right] == 0:
        zero += 1
    while zero > k:
        if nums[left] == 0:
            zero -= 1
        left += 1
    if zero <= k:
        maxi = max(maxi, right - left + 1)
    right += 1

print(maxi)


"""
Brut Solution

T.C. = O(N^2)
S.C. = O(N)

"""

nums = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0]

maxi = 0
k = 2

for i in range(0, len(nums)):
    zero = 0
    for j in range(i, len(nums)):
        if nums[j] == 0:
            zero += 1
        if zero > k:
            break
        maxi = max(maxi, j - i + 1)
print(maxi)
