"""
ABOUT PROBLEM:

- At any position, we can jump either 1 or 2 steps.
- Cost = Absolute difference between the current and previous position.
- Goal: Minimize the total cost.
"""

# Try all possible ways -> Return the best -> Use Dynamic Programming (DP)

# WHY GREEDY DOESN'T WORK?
# Example: [30, 10, 60, 10, 60, 50]
# Greedy approach (minimizing locally at each step): 30 -> 10 -> 10 -> 50
# Cost: (30-10) + (10-10) + (50-10) = 20 + 0 + 40 = 60
# Optimal path: 30 -> 60 -> 60 -> 50
# Cost: (60-30) + (60-60) + (50-60) = 30 + 0 + 10 = 40

"""
STEPS TO SOLVE:
1. Express the problem in terms of an idxex.
2. Solve recursively using the idxex.
3. Return the minimum cost among possible jumps.
"""


# RECURSIVE SOLUTION
def recursive(height):
    def helper(idx):
        if idx == 0:
            return 0  # No cost to reach the first position.

        jumpOne = helper(idx - 1) + abs(height[idx] - height[idx - 1])
        jumpTwo = float("inf")  # Initialize with infinity to handle idx = 1 case.
        if idx > 1:
            jumpTwo = helper(idx - 2) + abs(height[idx] - height[idx - 2])

        return min(jumpOne, jumpTwo)

    return helper(len(height) - 1)  # Start recursion from the last index


# height = [30, 10, 60, 10, 60, 50]
# print(recursive(height))


# ============= MEMOIZATION =============
# There is overlapping subproblems in recursion tree -> USE MEMOIZATION
"""
RECURSION --> MEMOIZATION (TOP DOWN)
1. Declare DP array
2. Instead of return store value in DP array
3. Before calling recursion, check if already computed
"""

# TC = O(N), SC = O(N)
def memoization(idx, height, dp):
    if idx == 0:
        return 0
    """STEP 3"""
    if dp[idx] != -1:
        return dp[idx]
    jumpTwo = float("inf")
    jumpOne = memoization(idx - 1, height, dp) + abs(height[idx] - height[idx - 1])
    if idx > 1:
        jumpTwo = memoization(idx - 2, height, dp) + abs(height[idx] - height[idx - 2])
    """STEP 2"""
    dp[idx] = min(jumpOne, jumpTwo)
    return dp[idx]

# test
height = [30, 10, 60, 10, 60, 50]
n = len(height)
"""STEP 1"""
dp = [-1] * n
print(memoization(n - 1, height, dp))


# ============= TABULATION TO AVOID RECURSION =============
"""
TABULATION (BOTTOM UP)
1. See in memoization how much DP array we used, init it
2. Base case
3. For loop instead of recursion
"""

# TC = O(N), SC = O(N)
def tabulation(height):
    n = len(height)

    """STEP 1 - Init"""
    dp = [-1 for _ in range(n)]

    """STEP 2 - Base Case"""
    dp[0] = 0

    """STEP 3"""
    for ind in range(1, n):
        jumpTwo = float("inf")
        jumpOne = dp[ind - 1] + abs(height[ind] - height[ind - 1])
        if ind > 1:
            jumpTwo = dp[ind - 2] + abs(height[ind] - height[ind - 2])
        dp[ind] = min(jumpOne, jumpTwo)
    return dp[n - 1]

# test
height = [30, 10, 60, 10, 60, 50]
print(tabulation(height))


# ============= SPACE OPTIMIZED =============
"""
- We are just using "prev two value" (in this case) to predict next one
- So, don't need to store whole DP array
"""

# TC = O(N), SC = O(1)
def optimal(height):
    n = len(height)
    prev = 0
    prev2 = 0
    for i in range(1, n):
        jumpTwo = float("inf")
        jumpOne = prev + abs(height[i] - height[i - 1])
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])

        cur_i = min(jumpOne, jumpTwo)
        prev2 = prev
        prev = cur_i

    return prev

# test
height = [30, 10, 60, 10, 60, 50]
print(optimal(height))