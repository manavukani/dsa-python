# return the minimum number of jumps to reach end
# NO need to check if reach end, input will take care


# RECURSION - try out all ways and return minimum of those
# TC = O(N^N), SC = O(N)
def brute(arr):
    n = len(arr)

    def helper(idx, jumps):
        # Base case: If we reach or cross the last index
        if idx >= n - 1:
            return jumps

        mini = float("inf")

        # try all possible jumps from the current position
        for i in range(1, arr[idx] + 1):
            mini = min(mini, helper(idx + i, jumps + 1))

        return mini

    return helper(0, 0)


# By using Dynammic Progg, can make it TC = O(N^2) and SC = O(N)
def jump_DP(nums):
    """
    nums = [2,   3,   0,   1,   4]
    dp =   [inf, inf, inf, inf, 0]
    """

    if nums[0] == 0 or len(nums) == 1:
        return 0
    if nums[0] >= len(nums) - 1:
        return 1

    dp = [float("inf")] * (len(nums) - 1) + [0]

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] == 0:
            continue

        if i + nums[i] >= len(nums) - 1:
            dp[i] = 1
        else:
            dp[i] = 1 + min(dp[i + 1 : i + nums[i] + 1])

    return dp[0]


# ========= GREEDY =========
"""
- At each jump, obtain the window that can be reached from the previous window.
- Start of following window will always be the next element of the previous window's right-end.
- The first window is the first element only. e.g. '1' is the furthest element that can be jumped to from the first element.

Eg:
    nums = [2, 3, 1, 1, 4]
            lr
1st jump:      l  r
2nd jump:            l  r

---> TC: O(N)  |   SC: O(1)
"""


def minJumps(arr):
    jumps = 0
    left = right = 0

    # last element is covered in range, loop ends
    while right < len(arr) - 1:

        farthest = 0

        # which index is farthest one that can be reached
        # from the current range -> [left, right]
        for i in range(left, right + 1):
            farthest = max(farthest, i + arr[i])

        left = right + 1
        right = farthest

        jumps += 1

    return jumps


arr = [2, 3, 1, 1, 4]
print(minJumps(arr))  # Output: 2
