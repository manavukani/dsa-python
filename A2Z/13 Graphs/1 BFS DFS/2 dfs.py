# TC: O(N) + O(2E) -----> N for visiting all nodes, 2E for visiting all edges (neighbors)
# SC: O(N) -------------> for skewed tree stack space will be N


def dfs_recursive(adj):
    # initialize
    visited = [False] * len(adj)
    dfs_res = []

    def dfs(node):
        visited[node] = True
        dfs_res.append(node)
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)

    # start from node 0
    dfs(0)
    return dfs_res


# test
adj = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
print(dfs_recursive(adj))  # [0, 1, 3, 4, 2, 5]


def dfs_iterative(adj):
    visited = [False] * len(adj)
    dfs = []

    stack = []
    stack.append(0)

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            dfs.append(node)
            for nei in reversed(adj[node]):
                if not visited[nei]:
                    stack.append(nei)

    return dfs


print(dfs_iterative(adj))  # [0, 1, 3, 4, 2, 5]
