# USING CYCLE DETECTION METHOD

def validTree(n, edges) -> bool:
    if len(edges) > (n - 1):
        return False

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visit = set()

    def dfs(node, par):
        if node in visit:
            return False

        visit.add(node)
        for nei in adj[node]:
            if nei == par:
                continue
            if not dfs(nei, node):
                return False
        return True

    return dfs(0, -1) and len(visit) == n


print(validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # true
