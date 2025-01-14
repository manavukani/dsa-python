# find # 1s for which you cannot go out of boundary
# same intution - all those connected to boundary can move out
# result - rest of 1s

"""
0  0  0  0
1  0  1  0
0  1  1  0
1  0  0  1

res = 3
"""

# Same logic as 'surrounded regions' for DFS


# ===== Using BFS =====
# multisource flood fill as we start BFS with all 1s (at boundary) as source
from collections import deque


def solve(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    q = deque()

    # ALRENATIVE WAY TO TRAVERSE - FIRST AND LAST ROW / COL (but I prefer prior one)
    for i in range(n):
        for j in range(m):
            # condn for first/last row/col
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                if grid[i][j] == 1:
                    q.append((i, j))
                    visited[i][j] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        row, col = q.popleft()
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc
            if (
                newRow in range(n)
                and newCol in range(m)
                and not visited[newRow][newCol]
                and grid[newRow][newCol] == 1
            ):
                q.append((newRow, newCol))
                visited[newRow][newCol] = True

    cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                cnt += 1
    return cnt


grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
print(solve(grid))

"""

TC: O(N * M)
SC: O(N * M)

SPACE OPTIMIZATION:
- can save space by eliminating the need of visited by marking the visited as 'X'
- "but never change the data"
"""
