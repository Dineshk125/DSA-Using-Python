## Brut Force Sollution

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(matrix, end=" ")
print()
row = len(matrix)
col = len(matrix[0])


def mark_inf(matrix, r, c):

    row = len(matrix)
    col = len(matrix[0])

    for i in range(0, col):
        if matrix[r][i] != 0:
            matrix[r][i] = float("-inf")

    for j in range(0, row):
        if matrix[j][c] != 0:
            matrix[j][c] = float("-inf")


def set_zero(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(0, row):
        for j in range(0, col):
            if matrix[i][j] == float("-inf"):
                matrix[i][j] = 0
    return matrix


for i in range(0, row):
    for j in range(0, col):
        if matrix[i][j] == 0:
            mark_inf(matrix, i, j)

for i in range(0, row):
    for j in range(0, col):
        if matrix[i][j] == 0:
            set_zero(matrix)


print(matrix)

# Optimal Solution


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(matrix, end=" ")
print()
row = len(matrix)
col = len(matrix[0])

rowtrack = [0 for _ in range(0, row)]
coltrack = [0 for _ in range(0, col)]

for i in range(0, row):
    for j in range(0, col):
        if matrix[i][j] == 0:
            rowtrack[i] = -1
            coltrack[j] = -1

for i in range(0, row):
    for j in range(0, col):
        if rowtrack[i] == -1 or coltrack[j] == -1:
            matrix[i][j] = 0

print(matrix)
