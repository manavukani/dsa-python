# INPUT: s = AABABBA, k = 2
# OUTPUT: 4 ---> longest substring with all characters same
# s = string
# k = number of replacements allowed

# TODO - convert k characters and find the longest substring

# no of conversions = length - max_freq <= k

from collections import defaultdict

# O(N^2)


def brute(s, k):
    maxLen = 0
    n = len(s)
    for i in range(n):
        maxf = 0
        mpp = defaultdict(int)
        for j in range(i, n):
            mpp[s[j]] += 1
            maxf = max(maxf, mpp[s[j]])
            changes = j - i + 1 - maxf
            if changes <= k:
                maxLen = max(maxLen, j - i + 1)
            else:
                break
    return maxLen


# TC = O(2N*26) ---> 2N for 2 'while' loops, 26 for 'for' loop
# SC = max O(26)
def solve(s, k):
    l, r = 0, 0
    maxf = 0
    maxLen = 0
    n = len(s)
    mpp = defaultdict(int)
    while r < n:
        mpp[s[r]] += 1
        maxf = max(maxf, mpp[s[r]])
        # len - maxf = changes <= k
        while (r - l + 1) - maxf > k:
            mpp[s[l]] -= 1
            maxf = 0
            for val in mpp.values():
                maxf = max(maxf, val)
            l += 1

        if r - l + 1 - maxf <= k:
            maxLen = max(maxLen, r - l + 1)

        r += 1
    return maxLen


# print(solve('AABABBA', 2))


# TC = O(N)
# SC = max O(26)
def optimal(s, k):
    l, r = 0, 0
    maxf = 0
    maxLen = 0
    n = len(s)
    mpp = defaultdict(int)
    while r < n:
        mpp[s[r]] += 1
        maxf = max(maxf, mpp[s[r]])
        # ONLY CHNAGE -> while to if ----> just remove 1 ele
        if (r - l + 1) - maxf > k:
            mpp[s[l]] -= 1
            maxf = 0
            for val in mpp.values():
                maxf = max(maxf, val)
            l += 1

        if r - l + 1 - maxf <= k:
            maxLen = max(maxLen, r - l + 1)

        r += 1
    return maxLen

def optimal2(s, k):
    mpp = defaultdict(int)
    L = 0
    max_freq = 0
    # O(n)
    for R in range(len(s)):
        # add count of new ele
        mpp[s[R]] += 1

        max_freq = max(max_freq, mpp[s[R]])

        # CASE 1
        # if windowSize - mostFrequent <= k its doable to replace rest of char
        # so we increment R pointer (make window bigger)

        # CASE 2
        # if not we shrink the window (increment L pointer)
        if (R - L + 1) - max_freq > k:
            # rwmove the left most ele from window
            mpp[s[L]] -= 1
            L += 1

        # else case 1 is done auomatically -> increment R

    return R - L + 1
