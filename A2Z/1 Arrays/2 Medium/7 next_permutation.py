# Given an array Arr[] of integers, rearrange the numbers of the given array into the
# lexicographically next greater permutation of numbers

# INPUT => {1,3,2}
# Output => {2,1,3}
# All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}.
# So, the next permutation just after {1,3,2} is {2,1,3}.


# INPUT => {3,2,1}
# OUTPUT => {1,2,3}
# As we see all permutations of {1,2,3}, we find {3,2,1} at the last position.
# So, we have to return the topmost permutation.


def brute(nums):
    # find all -> recursion
    # linear search for i/p
    # return next -> o/p

    # very time consuming -> O (n! * n)
    # just explain no need to implement
    pass


def optimal(nums):
    brkPntInd = -1
    n = len(nums)
    # finding breaking point index
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            brkPntInd = i
            print(f"Breaking point index: {i}")
            break
    
    # if sorted descending
    if brkPntInd == -1:
        nums = nums.reverse()
        return nums

    # from back find any element smaller than breaking point ele, right part is sorted
    for i in range(n-1, brkPntInd, -1):
        if nums[i] > nums[brkPntInd]:
            nums[i], nums[brkPntInd] = nums[brkPntInd], nums[i]
            break

    # reverse the remaining at end after the breaking point
    nums[brkPntInd + 1:] = reversed(nums[brkPntInd + 1:])

    return nums

