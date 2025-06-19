class Solution(object):
    def FourSum(self, nums, target):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(0, n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k = j + 1
                l = n - 1
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        result.append((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1

                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while l > k and nums[l] == nums[l + 1]:
                            l -= 1
                    elif total < target:
                        k += 1
                    else:
                        l -= 1
        return [list(ans) for ans in result]


c1 = Solution()
print(c1.FourSum(nums=[-3, -2, -1, 0, 0, 1, 2, 3], target=0))


## Brutforce Solution


def FourSum(nums, target):

    n = len(nums)
    target = 0
    my_set = set()
    result = []
    if n < 4:
        return []
    for i in range(0, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    if total == target:
                        temp = [nums[i], nums[j], nums[k], nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    for ans in my_set:
        result.append(list(ans))
    return result


print(FourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
