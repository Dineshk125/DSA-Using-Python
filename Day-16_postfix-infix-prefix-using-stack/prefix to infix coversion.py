class PosttoInfix:

    def postToinfix(self, s):
        s = s[::-1]

        stack = []

        for char in s:
            if char.isalnum():  # If charector is an operator, push it into stack
                stack.append(char)
            else:
                # Pop two operands
                operator1 = stack.pop()
                operator2 = stack.pop()

                # Combine operator with the operator
                new_expr = f"({operator1}{char}{operator2})"

                # Push new result in to the stack
                stack.append(new_expr)

        return stack[-1]


s1 = PosttoInfix()

exp = input("Enter Postfix Expression: ")

x = s1.postToinfix(exp)
print(x)


# methid -> 2


class PosttoInfix:

    def postToinfix(self, s):

        stack = []

        for char in s[::-1]:
            if char.isalnum():  # If charector is an operator, push it into stack
                stack.append(char)
            else:
                # Pop two operands
                operator1 = stack.pop()
                operator2 = stack.pop()

                # Combine operator with the operator
                new_expr = f"({operator1}{char}{operator2})"

                # Push new result in to the stack
                stack.append(new_expr)

        return stack[-1]


s1 = PosttoInfix()

exp = input("Enter Postfix Expression: ")

x = s1.postToinfix(exp)
print(x)

# method -> 3 , Without using slicing


class PosttoInfix:

    def postToinfix(self, s):
        n = len(s)

        stack = []

        for i in range(n - 1, -1, -1):
            if s[i].isalnum():  # If charector is an operator, push it into stack
                stack.append(s[i])
            else:
                # Pop two operands
                operator1 = stack.pop()
                operator2 = stack.pop()

                # Combine operator with the operator
                new_expr = f"({operator1}{s[i]}{operator2})"

                # Push new result in to the stack
                stack.append(new_expr)

        return stack[-1]


s1 = PosttoInfix()

exp = input("Enter Postfix Expression: ")

x = s1.postToinfix(exp)
print(x)
