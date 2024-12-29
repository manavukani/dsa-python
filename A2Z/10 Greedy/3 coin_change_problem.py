# ip = coins of size n, sum,
# infinite supply of each coin
# op = minimum number of coins required to make the sum, -1 if not possible


def coin_change(coins, sum):
    n = len(coins)
    ans = []
    for i in range(n - 1, -1, -1):
        while sum >= coins[i]:
            sum -= coins[i]
            ans.append(coins[i])
    return ans


coins = [1, 2, 5]
sum = 11
print(coin_change(coins, sum))  # works

# when coins are not in the proper order - 6 + 5 > 9 (summation of previous coins > next coin)
coins = [1, 5, 6, 9]
sum = 11
# should be 6, 5, not 9, 1, 1 ----> fails
print(coin_change(coins, sum))


# dynamic programming
def coin_change_dp(coins, sum):
    n = len(coins)
    dp = [float("inf")] * (sum + 1)
    dp[0] = 0
    for i in range(1, sum + 1):
        for j in range(n):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return dp[sum] if dp[sum] != float("inf") else -1


coins = [1, 5, 6, 9]
sum = 11
print(coin_change_dp(coins, sum))  # 2 -- works
