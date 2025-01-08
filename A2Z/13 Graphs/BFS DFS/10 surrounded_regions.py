"""
GIVEN:
X X X X
X O O X
X X O X
X O X X

ANS:
X X X X
X X X X
X X X X
X O X X

APPROACH: DFS
- start from boundary O and mark all connected O as safe.
- convert all remaining O to X.

"""

# def dfs(r, c, board, visited):
#     n = len(board)
#     m = len(board[0])
#     if r in range(n) and c in range(m) and not visited[r][c] and board[r][c] == "O":
#         visited[r][c] = True
#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)


# Do not return anything, modify board in-place instead.
def solve(board):
    if not board or not board[0]:
        return

    n = len(board)
    m = len(board[0])
    visited = [[False] * m for _ in range(n)]

    # === dfs logic ===
    def dfs(r, c):
        if r in range(n) and c in range(m) and not visited[r][c] and board[r][c] == "O":
            visited[r][c] = True
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        else:
            return

    # === SWAP LOGIC ===
    # all 'O' connected to boundary 'O' are safe
    # 1. first and last row
    for j in range(m):
        if board[0][j] == "O" and not visited[0][j]:
            dfs(0, j)
        if board[n - 1][j] == "O" and not visited[n - 1][j]:
            dfs(n - 1, j)
    # 2. first and last col
    for i in range(n):
        if board[i][0] == "O" and not visited[i][0]:
            dfs(i, 0)
        if board[i][m - 1] == "O" and not visited[i][m - 1]:
            dfs(i, m - 1)

    # all 'O' yet not visited will be unsafe --> mark as 'X'
    for i in range(n):
        for j in range(m):
            if board[i][j] == "O" and not visited[i][j]:
                board[i][j] = "X"

# TC: O(m * n)
# SC: O(m * n) --- visited matrix