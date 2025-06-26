# count the subsequences of with k sum :--->
# T.C = O(2**n) ,S.C = O(n) where n is stack space


def countSubset(index, subset):
    global result
    global nums
    global target
    n = len(nums)

    if index >= n:
        if sum(subset) == target:
            result.append(subset.copy())
            return 1
        else:
            return 0
    subset.append(nums[index])
    pick = countSubset(index + 1, subset)
    subset.pop()
    not_pick = countSubset(index + 1, subset)
    return pick + not_pick


nums = [5, 9, 4]
target = 9
result = []
index = 0
subset = []
print(countSubset(index, subset))
print("this is the sequence that are sum of k(target):", result)


# Optimal
# method 2:-->
# T.C = O(2**n) ,S.C = O(n) where n is stack spac


def countSubset(index, total):
    global result
    global nums
    global target
    n = len(nums)

    if total == target:
        return 1
    elif total > target:
        return 0
    if index >= n:
        return 0
    summ = total + nums[index]
    pick = countSubset(index + 1, summ)
    summ = total
    not_pick = countSubset(index + 1, summ)
    return pick + not_pick


nums = [5, 9, 4]
target = 9
result = []
print(countSubset(index=0, total=0))
