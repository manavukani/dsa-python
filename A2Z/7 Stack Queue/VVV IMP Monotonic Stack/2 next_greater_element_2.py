# if not on right, then look in circular way

# input = [1, 2, 1]
# output = [2, -1, 2]

# input = [2, 10, 12, 1, 11]
# output = [10, 12, -1, 11, 12]

# brute force approach -> for each arr[i], traverse from i+1 to n, if not found, check 0 to i-1

'''
Monotonic stack approach

- double the input array, so that we can look in circular way
eg: [2, 10, 12, 1, 11] => [2, 10, 12, 1, 11, 2, 10, 12, 1, 11]
- for each element, we can look to right

Same as before,
- start from back, so that we know what are the elements to the right for any idx
- when stack empty, NGE = -1 (no element to right), add ele to stack
- when stack not empty
    - if current < top, keep adding to stack, NGE = top
    - if current > top, pop from stack until current < top, NGE = top, add ele to stack
- return nge array

JUST: we only assign NGE when idx < n

'''

# TC = O(4N) => 2N for for loop and 2N for while loop (max pop 2N)
def nextGreaterCircular(nums):
    n = len(nums)
    stack = []
    nge = [-1] * n
    for i in range(2*n - 1, -1, -1):
        # i%n to get idx in original array
        while stack and stack[-1] <= nums[i % n]:
            stack.pop()
        if i < n:
            if stack:
                nge[i] = stack[-1]
            else:
                nge[i] = -1
        stack.append(nums[i % n])
    return nge

# input = [2, 10, 12, 1, 11]
input = [1, 2, 1]
print(nextGreaterCircular(input))