# try all possible combinations --> return max ---> DP

# ================ RECURSIVE ================
# 1. Express as indexes
# 2. Do stuff --- 2 choices:  Pick / Not pick
#       - if pick current, cannot pick next, need to pick idx-2
#       - if not pick current, have to pick next (idx-1)
# 3. Return best --- max for this case


def solve(nums):
    def helper(idx):
        if idx < 0:
            return 0

        # pick
        pick = nums[idx] + helper(idx - 2)
        # not pick
        notPick = 0 + helper(idx - 1)

        return max(pick, notPick)

    return helper(len(nums) - 1)


# ================ MEMOIZATION --- TOP DOWN ================
# 1. Init DP
# 2. Do not repeat calculation
# 3. Store in DP, not return


# TC = O(N), SC = O(N)
def memoization(nums):
    n = len(nums)
    dp = [-1] * n

    def helper(idx):
        # no houses left
        if idx < 0:
            return 0

        # if pre-computed, return3
        if dp[idx] != -1:
            return dp[idx]

        # 2 conditions
        pick = nums[idx] + helper(idx - 2)
        notPick = 0 + helper(idx - 1)

        dp[idx] = max(pick, notPick)

        return dp[idx]

    return helper(n - 1)


arr = [2, 1, 4, 9]
print(memoization(arr))


# ================ TABULATION --- BOTTOM UP ================
# TC = O(N), SC = O(N)
def tabulation(nums):
    n = len(nums)
    dp = [-1] * n

    # base cases for further calculation
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):
        pick = nums[i] + dp[i - 2]
        notPick = dp[i - 1]
        dp[i] = max(pick, notPick)

    return dp[-1]  # last ele


# ================ SPACE OPTIMIZED ================
# - just need (i-1) and (i-2), no need of whole DP array

# TC = O(N), SC = O(1)
def optimal(nums):
    prev2 = 0
    prev = 0

    if not nums:
        return 0

    # [prev2, prev, n, n+1, n+2 ....]
    for n in nums:
        # pick -> prev2 + n
        # notPick -> prev
        tmp = max(prev2 + n, prev)
        prev2 = prev
        prev = tmp

    return prev
