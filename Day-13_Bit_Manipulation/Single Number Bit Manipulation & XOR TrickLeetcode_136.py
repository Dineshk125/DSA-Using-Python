# Method -> 1

arr = [1, 1, 2, 2, 4, 6]

hash_map = {}

for num in arr:
    hash_map[num] = hash_map.get(num, 0) + 1

for key in hash_map:
    if hash_map[key] == 1:
        print(key, end=" ")

## Method -> 2

arr = [1, 1, 2]

ans = 0

for num in arr:
    ans = ans ^ num
print()
print(ans)
