# O(N^2)
def brute(arr, k):
    maxLen = 0
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum <= k:
                maxLen = max(maxLen, j-i+1)
            elif sum > k:
                break
    return maxLen

# O(2N) -> N for each - traversing with R and shrinking


def sliding_window(arr, k):
    l, r = 0, 0
    sum = 0
    maxLen = 0
    while r < len(arr):
        sum = sum + arr[r]
        while sum > k:
            sum = sum - arr[l]
            l += 1
        if sum <= k:
            maxLen = max(maxLen, r-l+1)
            # if print subarray -> store L and R here
        r += 1
    return maxLen

# don't shrink below maxLen, coz it wont be answer anyway
# if we need to find subarray, can't use this. ONLY for LENGTH ---------> IMP
# O(N)
def optimal(arr, k):
    l, r = 0, 0
    sum = 0
    maxLen = 0
    while r < len(arr):
        sum = sum + arr[r]
        # just once
        # no point in removing all arr[l]
        # we maintain the maxLen since there is no point in decreasing it
        # as we just need to find the maxLen
        if sum > k:
            sum = sum - arr[l]
            l += 1
        if sum <= k:
            maxLen = max(maxLen, r-l+1)
            # if print subarray -> store L and R here
        r += 1
    return maxLen