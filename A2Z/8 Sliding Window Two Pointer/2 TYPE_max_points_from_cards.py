# INPUT -
# arr = [6,2,3,4,7,2,1,7,1] (points of avalable cards)
# k = 4 (cards you can pick)
# CONDITION: can pick up from front or from back not middle -> can pick in rotating array manner
# OUTPUT - Max points you can get

'''
[6,2,3,4,7,2,1,7,1]
 -------
[6,2,3,4,7,2,1,7,1]
 -----           --
[6,2,3,4,7,2,1,7,1]
 ---           ----
[6,2,3,4,7,2,1,7,1]
 --          ------
[6,2,3,4,7,2,1,7,1]
           --------

Full window at left and then left rotate

'''

# TC = O(k) + O(k) = O(2k)


def solve(arr, k):
    lsum = 0
    rsum = 0
    maxSum = 0
    # first k on left
    for i in range(k):
        lsum += arr[i]
    maxSum = lsum
    # remove from left, add from right
    rightIdx = len(arr)-1
    for i in range(k-1, -1, -1):
        lsum -= arr[i]
        rsum += arr[rightIdx]
        rightIdx -= 1
        maxSum = max(maxSum, lsum+rsum)
    return maxSum


print(solve([6, 2, 3, 4, 7, 2, 1, 7, 1], 4))
