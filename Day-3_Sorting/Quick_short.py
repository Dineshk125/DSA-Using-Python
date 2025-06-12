# Quick sort in Acending order


def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] <= pivot and i <= high - 1:
            i += 1
        while nums[j] > pivot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def Quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        Quick_sort(nums, low, p_index - 1)
        Quick_sort(nums, p_index + 1, high)


nums = [2, 6, 8, 5, 3, 2, 4, 65, 7]
high = len(nums) - 1
Quick_sort(nums, 0, high)
print(nums)


## Quick sort in decending order


def partition(nums, low, high):
    pivot = nums[low]
    i = low
    j = high
    while i < j:
        while nums[i] >= pivot and i <= high - 1:
            i += 1
        while nums[j] < pivot and j >= low + 1:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j


def Quick_sort(nums, low, high):
    if low < high:
        p_index = partition(nums, low, high)
        Quick_sort(nums, low, p_index - 1)
        Quick_sort(nums, p_index + 1, high)


nums = [2, 6, 8, 5, 3, 2, 4, 65, 7]
high = len(nums) - 1
Quick_sort(nums, 0, high)
print(nums)
