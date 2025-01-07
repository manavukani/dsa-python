"""
TC = O(N) + O(V + 2E) ----> N for dfs calls for each node, V+2E for traversing all nodes during dfs
SC = O(N) ----------------> N for stack space in case of skewed tree, N for visited array
"""


# iterate all nodes, if unvisited, increment province count
# do dfs -- will visit all connected nodes to it
def solve(adjMatrix):

    # convert adjacency matrix to adjacency list
    adjList = [[] for _ in range(len(adjMatrix))]
    for i in range(len(adjMatrix)):
        for j in range(len(adjMatrix[i])):
            if adjMatrix[i][j] == 1 and i != j:
                adjList[i].append(j)
                adjList[j].append(i)

    # dfs
    def dfs(i):
        visited[i] = True  # marks all connected nodes as visited
        for j in adjList[i]:
            if not visited[j]:
                dfs(j)

    visited = [False] * len(adjList)
    provinces = 0
    for i in range(len(adjList)):
        if not visited[i]:
            provinces += 1
            dfs(i)
    return provinces


isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solve(isConnected))  # 2


# ------ WITHOUT CONVERTING TO ADJACENCY LIST ------
def solve_withoutConverting(isConnected):
    visited = set()
    provinces = 0
    n = len(isConnected)

    def dfs(i):
        visited.add(i)
        for j in range(n):
            if isConnected[i][j] == 1:
                if j not in visited:
                    dfs(j)

    for i in range(n):
        if i not in visited:
            dfs(i)
            provinces += 1
    return provinces
