# no. of subarray with k different int

# 1 2 1 3 4 -> [1,2,1], [1,3,4], [2,1,3]


# brute - generate all subarray - O(N^2)
def brute(arr, k):
    cnt = 0
    for i in range(len(arr)):
        mpp = {}
        for j in range(i, len(arr)):
            mpp[arr[j]] = 1 + mpp.get(arr[j], 0)
            if len(mpp) == k:
                cnt += 1
            if len(mpp) > k:
                break
    return cnt


# 2 1 1 1 3 4 3 2, k = 3
#   l       r>r
# moving normally will lead to losing of some subarray
# we lose 1 1 3 4, 1 3 4

# TODO - find the no of subarray where distinct elements <= k

"""
becomes similar to question 6

2 1 1 1 3 4 3 2
l   r

- since we are counting subarray where distinct elements <= k
- if 2 1 1 is valid all of the subarrays are valid -> 1, 1 1, 2 1 1
- so we add 3 to conut
- similarly, if 2 1 1 1 3 is valid we add - 5
- we are adding r-l+1
"""

# since we are calling 2 times...
# TC = 2 * O(2N)
# SC = 2 * O(N)
def solve(arr, k):

    def helper(arr, k):
        l, r = 0, 0
        cnt = 0
        mpp = {}
        while r < len(arr):
            mpp[arr[r]] = 1 + mpp.get(arr[r], 0)
            while len(mpp) > k:
                mpp[arr[l]] -= 1
                if mpp[arr[l]] == 0:
                    del mpp[arr[l]]
                l += 1
            cnt += r - l + 1
            r += 1
        return cnt

    return helper(arr, k) - helper(arr, k - 1)

# Calculate the number of subarrays with at most k distinct elements
# Subtract the number of subarrays with at most k-1 distinct elements
# This gives the number of subarrays with exactly k distinct elements



nums = [1,2,1,2,3]
k = 2
print(solve(nums, k))
