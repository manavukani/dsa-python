# Terminal node - if no outgoing edges.
# Safe node - if every possible path starting from that node, leads to terminal node (or another safe node).

# Return - safe nodes of the graph, sorted in ascending order


"""
Observation:
- initially all terminal nodes are safe nodes (outdegree = 0)

Approach:
- reverse all edges (terminal nodes now have indegree = 0)
- we do topological sort
    - get all nodes with indegree = 0
    - add node to res
    - do removal of edges on nei nodes
    - when q empty -> stop
- this ensures we get all safe nodes in res
- sort res before returning

"""


from collections import deque


def safeStates(graph):
    V = len(graph)

    # reverse edges
    adjRev = [[] for _ in range(V)]
    indegree = [0] * V  # reversed edges

    for i in range(V):
        # current: i -> nei || convert: nei -> i
        for nei in graph[i]:
            adjRev[nei].append(i)
            indegree[i] += 1

    # PLAIN TOPO SORT
    # add terminal nodes to queue
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    res = []
    while q:
        node = q.popleft()

        res.append(node)

        for nei in adjRev[node]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    # sort res - question requirement
    res.sort()
    return res


print(safeStates([[1, 2], [2, 3], [5], [0], [5], [], []]))

# TC: TOPO SORT + sorting ==> O(V+E) + O(N*logN)
# SC: indegree, queue, reverse adj ===> O(3N)
