from collections import deque


# TC = SC = O(N*M)
def solve(maze, entrance):
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()

    n = len(maze)
    m = len(maze[0])

    q = deque()
    q.append((*entrance, 0))
    visited.add(tuple(entrance))

    while q:
        r, c, steps = q.popleft()

        # reached exit (not same as entry)
        if (r == 0 or r == n - 1 or c == 0 or c == m - 1) and (
            r != entrance[0] or c != entrance[1]
        ):
            return steps

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            if (
                nr in range(n)
                and nc in range(m)
                and maze[nr][nc] == "."
                and (nr, nc) not in visited
            ):
                visited.add((nr, nc))
                q.append((nr, nc, steps + 1))

    return -1


# instead of visited ccan modify the visited cells to wall '+', but "DO NOT MODIFY THE INPUT UNTIL ASKED"
