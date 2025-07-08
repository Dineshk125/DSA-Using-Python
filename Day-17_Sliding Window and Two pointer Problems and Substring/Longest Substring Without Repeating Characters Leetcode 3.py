"""
Brut Force Solution

T.C. = O(N(N+1))//2 ~~ O(N^2)
S.C. = O(N)

"""

x = "abcdefabesd"

maxi = 0

for i in range(0, len(x)):
    my_set = set()
    for j in range(i, len(x)):
        if x[j] in my_set:
            break
        maxi = max(maxi, j - i + 1)
        my_set.add(x[j])
print(maxi)

"""
Complexity
Time complexity: O(n)

Space complexity: O(n)

"""
s = "ancdefsaghojklramnopqr"

left = 0
right = 0

my_dict = {}
maxi = 0

while right < len(s):
    if s[right] in my_dict:
        left = max(left, my_dict[s[right]] + 1)
    maxi = max(maxi, right - left + 1)
    my_dict[s[right]] = right
    right += 1
print(maxi)
print(my_dict)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        maxi = 0
        my_dict = {}

        while right < len(s):
            if s[right] in my_dict:
                left = max(left, my_dict[s[right]] + 1)
            maxi = max(maxi, right - left + 1)
            my_dict[s[right]] = right
            right += 1
        return maxi


s1 = Solution()

print(s1.lengthOfLongestSubstring(s="abcdasdf"))
