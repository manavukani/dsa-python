"""
You are given an integer array nums. The range of a subarray of nums is the difference between
the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
Input: nums = [1,2,3]
Explanation:
The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
OUTPUT = 4
"""


# brute -> O(n^3) - for each element, find subarray (j = i+1 to n-1), find range of each subarray and keep adding to total
def brute(arr):
    total = 0
    n = len(arr)
    for i in range(n):
        largest = arr[i]
        smallest = arr[i]
        for j in range(i + 1, n):
            largest = max(largest, arr[j])
            smallest = min(smallest, arr[j])
            total += largest - smallest
    return total

# print(brute([1,2,3]))

# ============ OPTIMAL ============
# Find => (sum of subarray maximum) - (sum of subarray minimum)

def optimal(arr):
    n = len(arr)
    
    # Next greater element to the right
    def find_next_greater_element(arr):
        n = len(arr)
        nge = [n] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            
            if stack:
                nge[i] = stack[-1]
            
            stack.append(i)
        
        return nge
    
    # Previous greater element to the left
    def find_prev_greater_equal_element(arr):
        n = len(arr)
        pge = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            
            if stack:
                pge[i] = stack[-1]
            
            stack.append(i)
        
        return pge
    
    # Next smaller element to the right
    def find_next_smaller_element(arr):
        n = len(arr)
        nse = [n] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                nse[i] = stack[-1]
            
            stack.append(i)
        
        return nse
    
    # Previous smaller element to the left
    def find_prev_smaller_equal_element(arr):
        n = len(arr)
        pse = [-1] * n
        stack = []
        
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                pse[i] = stack[-1]
            
            stack.append(i)
        
        return pse
    
    total = 0

    next_greater = find_next_greater_element(arr)
    prev_greater = find_prev_greater_equal_element(arr)
    next_smaller = find_next_smaller_element(arr)
    prev_smaller = find_prev_smaller_equal_element(arr)
    
    for i in range(len(arr)):
        # sum of max
        max_left = i - prev_greater[i]
        max_right = next_greater[i] - i
        max_contribution = max_left * max_right * arr[i]
        
        # sum of min
        min_left = i - prev_smaller[i]
        min_right = next_smaller[i] - i
        min_contribution = min_left * min_right * arr[i]

        total += max_contribution - min_contribution
    
    return total

print(optimal([1,2,3]))
print(optimal([4,-2,-3,4,1]))
