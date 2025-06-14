# Method -> 1
nums1 = [1, 2, 3, 4, 5, 6, 8, 11]
nums2 = [1, 1, 2, 4, 6, 7, 8]

n = len(nums1)
m = len(nums2)
i, j = 0, 0
result = []

while i < n and j < m:
    if nums1[i] <= nums2[j]:
        if len(result) == 0 or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    else:
        if len(result) == 0 or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1

while i < n:
    if len(result) == 0 or result[-1] != nums1[i]:
        result.append(nums1[i])
    i += 1
while j < m:
    if len(result) == 0 or result[-1] != nums2[j]:
        result.append(nums2[j])
    j += 1

print(result)


# Method -> 2

nums1 = [1, 2, 3, 4, 5, 6, 8]
nums2 = [1, 1, 2, 4, 6, 7, 8]


def Merge_Sorted_Array(nums1, nums2):
    result = []
    if nums1 == nums2:
        return
    for i in nums1:
        if i not in result:
            result.append(i)
    for j in nums2:
        if j not in result:
            result.append(j)
    print(result)


Merge_Sorted_Array(nums1, nums2)


# Method -> 3
nums1 = [1, 2, 3, 4, 5, 6, 8]
nums2 = [1, 1, 2, 4, 6, 7, 8]


result = []
for i in nums1:
    if i not in result:
        result.append(i)
for j in nums2:
    if j not in result:
        result.append(j)
print(result)
