# method -> 1 Optimal solution


class Solution:
    def backtrack_sub(self, index, total, subset, nums, target, result):
        if total == target:
            result.append(subset.copy())
            return
        elif total > target:
            return

        if index >= len(nums):
            return
        summ = total + nums[index]
        subset.append(nums[index])
        self.backtrack_sub(index, summ, subset, nums, target, result)
        summ = total
        subset.pop()
        self.backtrack_sub(index + 1, summ, subset, nums, target, result)

    def combinationSum(self, candidates, target):
        result = []
        self.backtrack_sub(0, 0, [], candidates, target, result)
        return result


s1 = Solution()
nums = [1, 2, 3, 6, 7]
result = []
target = 7
print(s1.combinationSum(candidates=[2, 3, 6, 7], target=7))
