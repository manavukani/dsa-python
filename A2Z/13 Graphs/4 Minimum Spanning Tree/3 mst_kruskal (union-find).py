class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * n  # size actually

    def findParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        p1 = self.findParent(node1)
        p2 = self.findParent(node2)

        if p1 == p2:
            return

        if self.rank[p1] >= self.rank[p2]:
            self.rank[p1] += self.rank[p2]  # update rank
            self.parent[p2] = p1  # update parent
        elif self.rank[p1] < self.rank[p2]:
            self.rank[p2] += self.rank[p1]  # update rank
            self.parent[p1] = p2  # update parent


# TC = O(V+E) + O(E logE) + O(E)
# SC = 2 * O(V) + O(E)
def mstKruskal(V, adj):
    """
    - sort all edges by weight (ensures smallest taken first, just like PQ)
    - perform union find on this
    """

    edges = []

    # ===============================> TC - O(V+E)
    # convert adj list to edges
    # NOTE: may add duplicate (2,1) and (1,2) but disjoint set will discard them
    for i in range(V):
        for nei, wt in adj[i]:
            edges.append((wt, i, nei))

    # ===============================> TC - O(E log E)
    # sort by weight
    edges.sort()

    # perform union find
    ds = DisjointSet(V)
    mstWt = 0
    # ===============================> TC - O(E*4α*2) ~ O(E) -----> 2 for finding p1 and p2 (2 find calls)
    for wt, u, v in edges:

        # does not belong to same component
        if ds.findParent(u) != ds.findParent(v):
            mstWt += wt
            ds.union(u, v)

    return mstWt


V = 3
adjList = [[(1, 5), (2, 1)], [(0, 5), (2, 3)], [(0, 1), (1, 3)]]
print(mstKruskal(V, adjList))
