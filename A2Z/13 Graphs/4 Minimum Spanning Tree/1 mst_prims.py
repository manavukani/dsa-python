# Spanning Tree: a tree with n nodes, n-1 edges and all nodes reachable to each other
# there can be more than 1 spanning tree

# MST: spanning tree with minimum path wt

# 2 ways: Prim's Algo & Kruskal's Algo (disjoint sets)


"""
PRIM'S ALGO:
- start from 0th node with parent -1
- mark 0 as visited and for all nei add them to PQ --- do NOT add to MST if parent = -1
- get the smallest edge wt node from PQ and add that to MST path & add that to the MST total as well
- mark that node as visited and check for all nei if unvisited and add them to PQ

Intution:
- Greedy
- Keep finding the minimal edge wt (using min-heap/PQ) and connecting it to make the MST
"""


from queue import PriorityQueue


# TC = O(E log E) + O(E log E) = O(E log E)
# SC = O(E)
def primsMst(V, edges):
    # edges -> adj list
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append((v, wt))
        adj[v].append((u, wt))

    # prims logic
    visited = [False] * V
    q = PriorityQueue()
    q.put((0, 0, -1))  # wt, node, parent

    total = 0
    mst_edges = []

    # ==================================> TC - E       - worst case, all edges in queue
    while not q.empty():
        # ==============================> TC - log E   - get minimum node
        wt, node, par = q.get()

        # already part of MST, skip it
        if visited[node]:
            continue

        # add to MST
        visited[node] = True
        total += wt
        if par != -1:
            mst_edges.append((par, node))

        # ==============================> TC - E log E - worst case, star topology, E edges, log E for put
        # check adjacent
        for nei, edgeWt in adj[node]:
            if not visited[nei]:
                q.put((edgeWt, nei, node))

    return total, mst_edges


V = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
mstWt, mst = primsMst(V, edges)
print(mstWt)
print(mst)
