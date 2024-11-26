# hard

# input = heights[i] represents the height of a bar
# width of each bar is 1
# output = area of the largest rectangle in the histogram


# single stack approach - neetcode
def largestRectangleArea(heights):
    n = len(heights)
    maxArea = 0
    stack = []
    
    for i in range(n + 1):
        while stack and (i == n  or heights[stack[-1]] >= heights[i]):
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            maxArea = max(maxArea, height * width)
        stack.append(i)
    return maxArea

# monotonic stack
# https://youtu.be/X0X6G-eWgQ8 - striver
def largestRectangleArea(heights):
    n = len(heights)
    stack = []
    leftMost = [-1] * n
    
    # calculate the array for idx of
    # left smallest element and right smallest element
    
    # if top of stack is greater than current element - pop
    # if stack is empty - leftMost = -1
    # else leftMost = stack[-1]
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftMost[i] = stack[-1]
        stack.append(i)
    
    # if top of stack is greater than current element - pop
    # if stack is empty - rightMost = n
    # else rightMost = stack[-1]
    # start from the end of the array
    stack = []
    rightMost = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightMost[i] = stack[-1]
        stack.append(i)
    
    # traverse thorugh the heights array and calculate the area
    maxArea = 0
    for i in range(n):
        leftMost[i] += 1
        rightMost[i] -= 1
        maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
    return maxArea