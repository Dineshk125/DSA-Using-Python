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


# method 2 --->
class Solution:
    def isValid(self, s):
        sb = 0
        cb = 0
        simp = 0

        for ch in s:
            if ch == "(" and simp >= 0:
                simp += 1
            elif ch == "[" and sb >= 0:
                sb += 1
            elif ch == "{" and cb >= 0:
                cb += 1
            elif ch == ")":
                simp -= 1
            if ch == "]":
                sb -= 1
            if ch == "}":
                cb -= 1

        if sb == 0 and cb == 0 and simp == 0:
            return True
        else:
            return False


s1 = Solution()
print(s1.isValid("[({[]})]"))
