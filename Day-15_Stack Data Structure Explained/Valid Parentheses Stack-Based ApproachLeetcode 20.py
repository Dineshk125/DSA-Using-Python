class Parenthesis:

    def validParths(self, s):

        stack = []

        for bracket in s:
            if bracket == "(" or bracket == "[" or bracket == "{":
                stack.append(bracket)

            else:
                if len(stack) == 0:
                    return False
                ch = stack.pop()

                if (
                    (bracket == ")" and ch == "(")
                    or (bracket == "]" and ch == "[")
                    or (bracket == "}" and ch == "{")
                ):
                    continue
                else:
                    return False
        return len(stack) == 0


s1 = Parenthesis()

print(s1.validParths(s=""))


class Solution:
    def isPalindrome(self, x):
        def palindrom(x):
            k = x
            if k[::-1] == k:
                return True
            else:
                return False

        return palindrom(x)


s1 = Solution()
print(s1.isPalindrome(121))
