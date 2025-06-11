## Bubble Sort in Acending order


nums = [3, 4, 6, 2, 3, 2, 2, 5, 6]


def Bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(Bubble_sort(nums))


## Bubble Sort in Decending order

nums = [3, 4, 6, 2, 3, 2, 2, 5, 6]


def Bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


print(Bubble_sort(nums))
