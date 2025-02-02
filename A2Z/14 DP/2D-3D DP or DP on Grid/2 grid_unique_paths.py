# QUESTION: start from (0,0) -> end at (m-1,n-1) in a grid
# RETURN: count of all ways to reach there, can only move to bottom / right


"""RECURSIVE SOLUTION"""
# 1. Express as indexes -> (i,j)
# 2. Do stuff
# 3. Count/min/max


# TC = O(2 ^ (m*n)) ---- at each cell we have 2 possibility, up  or left
# SC = path length = O((N-1)+(M-1))
def recusrive(m, n):
    def helper(i, j):

        # base cases
        if i == 0 and j == 0:
            return 1  # valid path
        if i < 0 or j < 0:
            return 0  # invalid path

        up = helper(i - 1, j)
        left = helper(i, j - 1)

        return up + left

    return helper(m - 1, n - 1)


"""notice overlapping subproblems in recursion tree ---> MEMOIZATION"""
# top down ---> start from end and use recursion with base case to return
# STEPS: Don't recompute, init DP, store in DP


# TC = O(M * N)
# SC = O((N-1)+(M-1)) - for  recursion & O(M*N) - for DP array
def memoization(m, n):
    dp = [[-1] * n for _ in range(m)]

    def helper(i, j):
        if dp[i][j] != -1:
            return dp[i][j]

        # base cases
        if i == 0 and j == 0:
            return 1  # valid path
        if i < 0 or j < 0:
            return 0  # invalid path

        up = helper(i - 1, j)
        left = helper(i, j - 1)

        dp[i][j] = up + left
        return dp[i][j]

    return helper(m - 1, n - 1)


"""recursive stack space is redundant ----> TABULATION"""
# bottom up --> start from base case and go till end
# STEPS: declare base case, express all states in for loops, copy recurrence


# TC = O(M*N) --- 2 for loops
# SC = O(M*N) --- only for DP array
def tabulation(m, n):
    dp = [[-1] * n for _ in range(m)]

    # express all states
    for i in range(m):
        for j in range(n):

            # base condition: if at start, only 1 way to reach there
            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up = 0
            left = 0

            # boundary condition: check cannot move beyond 0
            if i > 0:
                up = dp[i - 1][j]
            if j > 0:
                left = dp[i][j - 1]

            dp[i][j] = up + left

    return dp[m - 1][n - 1]


"""as we only use previous row/column ---> SPACE OPTIMIZE"""
# dp = up + left -> use prev row, prev col (same row, prev value)


# TC = O(M*N)
# SC = O(N)
def optimal(m, n):

    # init prev row ---- IMP
    prev_row = [0] * n

    for i in range(m):

        # init current row ---- IMP
        curr = [0] * n

        for j in range(n):

            if i == 0 and j == 0:
                curr[j] = 1
                continue

            up = 0
            left = 0

            # boundary condition: check cannot move beyond 0
            if i > 0:
                up = prev_row[j]
            if j > 0:
                left = curr[j - 1]

            curr[j] = up + left

        # update curr ---- IMP
        prev_row = curr

    return prev_row[n - 1]


print(optimal(3, 2))
