# follow up to Frog Jump problem
# what if we frog can jump K steps

"""
If we are at idx = i, we can go to -> i+1, i+2, ...., i+k
"""


# ============== RECURSIVE ==============
def recursive(height, k):
    def helper(idx):
        if idx == 0:
            return 0  # No cost to reach the first position.

        minSteps = float("inf")

        # go thorugh all k jumps
        for j in range(1, k + 1):
            if idx - j >= 0:
                jump = helper(idx - j) + abs(height[idx] - height[idx - j])
                minSteps = min(jump, minSteps)
        return minSteps

    return helper(len(height) - 1)  # Start recursion from the last index


# ============== MEMOIZATION ==============
# TC = O(N*K), SC = O(N)
def memoization(height, k):
    n = len(height)
    # initialize DP array
    dp = [-1] * n

    def util(ind):
        # base case
        if ind == 0:
            return 0
        # If pre-calculated, directly return
        if dp[ind] != -1:
            return dp[ind]

        minSteps = float("inf")

        # try all possible jumps from 1 -> k
        for j in range(1, k + 1):
            # Ensure that we do not jump beyond 0th idx (-ve)
            if ind - j >= 0:
                jump = util(ind - j) + abs(height[ind] - height[ind - j])
                minSteps = min(jump, minSteps)

        # Store the minimum cost
        dp[ind] = minSteps
        return dp[ind]

    # start from last index ----- TOP DOWN
    return util(n - 1)


height = [30, 10, 60, 10, 60, 50]
k = 2
print(memoization(height, k))


# ============== TABULATION ---- BOTTOM UP ==============
# TC = O(N*K), SC = O(N)
def tabulation(height, k):
    n = len(height)

    # initialize DP array
    dp = [-1] * n

    # Base case
    dp[0] = 0

    # for all elements of array
    for i in range(1, n):
        minSteps = float("inf")
        # try all possible jumps from 1 -> k
        for j in range(1, k + 1):
            # Ensure that we do not jump beyond 0th idx (-ve)
            if i - j >= 0:
                jump = dp[i - j] + abs(height[i] - height[i - j])
                minSteps = min(jump, minSteps)

        # Store the minimum cost for each idx
        dp[i] = minSteps

    return dp[n - 1]  # min steps to reach end


height = [30, 10, 60, 10, 60, 50]
k = 2
print(tabulation(height, k))


# WE CANNOT HAVE A SPACE OPTIMIZED ALGO SINCE WE NEED K VALUES, IF N=K (worst case) --> SC = O(N)
