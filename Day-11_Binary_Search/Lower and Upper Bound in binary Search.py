# lower Bound [find smalest index such that target nums[i] >= target]


def lowerBound(nums, target):
    nums.sort()
    n = len(nums)
    lower_boundd = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            lower_boundd = mid
            high = mid - 1
        else:
            low = mid + 1

    return lower_boundd


print(
    lowerBound(
        nums=[1, 2, 3, 4, 4, 5, 7, 6, 7, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15],
        target=7,
    )
)


# Upper Bound [find smalest index such that target nums[i] > target]


def upperBound(nums, target):
    nums.sort()
    n = len(nums)
    upper_boundd = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            upper_boundd = mid
            high = mid - 1
        else:
            low = mid + 1

    return upper_boundd


print(
    upperBound(
        nums=[1, 2, 3, 4, 4, 5, 7, 6, 7, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15],
        target=4,
    )
)
