"""
My approach: Multi-source BFS

- start from all gates and find distance to empty rooms
- only move in a particular direction if its empty room ('inf') and not wall (-1)
- distance to each room is set as rooms[row][col] + 1 (distance from the current room) when it is first visited.
- This ensures the minimum distance is calculated since BFS propagates layer by layer.

"""

from collections import deque


class Solution:
    """
    @param rooms: m x n 2D grid --- 0 = gate, -1 = wall, INF = empty
    @return: nothing + do not use extra 2D array space

    modify rooms to
    """

    def walls_and_gates(self, rooms):
        n = len(rooms)
        m = len(rooms[0])

        q = deque()

        # Add all gates to the queue
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:  # Gate
                    q.append((i, j))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Perform BFS
        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                # within bounds and empty room
                if (
                    0 <= new_row < n
                    and 0 <= new_col < m
                    and rooms[new_row][new_col] == 2147483647  # INF
                ):
                    # IMP ---> ensures the minimum distance to gate
                    rooms[new_row][new_col] = rooms[row][col] + 1
                    q.append((new_row, new_col))


input = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647],
]
Solution().walls_and_gates(input)
print(input)
# Expected = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]


""" NEETCODE SOLN: Multi-source BFS """


class Solution:
    def islandsAndTreasure(self, grid) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
