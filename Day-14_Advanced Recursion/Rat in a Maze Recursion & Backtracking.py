"""
Complexity:
Time Complexity: O(4(m*n)), because on every cell we need to try 4 different directions.
Space Complexity:  O(m*n), Maximum Depth of the recursion tree(auxiliary space).

"""


class Solution:

    def func(self, i, j, a, n, ans, move, visit):
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return

        # Downword

        if i + 1 < n and not visit[i + 1][j] and a[i + 1][j] == 1:
            visit[i][j] = 1
            self.func(i + 1, j, a, n, ans, move + "D", visit)
            visit[i][j] = 0

        # left

        if j - 1 >= 0 and not visit[i][j - 1] and a[i][j - 1] == 1:
            visit[i][j] = 1
            self.func(i, j - 1, a, n, ans, move + "L", visit)
            visit[i][j] = 0

        # right

        if j + 1 < n and not visit[i][j + 1] and a[i][j + 1] == 1:
            visit[i][j] = 1
            self.func(i, j + 1, a, n, ans, move + "R", visit)
            visit[i][j] = 0

        # Upward

        if i - 1 >= 0 and not visit[i - 1][j] and a[i - 1][j] == 1:
            visit[i][j] = 1
            self.func(i - 1, j, a, n, ans, move + "U", visit)
            visit[i][j] = 0

    def ratInMaze(self, matrix):
        n = len(matrix)
        ans = []
        visit = [[0 for _ in range(n)] for _ in range(n)]
        matrix[0][0] == 1
        self.func(0, 0, matrix, n, ans, "", visit)
        return ans


s1 = Solution()

print(s1.ratInMaze(matrix=[[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]))

print(
    s1.ratInMaze(
        matrix=[
            [1, 0, 0, 1, 0],
            [1, 0, 0, 1, 1],
            [0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1],
        ]
    )
)


# matrix = [[1 0 0 1 0],
#           [0 0 1 1],
#           [1 0 1 0 1 0],
#           [1 1 1 1 1],
#           [0 1 0 1 1]]
