# INPUT - s = aaabbccd, k = 2
# OUTPUT - max len of k distinct char

from collections import defaultdict

# brute - O(N^2)
# SC = O(26) or O(256) depending upon the chars


def brute(s, k):
    maxLen = 0
    mpp = defaultdict(int)
    for i in range(len(s)):
        for j in range(i, len(s)):
            mpp[s[j]] += 1
            if len(mpp) <= k:
                maxLen = max(maxLen, j-i+1)
            else:
                break
    return maxLen

# 2 pointer
# TC = O(N) + O(N) + O(log 256) {for hash map} = O(2N)
# SC = O(256)


def solve(s, k):
    maxLen = 0
    l, r = 0, 0
    mpp = defaultdict(int)
    # r traverse -> N
    # l at most traverse N-1
    while r < len(s):
        mpp[s[r]] += 1
        while len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                del mpp[s[l]]
            l += 1
        if len(mpp) <= k:
            maxLen = max(maxLen, r-l+1)
        r += 1
    return maxLen


# optimal - O(N)
def optimal(s, k):
    maxLen = 0
    l, r = 0, 0
    mpp = defaultdict(int)
    while r < len(s):
        mpp[s[r]] += 1
        if len(mpp) > k:
            mpp[s[l]] -= 1
            if mpp[s[l]] == 0:
                del mpp[s[l]]
            l += 1
        if len(mpp) <= k:
            maxLen = max(maxLen, r-l+1)
        r += 1
    return maxLen


s = "eceba"
k = 2
result = solve(s, k)
print(result)  # Output: 3
