# brute - O(n^2) -> for each element, check all previous elements

'''
Monotonic stack

- we do in FORWARD direction
- push elements in stack, if current > top
- if current < top, pop until current > top
- for each ele, store the top as PSE
- if no ele, store -1
'''

def previous_smaller_element(arr):
    stack = []
    res = []
    for ele in arr:
        while stack and stack[-1] >= ele:
            stack.pop()
        if stack:
            res.append(stack[-1])
        else:
            res.append(-1)
        stack.append(ele)
    return res

arr = [4, 5, 2, 10, 8]
print(previous_smaller_element(arr)) # [-1, 4, -1, 2, 2]