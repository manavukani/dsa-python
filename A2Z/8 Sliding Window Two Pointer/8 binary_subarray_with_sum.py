# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4 - # subarray with sum = goal

# similar to count subarray with sum equals k (+ve and -ve numbers) -> O(N) using hashing
# TC = SC = O(N)
def using_hashmap(nums, goal):
    prefix_sum = 0
    count = 0
    sum_freq = {0: 1}
    
    for num in nums:
        prefix_sum += num
        
        if prefix_sum - goal in sum_freq:
            count += sum_freq[prefix_sum - goal]

        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    
    return count

# optimize the O(N) space => O(1)
# finds subarray with sum <= goal
# TODO - find subarray with sum == goal

def solve(arr, goal):
    if goal < 0:
        return 0

    # suarray with sum <= k
    def atMost(k):
        l, r, cnt, currSum = 0, 0, 0, 0
        while r < len(arr):
            currSum += arr[r]
            # If sum exceeds target, shrink window
            while currSum > k and l <= r:
                currSum -= arr[l]
                l += 1
            # Count subarrays ending at current right
            cnt += (r-l+1)
            r += 1
        return cnt

    # Key trick: subarrays with exact sum = goal 
    return atMost(goal) - atMost(goal - 1)
