class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A, B):
        m = len(A)
        n = len(B)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1],
                                       min(dp[i - 1][j], 
                                           dp[i][j - 1]))

        return dp[m][n]


sol = Solution()

print(sol.minDistance(A="Anshuman", B="Antihuman"))  # 2

# Operation 1: Replace s with t.
# Operation 2: Insert i.


# ------------- SPACE OPTIMIZED ------------------

def editDistance(S1, S2):
    m = len(S1)
    n = len(S2)

    # Initialize two lists, prev and cur, to store the previous and current rows of the DP array
    prev = [j for j in range(n + 1)]
    cur = [0 for _ in range(n + 1)]

    # Loop through the characters of S1 and S2
    for i in range(1, m + 1):
        cur[0] = i  # Initialize the first element of the current row

        for j in range(1, n + 1):
            # If the characters at the current positions match, no operation is needed
            if S1[i - 1] == S2[j - 1]:
                cur[j] = prev[j - 1]
            else:
                # Calculate the minimum of three choices:
                # 1. Replace the current character (diagonal move)
                # 2. Insert a character into S1 (move up)
                # 3. Delete a character from S1 (move left)
                cur[j] = 1 + min(prev[j - 1], min(prev[j], cur[j - 1]))

        prev, cur = cur, prev  # Update prev to be the current row, and cur to be the new empty row

    # The final value in prev[m] is the minimum number of operations required
    return prev[n]

def main():
    s1 = "horse"
    s2 = "ros"

    # Calculate and print the minimum number of operations required
    print("The minimum number of operations required is:", editDistance(s1, s2))

if __name__ == "__main__":
    main()


