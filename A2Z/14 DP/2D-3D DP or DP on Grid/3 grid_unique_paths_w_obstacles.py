# QUESTION: start from (0,0) -> end at (m-1,n-1) in a grid
# CONSTRAINTS: 1 is blocked, 0 is normal
# RETURN: count of all ways to reach there, can only move to bottom / right


def recursive(maze):
    m = len(maze)
    n = len(maze[0])

    def helper(i, j):

        # REACHED BLOCKED CELL
        if i >= 0 and j >= 0 and maze[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            return 1

        if i < 0 or j < 0:
            return 0

        up = helper(i - 1, j)
        left = helper(i, j - 1)

        return up + left

    return helper(m - 1, n - 1)


def memoization(maze):
    m = len(maze)
    n = len(maze[0])

    dp = [[-1 for _ in range(n)] for _ in range(m)]

    def helper(i, j):

        #  out of bounds / OBSTACLE
        if i < 0 or j < 0 or maze[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            return 1

        if dp[i][j] != -1:
            return dp[i][j]

        up = helper(i - 1, j)
        left = helper(i, j - 1)

        dp[i][j] = up + left
        return dp[i][j]

    return helper(m - 1, n - 1)


def tabulation(maze):
    m = len(maze)
    n = len(maze[0])

    dp = [[-1] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):

            # OBSTACLE (won't go out of bounds, cause using for loop to stay within)
            if maze[i][j] == 1:
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up = 0
            left = 0

            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = up + left

    return dp[m - 1][n - 1]


def optimal(maze):
    m = len(maze)
    n = len(maze[0])

    prev_row = [0] * n
    for i in range(m):
        curr = [0] * n

        for j in range(n):
            # OBSTACLE
            if maze[i][j] == 1:
                curr[j] = 0
            elif i == 0 and j == 0:
                # Starting pt
                curr[j] = 1
            else:
                # For other cells
                up = prev_row[j] if i > 0 else 0
                left = curr[j - 1] if j > 0 else 0
                curr[j] = up + left

        prev_row = curr

    return prev_row[n - 1]
