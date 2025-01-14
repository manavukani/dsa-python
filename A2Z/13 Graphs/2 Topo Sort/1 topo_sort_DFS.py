"""
for a graph,  a -> b, c -> d, ...

topo sort will have a before b, c before d:   a c b d / a b c d / ...

- CYCLIC DIRECTED GRAPHS CANNOT HAVE TOPO SORT (due to cycle)
- ONLY IN DAG
"""


# do DFS, when going back push node to stack
# at end, pop all from stack to get a valid topo sort
def topo_sort(graph):
    visited = [False] * len(graph)
    stack = []

    def dfs(node):
        visited[node] = True

        for nei in graph[node]:
            if not visited[nei]:
                dfs(nei)

        # add to stack before returning
        stack.append(node)

    # visit all nodes (unvisited)
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i)

    # # pop from stack
    # ans = []
    # while stack:
    #     top = stack.pop()
    #     ans.append(top)

    # return ans
    
    # basically just reveresd order, saves SC
    return stack[::-1]


graph = [[], [0], [0], [0]]
print(topo_sort(graph))
graph = [[], [3], [3], [], [0, 1], [0, 2]]
print(topo_sort(graph))


# intution:
# - node at leaf of DFS tree will be at end of topo sort
# - so we just add to stack before returning
# - at end we pop from top (top = front of topo sort)


"""
TC: O(V+E) + O(V), where
        - V = no. of nodes
        - E = no. of edges.
        - There can be at most V components. So, another O(V) time complexity.

SC: O(2N) + O(N) ~ O(2N)
        - 2N - visited array and stack carried during DFS calls
        - N - for recursive stack space, where N = no. of nodes.
"""
