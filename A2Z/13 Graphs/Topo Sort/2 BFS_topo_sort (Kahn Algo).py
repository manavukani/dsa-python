# using the indegree


"""
Approach:
1. Compute the indegree of each vertex (number of incoming edges).
2. Initialize a queue with all vertices whose indegree is zero, they will be at start of topo sort order
    (but since we use stack they go to bottom)
3. Repeatedly dequeue a vertex/node, add it to the topological order
    IMP ----> remove its associated outdegree ie - indegree for nei
    IMP ----> If any nei's indegree becomes zero, enqueue it.
4. Continue until the queue is empty.
"""

from collections import deque


def kahns_algo(adj):
    V = len(adj)

    # fill indegree
    indegree = [0] * V
    for i in range(V):
        for nei in adj[i]:
            indegree[nei] += 1

    # initial queue with all indegree = 0 nodes
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    # bfs
    ans = []
    while q:
        node = q.popleft()
        ans.append(node)

        # IMP
        for nei in adj[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return ans


graph = [[], [0], [0], [0]]
print(kahns_algo(graph))
graph = [[], [3], [3], [], [0, 1], [0, 2]]
print(kahns_algo(graph))

"""
TC: O(V+E), where
        - V = no. of nodes
        - E = no. of edges.
        - There can be at most V components. So, another O(V) time complexity.

SC: O(N) + O(N) ~ O(2N)
        - O(N) for the indegree array
        - O(N) for the queue used in BFS
        - N = no. of nodes
"""
