def solve(A):
    dp = [0, 0, 0]
    for i in range(len(A)):
        cost_0 = A[i][0] + min(dp[1], dp[2])
        cost_1 = A[i][1] + min(dp[0], dp[2])
        cost_2 = A[i][2] + min(dp[0], dp[1])
        dp = [cost_0, cost_1, cost_2]
    return min(dp)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
print(solve(costs)) # 10
