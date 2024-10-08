# memoizaiton
class Memoization:
    def lcsUtil(s1, s2, ind1, ind2, dp):
        # Base case: If either of the strings has reached the end
        if ind1 < 0 or ind2 < 0:
            return 0

        # If the result for this state is already calculated, return it
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        # If the characters at the current indices match, include them in the LCS
        if s1[ind1] == s2[ind2]:
            dp[ind1][ind2] = 1 + lcsUtil(s1, s2, ind1 - 1, ind2 - 1, dp)
        else:
            # If the characters do not match, consider both possibilities:
            # 1. Exclude character from s1 and continue matching in s2
            # 2. Exclude character from s2 and continue matching in s1
            dp[ind1][ind2] = max(lcsUtil(s1, s2, ind1, ind2 - 1, dp), lcsUtil(s1, s2, ind1 - 1, ind2, dp))

        return dp[ind1][ind2]

    def lcs(s1, s2):
        n = len(s1)
        m = len(s2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        return lcsUtil(s1, s2, n - 1, m - 1, dp)

# tabulation
def TABULATION(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Create a DP table of size (n+1) x (m+1) initialized with -1
    dp = [[-1 for j in range(m + 1)] for i in range(n + 1)]

    # Initialize the base cases:
    # - The length of LCS with an empty string is 0, so dp[i][0] = 0 for all i
    # - The length of LCS with an empty string is 0, so dp[0][j] = 0 for all j
    for i in range(n + 1):
        dp[i][0] = 0
    for j in range(m + 1):
        dp[0][j] = 0

    # Fill in the DP table by considering characters from both strings
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                # If the characters match, increment the LCS length
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                # If the characters do not match, take the maximum of
                # LCS length without one character from s1 or s2
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
    
    # The value in dp[n][m] represents the length of the Longest Common Subsequence
    return dp[n][m]

# OPTIMIZED
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize two arrays, 'prev' and 'cur', to store the DP values
    prev = [0] * (m + 1)
    cur = [0] * (m + 1)

    # Loop through the characters of both strings to compute LCS
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                # If the characters match, increment LCS length by 1
                cur[ind2] = 1 + prev[ind2 - 1]
            else:
                # If the characters do not match, take the maximum of LCS
                # by excluding one character from s1 or s2
                cur[ind2] = max(prev[ind2], cur[ind2 - 1])
        
        # Update 'prev' to be the same as 'cur' for the next iteration
        prev = cur[:]

    # The value in 'prev[m]' represents the length of the Longest Common Subsequence
    return prev[m]

def main():
    s1 = "acd"
    s2 = "ced"

    print("The Length of Longest Common Subsequence is", lcs(s1, s2))

if __name__ == '__main__':
    main()

