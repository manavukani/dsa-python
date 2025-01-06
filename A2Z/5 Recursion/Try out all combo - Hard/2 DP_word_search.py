# input - string s, dictionary of words
# output - return True if s can be segmented into a space-separated sequence of one or more dictionary words


class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        def solve(index):
            if index == len(s):
                return True

            for i in range(index + 1, len(s) + 1):
                if s[index:i] in wordSet:
                    if solve(i):  # Recur for the remaining string
                        return True

            return False

        return solve(0)


""" ABOVE SOLUTION GIVES TLE FOR LARGE INPUTS """


# ----- Dynamic Programming -----
# dp[i] = True -- substring s[0:i] can be segmented --- segmentable till i
# we go till len(s) + 1 because we have dp[0] as base case, so string segmentation is possible till len(s)


def wordBreak_withDP(s, wordDict):
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    # Base case
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            # If dp[j] is True and the substring s[j:i] is in the dictionary
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    # Return if the entire string can be segmented
    return dp[len(s)]


# test cases
print(wordBreak_withDP("leetcode", ["leet", "code"]))  # True
print(wordBreak_withDP("applepenapple", ["apple", "pen"]))  # True
