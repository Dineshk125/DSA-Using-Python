# Upper Right Triangle

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]


row = len(matrix)
col = len(matrix[0])

for i in range(0, row):
    for j in range(0, col):
        if j >= i:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()


#  Upper Left Triangal

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]


row = len(matrix)
col = len(matrix[0])

for i in range(0, row):
    for j in range(i, col):
        print(matrix[i][j], end=" ")
    print()

# Upper left using if else

matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1], [2, 3, 4, 5]]


row = len(matrix)
col = len(matrix[0])

for i in range(0, row):
    for j in range(0, col):
        if i + j <= col - 1:
            print(matrix[i][j], end=" ")
        else:
            print(" ", end=" ")
    print()
