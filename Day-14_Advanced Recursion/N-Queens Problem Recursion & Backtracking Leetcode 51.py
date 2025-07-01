print("# Optimal Solution , method -> 1")

"""
T.C. = O(N!)
S.C. = O(N)+O(5N)+O(N^2)

"""


class Solution:

    def solve(self, col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
        if col == n:
            ans.append(board[:])
            return

        for row in range(n):
            if (
                leftRow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftRow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1
                self.solve(
                    col + 1, board, ans, leftRow, upperDiagonal, lowerDiagonal, n
                )
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftRow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]
        leftRow = [0] * n
        lowerDiagonal = [0] * (2 * n - 1)
        upperDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
        return ans


s1 = Solution()

print(s1.solveNQueens(4))

print("# Brut Solution , method -> 2")

"""
T.C. -> O(N! * N)
S.C. -> O(N^2 + N)

"""


class Solution:
    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]

        def isSafe(row, col):
            # Check upper-left diagonal
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check left row
            c = col
            while c >= 0:
                if board[row][c] == "Q":
                    return False
                c -= 1

            # Check bottom-left diagonal
            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == "Q":
                    return False
                r += 1
                c -= 1

            return True

        def solve(col):
            if col == n:
                ans.append(list(board))
                return

            for row in range(n):
                if isSafe(row, col):
                    board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                    solve(col + 1)
                    board[row] = (
                        board[row][:col] + "." + board[row][col + 1 :]
                    )  # backtrack

        solve(0)
        return ans


s = Solution()

print(s.solveNQueens(n=4))
# output = s.solveNQueens(4)
# for board in output:
#     for row in board:
#         print(row)
#     print()  # separator between solutions
