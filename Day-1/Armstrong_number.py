n = int(input("Enter a number: "))

num = n

count = len(str(n))
digits = 0
while num > 0:
    result = num % 10
    digits += result**count
    num = num // 10

if digits == n:
    print("Is armstrong")
else:
    print("Not armstrong")
