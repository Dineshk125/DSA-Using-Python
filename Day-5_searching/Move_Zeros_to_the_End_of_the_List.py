# Method -> 1 Optimal approach

nums = [0, 0, 0, 0, 5, 6, 7, 8, 9, 0, 0]

if len(nums) == 1:
    print()
i = 0

while i < len(nums):
    if nums[i] == 0:
        break
    i += 1
if i == len(nums):
    print()

j = i + 1

while j < len(nums):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1
print(nums)


# Method -> 2

nums = [0, 0, 0, 0, 5, 6, 7, 8, 9, 0, 0]
n = len(nums)

for i in range(0, n - 1):
    if nums[i] == 0:
        for j in range(i + 1, n):
            if nums[j] != 0:
                nums[i] == 0
                nums[i], nums[j] = nums[j], nums[i]
print(nums)

# Time Complexity: O(n^2)
# Space Complexity: O(1)


# Method -> 3

nums = [0, 0, 0, 0, 5, 6, 7, 8, 9, 0, 0]


def add_zero_end(nums):
    n = len(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] == 0 and nums[i + 1] != 0:
            nums.append(nums.pop(i))
            return add_zero_end(nums)
    return nums


print(add_zero_end(nums))

# Time Complexity: O(n)
# Space Complexity: O(1)

# Method -> 4

nums = [0, 0, 0, 0, 5, 6, 7, 8, 9, 0, 0]

non_zero = [num for num in nums if num != 0]

nums = non_zero + [0] * (len(nums) - len(non_zero))

print(nums)
# Time Complexity: O(n)
# Space Complexity: O(n)
