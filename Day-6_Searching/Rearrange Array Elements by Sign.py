# Method -> 1 Optimal solution


nums = [3, 1, -2, -5, 2, -4]
n = len(nums)
negLi = 1
posiLi = 0
reArr = [0] * n

for i in range(0, n):
    if nums[i] >= 0:
        reArr[posiLi] = nums[i]
        posiLi += 2
    else:
        reArr[negLi] = nums[i]
        negLi += 2

print(reArr)

# Method -> 2 Brutforce solution

nums = [3, 1, -2, -5, 2, -4]

negLi = []
posiLi = []
reArr = []

n = len(nums)

for i in range(0, n):
    if nums[i] < 0:
        negLi.append(nums[i])
    else:
        posiLi.append(nums[i])

for i in range(0, n // 2):
    reArr.append(posiLi[i])
    reArr.append(negLi[i])


print(reArr)


# Brut Force Solution

nums = [3, 1, -2, -5, 2, -4]

negLi = []
posiLi = []
n = len(nums)

for i in range(0, n):
    if nums[i] < 0:
        negLi.append(nums[i])
    else:
        posiLi.append(nums[i])

for i in range(0, len(posiLi)):

    nums[2 * i] = posiLi[i]
    nums[(2 * i) + 1] = negLi[i]

print(nums)
