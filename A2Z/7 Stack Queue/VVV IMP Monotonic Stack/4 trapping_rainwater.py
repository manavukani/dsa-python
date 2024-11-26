# brute - O(n^2)
# for each element, check all previous elements for left max (0 to i-1)
# and all elements to right for right max (i+1 to n-1)


# prefix, suffix array -> O(n) both
def trap(height):
    n = len(height)
    if n == 0:
        return 0
    leftMax = [0] * n
    rightMax = [0] * n
    leftMax[0] = height[0]
    for i in range(1, n):  # O(n)
        leftMax[i] = max(leftMax[i - 1], height[i])
    rightMax[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):  # O(n)
        rightMax[i] = max(rightMax[i + 1], height[i])
    res = 0
    for i in range(n):  # O(n)
        res += min(leftMax[i], rightMax[i]) - height[i]
    return res

# stack - O(n) both


def trap2(height):
    if not height:
        return 0
    stack = []
    res = 0
    for i in range(len(height)):
        while stack and height[i] >= height[stack[-1]]:
            mid = height[stack.pop()]
            if stack:
                right = height[i]
                left = height[stack[-1]]
                h = min(right, left) - mid
                w = i - stack[-1] - 1
                res += h * w
        stack.append(i)
    return res

# OPTIMAL - 2 pointers - TC = O(n), SC = O(1)
def trap3(height):
    if not height:
        return 0
    # both start at opposite ends
    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l], height[r]
    res = 0
    while l < r:
        # move the smaller one
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]
    return res
