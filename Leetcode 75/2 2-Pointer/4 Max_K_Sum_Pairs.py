# TC = O( N log N )
# with sorting
def twoPointer(nums, k):
    """
    params: nums = array, k = target
    result: # pairs with sum k
    """
    nums.sort()
    L, R = 0, len(nums) - 1
    ans = 0

    while L < R:
        if ((nums[L] + nums[R]) == k):
            ans += 1
            L +=1 
            R -=1
        elif((nums[L] + nums[R]) < k):
            L += 1
        else:
            R -= 1
    return ans

# TC = O(N)
def optimal(nums, k):
    d = {}
    count = 0

    for x in nums:
        if d.get(k - x, 0) > 0:
            count+=1
            d[k-x]-=1
        else:
            d[x] = d.get(x, 0) + 1

    return count