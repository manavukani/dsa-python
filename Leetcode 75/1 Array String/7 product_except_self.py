def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # arr = [1,2,3,4]
    # prefix product = [1,1,2,6]
    # suffix product = [24,12,4,1]

    prefix = []
    pre = 1
    for i in range(len(nums)):
        prefix.append(pre)
        pre *= nums[i]
    
    suff = 1
    for j in range(len(nums)-1,-1,-1):
        prefix[j] *= suff
        suff *= nums[j]

    return prefix

# same but cleaner
def productExceptSelf(nums):
    res = [1] * (len(nums))

    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix  # prefix * postfix
        postfix *= nums[i]
    return res