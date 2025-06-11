# insertion sort inn acending order

nums = [2, 5, 6, 3, 2, 4, 20, 9, 8]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertion_sort(nums))


# insertion sort inn Decending order

nums = [2, 5, 6, 3, 2, 4, 20, 9, 8]


def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertion_sort(nums))
