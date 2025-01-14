"""
mat =
1  0  1
1  1  0
1  0  0

- find the distance to nearest 1 for each cell (manhattan distance)

ans =
0  1  0
0  0  1
0  1  2
"""

# STRIVER APPROACH: BFS, without modifying original matrix
# TC: O(m * n)
# SC: O(m * n)

from collections import deque


def nearest_01_matrix(mat):
    m, n = len(mat), len(mat[0])
    visited = [[False] * n for _ in range(m)]
    distance = [[0] * n for _ in range(m)]
    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                queue.append((i, j, 0))  # row, col, steps
                visited[i][j] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS from all 1s
    # update distance for all 0s as per steps required to reach from nearest 1
    while queue:
        row, col, steps = queue.popleft()
        # update distance for 0s when first time visited (popped)
        distance[row][col] = steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if (
                new_row in range(m)
                and new_col in range(n)
                and not visited[new_row][new_col]
            ):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, steps + 1))

    return distance


mat = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
print(nearest_01_matrix(mat))


# WITHOUT USING EXTRA SPACE
# TC: O(m * n)
# SC: O(V) ---> just the queue
def updateMatrix(mat):
    m, n = len(mat), len(mat[0])
    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                queue.append((i, j))
                # update nearest "1" distance ---> for 1s = 0, for 0s = infinity
                mat[i][j] = 0
            else:
                mat[i][j] = float("inf")

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # BFS from all 1s
    # update distance for all 0s where distance is less than current
    while queue:
        row, col = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # within bounds
            if new_row in range(m) and new_col in range(n):
                # only update if new distance is less than current
                if mat[new_row][new_col] > mat[row][col] + 1:
                    mat[new_row][new_col] = mat[row][col] + 1
                    queue.append((new_row, new_col))

    return mat

print(updateMatrix(mat))


# LEETCODE VARIANT: 01 MATRIX -- find the nearest 0 for each cell