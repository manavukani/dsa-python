# continuous subarray where there are k odd numbers = nice

# say all odd = 1
# all even = 0
# becomes binary subarray problem
# any odd number = 1
# k = goal, so when sum = goal ---> odd nums = k

def solve(arr, goal):
    if goal < 0:
        return 0 

    def atMost(k):
        l, r, cnt, currSum = 0, 0, 0, 0
        while r < len(arr):
            # ONLY CHANGE IN CODE -> if odd gives 1, if even gives 0
            currSum += (arr[r] % 2)
            while currSum > k and l <= r:
                # ONLY CHANGE
                currSum -= (arr[l] % 2)
                l += 1
            cnt += (r-l+1)
            r += 1
        return cnt

    return atMost(goal) - atMost(goal - 1)

# since we are calling 2 times...
# TC = 2 * O(2N)
# SC = 2 * O(N)