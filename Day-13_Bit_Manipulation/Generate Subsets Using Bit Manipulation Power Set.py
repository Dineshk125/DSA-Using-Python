arr = [1, 2, 3]
n = len(arr)
total_Subset = 1 << n
result = []
for num in range(0, total_Subset):
    lst = []
    for i in range(0, n):
        if num & (1 << i):
            lst.append(arr[i])
    result.append(lst)
print(result)
