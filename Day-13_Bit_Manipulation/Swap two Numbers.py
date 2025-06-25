a = 9
b = 7

print(f"first : {a}")
print(f"Second: {b}")

a = a ^ b
b = a ^ b  # a = a^b , b = (a^b)^b, '.' b^b = 0 , b = a
a = a ^ b  # b = a^b , b = a^(a^b), '.' a^a = 0 , a = b

print("After Swapping")

print(f"first : {a}")
print(f"Second: {b}")
