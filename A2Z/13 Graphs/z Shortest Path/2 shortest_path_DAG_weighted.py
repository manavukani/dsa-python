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

"""


# TC = E +
def dag_shortes_path(V, E, edges, src=0):
    """
    Parameters:
        V (int): Number of vertices in the graph.
        E (int): Number of edges in the graph.
        edges (List[Tuple[int, int, int]]): A list of edges, each represented as a tuple (u, v, weight) where u is the source vertex, v is the destination vertex, and weight is the edge weight.
        src (int, optional): The source vertex from which to calculate distances. Defaults to 0.
    """

    # convert edges, wt -> adj list
    adj = [[] for _ in range(V)]
    for u, v, wt in edges:
        adj[u].append((v, wt))

    # find topological sorted order
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

    # caluclate distance of edges from source
    distance = [float("inf")] * V
    distance[src] = 0

    while topo_sorted:
        # start from first element in the order
        node = topo_sorted[0]
        topo_sorted.pop(0)

        for nei in adj[node]:
            v = nei[0]
            wt = nei[1]
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
