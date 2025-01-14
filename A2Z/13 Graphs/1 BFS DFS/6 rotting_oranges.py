# rotten orange spread in all 4 directions
# return minutes it will take to rot all oranges, return -1 if not possible
# NOTE: multiple oranges can rot at the same time - simultaneous rotting

"""

0 1 2
0 1 1
2 1 1

- returns 2 - all oranges will rot in 2 minutes - simultaneous rotting

INTUTION:
- BFS to spread rotten oranges in all 4 directions
- use a queue to keep track of rotten oranges and time passed

NOTE: Multisource Flood Fill - as we start BFS with all 2s as source

"""


from collections import deque


# BFS: O(N*M) time and space
class Solution:
    def orangesRotting(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        fresh_oranges = 0  # avoid extra loop at end
        q = deque()

        # add all rotten oranges to queue
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))  # (row, col, minutes)
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh_oranges += 1

        # compared to NEETCODE APPROACH, here using time_max, cause we only check for `while queue` and not fresh > 0
        time_max = 0

        while q:
            r, c, time = q.popleft()
            time_max = max(time_max, time)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if (
                    new_row in range(n)
                    and new_col in range(m)
                    and (new_row, new_col) not in visited
                    and grid[new_row][new_col] == 1
                ):
                    q.append((new_row, new_col, time + 1))
                    visited.add((new_row, new_col))
                    grid[new_row][new_col] = 2
                    fresh_oranges -= 1  # Reduce fresh oranges count

        # # Check if any fresh oranges left
        # for i in range(n):
        #     for j in range(m):
        #         if grid[i][j] == 1:
        #             return -1

        if fresh_oranges > 0:
            return -1

        return time_max


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(Solution().orangesRotting(grid))  # 4

""" SPACE OPTIMIZED: O(N*M) time and O(1) space --- NEETCODE APPROACH"""


class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while fresh > 0:
            flag = False
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            row, col = r + dr, c + dc
                            if (
                                row in range(ROWS)
                                and col in range(COLS)
                                and grid[row][col] == 1
                            ):
                                grid[row][col] = 3
                                fresh -= 1
                                flag = True

            if not flag:
                return -1

            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time
