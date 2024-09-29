# Given an array of integers and an integer k,
# return the total number of subarrays whose sum equals k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Input : {3, 1, 2, 4}, k = 6
# Output: 2


# generate all and check how many gives k

# O(n^3)
'''
def n_cube(nums, k):
    cnt = 0
    for....
        for....
            sum = 0
            for (to find sum)....
            if sum == k:
                cnt += 1
'''

# O(n^2)


def brute(nums, k):
    cnt = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]

            if sum == k:
                cnt += 1
    return cnt


# USING PREFIX SUM
def optimal(nums, k):
    from collections import defaultdict
    n = len(nums)
    mpp = defaultdict(int)
    preSum = 0
    cnt = 0

    mpp[0] = 1  # Setting 0 in the map.
    for i in range(n):
        # add current element to prefix Sum:
        preSum += nums[i]

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        cnt += mpp[remove]

        # Update the count of prefix sum
        # in the map.
        mpp[preSum] += 1

    return cnt


print(brute([1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3))
