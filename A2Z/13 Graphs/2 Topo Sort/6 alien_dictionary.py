# For alien language, with order among letters unknown
# Using list of non-empty words from the dictionary, where words are sorted lexicographically.
# Return the order of letters in this language.

"""
Input:  ['baa', 'abcd', 'abca', 'cab', 'cad']
Output: 'bdac'

Approach:
- check for each consecutive pair of words why is it before another
    - baa & abcd ---> b before a ----> b --> a
    - abcd & abca ---> d before a ----> d --> a
    - abca & cab ----> a before c ----> a --> c
    - cab & cad -----> b before d ----> b --> d
- this gives use the directed graph
- IMP --> convert letter to numbers
- return topo sort of this graph for all nodes
- IMP --> convert back to letters and make a string

"""

# BFS - TOPO SORT
from collections import deque


def topoSort(V, adj):
    indegree = [0] * V
    for i in range(V):
        for it in adj[i]:
            indegree[it] += 1

    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)

    topo = []
    while q:
        node = q.popleft()
        topo.append(node)

        for it in adj[node]:
            indegree[it] -= 1
            if indegree[it] == 0:
                q.append(it)

    return topo


def findOrder(dict, K):
    N = len(dict)
    adj = [[] for _ in range(N)]
    for i in range(N - 1):
        s1 = dict[i]
        s2 = dict[i + 1]
        length = min(len(s1), len(s2))
        for ptr in range(length):
            if s1[ptr] != s2[ptr]:
                adj[ord(s1[ptr]) - ord("a")].append(ord(s2[ptr]) - ord("a"))
                break

    topo = topoSort(K, adj)
    ans = ""
    for it in topo:
        ans += chr(it + ord("a"))

    return ans


print(findOrder(["baa", "abcd", "abca", "cab", "cad"], 4))


# USING DFS
def alienDict(words):
    # dict for all unique char: c -> set()
    adj = {c: set() for w in words for c in w}

    # find the relations (a->b) between chars
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        minLen = min(len(w1), len(w2))
        # Edge case: same prefix, but 1 word is longer -> no need to check
        if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
            return ""
        for j in range(minLen):
            if w1[j] != w2[j]:
                adj[w1[j]].add(
                    w2[j]
                )  # char in w2 comes after char in w1: w1_j --> w2_j
                break

    visited = {}  # path visited
    stack = []

    # DFS logic
    def dfs(node):
        if node in visited:
            return visited[node]

        visited[node] = True

        for nei in adj[node]:
            if dfs(nei):
                return True  # loop

        visited[node] = False

        stack.append(node)

    # go through all char
    for char in adj:
        if dfs(char):
            return ""  # loop

    stack.reverse()  # stack pop all to give result
    return "".join(stack)


print(alienDict(["baa", "abcd", "abca", "cab", "cad"]))


"""
Above gives any of the valid order back, but not always the lexicographically smallest,

-  when multiple characters have the same in-degree, they are processed in lexicographical order.
-  min-heap (heapq) for topological sorting ensure lexicographical order

"""
import heapq
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """

    def alien_order(self, words):
        # edge case? empty word?
        if not words:
            return ""
        graph = self.get_graph(words)
        if not graph:
            return ""
        in_degree = self.get_indegree(graph)
        result = self.topo_sort(graph, in_degree)
        # print(result)
        # final check if there's any loop in the topo graph. If there's loop, the nodes in loop
        # will never get to 0 in_degree, so len of result will be less than graph
        return result if len(result) == len(graph) else ""

    def get_graph(self, words):
        # scan through all words to find all chars. Need to do this because
        # not all char necessarily appear in comparisons
        graph = {c: set() for w in words for c in w}
        """
        graph = {}
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char] = set()
        """
        # Now compare each pair of adjacent words
        for i in range(len(words) - 1):
            min_len = min(len(words[i]), len(words[i + 1]))
            for j in range(min_len):
                if words[i][j] != words[i + 1][j]:
                    graph[words[i][j]].add(words[i + 1][j])
                    break  # comparison complete, go to next pair of words
                if j == min_len - 1 and len(words[i]) > len(words[i + 1]):
                    return None  # invalid dictionary
        return graph

    def get_indegree(self, graph):
        in_degree = {node: 0 for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                in_degree[neighbor] += 1
        return in_degree

    # topo sort with heap instead of queue
    def topo_sort(self, graph, in_degree):
        queue = []
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        # ensures lexicographical order
        heapq.heapify(queue)

        result = []
        while queue:
            node = heapq.heappop(queue)
            result.append(node)
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    heapq.heappush(queue, neighbor)
        return "".join(result)
