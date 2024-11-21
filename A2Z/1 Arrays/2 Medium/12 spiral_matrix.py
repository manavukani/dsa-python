# Given a Matrix, print the given matrix in spiral order.

# Matrix[][] =  { 1, 2, 3, 4 }
# 		        { 5, 6, 7, 8 }
# 		        { 9, 10, 11, 12 }
# 	            { 13, 14, 15, 16 }

# Output: 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.


def solve(matrix):
    result = []

    top = 0
    bottom = len(matrix) - 1
    left = 0
    right = len(matrix[0]) - 1

    # whole matrix is traversed
    while top <= bottom and left <= right:

        # L -----> R
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top += 1

        # Top ------> Bottom
        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right -= 1

        # L <-------- R
        if (top <= bottom):
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])

            bottom -= 1

        # Top <------- Bottom
        if (left <= right):
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

print(solve(mat))
