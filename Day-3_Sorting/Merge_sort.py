arr = [1, 3, 2, 21, 5, 43, 3, 35, 56]

left = [23, 3, 23, 23]
right = [23, 4, 45, 56, 67]


def Merge_array(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m:
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < n:
        while i < n:
            result.append(left[i])
            i += 1
    if j < m:
        while j < m:
            result.append(right[j])
            j += 1
    return result


print(Merge_array(left, right))


def Merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left = Merge_sort(left_half)
    right = Merge_sort(right_half)
    return Merge_array(left, right)


print(Merge_sort(arr))
