# Shortest Path in Undirected Graph with Unit Weights


"""
Plain BFS Search: 
We do not need additional check like: if res[nei] > dist + 1
because BFS inherently guarantees that first time a node is visited, it is visited with the shortest distance.
"""

from collections import deque


# TC = BFS = O(V+2E)
def shortest_dist_to_all(adj, src):
    res = [-1] * len(adj)
    q = deque()
    q.append(src)
    res[src] = 0
    while q:
        node = q.popleft()
        for nei in adj[node]:
            if res[nei] == -1:
                res[nei] = res[node] + 1
                q.append(nei)
    return res


adj = [[1, 3], [0, 2], [1, 6], [0, 4], [3, 5], [4, 6], [2, 5, 7, 8], [6, 8], [7, 6]]
src = 0
print(shortest_dist_to_all(adj, src))  # 0 1 2 1 2 3 3 4 4
