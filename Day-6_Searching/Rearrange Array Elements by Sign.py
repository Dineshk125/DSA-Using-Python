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
