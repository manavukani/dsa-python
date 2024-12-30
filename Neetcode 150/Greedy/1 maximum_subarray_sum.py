# NAIVE SOLUTION => O(N^2)
def brute(arr):
    maxi = float('-inf')
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            sum += arr[j]
            maxi = max(maxi, sum)
    return maxi


# KADANE's ALGORITHM => O(N)
def optimal(arr):
    total = 0
    max_total = float("-inf")
    for val in arr:
        total += val
        max_total = max(total, max_total)
        if total < 0:
            total = 0
    return max_total

# print("Sum", optimal([2,-3,4,-2,2,1,-1,4]))

# FOLLOW_UP => print the subarray with maxi sum ====> REVISIT THIS

def print_maxi(arr):
    maxi = float("-inf")
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


res = print_maxi([2,-3,4,-2,2,1,-1,4])

print("Sum is:", res)
