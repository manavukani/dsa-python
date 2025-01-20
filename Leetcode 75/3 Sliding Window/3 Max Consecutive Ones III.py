def longestOnes(nums, k):
    numZero = 0
    L,R = 0, 0
    maxLen = 0
    while R < len(nums):
        # expand
        if nums[R] == 1:
            R+=1
        # numZero within limit, expand
        elif numZero < k and nums[R] == 0:
            numZero += 1
            R+=1
        # reached limit, shrink
        elif numZero == k and nums[R] == 0:
            maxLen = max(maxLen, R-L)
            while nums[L] != 0:
                L+=1
            L+=1
            numZero -= 1
    
    # IMP - after loop, may have valid window that wasn't checked
    maxLen = max(maxLen, R-L)

    return maxLen

# simplified, same logic
def longestOnes(nums, k):
    numZero = 0
    L = 0
    maxLen = 0

    for R in range(len(nums)):
        if nums[R] == 0:
            numZero += 1
        
        # exceed k, shrink window
        while numZero > k:
            # track of numZero
            if nums[L] == 0:
                numZero -= 1
            # shrink
            L += 1

        maxLen = max(maxLen, R - L + 1)

    return maxLen

