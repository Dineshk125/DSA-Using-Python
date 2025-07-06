class PosttoInfix:

    def postToinfix(self, s):

        stack = []

        for char in s:
            if char.isalnum():  # If charector is an operator, push it into stack
                stack.append(char)
            else:
                # Pop two operands
                operator2 = stack.pop()
                operator1 = stack.pop()

                # Combine operator with the operator
                new_expr = f"({operator1}{char}{operator2})"

                # Push new result in to the stack
                stack.append(new_expr)

        return stack[-1]


s1 = PosttoInfix()

exp = input("Enter Postfix Expression: ")

x = s1.postToinfix(exp)
print(x)
