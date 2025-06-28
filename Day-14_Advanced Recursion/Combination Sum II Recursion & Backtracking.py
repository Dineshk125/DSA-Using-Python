# Optimal Solution


class Solution:

    def backtrack(self, index, target, subset, nums, result):
        if target == 0:
            result.append(subset.copy())
            return
        if target > 0 and index >= len(nums):
            return

        for i in range(index, len(nums)):
            if nums[i] > target:
                break
            if i > index and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            summ = target - nums[i]
            self.backtrack(i + 1, summ, subset, nums, result)
            subset.pop()

    def combinationSumTwo(self, candidates, target):
        candidates.sort()
        result = []
        self.backtrack(0, target, [], candidates, result)
        return result


s1 = Solution()
print(s1.combinationSumTwo(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))

# Brut Solution


class Solution(object):
    def combinationSum2(self, candidates, target):

        results = []
        candidates.sort()

        def backtrack(index, subset, target):
            if target == 0:
                results.append(list(subset))
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                subset.append(candidates[i])
                backtrack(i + 1, subset, target - candidates[i])
                subset.pop()

        backtrack(0, [], target)
        return results


s1 = Solution()
print(s1.combinationSum2(candidates=[10, 1, 2, 7, 6, 1, 5], target=8))
