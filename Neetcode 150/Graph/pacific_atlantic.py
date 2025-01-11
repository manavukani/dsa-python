from collections import deque

"""

DFS SOLUTION: TC = SC = O(m*n)

"""


class Solution:
    def using_dfs(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            if (
                r in range(ROWS)
                and c in range(COLS)
                and (r, c) not in visit
                # since we go from ocean to nodes, current needs to be >= prevHeight
                and heights[r][c] >= prevHeight
            ):
                # mark visited
                visit.add((r, c))

                # explore neighbors
                dfs(r + 1, c, visit, heights[r][c])
                dfs(r - 1, c, visit, heights[r][c])
                dfs(r, c + 1, visit, heights[r][c])
                dfs(r, c - 1, visit, heights[r][c])
            else:
                return

        # first and last row
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        # first and last col
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # common
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res


"""

BFS SOLUTION: TC = SC = O(m*n)

"""


class Solution:
    def using_bfs(self, heights):
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS
                        and 0 <= nc < COLS
                        and not ocean[nr][nc]
                        and heights[nr][nc] >= heights[r][c]
                    ):
                        q.append((nr, nc))

        pacific = []
        atlantic = []
        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res
