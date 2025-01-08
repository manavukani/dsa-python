# UNDIRECTED GRAPH
# Cycle detection using BFS

# INTUTION: if we get to parent during DFS traversal, then there is a cycle


def dfs(node, parent, visited, adj):
    visited[node] = True
    for nei in adj[node]:
        if not visited[nei]:
            if dfs(nei, node, visited, adj):
                return True
        # EDGE CASE: if nei is visited and not parent, then also cycle
        elif nei != parent:
            return True
    return False


def hasCycle(n, adj):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if dfs(i, -1, visited, adj):
                return True
    return False

# test
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(hasCycle(5, adj))  # True

adj = [[], [2], [1, 3], [2]]
print(hasCycle(4, adj))  # False