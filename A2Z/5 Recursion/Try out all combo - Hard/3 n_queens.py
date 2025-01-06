# each row has one queen
# each column has one queen
# each diagonal has one queen


# we need o(N) for a row, o(N) for the column, and o(N) for the diagonal
def is_safe(row, col, board, n):
    dup_row = row
    dup_col = col

    # check previous diagonally top left
    while row >= 0 and col >= 0:
        if board[row][col] == "Q":
            return False
        row -= 1
        col -= 1

    row = dup_row
    col = dup_col

    # check previous columns (same row)
    while col >= 0:
        if board[row][col] == "Q":
            return False
        col -= 1

    # check previous diagonally botoom left
    row = dup_row
    col = dup_col
    while row < n and col >= 0:
        if board[row][col] == "Q":
            return False
        row += 1
        col -= 1

    return True


def solve(col, board, ans, n):
    if col == n:
        ans.append(["".join(row) for row in board])
        return

    for row in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = "Q"
            solve(col + 1, board, ans, n)
            board[row][col] = "."


def n_queens(n):
    ans = []
    board = [["."] * n for _ in range(n)]

    solve(0, board, ans, n)
    return ans


# Time Complexity: O(n!)
# Space Complexity: O(n^2)

# test cases
print(n_queens(4))


"""
APPROACH 2: OPTIMIZED IS_SAFE FUNCTION WITH HASHING

https://www.youtube.com/watch?v=i05Ju7AftcM&t=1750s
"""


class Solution:
    def solve(self, col, board, ans, leftrow, upperDiagonal, lowerDiagonal, n):
        # If all queens are placed, add the board configuration to the answer
        if col == n:
            ans.append(board[:])
            return

        # Try placing a queen in all rows one by one
        for row in range(n):
            # Check if the queen can be placed on board[row][col]
            if (
                leftrow[row] == 0
                and lowerDiagonal[row + col] == 0
                and upperDiagonal[n - 1 + col - row] == 0
            ):
                # Place the queen
                board[row] = board[row][:col] + "Q" + board[row][col + 1 :]
                leftrow[row] = 1
                lowerDiagonal[row + col] = 1
                upperDiagonal[n - 1 + col - row] = 1

                # Recur to place the rest of the queens
                self.solve(
                    col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n
                )

                # If placing queen in board[row][col] doesn't lead to a solution,
                # then remove the queen (backtrack)
                board[row] = board[row][:col] + "." + board[row][col + 1 :]
                leftrow[row] = 0
                lowerDiagonal[row + col] = 0
                upperDiagonal[n - 1 + col - row] = 0

    def solveNQueens(self, n):
        ans = []
        board = ["." * n for _ in range(n)]
        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)
        self.solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n)
        return ans


sol = Solution()
print(sol.solveNQueens(4))