# Methos -> 1 Using List

n = 234233242

num = n
digits = []

while num > 0:
    digits.append(num % 10)
    num = num // 10
print(digits)


# Method -> 2

n = 234233242

num = n
digit = 0

while num > 0:
    digit = num % 10
    num = num // 10
    print(digit, end="")
