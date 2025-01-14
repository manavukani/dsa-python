from collections import deque

""" ----- ORIGNAL QUESTION ----- """


# WITH DFS
def dfs_solve(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def dfs(r, c):
        # out of bounds + IMPORTANT --> water, already visited
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return

        visited.add((r, c))

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                dfs(r, c)

    return islands


# WITH BFS
def numIslands(self, grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    # bfs logic
    def bfs(r, c):
        q = deque()
        visited.add((r, c))
        q.append((r, c))

        while q:
            cur_row, cur_col = q.popleft()  # queue for BFS
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                next_row, next_col = cur_row + dr, cur_col + dc
                # within bounds, land, not visited
                if (
                    next_row in range(rows)
                    and next_col in range(cols)
                    and grid[next_row][next_col] == "1"
                    and (next_row, next_col) not in visited
                ):

                    visited.add((next_row, next_col))
                    q.append((next_row, next_col))

    # iterate through grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print("Num of Islands:", numIslands(grid))


""" ----- FOLLOW-UP: Return the maximum area of an island ----- """


def maxArea_dfs(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    max_area = 0

    def dfs(r, c):
        if (
            r < 0
            or r >= rows
            or c < 0
            or c >= cols
            or grid[r][c] == "0"
            or (r, c) in visited
        ):
            return 0

        visited.add((r, c))
        area = 1

        area += dfs(r + 1, c)
        area += dfs(r - 1, c)
        area += dfs(r, c + 1)
        area += dfs(r, c - 1)

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                max_area = max(max_area, dfs(r, c))

    return max_area


# test
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
print("Max Area:", maxArea_dfs(grid))


""" ----- FOLLOW-UP 2: Perimeter of island ----- """


# when we reach boundar or water, we add 1, so base case is 1
def find_perimeter(grid):
    visited = set()
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        # if reach boundary or water, add 1
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 1

        # IMP: not add 1 if already visited
        if (r, c) in visited:
            return 0

        visited.add((r, c))

        perimeter = 0

        perimeter += dfs(r + 1, c)
        perimeter += dfs(r - 1, c)
        perimeter += dfs(r, c + 1)
        perimeter += dfs(r, c - 1)

        return perimeter

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return dfs(r, c)


# test
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print("Perimeter:", find_perimeter(grid))  # 16
