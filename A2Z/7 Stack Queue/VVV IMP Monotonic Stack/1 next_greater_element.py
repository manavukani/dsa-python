# input = [6, 0, 8, 1, 3]
# output = [8, 8, -1, 3, -1]

# brute - O(n^2) --> for each element, check all elements to right

# monotonic stack - O(n)

'''
NGE = Next Greater Element

- start from back, so that we know what are the elements to the right for any idx
- when stack empty, NGE = -1 (no element to right), add ele to stack
- when stack not empty
    - if current < top, keep adding to stack, NGE = top
    - if current > top, pop from stack until current < top, NGE = top, add ele to stack
- return nge array

'''


def nextGreaterElement(nums):
    stack = []
    nge = [-1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        # pop until stack[-1] > nums[i]
        while stack and nums[i] >= stack[-1]:
            stack.pop()
        # now stack[-1] > nums[i]
        if stack:
            nge[i] = stack[-1]
        # if not stack => no element to right OR no element greater (on right, we popped all)
        else:
            nge[i] = -1
        stack.append(nums[i])
    return nge


input = [6, 0, 8, 1, 3]
print(nextGreaterElement(input))

# TC = O(2N)
# SC = O(N) + O(N) = O(N) - stack and nge array (can reduce SC by modifying input array)