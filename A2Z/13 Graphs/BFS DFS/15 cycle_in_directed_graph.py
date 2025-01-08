# using the same technique as undirected wont work. it would give false positive for cycles
# eg:


"""

... ->  3 ->  4
        |     |               both are down 3 -> 5 and 4 -> 6
        7 ->  5  -> 6

this would give me a false positive for cycle

"""

# MODIFIED APPROACH: we use visited and path visited. whenever we backtrack from return we reset the path visited node
# USING DFS

def detectCycle(graph):
    visited = [False] * len(graph)
    pathVisited = [False] * len(graph)

    def dfs(node):
        visited[node] = True
        pathVisited[node] = True

        for nei in graph[node]:
            # not visited
            if not visited[nei]:
                if dfs(nei):
                    return True
            # visited and on same path
            elif pathVisited[nei]:
                return True

        # reset the path visited when backtracking ---- VERY IMP
        pathVisited[node] = False
        return False

    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i):
                return True

    return False


# test

graph = [[1], [2], [3, 6], [4], [5], [], [4], [8, 2], [9], [7]]
print(detectCycle(graph))

graph = [[1], [2], [3, 6], [4], [5], [], [4]]
print(detectCycle(graph))
