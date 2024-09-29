# Given a matrix, your task is to rotate the matrix 90 degrees clockwise. (can also be ANTI-CLOCKWISE)

# Input: matrix = [
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]]
# Output: [
    # [7,4,1],
    # [8,5,2],
    # [9,6,3]]

# Observation - sawp rows and columns

# create dummy matrix for result
# time and space => O(M*N)
def brute(matrix):
    n = len(matrix)
    dummy = [[0 for _ in range(n)] for _ in range(n)] # empty matrix
    for i in range(n):
        for j in range(i):
            dummy[j][n - i - 1] = matrix[i][j]
    return dummy

# improve space complexity => no extra matrix
def optimal(matrix):
    n = len(matrix)
    # transposing the matrix => first row -> first column, so on.....
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row
    for i in range(n):
        matrix[i].reverse()

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
optimal(arr)
print("Rotated Image")
for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end=" ")
    print()


# FOR ANTI-CLOCKWISE => after transpose, reverse each column