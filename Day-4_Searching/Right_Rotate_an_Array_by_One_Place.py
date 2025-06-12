## Method -> 1

# nums = [7, 5, 4, 6, 9, 3, 2, 1]

# n = len(nums)
# temp = nums[n - 1]
# for i in range(n - 2, -1, -1):
#     nums[i + 1] = nums[i]
# nums[0] = temp

# print(nums)

## Method -> 2

nums = [7, 5, 4, 6, 9, 3, 2, 1]
print(f"Original list is: {nums},{id(nums)}")

n = len(nums)

nums[:] = [nums[n - 1]] + nums[0:-1]
print(f"Before rotated by 1 place in to Original list: {nums},{id(nums)}")
