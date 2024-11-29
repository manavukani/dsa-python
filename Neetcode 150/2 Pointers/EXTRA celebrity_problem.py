'''
- Given a square matrix mat[][] of size n x n, such that mat[i][j] = 1 means ith person knows jth person
- The task is to find the celebrity. 
- A celebrity is a person who is known to all but does not know anyone.
- Return the index of the celebrity, if there is no celebrity return -1.

- Note: Follow 0 based indexing and M[i][i] will always be 0.


'''


'''
================= Brute Force =================

eg:

    0 1 2 3
------------
0 | 0 1 1 0
1 | 0 0 0 0
2 | 0 1 0 0
3 | 1 1 0 0

-> we maintain 2 arrays, indegree and outdegree (both of size n)
-> indegree[i] = number of people who know ith person -> knows me
-> outdegree[i] = number of people whom ith person knows -> i know
-> we iterate through the matrix and update indegree and outdegree arrays

for a celebrity:
-> indegree[celebrity] = n-1
-> outdegree[celebrity] = 0

indegree = [1, 3, 1, 0]
outdegree = [2, 0, 1, 2]

so the celebrity is 1
'''

# TC: O(n^2) + O(n) = O(n^2)
# SC: O(2*n) = O(n)


def celebrity_problem(M):
    n = len(M)
    indegree = [0]*n
    outdegree = [0]*n

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                indegree[j] += 1  # knows me
                outdegree[i] += 1  # i know

    for i in range(n):
        if indegree[i] == n-1 and outdegree[i] == 0:
            return i

    return -1


# Optimized Approach - 2 Pointers
'''
Minimum # celebrities = 0
Maximum # celebrities = 1
-> if i knows j, then i is not a celebrity


-> we maintain 2 pointers, a and b
-> a = 0, b = n-1
-> if a knows b, then a is not a celebrity, so a++
-> if a does not know b or b knows a, then b is not a celebrity, so b--
-> we continue this until a < b
-> finally we check if 'a' (candidate) is celebrity or not
'''


def two_pointer(M):
    n = len(M)
    top = 0
    down = n-1
    while top < down:
        if M[top][down] == 1:  # top knows down, not a celebrity
            top += 1
        elif M[down][top] == 1:  # down knows top, not a celebrity
            down -= 1
        else:  # both don't know each other, so both are not celebrities
            top += 1
            down -= 1

    # if not at same position, then no celebrity
    if top > down:
        return -1

    # checking candidate
    # for a celebrity, 
    for i in range(n):
        '''
        # skip the same person
        if i == top:
            continue
        
        # everyone should know the candidate -> i, top = 1 (all rows)
        # candidate should not know anyone -> top, i = 0 (all columns)
        if M[i][top] == 1 or M[top][i] == 0:
            continue
        else:
            return -1
        '''
        
        # same as above, but optimized
        if i != top and (M[top][i] == 1 or M[i][top] == 0):
            return -1
    return top


M = [[0, 1, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 1, 1, 0]]

M2 = [[0, 1, 1, 0],
      [0, 0, 0, 0],
      [0, 1, 0, 0],
      [1, 1, 0, 0]]

print(celebrity_problem(M))
print(two_pointer(M2))
