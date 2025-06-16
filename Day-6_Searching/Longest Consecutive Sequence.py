# Brut force Solution

nums = [100, 4, 200, 1, 3, 5, 2]

n = len(nums)
mx_count = 0
for i in range(0, n):
    s = nums[i]
    count = 1
    while s + 1 in nums:
        count += 1
        s = s + 1
    mx_count = max(mx_count, count)
print(mx_count)

# Batter Solution

nums = [100, 4, 200, 1, 3, 5, 2]
nums.sort()
n = len(nums)
count = 0
last_samller = float("-inf")

longest = 0
for i in range(0, n):
    num = nums[i]

    if num - 1 == last_samller:
        count += 1
        last_samller = num
    elif num != last_samller:
        count = 1
        last_samller = num

    longest = max(longest, count)
print(longest)


# Optimal Solution


nums = [100, 4, 200, -1, 0, 1, 3, 5, 2]
my_set = set()
n = len(nums)


for i in range(0, n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    count = 0
    if num - 1 not in my_set:

        x = num
        count += 1
        while x + 1 in my_set:
            count += 1
            x += 1

    longest = max(longest, count)
print(longest)
