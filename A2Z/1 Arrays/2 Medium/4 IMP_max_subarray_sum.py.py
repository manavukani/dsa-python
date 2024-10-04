# Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# [-2,1,-3,4,-1,2,1,-5,4]  => 6
# [4,-1,2,1] has the largest sum = 6.

# O(N^3)
def shit_sol(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            # subarray = arr[i.....j]
            summ = 0
            # add all the elements of subarray:
            for k in range(i, j+1):
                summ += arr[k]
            maxi = max(maxi, summ)
    return maxi


# O(N^2)
def brute(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            maxi = max(maxi, sum)
    return maxi

# ============================================
# ============ Kadane's Algorithm ============
# ============================================
# keep track of sum and make it zero if sum goes negative, reinit sum from next index
# O(N)


def optimal(arr):
    maxi = float('-inf')
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi

# FOLLOW_UP => print the subarray with maxi sum ====> REVISIT THIS


def print_maxi(arr):
    maxi = float('-inf')
    sum = 0
    start = 0
    ansstart, ansend = -1, -1
    for i in range(len(arr)):
        # we reset sum to 0 evertime we start a new subarray
        if sum == 0:
            start = i
        sum += arr[i]
        if sum > maxi:
            maxi = sum
            # update max sum => find the current subarray which has max sum
            ansstart = start
            ansend = i
        if sum < 0:
            sum = 0

    print("The subarray is: [", end="")
    for i in range(ansstart, ansend + 1):
        print(arr[i], end=" ")
    print("]")

    return maxi


arr = [-2, -1, -3, -4, -1, -2, -1, -5, -4]
print(print_maxi(arr))
