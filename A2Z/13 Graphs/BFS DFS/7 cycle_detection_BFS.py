# UNDIRECTED GRAPH
# Cycle detection using BFS

# INTUTION: if we get to same node from 2 different paths, then there is a cycle

from collections import deque


# TC: O(N+2E)
def detect(src, adjList, visited):
    visited[src] = True
    q = deque()
    q.append((src, -1))  # node, parent
    while q:
        node, parent = q.popleft()
        for nei in adjList[node]:
            if not visited[nei]:
                visited[nei] = True
                q.append((nei, node))
            elif nei != parent:
                return True
    return False


# TC: O(N)
# what if the graph is disconnected, multiple components ---> we need to run the cycle detection for each component
def hasCycle(n, adjList):
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            if detect(i, adjList, visited):
                return True

    return False


# test
adj = [[1], [0, 2, 4], [1, 3], [2, 4], [1, 3]]
print(hasCycle(5, adj))  # True

adj = [[], [2], [1, 3], [2]]
print(hasCycle(4, adj))  # False


# OVERALL - TC: O(N+2E), SC: O(N)