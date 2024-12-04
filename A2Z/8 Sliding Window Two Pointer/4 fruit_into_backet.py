# idx = tree
# arr[i] = type of fruit

# we have 2 container, each can only used for same kind of fruit
# once we start picking up, we cant skip - must be subarray

# INPUT - [3,3,3,1,2,1,1,2,3,3,4]
#                ---------
# OUTPUT - max fruits you can pick - 5

# TODO: finding MAX LENGTH SUBARRAY w/ at-most 2 types of #

# brute - O(N^2)
# st.add --> O(log N) but here N = sizeof set = at max 3 = const
def brute(arr):
    maxLen = 0
    for i in range(len(arr)):
        st = set()
        for j in range(i, len(arr)):
            st.add(arr[j])
            if len(st) <= 2:
                maxLen = max(maxLen, j-i+1)
            else:
                break
    return maxLen


# two pointer - O(2N)
def solve(arr):
    k = 2
    l, r = 0, 0
    maxLen = 0
    mpp = {}
    while r < len(arr):
        # Expand the window to the right
        mpp[arr[r]] = 1 + mpp.get(arr[r], 0)
        if len(mpp) > k:
            # Shrink the window from the left if the condition is violated
            while len(mpp) > k:
                mpp[arr[l]] -= 1
                if mpp[arr[l]] == 0:
                    del mpp[arr[l]]
                l += 1
        # Update max length
        if len(mpp) <= k:
            maxLen = max(maxLen, r-l+1)
        r += 1
    return maxLen

# optimal - O(N)
# SC = O(1)
def optimal(arr):
    k = 2
    l, r = 0, 0
    maxLen = 0
    mpp = {}
    while r < len(arr):
        # Expand the window to the right
        mpp[arr[r]] = 1 + mpp.get(arr[r], 0)
        if len(mpp) > k:
            # Shrink the window only ONCE
            # from the left if the condition is violated
            if len(mpp) > k:
                mpp[arr[l]] -= 1
                if mpp[arr[l]] == 0:
                    del mpp[arr[l]]
                l += 1
        # Update max length
        if len(mpp) <= k:
            maxLen = max(maxLen, r-l+1)
        r += 1
    return maxLen