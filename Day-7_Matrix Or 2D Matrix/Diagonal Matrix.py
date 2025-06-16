matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

row = len(matrix)
col = len(matrix[0])

for i in range(0, row):
    for j in range(0, col):
        if i == j:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

row = len(matrix)
col = len(matrix[0])

for i in range(0, row):
    for j in range(0, col):
        if i + j == row - 1:  # if i + j == col - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
