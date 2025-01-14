# MULTI-SOURCE SHORTEST PATH ALGO - can detect negative cycles as well

"""
Method:
- go via every node and take minimum of all the paths
- using DP to know pre-computed values
- use adj Matrix to store all dist between diff nodes
- brute force algo which goes from each point to other points via every point

How to detect negative cycle:
- costing of node to itself will become less than 0, which unusual
- so negative cycle exist

"""


# TC = O( n^3 )
# SC = O( n^2 )
def floydWarshall(matrix):
    """
    in-place, do not return anything
    """
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            # in question its given -1 for unreachable so replace with inf
            if matrix[i][j] == -1:
                matrix[i][j] = float("inf")
            # diagonal
            if i == j:
                matrix[i][j] = 0

    # via each node
    for k in range(n):
        # check distance between all nodes, update if lesser
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    """ check for negative cycle"""
    for i in range(n):
        if matrix[i][i] < 0:
            print("NEGATIVE CYCLE PRESENT")

    for j in range(n):
        # undo the -1 and inf swap
        if matrix[i][j] == float("inf"):
            matrix[i][j] = -1


matrix = [[0, 1, 43], [1, 0, 6], [-1, -1, 0]]
floydWarshall(matrix)
print(matrix)
