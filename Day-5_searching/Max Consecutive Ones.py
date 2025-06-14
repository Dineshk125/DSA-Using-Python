nums = [1, 1, 0, 1, 0, 1, 1, 1, 1, 10, 1, 1, 1, 1, 1]

n = len(nums)
count = 0
mx_Count = 0

for i in range(0, n):
    if nums[i] == 1:
        count += 1
    else:
        mx_Count = max(mx_Count, count)
        count = 0
print(max(mx_Count, count))
