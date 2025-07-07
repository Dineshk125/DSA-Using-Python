nums = [2, 10, 12, 1, 11]

n = len(nums)
result = [-1] * n
stack = []

for i in range(2 * n - 1, -1, -1):

    while stack and stack[-1] <= nums[i % n]:
        stack.pop()
    if i < n:
        if stack:
            result[i % n] = stack[-1]
    stack.append(nums[i % n])
print(result)


class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        result = [-1] * n
        stack = []

        for num in range(2 * n - 1, -1, -1):
            i = num % n
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(nums[i])
        return result


s1 = Solution()
print(s1.nextGreaterElements(nums=[2, 10, 12, 1, 11]))
