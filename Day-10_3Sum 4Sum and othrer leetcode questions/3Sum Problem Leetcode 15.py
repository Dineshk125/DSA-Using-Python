class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = float("inf")
        n = len(nums)

        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if abs(total_sum - target) < abs(result - target):
                    result = total_sum
                if total_sum < target:
                    j += 1
                elif total_sum > target:
                    k -= 1
                else:
                    return target
        return result


c1 = Solution()
print(c1.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
