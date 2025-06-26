# method -> 1 Optimal solution


def backtrack_sub(index, total, subset):
    global nums
    global result
    global target
    n = len(nums)

    if total == target:
        result.append(subset.copy())
        return
    elif total > target:
        return

    if index >= n:
        return
    subset.append(nums[index])
    summ = total + nums[index]
    backtrack_sub(index + 1, summ, subset)
    e = subset.pop()
    summ -= e  ## sum = total
    backtrack_sub(index + 1, summ, subset)


nums = [5, 9, 0, 4]
result = []
target = 9
backtrack_sub(index=0, total=0, subset=[])
print(result)


# method -> 2, brut
def backtrack_sub(index, subset):
    global result
    global nums
    global target
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
            return
    subset.append(nums[index])
    backtrack_sub(index + 1, subset)
    subset.pop()
    backtrack_sub(index + 1, subset)


nums = [5, 9, 4, 0]
result = []
target = 9
backtrack_sub(index=0, subset=[])
print(result)
