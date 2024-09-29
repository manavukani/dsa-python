# Rearrange Array Elements by Sign =====> THERE ARE 2 TYPES

# ==================== TYPE 1 - EQUAL # POSTITIVE & NEGATIVE ====================
# Input:  nums[] = {1,2,-4,-5}, N = 4
# Output: 1 -4 2 -5

# There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
# Without altering the relative order of positive and negative elements,
# you must return an array of alternately positive and negative values.

'''
Time Complexity: O(N+N/2) 
O(N) for traversing the array once for segregating
O(N/2) for adding those elements alternatively to the array

Space Complexity:  O(N/2 + N/2) = O(N)
'''


def brute(nums):
    pos = []
    neg = []
    for ele in nums:
        if ele >= 0:
            pos.append(ele)
        elif ele < 0:
            neg.append(ele)
    # equal number of positive and negative elements
    i = 0
    nums.clear()
    while i < len(pos):
        nums.append(pos[i])
        nums.append(neg[i])
        i += 1
    return nums

# Time - O(N)
# Space - O(N)


def optimal(nums):
    ans = [0] * len(nums)
    # since we need to insert first +ve @ 0 and first -ve @ 1
    posIndex = 0
    negIndex = 1
    for i in range(len(nums)):
        if nums[i] >= 0:
            ans[posIndex] = nums[i]
            posIndex += 2
        else:
            ans[negIndex] = nums[i]
            negIndex += 2
    return ans


# ===> BOTH ARE 'N' ORDER
print(optimal([1, 2, -4, -5]))

# ==================== TYPE 2 - UNEQUAL # POSTITIVE & NEGATIVE ====================
# Input:  arr[] = {1,2,-4,-5,3,4}
# Output: 1 -4 2 -5 3 4


def solve(nums):
    pos = []
    neg = []
    for ele in nums:
        if ele >= 0:
            pos.append(ele)
        elif ele < 0:
            neg.append(ele)
    # unequal number of positive and negative elements
    i = 0
    j = 0
    nums.clear()
    while i < len(pos) and j < len(neg):
        nums.append(pos[i])
        nums.append(neg[j])
        i += 1
        j += 1

    while i < len(pos):
        nums.append(pos[i])
        i += 1

    while j < len(neg):
        nums.append(neg[j])
        j += 1
        
    return nums

print(solve([1,2,-4,-5,3,4]))
