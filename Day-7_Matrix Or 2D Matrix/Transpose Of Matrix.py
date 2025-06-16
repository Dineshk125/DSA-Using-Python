matrix = [[0, 1, 2, 3], [4, 5, 6, 7]]
print(matrix, end=" ")
print()

row = len(matrix)
col = len(matrix[0])
result = [[0] * row for _ in range(0, col)]
diff = col - row
for i in range(0, row - diff):
    for j in range(0, col - diff):
        result[j][i] = matrix[i][j]
print(result, end=" ")
print()

matrix = [[0, 1, 2, 3], [4, 5, 6, 7]]
print(matrix, end=" ")
print()

row = len(matrix)
col = len(matrix[0])

result = [[matrix[j][i] for j in range(0, row)] for i in range(0, col)]

print(result, end=" ")
