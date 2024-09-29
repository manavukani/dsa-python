# Given an m x n integer matrix matrix, if an element is 0,
# set its entire row and column to 0's.

# You must do it in place.

# INPUT => [[1,1,1],[1,0,1],[1,1,1]]
# OUTPUT => [[1,0,1],[0,0,0],[1,0,1]]

# O(N*M)
def brute(matrix):
    # 0 can be at multiple places
    row, col = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix

# the time complexity is minimal as the traversal of a matrix takes at least O(N*M)(where N = row and M = column).
# Just try improve the space complexity.
# Instead of using two extra lists row and col, we will use the 1st row and 1st column of the given matrix. But if we try to use the 1st row and 1st column, matrix[0][0] is taken twice. To solve this problem we will take an extra variable col0 initialized with 1.
def better(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    col0 = 1
    # step 1: Traverse the matrix and
    # mark 1st row & col accordingly:
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                # mark i-th row:
                matrix[i][0] = 0

                # mark j-th column:
                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    # Step 2: Mark with 0 from (1,1) to (n-1, m-1):
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                # check for col & row:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    #step 3: Finally mark the 1st col & then 1st row:
    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0

    return matrix

print(brute([[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1,1]]))
print(better([[1,1,1],[1,0,1],[1,1,1]])) # [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(better([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # [[0,0,0,0],[0,4,5,0],[0,3,1,0]]