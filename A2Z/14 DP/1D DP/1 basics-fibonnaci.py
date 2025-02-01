# memoization -> tabulation -> space optimization


def recursiveFib(n):
    if n <= 1:
        return 1
    return recursiveFib(n - 1) + recursiveFib(n - 2)


def memoizationFib(n, dp):
    if n <= 1:
        return n

    if dp[n] != -1:
        return dp[n]
    dp[n] = memoizationFib(n - 1, dp) + memoizationFib(n - 2, dp)
    return dp[n]


# print("Memoization: TC = N, SC = N")
# n = 5
# dp = [-1] * (n+1)
# print(memoizationFib(n, dp))


def tabulationFib(n):

    if n <= 1:
        return n

    dp = [-1] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print("Tabulation: TC = N, SC = N")
print(tabulationFib(8))


def spaceOptimizedFib(n):
    prev2 = 0
    prev = 1

    for _ in range(2, n + 1):
        cur_i = prev2 + prev
        prev2 = prev
        prev = cur_i

    return prev


print("Space Optimized: TC = N, SC = 1")
print(spaceOptimizedFib(8))
