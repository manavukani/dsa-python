from collections import deque


# TC: O(V) + O(2E) = O(V+E)
# SC: O(V) --- for visited array
def bfs_traversal(adj):
    visited = [False] * len(adj)
    visited[0] = True

    q = deque()
    q.append(0)

    res = []

    # TC = V
    while q:
        node = q.popleft()
        res.append(node)

        # visit all neighbors: TC = 2E
        for nei in adj[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append(nei)

    return res


# test
adj = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
print(bfs_traversal(adj))  # [0, 1, 2, 3, 4, 5]
