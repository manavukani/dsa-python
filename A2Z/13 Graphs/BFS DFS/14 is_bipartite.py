# given adj list
# bipartite --> if nodes partitioned into 2 independent sets A and B such that every edge of graph connects a node in set A and set B.
# alternate def. --> all adjacent nodes have different color

# Observation:
# if cycle --> even lenght -> is bipartite
#          --> odd lenght -> NOT bipartite

"""
APPROACH:
- use color vector of size len(graph) ==> -1 not colored, 0/1 colored
- we go to each node, if not colored, traverse DFS way (so that we can check continuously)
- if neighbor not colored, give it opposite color and do dfs for it
- if colored but same as current node, return False -- cannot be bipartite
- if all done, loop thorugh all vertices to ensure 'multiple components' are checked if present

"""


# TC = V + 2E
# SC = V
def solve(graph):
    V = len(graph)
    visited = [-1] * V  # -1 not colored, 0/1 colored

    def dfs(node, color):
        # color the node
        visited[node] = color

        # check all adjacent nodes
        for nei in graph[node]:
            if visited[nei] == -1:
                # check for nei with opposite color
                if dfs(nei, not color) == False:
                    return False

            # nei has same color as node
            elif visited[nei] == color:
                return False

        return True

    # for multiple components, we iterate all nodes
    for i in range(V):
        if visited[i] == -1:
            # do dfs, if any call is false, not bipartite
            if dfs(i, 0) == False:
                return False

    return True


g = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
print(solve(g))
