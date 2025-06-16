matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        print(matrix[i][j], end=" ")
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
        if i != j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if i >= j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if j + i >= rows - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = len(matrix)
col = len(matrix[0])

for i in range(0, rows):
    for j in range(0, col):
        if i + j == rows - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
