# # Hashing using charactors
# s = "azxyxxxyzazxy"
# r = ["a", "z", "d", "r"]

# hash_list = [0] * 26
# for ch in s:
#     ascii_val = ord(ch)
#     index = ascii_val - 97
#     hash_list[index] += 1

# for ch in r:
#     ascii_val = ord(ch)
#     index = ascii_val - 97
#     print(hash_list[index])


# Hashing using charactors
s = "azxyxxxyzazxyAAAAA"
r = ["a", "z", "d", "r", "A"]
hash_list = [0] * 52
for ch in s:
    index = ord(ch) - 97 + 26
    hash_list[index] += 1

for ch in r:
    index = ord(ch) - 97 + 26
    print(f"{ch} : {hash_list[index]}")

