# OPTIMAL => O(n)
def maxSubArray(A):
    sum_max = float('-inf')
    sum_curr = 0
    for i in range(len(A)):
        sum_curr += A[i]
        sum_max = max(sum_curr, sum_max)
        if sum_curr < 0:
            sum_curr = 0
    return sum_max


# BRUTE => O(n^2)
def brute(A):
    sum_max = float('-inf')
    for i in range(len(A)):
        sum_curr = 0
        for j in range(i, len(A)):
            sum_curr += A[j]
            sum_max = max(sum_curr, sum_max)
    return sum_max