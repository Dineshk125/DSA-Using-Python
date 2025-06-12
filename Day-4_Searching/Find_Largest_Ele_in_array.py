## Method -> 1 , Find largest element in array

nums = [2, 4, -2, 54, 6, 3]

largest = nums[0]
n = len(nums)
for i in range(0, n):
    largest = max(largest, nums[i])

print(largest)

# Method -> 2 , It work when all list/array have nagitive elements, and also work on positive elements

nums = [-2, -4, -2, -54, -6, -3]

largest = float("-inf")
n = len(nums)
for i in range(0, n):
    largest = max(largest, nums[i])

print(largest)

## Method -> 3 using if Statement


nums = [2, 4, -2, 54, 6, 3]

largest = nums[0]
n = len(nums)
for i in range(0, n):
    if largest <= nums[i]:
        largest = nums[i]
print(largest)
