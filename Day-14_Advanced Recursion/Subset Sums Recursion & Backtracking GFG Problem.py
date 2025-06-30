# brut Solution


class Solution:
    def sub(self, nums):
        result = []

        def subsetSums(index, total):

            if index >= len(nums):
                result.append(total)
                return
            summ = total + nums[index]
            subsetSums(index + 1, summ)
            summ = total
            subsetSums(index + 1, summ)

        subsetSums(0, 0)
        return result


s1 = Solution()

print(s1.sub(nums=[5, 9, 3]))

# Optimal Solution
"""
T.C. = O(2^N)
S.C. = O(N) , N = Stack space
"""


class Solution:

    def subsetSums(self, index, total, nums, result):

        if index >= len(nums):
            result.append(total)
            return
        summ = total + nums[index]
        self.subsetSums(index + 1, summ, nums, result)
        summ = total
        self.subsetSums(index + 1, summ, nums, result)

    def sub(self, nums):
        result = []
        self.subsetSums(0, 0, nums, result)
        return result


s1 = Solution()

print(s1.sub(nums=[5, 9, 3]))
