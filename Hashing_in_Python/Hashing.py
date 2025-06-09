# Prestoring values into same datastructure like list/set/ dict and the fatching it.


# Brut forc solution

n = [1, 2, 3, 3, 3, 4, 4, 5, 6, 72, 22, 4, 3]
m = [3, 4, 1, 111, 33, 22, 5, 7]

result = {}
for i in m:
    count = 0

    for j in n:
        if i == j:
            count += 1
    print(count, end=" ")
"""
T.C. = O(nxm) => O(10^8x10^8) => O(10^16) > 10^8 because  - 1<=n[i]<=10, n can have 10^8 elements
S.C. = O(1)
"""


# Optimal Solution

n = [1, 2, 3, 4, 7]
m = [1, 3, 4, 33, 22, 5, 7]

hash_list = [0] * 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(f"{num} : {hash_list[num]}")


"""
T.C. = O(n+m)=> O(N+N) => O(2N) => remove constant => O(N)
S.C. => O(11) => O(1)
"""


n = [1, 2, 3, 4, 7]
m = [1, 3, 4, 33, 22, 5, 7]

hash_list = []
for num in range(0, 11):
    hash_list.append(n.count(num))
print(f"{num} = {hash_list}")

for num in m:
    if num > 0 and num < 11:
        print(f"{num} : {hash_list[num]}")
    else:
        print(0)


# Hashing using Dictionary

n = [1, 2, 3, 4, 7, 4, 5, 6, 7, 8, 9]
m = [1, 3, 4, 33, 22, 5, 7]

hash_dict = {}
for num in n:
    hash_dict[num] = hash_dict.get(n[num], 0) + 1
print(hash_dict)

for num in m:
    if num in hash_dict:
        print(f"{num}:{hash_dict[num]}")
    else:
        print(0)


# Hashing using charactors
s = "azxyxxxyzazxy"
r = ["a", "z", "d", "r"]

hash_list = [0] * 26
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97
    hash_list[index] += 1

for ch in r:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(hash_list[index])
