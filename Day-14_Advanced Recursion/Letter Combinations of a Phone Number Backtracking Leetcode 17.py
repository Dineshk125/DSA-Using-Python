"""
Complexity
Time complexity: O(4^N∗N)

Space complexity: O(N), N = Stack Space
"""

print("Method -> 1")


class Solution:

    def laterCombination(self, digits):
        result = []
        char_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, subset):

            if index >= len(digits):
                result.append("".join(subset))
                return

            for ch in char_map[digits[index]]:
                subset.append(ch)
                backtrack(index + 1, subset)
                subset.pop()

        backtrack(0, [])
        return result


s1 = Solution()

print(s1.laterCombination("23"))


print("Method -> 2")


class Solution(object):

    def backtrack(self, index, subset, char_map, digits, result):
        if index >= len(digits):
            result.append("".join(subset))
            return

        for ch in char_map[digits[index]]:
            subset.append(ch)
            self.backtrack(index + 1, subset, char_map, digits, result)
            subset.pop()

    def letterCombinations(self, digits):
        if not digits:
            return []
        result = []
        char_map = {
            # "1": "00",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
            # "*": ".",
            # "0": "+-*/",
            # "#": "@",
        }
        self.backtrack(0, [], char_map, digits, result)
        return result


s1 = Solution()

print(s1.letterCombinations("9"))
