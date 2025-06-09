n = 12121

num = n
peli = 0

while num > 0:
    d = num % 10
    peli = peli * 10 + d
    num = num // 10
if peli == n:
    print("Pelindrome")
else:
    print("not pelindrome")
