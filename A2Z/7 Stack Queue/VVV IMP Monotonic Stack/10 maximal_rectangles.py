'''
INPUT => rows x cols binary matrix filled with 0's and 1's
OUTPUT => area of largest rectangle containing only 1's

INPUT:
1 0 1 0 1
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Use "largest rectangle in histogram" to finding largest rectangle

input -> height of histogram (prefix sum)
1 0 1 0 1 -> 1 0 1 0 1
1 0 1 1 1 -> 2 0 2 1 2
1 1 1 1 1 -> 3 1 3 2 3
1 0 0 1 0 -> 4 0 0 3 0


we give each row to largest rectangle in histogram function. Here:
- mat[0]
- mat[1] + mat[0]
- mat[2] + mat[1] + mat[0]
- mat[3] + mat[2] + mat[1] + mat[0]

'''


def largestRectangleArea(heights):
    n = len(heights)
    stack = []
    leftMost = [-1] * n
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            leftMost[i] = stack[-1]
        stack.append(i)
    stack = []
    rightMost = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        if stack:
            rightMost[i] = stack[-1]
        stack.append(i)
    maxArea = 0
    for i in range(n):
        leftMost[i] += 1
        rightMost[i] -= 1
        maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
    return maxArea

# TC = O(n*m)

# M1
def maximal_rectangle(matrix):
    n = len(matrix)
    m = len(matrix[0])
    max_area = 0
    p_sum = [[0] * m for _ in range(n)]
    # TC = O(n*m)
    for j in range(m):
        running_sum = 0
        for i in range(n):
            running_sum += int(matrix[i][j])
            if matrix[i][j] == '0':
                running_sum = 0
            p_sum[i][j] = running_sum
    # TC = O(n*2m)
    for i in range(n):
        max_area = max(max_area, largestRectangleArea(p_sum[i]))
    return max_area

# M2
# def maximal_rectangle(matrix):
    # rows, cols = len(matrix), len(matrix[0])
    # histogram = [0] * cols
    # max_rec = 0
    # for r in range(rows):
    #     for c in range(cols):
    #         histogram[c] = histogram[c] + 1 if matrix[r][c] == '1' else 0
    #     max_rec = max(max_rec, largestRectangleArea(histogram))
    # return max_rec


input_mat = [["1", "0", "1", "0", "1"], ["1", "0", "1", "1", "1"],
             ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(maximal_rectangle(input_mat))  # 6