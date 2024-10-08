
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    # Initialize a 2D array to store the length of the LCS
    dp = [[-1] * (m + 1) for i in range(n + 1)]

    # Initialize the first row and first column with 0
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # Fill in the dp array using dynamic programming
    for ind1 in range(1, n + 1):
        for ind2 in range(1, m + 1):
            if s1[ind1 - 1] == s2[ind2 - 1]:
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

    # The final value in dp will be the length of the LCS
    return dp[n][m]

def longestPalindromeSubsequence(s):
    # Reverse the input string
    # t = s
    rev_s = s[::-1]

    # Find the longest common subsequence between s and its reverse
    return lcs(s, rev_s)

def main():
    s = "bbabcbcab"

    # Calculate and print the length of the longest palindromic subsequence
    print("The Length of Longest Palindromic Subsequence is", longestPalindromeSubsequence(s))

if __name__ == "__main__":
    main()

