"""
WHY NOT DIJKSTRA (GREEDY ALGO) AND WHY DP?
REASON 1: The grid is constrained with only down and right movements, meaning the possible directions are limited
REASON 2: Can give wrong answers

for eg:

10 8 2
10 5 100
1  1 2

Greedy path: 10 -> 8 -> 2 -> 100 -> 2 (after reaching 2, has only 1 option = 100)

So need to try all paths ---> recursion ---> overlapping ---> DP
"""

# TRY OUT ALL PATHS --> FIND MINIMUM
# WRITE IN TERMS OF INDEX ---> i, j (min cost to reach from 0,0 to i,j)


def recursive(grid):
    def helper(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        # out of bound, increase cost too much ==> path becomes invalid
        if i < 0 or j < 0:
            return float("inf")
        # up / left
        up = helper(i - 1, j) + grid[i][j]
        left = helper(i, j - 1) + grid[i][j]
        return min(up, left)

    m = len(grid)
    n = len(grid[0])
    return helper(m - 1, n - 1)


# MEMOIZATION
# TC = O(M*N)
# SC = O(M*N) + O(M-1 + N-1) ---- DP array + path length
def memoization(grid):
    m = len(grid)
    n = len(grid[0])
    # INIT DP
    dp = [[-1] * n for _ in range(m)]

    def helper(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float("inf")
        # AVOID REPEAT CALCULATION
        if dp[i][j] != -1:
            return dp[i][j]
        up = helper(i - 1, j) + grid[i][j]
        left = helper(i, j - 1) + grid[i][j]
        # STORE TO DP
        dp[i][j] = min(up, left)
        return dp[i][j]

    return helper(m - 1, n - 1)


# TABULATION
# TC = O(M*N)
# SC = O(M*N)
def tabulation(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[-1] * n for _ in range(m)]

    # BASE CASE
    dp[0][0] = grid[0][0]

    # FOR LOOPS
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[i][j]
            else:
                # UP
                up = grid[i][j]
                # if i > 0: then only we move up --> add up value
                if i > 0:
                    up += dp[i - 1][j]
                # else i < 0 ---> invalid path
                else:
                    up += float("inf")

                # LEFT
                left = grid[i][j]
                # if j > 0: then only we move left --> add left value
                if j > 0:
                    left += dp[i][j - 1]
                # else j < 0 ---> invalid path
                else:
                    left += float("inf")

                # STORE TO DP
                dp[i][j] = min(up, left)

    return dp[m - 1][n - 1]


def tabulationButBetter(grid):
    m = len(grid)
    n = len(grid[0])
    dp = [[0] * n for _ in range(m)]

    # BASE CASE
    dp[0][0] = grid[0][0]

    # FIRST ROW
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # FIRST COL
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # REST DP TABLE
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]


# SPACE OPTIMIZATION
def optimal(grid):
    m = len(grid)
    n = len(grid[0])

    # PREVIOUS ROW
    prev_row = [0] * n

    for i in range(m):
        # CURRENT ROW
        curr = [0] * n
        for j in range(n):
            if i == 0 and j == 0:
                curr[j] = grid[i][j]
            else:
                up = grid[i][j]
                if i > 0:
                    up += prev_row[j]
                else:
                    up += float("inf")

                left = grid[i][j]
                if j > 0:
                    left += curr[j - 1]
                else:
                    left += float("inf")

                # STORE TO CURR
                curr[j] = min(up, left)

        # UPDATED CURR
        prev_row = curr

    return prev_row[n - 1]


# def inplaceTabulation(grid):
#     n = len(grid)
#     m = len(grid[0])

#     for i in range(n):
#         for j in range(m):
#             # FIRST COL
#             if i == 0:
#                 if j != 0:
#                     grid[i][j] += grid[i][j - 1]
#             # FIRST ROW
#             elif j == 0:
#                 if i != 0:
#                     grid[i][j] += grid[i - 1][j]
#             # REST DP TABLE
#             else:
#                 grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
#     return grid[n - 1][m - 1]
