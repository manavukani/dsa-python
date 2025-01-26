# treat edges as undirected but give weight to real edges = 1
# count will be updated each time with edge wt

class Solution:
    def minReorder(self, n, connections) -> int:
        count = 0
        adjList = [[] for _ in range(n)]
        for u, v in connections:
            adjList[u].append((v, 1))
            adjList[v].append((u, 0))

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei, val in adjList[node]:
                if nei not in visited:
                    nonlocal count
                    count += val
                    dfs(nei)

        dfs(0)

        return count


# WITHOUT USING VISITED ---> instead keeping track of parent
class Solution:
    def minReorder(self, n, connections):
        count = 0
        adjList = [[] for _ in range(n)]
        for u, v in connections:
            adjList[u].append((v, 1))
            adjList[v].append((u, 0))

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei, val in adjList[node]:
                if nei not in visited:
                    nonlocal count
                    count += val
                    dfs(nei)

        dfs(0, -1)

        return count
