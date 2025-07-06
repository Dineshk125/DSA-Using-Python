"""
T.C. - O(N) + O(N) = O(2N) ~ O(N)
S.C. - O(N) + O(N) ~ O(N)
"""


class InfixToPostfix:

    def operators(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def infiTopost(self, s):
        stack = []
        result = []
        for char in s:
            # if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= "9"):
            if char.isalnum():
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:
                while stack and self.operators(stack[-1]) >= self.operators(char):
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        return "".join(result)


s1 = InfixToPostfix()
user_input = input("Enter Infix Expression: ")
x = s1.infiTopost(user_input)
print("postfix expression:", x)
