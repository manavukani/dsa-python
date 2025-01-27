"""

eg: 3 = 0 1 1

to check if last digit is 0/1 ---> 3 % 2 = 1 so its 1
for check other remamining, we divide by 3 (same as right shifting by 1) ---> remanining = 01 again % 2 = 1

to eliminate repetative work, we can use DP

0 - 0 0 0 0 ----> 0
1 - 0 0 0 1 ----> 1 -----> here as well, 1 + dp[n-1] = 1 + dp[0] = 1
2 - 0 0 1 0 ----> 1 -----> 1 + dp[n-2] = 1 + dp[0] = 1
3 - 0 0 1 1 ----> 2
4 - 0 1 0 0 ----> 1 + dp[n-4] = 1 + dp[0] = 1 + 0 = 0
5 - 0 1 0 1 ----> 1 + dp[n-4] = 1 + dp[1] = 1 + 1 = 2
6 - 0 1 1 0 ----> 1 + dp[n-4] = 1 + dp[2] = 1 + 1 = 2
7 - 0 1 1 1 ----> 1 + dp[n-4] = 1 + dp[3] = 1 + 2 = 3
8 - 1 0 0 0 ----> 1 + dp[n-8] = 1

offset = most significant bit

"""


# TC = O(n)
def solve(n):
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]

    return dp
