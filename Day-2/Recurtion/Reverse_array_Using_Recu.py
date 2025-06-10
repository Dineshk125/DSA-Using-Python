nums = [1, 2, 3, 4, 5, 6]


def reverse_a(nums, left, right):
    if left >= right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    reverse_a(nums, left + 1, right - 1)


reverse_a(nums, 2, 4)
print(nums)
