# Computes the shortest paths from a source vertex to all other vertices in a weighted Directed Acyclic Graph (DAG).

# input: [[edge, wt]] -> [[0,1,2], [0,2,1]]
# output: list of shortest distances from the source vertex to each vertex, if unreachable dist = -1

"""
Intution:
- make the adj list
- find topo sorted order
- for each element in the topologically sorted order, updated the distance to its nei
- if visited, check for minimum
- return dist array


WHY TOPOLOGICAL SORT (and not Dijsktra or something)??
- first element of topo sorted order will have inorder = 0 (no incoming edge)
- there will be no one before it
- so we move according to reachability
- source will be the first elemnt of topo sort

MORE ABOUT IT:
- Finding the shortest path to a vertex is easy if you already know the shortest paths to all the vertices that can precede it. 
- Finding the longest path to a vertex in DAG is easy if you already know the longest path to all the vertices that can precede it
- Processing the vertices in topological order ensures that by the time you get to a vertex, you've already processed all the vertices that can precede it.
- Dijkstra's algorithm is necessary for graphs that can contain cycles, because they can't be topologically sorted.
"""


# TC = O(V+E)
# SC = O(V+E) ---> adj list,
def dag_shortes_path(V, E, edges):
    # convert edges, wt -> adj list
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append((v, wt))

    # find topological sorted order ------------> O(V+E)
    def topo_sort(adj):
        visited = [False] * len(adj)
        stack = []

        def dfs(node):
            visited[node] = True

            # for all adjacent vertices of node
            for nei in adj[node]:
                v = nei[0]
                wt = nei[1]
                if not visited[v]:
                    dfs(v)

            # add to stack before returning
            stack.append(node)

        # traverse all nodes --> ensure multiple components
        for node in range(len(adj)):
            if not visited[node]:
                dfs(node)

        # pop all from stack
        return stack[::-1]

    topo_sorted = topo_sort(adj)

    # caluclate distance of edges from source ---------> O(V+E) -- V for while loop of nodes, E for for loop of nei
    distance = [float("inf")] * V
    distance[0] = 0

    while topo_sorted:
        # start from first element in topo sort order
        node = topo_sorted[0]
        topo_sorted.pop(0)

        # if cannot reach node, no need to check nei
        if distance[node] != float("inf"):
            for nei in adj[node]:
                v = nei[0]
                wt = nei[1]
                # if new dist less than current best, updated
                distance[v] = min(distance[v], distance[node] + wt)

    # replace inf with -1 to indicate unreachable nodes
    return [-1 if dist == float("inf") else dist for dist in distance]


# test
print(
    dag_shortes_path(
        4,
        2,
        [[0, 1, 2], [0, 2, 1]],
    )
)

print(
    dag_shortes_path(
        6,
        7,
        [[0, 1, 2], [0, 4, 1], [4, 5, 4], [4, 2, 2], [1, 2, 3], [2, 3, 6], [5, 3, 1]],
    )
)
