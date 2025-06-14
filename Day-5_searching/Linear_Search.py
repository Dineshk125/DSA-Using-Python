def Linear_Search(nums):

    for i in range(0, len(nums)):
        if nums[i] == Target:
            return i
    return -1


Target = int(input("Enter a number: "))
nums = [2, 4, 6, 3, 2, 4, 6, 4, 4, 3, 3, 5, 4, 54]

print(Linear_Search(nums))
