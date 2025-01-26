from collections import deque

def solve(grid):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    """find fresh count and add rotten to queue"""
    fresh_count = 0
    q = deque()
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                fresh_count += 1
            if grid[i][j] == 2:
                q.append((i, j, 0))  # row, col, time
                visited.add((i, j))

    # answer to be returned
    time_max = 0

    """bfs logic"""
    while q:
        r, c, time = q.popleft()
        time_max = max(time, time_max)

        # check all nei
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if (
                nr in range(len(grid))
                and nc in range(len(grid[0]))
                and (nr, nc) not in visited # not visited
                and grid[nr][nc] == 1  # must be fresh
            ):
                visited.add((nr,nc)) # add nei to visited
                q.append((nr, nc, time + 1)) # add to queue, to rotten others
                grid[nr][nc] = 2  # make nei rotten
                fresh_count -= 1 # make nei rotten, fresh count dec.
                

    if fresh_count > 0:
        return -1

    return time_max
