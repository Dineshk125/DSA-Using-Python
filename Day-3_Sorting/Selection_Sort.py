## Selection Sort in Acending order

nums = [5, 6, 3, 4, 7, 8, 2, 1, 1, 2, 4, 0, 0]


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort(nums))


## Selection Sort in Decending order

nums = [5, 6, 3, 4, 7, 8, 2, 0]


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums


print(selection_sort(nums))
