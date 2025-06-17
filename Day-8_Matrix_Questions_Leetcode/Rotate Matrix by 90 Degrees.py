# Brut Force Solution

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

row = len(matrix)
col = len(matrix[0])
n = len(matrix)
result = [[0 for _ in range(0, n)] for _ in range(n)]

for i in range(0, row):
    for j in range(0, col):
        result[j][(n - 1) - i] = matrix[i][j]
print(result)

# for i in range(0, row):
#     for j in range(0, col):
#         result[j][i] = matrix[i][j]


# print(result, end=" ")

# Optimal Solution -> Rotate Matrix by 90 Degrees, Leetcode - 48


class Solution(object):
    def rotate(self, matrix):

        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]


c1 = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c1.rotate(matrix)
print(matrix)
