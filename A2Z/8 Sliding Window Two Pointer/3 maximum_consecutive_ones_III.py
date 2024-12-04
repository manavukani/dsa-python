# allowed to flip at most k zeroes
# INPUT - [1,1,1,0,0,0,1,1,1,1,0], k = 2
# OUTPUT - len of max consecutive ones

'''
similar to finding the longest subarray with atmost k zeroes
'''

# brute - O(N^2)
def brute(arr, k):
    maxLen = 0
    for i in range(len(arr)):
        numZero = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                numZero += 1
            if numZero > k:
                break
            maxLen = max(maxLen, j - i + 1)
    return maxLen

# sliding window - O(2N)
def solve(arr, k):
    l, r = 0, 0
    numZero = 0
    maxLen = 0
    while r < len(arr):
        if arr[r] == 0:
            numZero += 1
        while numZero > k:
            if arr[l] == 0:
                numZero -= 1
            l += 1  # Move the left pointer regardless of the element
        maxLen = max(maxLen, r - l + 1)
        r += 1
    return maxLen

# optimal - O(N)
# only update maxLen when numZero goes <= k
def optimal(arr, k):
    l, r = 0, 0
    numZero = 0
    maxLen = 0
    while r < len(arr):
        if arr[r] == 0:
            numZero += 1
        # no point in removing all arr[l]
        # we maintain the maxLen since there is no point in decreasing it
        # as we just need to find the maxLen
        if numZero > k:
            if arr[l] == 0:
                numZero -= 1
            l += 1
        if numZero <= k:
            maxLen = max(maxLen, r - l + 1)
        r += 1
    return maxLen