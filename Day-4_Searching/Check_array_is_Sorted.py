nums = [1, 2, 3, 4, 5, 62]

n = len(nums)


def Arrat_Sort(nums):
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return "False: Array is Not Sorted."
    return "True: Array is Sorted."


print(Arrat_Sort(nums))
