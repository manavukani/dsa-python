def solve(isConnected):
    # matrix to adj list
    adjList = [[] for _ in range(len(isConnected))]
    for i in range(len(isConnected)):
        for j in range(len(isConnected[0])):
            if isConnected[i][j] == 1 and i != j:
                adjList[i].append(j)
                adjList[j].append(i)

    # normal dfs
    def dfs(node):
        visited[node] = True
        for nei in adjList[node]:
            if not visited[nei]:
                dfs(nei)

    # for multiple components
    n = len(adjList)
    visited = [False] * n
    provinces = 0

    for i in range(n):
        if not visited[i]:
            provinces += 1
            dfs(i)

    return provinces


# ------ WITHOUT CONVERTING TO ADJACENCY LIST ------
def solve2(isConnected):
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
