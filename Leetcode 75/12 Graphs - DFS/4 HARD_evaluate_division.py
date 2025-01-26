from collections import defaultdict


# SOLUTION 1 DFS
# Binary relationship is represented as a graph usually.
# Does the direction of an edge matters? -- Yes. Take a / b = 2 for example, it indicates a --2--> b as well as b --1/2--> a.
# Thus, it is a directed weighted graph
# TC = O(E + Q * (N+E))
# SC = O(N+E)
class Solution:
    def calcEquation(self, equations, values, queries):
        """building graph"""
        graph = defaultdict(dict)  # O(E) space and time
        for (numerator, denominator), val in zip(equations, values):
            graph[numerator][denominator] = val
            graph[denominator][numerator] = 1.0 / val

        """dfs logic"""
        # O(N) space for visited, O(N+E) time for each call
        def dfs(start, end, visited):

            # DNE case
            if start not in graph or end not in graph:
                return -1.0
            # same variable
            if start == end:
                return 1.0

            visited.add(start)

            for nei in graph[start]:
                if nei not in visited:
                    visited.add(nei)
                    intermediate_result = dfs(nei, end, visited)
                    if intermediate_result != -1.0:
                        return intermediate_result * graph[start][nei]
            return -1.0

        """calculating result for each query"""
        result = []
        # Q queries so, TC = Q * O(N+E)
        for numerator, denominator in queries:
            result.append(dfs(numerator, denominator, set()))
        return result


# SOLUTION 2 - FLOYD WARSHAL
# NOTE: more efficient for scenarios with many queries, but can become expensive if the number of nodes is large due to its TC
#       for sparse graphs and fewer queries, the DFS-based approach is always better
# Time complexity: O(n^3)
# Space complexity: O(n^2)
class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1 / val

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j] if i != j else 1

        return [graph[u].get(v, -1) for u, v in queries]
