"""
T.C. - O(N) + O(N).... = O(5N) ~ O(N)
S.C. - O(N) + O(N) ~ O(N)
"""


class InfixToPrefix:

    def operators(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^" and ch == "**":
            return 3
        return 0

    def InfiTopre(self, s):

        s = s[::-1]

        s = s.replace("(", "temp").replace(")", "(").replace("temp", ")")

        stack = []
        result = []

        for char in s:
            if char.isalnum():
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.operators(stack[-1]) > self.operators(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())
        return "".join(result[::-1])


s1 = InfixToPrefix()

user_input = input("Enter Infix Expression: ")
x = s1.InfiTopre(user_input)
print(x)
