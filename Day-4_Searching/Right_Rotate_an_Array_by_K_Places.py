# Method -> 1 Brut Force Solution

nums = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]

n = len(nums)
rotate = 10 % n

for _ in range(0, rotate):
    e = nums.pop()
    nums.insert(0, e)
print(nums)


## Method -> 2, Better Solution


nums = [1, 2, 3, 4, 5, 6, 7, 1, 2, 3]

n = len(nums)
k = 3
k = k % n
nums[:] = nums[n - k :] + nums[: n - k]

print(nums)


## Method -> 2,  Optimal Solution

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n = len(nums)


def remove(nums, left, right):
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


k = 4
k = k % n
remove(nums, n - k, n - 1)
remove(nums, 0, n - k - 1)
remove(nums, 0, n - 1)
print(nums)
