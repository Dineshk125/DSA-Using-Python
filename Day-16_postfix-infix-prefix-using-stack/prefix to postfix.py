class PosttoInfix:

    def postToinfix(self, s):
        n = len(s)
        stack = []

        for char in range(n - 1, -1, -1):
            if s[char].isalnum():  # If charector is an operator, push it into stack
                stack.append(s[char])
            else:
                # Pop two operands
                operator1 = stack.pop()
                operator2 = stack.pop()

                # Combine operator with the operator
                new_expr = f"{operator1}{operator2}{s[char]}"

                # Push new result in to the stack
                stack.append(new_expr)

        return stack[-1]


s1 = PosttoInfix()

exp = input("Enter Postfix Expression: ")

x = s1.postToinfix(exp)
print(x)
