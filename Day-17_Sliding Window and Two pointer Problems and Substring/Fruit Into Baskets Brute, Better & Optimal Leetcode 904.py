"""
Better Solution

T.C. = O(n(n+1))/2 ~ O(n^2)
S.C. = O(n)

"""

nums = [3, 3, 3, 1, 2, 1, 1, 3]

n = len(nums)
max_length = 0


for i in range(0, n):
    my_set = set()
    for j in range(i, n):
        my_set.add(nums[j])
        if len(my_set) > 2:
            break
        max_length = max(max_length, j - i + 1)
print(max_length)


"""
Better Solution

T.C. = O(n)+O(n) = O(2n) ~ O(n)
S.C. = O(1)

"""
nums = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]

n = len(nums)
left = 0
right = 0

my_dict = {}
maxi = 0

while right < len(nums):
    my_dict[nums[right]] = my_dict.get(nums[right], 0) + 1
    while len(my_dict) > 2:
        my_dict[nums[left]] -= 1
        if my_dict[nums[left]] == 0:
            del my_dict[nums[left]]
        left += 1
    if len(my_dict) <= 2:
        maxi = max(maxi, right - left + 1)
    right += 1
print(maxi)


"""
Optimal Solution

T.C. = O(n)
S.C. = O(1)

"""


class Solution(object):
    def totalFruit(self, fruits):
        n = len(fruits)
        left = 0
        right = 0

        my_dict = {}
        maxi = 0

        while right < len(fruits):
            my_dict[fruits[right]] = my_dict.get(fruits[right], 0) + 1
            if len(my_dict) > 2:
                my_dict[fruits[left]] -= 1
                if my_dict[fruits[left]] == 0:
                    del my_dict[fruits[left]]
                left += 1
            if len(my_dict) <= 2:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi


s1 = Solution()

print(s1.totalFruit(fruits=[1, 2, 3, 2, 2]))
print(s1.totalFruit(fruits=[1, 2, 1]))
print(s1.totalFruit(fruits=[0, 1, 2, 2]))
