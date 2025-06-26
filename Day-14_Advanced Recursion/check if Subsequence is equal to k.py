# method -> 1 Optimal solution


def backtrack_sub(index, total, subset):
    global nums
    global result
    global target
    n = len(nums)

    if total == target:
        result.append(subset.copy())
        return True

    elif total > target:
        return False

    if index >= n:
        return
    subset.append(nums[index])
    summ = total + nums[index]
    pick = backtrack_sub(index + 1, summ, subset)
    if pick == True:
        return True
    subset.pop()
    summ = total
    not_pick = backtrack_sub(index + 1, summ, subset)
    return not_pick


nums = [5, 9, 4]
result = []
target = 9
print(backtrack_sub(index=0, total=0, subset=[]))


# method -> 2, brut
def backtrack_sub(index, subset):
    global result
    global nums
    global target
    if index >= len(nums):
        if sum(subset) == target:
            result.append(subset.copy())
            return True
        else:
            return False
    subset.append(nums[index])
    pick = backtrack_sub(index + 1, subset)
    if pick == True:
        return True
    subset.pop()
    not_pick = backtrack_sub(index + 1, subset)
    return not_pick


nums = [5, 9, 4, 0]
result = []
target = 10
print(backtrack_sub(index=0, subset=[]))
