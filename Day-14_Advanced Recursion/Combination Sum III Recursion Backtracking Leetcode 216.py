"""
Complexity
Time complexity:
O(C(9,k)×k)

Space complexity:
O(k×#validcombinations)

"""


class Solution:

    def subsetSum(self, k, n):
        result = []

        def subsetSum3(index, total, subset, n, result):

            if total == n and len(subset) == k:
                result.append(subset.copy())
                return
            if total > n and len(subset) > k:
                return
            for i in range(index, 10):
                summ = total + i
                subset.append(i)
                subsetSum3(i + 1, summ, subset, n, result)
                subset.pop()
                # subsetSum3(index + 1, summ, subset, n, result)

        subsetSum3(1, 0, [], n, result)
        return result


s1 = Solution()

print(s1.subsetSum(k=3, n=8))


# Optimal Solution
"""
Complexity
Time complexity:
O(C(9,k)×k)

Space complexity:
O(k×#validcombinations)

"""


class Solution(object):

    def subsetSum3(self, index, total, subset, n, k, result):

        if total == n and len(subset) == k:
            result.append(subset[:])
            return
        if total > n and len(subset) > k:
            return

        for i in range(index, 10):
            summ = total + i
            subset.append(i)
            self.subsetSum3(i + 1, summ, subset, n, k, result)
            subset.pop()

    def combinationSum3(self, k, n):
        result = []
        self.subsetSum3(1, 0, [], n, k, result)
        return result


s1 = Solution()

print(s1.combinationSum3(k=2, n=8))


# Optimal Solution


class Solution:
    def __init__(self):
        self.result = []

    def combinationSum3(self, k, n):
        self.k = k
        self.n = n
        self._backtrack(1, 0, [])
        return self.result

    def _backtrack(self, index, total, subset):
        if total == self.n and len(subset) == self.k:
            self.result.append(subset[:])
            return
        if total > self.n or len(subset) > self.k:
            return

        for i in range(index, 10):
            subset.append(i)
            self._backtrack(i + 1, total + i, subset)
            subset.pop()


s1 = Solution()

print(s1.combinationSum3(3, 7))
