# Method -> 1

s = "NITI"
n = len(s)
left = 0
right = n - 1

while left < right:
    if s[left] != s[right]:
        print("Not Pelindrome")
        break
    else:
        print("Pelindrome")
        break

# Method -> 2
s = "NITIN"


def prlindrome(s, left=0, right=len(s) - 1):
    if s[left] == s[right]:
        return "Is Pelindrome"
    elif s[left] != s[right]:
        return "Not Pelindrome."
    return (left + 1, right - 1)


print(prlindrome(s))

# Method -> 3

s = input("Entter a string: ")


def pelindrome_No(s, left=0, right=len(s) - 1):
    if left >= right:
        return "Is Pelindrome"
    if s[left] != s[right]:
        return "Not Pelindrome."
    return pelindrome_No(s, left + 1, right - 1)


print(pelindrome_No(s))


# Method -> 1

s = "NITIN"
n = len(s)
left = 0
right = n - 1

while left < right:
    if s[left] != s[right]:
        print("Not Pelindrome")
    left += 1
    right -= 1
print("Is Pelindrome")
