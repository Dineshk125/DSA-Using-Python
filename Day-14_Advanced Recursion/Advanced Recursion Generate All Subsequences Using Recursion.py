## T.C. -> O(2^N), T.C. -> O(N)


def solve(index, subset):
    global arr
    global result
    n = len(arr)
    if index >= n:
        result.append(subset.copy())
        return
    subset.append(arr[index])
    solve(index + 1, subset)
    subset.pop()
    solve(index + 1, subset)
    return result


arr = [5, 9, 7]
subset = []
index = 0
result = []

print(solve(index, subset))
