from collections import deque

'''

1  0
0  1  ====> o/p = 2 steps

goal: start from (0,0) and reach (n-1,n-1)
condition: only walk on 0, in any directions (including diagonals)
output: steps taken

'''

# Simple BFS no need of Priority Queue since dist = 1 between all nodes
# O(V+E)
def shortestPathBinaryMatrix(grid):
    n = len(grid)

    # src or dest blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    q = deque()
    q.append((0, 0, 1)) # r, c, steps
    visited = set((0,0))

    while q:
        r, c, steps = q.popleft()

        # up, down, right, left and diagonals
        direction = [(-1, -1), (-1, 0), (-1, 1),
                        (0, -1),          (0, 1),
                        (1, -1),  (1, 0), (1, 1)]

        # reached destination ---> return
        if r == n-1 and c == n-1:
            return steps

        # unvisited
        if (r,c) not in visited:
            visited.add((r,c))
            
            # check adjacent cells
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if (
                    nr in range(n)
                    and nc in range(n)
                    and (nr,nc) not in visited
                    and grid[nr][nc] == 0
                ):
                    q.append((nr, nc, steps + 1))
    return -1