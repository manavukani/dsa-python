# for n nodes there are n edges in a graph, given graph is connected
# remove one and make it a tree --> n nodes, n-1 edges
# return the edge to be removed. If there are multiple answers, return the answer that occurs last in the input.

"""
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""


"""

================= TC = O (E * (V+E)) =================
================= loop all edges and check for redundant =================
================= SC = O(V+E) =================

"""


def dfs_brute(edges):
    n = len(edges)
    adj = [[] for _ in range(n + 1)]

    def dfs(node, par):
        if visit[node]:
            return True

        visit[node] = True
        for nei in adj[node]:
            if nei == par:
                continue
            if dfs(nei, node):
                return True
        return False

    # keep adding and check after each adding
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        visit = [False] * (n + 1)

        if dfs(u, -1):
            return [u, v]

    return []


""" ================= TC = SC = O(V+E) ================="""


def dfs_optimal(edges):
    n = len(edges)
    adj = [[] for _ in range(n + 1)]  # 1 based indexing
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    cycle = set()
    cycleStart = -1

    def dfs(node, parent):
        # if already visited --> loop detected
        nonlocal cycleStart
        if visited[node]:
            cycleStart = node  # beginning of the cycle
            return True

        visited[node] = True
        for nei in adj[node]:
            if nei == parent:
                continue
            # for others
            if dfs(nei, node):
                # when backtracking, add nodes to cycle until reach start
                if cycleStart != -1:
                    cycle.add(node)
                if node == cycleStart:
                    cycleStart = -1
                return True
        return False

    dfs(1, -1)

    # once the cycle is identified, check which edge ("redundant") in the reversed list connects 2 nodes in the cycle set
    # check in reveresed order
    # multiple (last occurence to remove) --> becomes first occurence when loop
    for u, v in reversed(edges):
        if u in cycle and v in cycle:
            return [u, v]

    return []


edges = [[1, 2], [1, 3], [2, 3]]
print(dfs_brute(edges))
edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
print(dfs_optimal(edges))

""" ========= MOST OPTIMAL ============== 

TC: O( V + (E * a(V)))
SC: O(V)
V = no. of vertices
E = no. of edges
a() = amortized complexity.

"""


def union_find_optimal(edges):
    # initiall all parents = self
    par = [i for i in range(len(edges) + 1)]
    # no. of nodes as its child - initially 1 (self)
    rank = [1] * (len(edges) + 1)

    def find(n):
        p = par[n]
        while p != par[p]:
            par[p] = par[par[p]]
            p = par[p]
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False
        # merge with bigger rank
        if rank[p1] > rank[p2]:
            par[p2] = p1
            rank[p1] += rank[p2]
        else:
            par[p1] = p2
            rank[p2] += rank[p1]
        return True

    # first 2 node which can't be union ---> are already connected --> redundant
    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]


"""
There's no need to explicitly reverse the input list or perform extra checks because
first cycle-causing edge encountered during the forward traversal of edges is guaranteed
to be the last such edge in the input order.
"""
